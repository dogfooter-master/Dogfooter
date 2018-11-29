
import threading
import time
import collections
import sys
import os
import likeyoubot_logger
import likeyoubot_win
import signal
from PIL import ImageGrab
import cv2
import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


signal.signal(signal.SIGINT, signal.SIG_DFL)

form_class = uic.loadUiType('mainwindow.ui')[0]
dogfootermacro_title = 'DogFooterMacro Thresholder'
global dogfootermacro_logger

class PlayThread(QThread):
	def __init__(self, ui):
		QThread.__init__(self)
		self.ui = ui
		self.hwnd = self.ui.hwnd_dic[self.ui.search_comboBox.currentText()]
		self.win = self.ui.win

	def __del__(self):
		self.wait()

	def run(self):

		(anchor_x, anchor_y, end_x, end_y) = self.win.get_window_location(self.hwnd)
		adj_x, adj_y = self.win.get_player_adjust(self.hwnd)
		while(True):
			# img = ImageGrab.grab(bbox=(anchor_x - adj_x, anchor_y - adj_y, end_x, end_y))
			img = self.win.get_window_screenshot(self.hwnd, 2)
			# img = ImageGrab.grab(bbox=(100,10,400,780)) #bbox specifies specific region (bbox= x,y,width,height)
			img_np = np.array(img)
			# img_np = cv2.resize(img_np, (width, height), interpolation = cv2.INTER_AREA)
			
			r = int(self.ui.lower_r_slider.value())
			g = int(self.ui.lower_g_slider.value())
			b = int(self.ui.lower_b_slider.value())

			# lowerBound = np.array((r, g, b), dtype=np.uint8, ndmin=1)
			# upperBound = np.array((255, 255, 255), dtype=np.uint8, ndmin=1)
			lowerBound = (r, g, b)
			
			r = int(self.ui.upper_r_slider.value())
			g = int(self.ui.upper_g_slider.value())
			b = int(self.ui.upper_b_slider.value())

			upperBound = (r, g, b)

			anchor_x = int(self.ui.view_anchor_x_spinBox.value())
			anchor_y = int(self.ui.view_anchor_y_spinBox.value())

			width = int(self.ui.view_width_spinBox.value())
			height = int(self.ui.view_height_spinBox.value())

			if width < anchor_x + 120:
				width = anchor_x + 120

			if height < anchor_y + 120:
				height = anchor_y + 120



			img_np = cv2.inRange(img_np, lowerBound, upperBound)
			img_np = img_np[anchor_y:height, anchor_x:width]
			# tgt = img_np.copy()
			# for row in range(img.height):
			# 	for col in range(img.width):
			# 		img_np[row][col][0] = 255 - img_np[row][col][0] 
			# 		img_np[row][col][1] = 255 - img_np[row][col][1] 
			# 		img_np[row][col][2] = 255 - img_np[row][col][2] 

			# frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
			title = "Press ESC or Q " + str(self.hwnd)

			cv2.imshow(title, img_np)
			wait_key = cv2.waitKey(25)

			if wait_key & 0xFF == ord('q'):
				break
			elif wait_key == 27:
				break

			if cv2.getWindowProperty(title, 0) == -1:
				break

		cv2.destroyAllWindows()	


class MainWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.setWindowTitle(dogfootermacro_title)
		self.search_button.clicked.connect(self.callback_search_button_clicked)
		self.search_comboBox.currentIndexChanged.connect(self.callback_search_comboBox_currentIndexChanged)
		self.play_button.clicked.connect(self.callback_play_button_clicked)

		self.upper_r_slider.valueChanged.connect(self.callback_upper_r_slider_changed)
		self.upper_r_spinBox.valueChanged.connect(self.callback_upper_r_spinBox_changed)
		self.upper_g_slider.valueChanged.connect(self.callback_upper_g_slider_changed)
		self.upper_g_spinBox.valueChanged.connect(self.callback_upper_g_spinBox_changed)
		self.upper_b_slider.valueChanged.connect(self.callback_upper_b_slider_changed)
		self.upper_b_spinBox.valueChanged.connect(self.callback_upper_b_spinBox_changed)


		self.lower_r_slider.valueChanged.connect(self.callback_lower_r_slider_changed)
		self.lower_r_spinBox.valueChanged.connect(self.callback_lower_r_spinBox_changed)
		self.lower_g_slider.valueChanged.connect(self.callback_lower_g_slider_changed)
		self.lower_g_spinBox.valueChanged.connect(self.callback_lower_g_spinBox_changed)
		self.lower_b_slider.valueChanged.connect(self.callback_lower_b_slider_changed)
		self.lower_b_spinBox.valueChanged.connect(self.callback_lower_b_spinBox_changed)


		self.win = likeyoubot_win.LYBWin(dogfootermacro_title)
		self.hwnd_dic = {}

	def callback_search_button_clicked(self):
		self.win.find_window_wildcard('')
		for each_hwnd in self.win.handle_list:
			dogfootermacro_logger.debug(str(each_hwnd) + ' ' + self.win.get_title(each_hwnd))
			if each_hwnd in self.win.parent_handle_dic:
				title = self.win.get_title(self.win.parent_handle_dic[each_hwnd])
			else:
				title = self.win.get_title(each_hwnd)

			self.search_comboBox.addItem(title)
			self.hwnd_dic[title] = each_hwnd

		dogfootermacro_logger.debug(self.search_comboBox.count())
		if self.search_comboBox.count() > 0:
			self.play_button.setEnabled(True)
		else:
			self.play_button.setEnabled(False)

	def callback_search_comboBox_currentIndexChanged(self):
		dogfootermacro_logger.debug('callback_search_comboBox_currentIndexChanged called()')

	def callback_play_button_clicked(self):
		dogfootermacro_logger.debug('callback_play_button_clicked called()')	
		self.play_thread =  PlayThread(self)
		self.play_thread.start()

	def callback_upper_r_slider_changed(self):
		self.upper_r_spinBox.setValue(self.upper_r_slider.value())

	def callback_upper_r_spinBox_changed(self):
		self.upper_r_slider.setValue(self.upper_r_spinBox.value())

	def callback_upper_g_slider_changed(self):
		self.upper_g_spinBox.setValue(self.upper_g_slider.value())

	def callback_upper_g_spinBox_changed(self):
		self.upper_g_slider.setValue(self.upper_g_spinBox.value())

	def callback_upper_b_slider_changed(self):
		self.upper_b_spinBox.setValue(self.upper_b_slider.value())

	def callback_upper_b_spinBox_changed(self):
		self.upper_b_slider.setValue(self.upper_b_spinBox.value())

	def callback_lower_r_slider_changed(self):
		self.lower_r_spinBox.setValue(self.lower_r_slider.value())

	def callback_lower_r_spinBox_changed(self):
		self.lower_r_slider.setValue(self.lower_r_spinBox.value())

	def callback_lower_g_slider_changed(self):
		self.lower_g_spinBox.setValue(self.lower_g_slider.value())

	def callback_lower_g_spinBox_changed(self):
		self.lower_g_slider.setValue(self.lower_g_spinBox.value())

	def callback_lower_b_slider_changed(self):
		self.lower_b_spinBox.setValue(self.lower_b_slider.value())

	def callback_lower_b_spinBox_changed(self):
		self.lower_b_slider.setValue(self.lower_b_spinBox.value())	
if __name__ == '__main__':
	try:
		dogfootermacro_logger = likeyoubot_logger.LYBLogger.getLogger()
		app = QApplication(sys.argv)
		mainWindow = MainWindow()
		mainWindow.show()
		app.exec_()
	except:
		print('create logger fail: ' +str(sys.exc_info()[0]) + '(' +str(sys.exc_info()[1]) + ')')
		sys.exit(1) 

import tkinter
from tkinter import ttk
import likeyoubot_logger
import likeyoubot_worker
import likeyoubot_win
import traceback
import queue
from PIL import Image, ImageTk, ImageGrab

class LYBMaker:
	def __init__(self, configure, window_name):
		self.logger = likeyoubot_logger.LYBLogger.getLogger()
		self.logger.warn('Hello, world')
		self.window_name = window_name
		self.configure = configure

		self.root = tkinter.Toplevel()
		self.root.overrideredirect(True)
		self.root.geometry('%dx%d+%d+%d' % (800, 480, 640, 360))
		self.button = ttk.Button(
			master 				= self.root, 
			text 				= "저장", 
			width 				= 4,
			command 			= lambda : self.callback_button(None)
			)
		self.button.pack(side=tkinter.LEFT, padx=2)
		self.win = likeyoubot_win.LYBWin(self.configure.window_title, self.configure)

	def callback_button(self, event):
		try:
			self.logger.debug(self.window_name)
			self.win.find_window_wildcard(self.window_name)
			current_window_image_grab = self.win.get_window_screenshot(self.win.handle_list[0], 2)
			self.logger.debug(current_window_image_grab)
			image1 = ImageTk.PhotoImage(current_window_image_grab)
			current_window_image_grab.save('11.png')
			label = tkinter.Label(master=self.root, image=image1)
			label.image = image1
			label.place(x=0, y=0)
			label.pack()
		except:
			self.logger.error(traceback.format_exc())




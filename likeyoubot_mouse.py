import pyautogui
import pickle
import time
import os
import win32api
import win32con
import win32gui
import sys
import operator
import likeyoubot_resource as lybresource
import likeyoubot_win as lybwin

class LYBMouse():
	def __init__(self):
		self.anchor_x = -1
		self.anchor_y = -1

	def moveUP(self):
		x, y = pyautogui.position()
		pyautogui.moveTo( x, y+1 )

	def moveDOWN(self):
		x, y = pyautogui.position()
		pyautogui.moveTo( x, y-1 )

	def moveRIGHT(self):
		x, y = pyautogui.position()
		pyautogui.moveTo( x+1, y )

	def moveLEFT(self):
		x, y = pyautogui.position()
		pyautogui.moveTo( x-1, y )

	def execute(self):

		while True:
			x, y = pyautogui.position()
			positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + \
				' ' + str(pyautogui.pixel(x, y)).rjust(16) + \
				'      ' + 'R-X: ' + str(x - self.anchor_x).rjust(4) + ' R-Y: ' + str(y - self.anchor_y).rjust(4)
			print(positionStr, end='')
			print('\b' * len(positionStr), end='', flush=True)

			a = win32api.GetAsyncKeyState(win32con.VK_UP)
			b = win32api.GetAsyncKeyState(win32con.VK_DOWN)
			c = win32api.GetAsyncKeyState(win32con.VK_RIGHT)
			d = win32api.GetAsyncKeyState(win32con.VK_LEFT)
			# d = win32api.GetAsyncKeyState(ord('D'))
			# w = win32api.GetAsyncKeyState(ord('W'))
			# c = win32api.GetAsyncKeyState(ord('C'))
			# f = win32api.GetAsyncKeyState(ord('F'))
			# z = win32api.GetAsyncKeyState(ord('Z'))
			# r = win32api.GetAsyncKeyState(ord('R'))
			# q = win32api.GetAsyncKeyState(ord('Q'))
			# t = win32api.GetAsyncKeyState(ord('T'))

			if a == 1:
				self.moveDOWN()
			elif b == 1:
				self.moveUP()
			elif c == 1:
				self.moveRIGHT()
			elif d == 1:
				self.moveLEFT()

			time.sleep(0.4)


LYBMouse().execute()
import likeyoubot_resource as lybrsc
import likeyoubot_message
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import operator
import random
import likeyoubot_game as lybgame
import likeyoubot_tera as lybgameTera
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBTeraScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBTeraScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'nox_init_screen_scene':
			rc = self.nox_init_screen_scene()
		else:
			rc = 0

		return rc

	def nox_init_screen_scene(self):
		print('DEBUG 1')
		self.schedule_list = self.get_game_config('schedule_list')
		if '게임 시작' in self.schedule_list:
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, self.game_object.resource_manager.pixel_box_dic['tera_icon'])
			self.lyb_mouse_click_location(loc_x, loc_y)
		print('DEBUG 2')
		return 0

	def logo_screen_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		print('DEBUG77:', self.schedule_list)
		if not '로그인' in self.schedule_list:
			return 0

		if time.time() - self.get_checkpoint('wait_finding_account') > 30:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('wait_finding_account')
			if self.get_window_config('multi_account'):
				self.loggingToGUI('구글 계정 변경 시도')
				
			self.status += 1
		elif self.status == 1:
			if time.time() - self.get_checkpoint('wait_finding_account') > 100:
				self.loggingToGUI('구글 계정 감지 실패')
				return -1

			if self.get_window_config('multi_account'):
				print('google multi account On')
				rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'account_change_icon', custom_tolerance=50)
				print('change icon:', int(rate*100), '%')
				is_there = self.lyb_mouse_click('account_change_icon', custom_tolerance=50, custom_threshold=0)
				print('account change is clicked:', is_there)
				if is_there:
					self.status = 2
					self.set_option('load_complete_flag', False)
			else:	
				self.status = 3
		elif self.status == 2:
			print('wait for loading account select')
			if self.get_option('load_complete_flag'):
				self.set_option('load_complete_flag', False)
				self.status = 3
			else:
				self.status = 1
		elif self.status == 3:
			self.lyb_mouse_click_location(320, 330)
			self.status +=1
		elif self.status == 4:
			self.status -= 1

		return self.status

	def connect_account_scene(self):
		if self.status == 0:
			self.set_checkpoint('interval_login')
			self.status += 1
		elif self.status == 1:

			print('select_complete_flag:', self.get_option('select_complete_flag'))
			if (self.get_option('select_complete_flag') == True or 
				time.time() - self.get_checkpoint('interval_login') > 100):
				self.lyb_mouse_click('connect_account_close_icon')
				self.game_object.get_scene('logo_screen_scene').set_option('load_complete_flag', True)
				self.set_option('select_complete_flag', False)
				self.status = 0
			else:
				# 회색
				print('DEBUG 00')
				is_logff_status = self.lyb_mouse_click('google_login_letter_0', custom_threshold=0.9)
				if not is_logff_status:
					print('DEBUG 11')
					# 파란색
					self.lyb_mouse_click('google_login_icon')
				else:
					print('DEBUG 12')
					self.set_option('select_complete_flag', False)

		return self.status

	def google_play_account_select_scene(self):
		(top_loc_x, top_loc_y) = lybgame.LYBGame.locationOnWindow(
			self.window_image, 
			self.game_object.resource_manager.pixel_box_dic['google_play_letter']
			)
		self.loggingToGUI('구글 계정 기준점: ' + str((top_loc_x, top_loc_y)))
		if top_loc_x == -1:
			return self.status

		if self.status == 0:
			(bottom_loc_x, bottom_loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['google_play_add_account_letter']
				)

			if bottom_loc_y == -1:
				# 계정 5개 이상이라는 의미
				self.google_account_number = 1000
			else:
				diff_y = bottom_loc_y - top_loc_y
				self.google_account_number = int(diff_y / self.google_account_height)

			if self.google_account_number > 5:
				self.loggingToGUI('구글 계정 5개 이상 감지됨')
			else:
				self.loggingToGUI('구글 계정 '+str(self.google_account_number)+'개 감지됨')

		print('google account DEBUG:', self.status, self.google_account_number)
		if self.status >= self.google_account_number:
			self.status = 0		
			self.loggingToGUI(str(self.google_account_number)+' 개의 계정 작업 완료')	
			return self.status
		else:
			self.loggingToGUI(str(self.status + 1)+' 번째 구글 계정 로그인 시도')
			self.game_object.get_scene('connect_account_scene').set_option('select_complete_flag', True)
		
		if self.status >= 0 and self.status < 5:
			click_loc_x = top_loc_x + 10
			click_loc_y = top_loc_y + self.google_account_height*self.status + self.google_account_height*0.8
			self.lyb_mouse_click_location(click_loc_x, click_loc_y)
			#self.lyb_mouse_move_location(click_loc_x, click_loc_y)
			self.status += 1
		else:
			if self.just_drag_completed == False:
				self.just_drag_completed = True

				drag_number = self.status - 5

				from_x = top_loc_x + 10
				from_y = top_loc_y + self.google_account_height * 2 + 5

				to_x = top_loc_x + 10
				to_y = top_loc_y + self.google_account_height * 1

				print(from_x, from_y, to_x, to_y)
				self.lyb_mouse_drag_location(from_x, from_y, to_x, to_y, delay=1)
				
			else:
				self.just_drag_completed = False
				# 맨아래까지 왔나?
				(bottom_loc_x, bottom_loc_y) = lybgame.LYBGame.locationOnWindow(
						self.window_image, 
						self.game_object.resource_manager.pixel_box_dic['google_play_add_account_letter']
					)
				if bottom_loc_x > 0 and bottom_loc_y > 0:
					self.lyb_mouse_click_location(top_loc_x - 150, top_loc_y)
					#self.lyb_mouse_move_location(top_loc_x - 150, top_loc_y)
					self.loggingToGUI(str(self.status + 1)+' 번째 구글 계정 감지 실패')
					self.loggingToGUI('총 '+str(self.status)+' 개의 계정 작업 완료')
					self.status = 0

				else:
					click_loc_x = top_loc_x + 10
					click_loc_y = top_loc_y + self.google_account_height*4 + self.google_account_height*0.8
					self.lyb_mouse_click_location(click_loc_x, click_loc_y)
					#self.lyb_mouse_move_location(click_loc_x, click_loc_y)
					self.status += 1

		return self.status


	def terms_of_use_scene(self):
		#print(self.game_object.rateMatchedPixelBox(self.window_pixels, 'terms_of_use_bottom_0'))
		self.lyb_mouse_click('terms_of_use_bottom_0')

		#print(self.game_object.rateMatchedPixelBox(self.window_pixels, 'terms_of_use_bottom_1'))
		self.lyb_mouse_click('terms_of_use_bottom_1')
		return 0
















	def get_work_status(self, work_name):
		if work_name in lybgameTera.LYBTera.work_list:
			return (lybgameTera.LYBTera.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
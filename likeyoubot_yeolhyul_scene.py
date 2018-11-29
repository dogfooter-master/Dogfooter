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
import likeyoubot_yeolhyul as lybgameYeolhyul
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBYeolhyulScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBYeolhyulScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'nox_init_screen_scene':
			rc = self.nox_init_screen_scene()
		elif self.scene_name == 'chulsuk_bosang_scene':
			rc = self.chulsuk_bosang_scene()
		elif self.scene_name == 'main_scene':
			rc = self.main_scene()
		elif self.scene_name == 'mission_scene':
			rc = self.mission_scene()
		elif self.scene_name == 'bimil_sangja_scene':
			rc = self.bimil_sangja_scene()
		elif self.scene_name == 'combat_scene':
			rc = self.combat_scene()
		elif self.scene_name == 'combat_result_scene':
			rc = self.combat_result_scene()
		elif self.scene_name == 'jangbi_scene':
			rc = self.jangbi_scene()
		elif self.scene_name == 'jangbi_2_scene':
			rc = self.jangbi_2_scene()
		elif self.scene_name == 'jangbi_place_scene':
			rc = self.jangbi_place_scene()
		elif self.scene_name == 'gate_dojun_scene':
			rc = self.gate_dojun_scene()
		elif self.scene_name == 'login_scene':
			rc = self.login_scene()
		elif self.scene_name == 'character_select_scene':
			rc = self.character_select_scene()
		elif self.scene_name == 'gwanmun_scene':
			rc = self.gwanmun_scene()
		else:
			rc = 0

		return rc


	# def combat_result_scene(self):

	# 	if self.status == 0:
	# 		self.status += 1
	# 	else:
	# 		self.lyb_mouse_click(self.scene_name + '_close_icon')
	# 		self.status = 0

	# 	return self.status



	def gwanmun_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def character_select_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('character_select_scene_start', custom_threshold=0)
			self.game_object.interval = self.period_bot(5)
			self.status += 1
		else:
			self.status = 0

		return self.status

	def login_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('login_scene_touch', custom_threshold=0)
			self.game_object.interval = self.period_bot(5)
			self.status += 1
		else:
			# self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def gate_dojun_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'gate_dojun_scene_possible')
			print('[DEBUG] match_rate:', match_rate)
			if match_rate < 0.9:
				self.status = 99999
			else:
				self.lyb_mouse_click('gate_dojun_scene_dojun')
				self.game_object.get_scene('combat_scene').status = 0
				self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def jangbi_place_scene(self):

		if self.status == 0:
			if time.time() - self.get_checkpoint('clicked') < self.period_bot(10):
				self.status = 99999
			else:
				self.status += 1
		elif self.status == 1:
			loc_x, loc_y = self.loc_gate()
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.set_checkpoint('clicked')
				self.status = 0
			else:
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def jangbi_2_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 100:
			# 승급
			self.lyb_mouse_click('jangbi_2_scene_sunggup', custom_threshold=0)
			self.status += 1
		elif self.status == 101:
			self.lyb_mouse_click('jangbi_2_scene_sunggup_button')
			self.status = 99999
		elif self.status == 200:
			# 승급
			self.lyb_mouse_click('jangbi_2_scene_sunggup', custom_threshold=0)
			self.status += 1
		elif self.status == 201:
			loc_x, loc_y = self.loc_plus()
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def jangbi_scene(self):

		if self.status == 0:
			self.status += 1
		elif (	self.status == self.get_work_status('무기 - 승급') or
				self.status == self.get_work_status('무기 - 승급 재료')
				):
			if self.status == self.get_work_status('무기 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_0', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('상의 - 승급') or
				self.status == self.get_work_status('상의 - 승급 재료')
				):
			if self.status == self.get_work_status('상의 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_1', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('하의 - 승급') or
				self.status == self.get_work_status('하의 - 승급 재료')
				):
			if self.status == self.get_work_status('하의 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_2', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('견장 - 승급') or
				self.status == self.get_work_status('견장 - 승급 재료')
				):
			if self.status == self.get_work_status('견장 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_3', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('허리띠 - 승급') or
				self.status == self.get_work_status('허리띠 - 승급 재료')
				):
			if self.status == self.get_work_status('허리띠 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_4', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('신발 - 승급') or
				self.status == self.get_work_status('신발 - 승급 재료')
				):
			if self.status == self.get_work_status('신발 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_5', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('목장식 - 승급') or
				self.status == self.get_work_status('목장식 - 승급 재료')
				):
			if self.status == self.get_work_status('목장식 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_6', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('팔찌 - 승급') or
				self.status == self.get_work_status('팔찌 - 승급 재료')
				):
			if self.status == self.get_work_status('팔찌 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_7', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('가락지 - 승급') or
				self.status == self.get_work_status('가락지 - 승급 재료')
				):
			if self.status == self.get_work_status('가락지 - 승급'):
				self.game_object.get_scene('jangbi_2_scene').status = 100
			else:
				self.game_object.get_scene('jangbi_2_scene').status = 200
			self.lyb_mouse_click('jangbi_scene_item_8', custom_threshold=0)
			self.status = 99999
		elif self.status == 99998:
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def combat_result_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def combat_scene(self):

		if self.status == 0:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'combat_stance_sudong')
			if match_rate > 0.8:
				self.status = 1
			else:
				self.lyb_mouse_click('combat_stance_sudong', custom_threshold=0)
		elif self.status == 1:
			# 연계기 자동
			self.lyb_mouse_click('combat_stance_sudong', custom_threshold=0)
			self.status += 1
		elif self.status == 2:
			# 자동 전투
			self.lyb_mouse_click('combat_stance_sudong', custom_threshold=0)
			self.status += 1			
		else:
			pass

		return self.status

	def bimil_sangja_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('bimil_sangja_scene_item', custom_threshold=0)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('bimil_sangja_scene_box_free')
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('bimil_sangja_scene_box_special_free')
			self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('bimil_sangja_scene_box_special_free_2')
			self.status += 1
		elif self.status == 4:
			self.lyb_mouse_click('bimil_sangja_scene_dongryo', custom_threshold=0)
			self.status += 1
		elif self.status == 5:
			self.lyb_mouse_click('bimil_sangja_scene_dongryo_free')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0


		return self.status

	def mission_scene(self):

		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'mission_scene_complete')
		if match_rate > 0.8:
			self.lyb_mouse_click('mission_scene_complete', custom_threshold=0.8)
			return self.status

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def main_scene(self):

		if self.game_object.current_schedule_work != self.current_work:
			self.game_object.current_schedule_work = self.current_work

		if self.game_object.main_scene == None:
			self.game_object.main_scene = self

		self.schedule_list = self.get_game_config('schedule_list')
		if len(self.schedule_list) == 1:
			self.loggingToGUI('스케쥴 작업이 없어서 종료합니다.')
			return -1

		if self.status == 0:
			print('[DEBUG] schedule_list length:', len(self.schedule_list))
			self.status += 1
		elif self.status >= 1 and self.status < 100:
			s_list_iter = 0
			s_list_number = len(self.schedule_list)

			if self.current_work != None:
				if self.current_work in self.move_status:
					self.status = self.move_status[self.current_work]
					self.move_status.pop(self.current_work)

			if self.status > s_list_number:
				self.status = s_list_number

			while True:
				self.current_work = self.schedule_list[self.status - 1]
				if self.current_work == '게임 시작':
					pass
				elif self.current_work == '로그인':
					pass
				else:
					break
				self.status += 1
				s_list_iter += 1
				if s_list_iter > s_list_number:
					break

			if len(self.current_work) < 1:
				is_multi_account = self.get_window_config('multi_account')
				if is_multi_account == True:
					self.loggingToGUI('[미지원   ] 구글 멀티 계정')
				else:
					self.loggingToGUI('[스케쥴링 ] 지정된 스케줄을 완료해서 처음으로 돌아갑니다')
					self.status = 1
					return self.status
			else:
				self.loggingToGUI('[스케쥴링 ] 작업 번호 - ' + str(self.status) + '. ' + self.current_work, log_type='good')
				self.set_work_status()

				return self.status
			
			self.status += 1
		elif self.status == self.get_work_status('비밀 상자'):

			elapsed_time = self.get_elapsed_time()
			if ( 	elapsed_time >  self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_bimil_sangja', custom_threshold=0)

		elif (	self.status == self.get_work_status('무기 - 승급 재료') or
				self.status == self.get_work_status('상의 - 승급 재료') or
				self.status == self.get_work_status('하의 - 승급 재료') or
				self.status == self.get_work_status('견장 - 승급 재료') or
				self.status == self.get_work_status('허리띠 - 승급 재료') or
				self.status == self.get_work_status('신발 - 승급 재료') or
				self.status == self.get_work_status('목장식 - 승급 재료') or
				self.status == self.get_work_status('팔찌 - 승급 재료') or
				self.status == self.get_work_status('가락지 - 승급 재료')
				):

			elapsed_time = self.get_elapsed_time()
			if ( 	elapsed_time >  self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_jangbi', custom_threshold=0)
			self.game_object.get_scene('jangbi_scene').status = self.status

		elif (	self.status == self.get_work_status('무기 - 승급') or
				self.status == self.get_work_status('상의 - 승급') or
				self.status == self.get_work_status('하의 - 승급') or
				self.status == self.get_work_status('견장 - 승급') or
				self.status == self.get_work_status('허리띠 - 승급') or
				self.status == self.get_work_status('신발 - 승급') or
				self.status == self.get_work_status('목장식 - 승급') or
				self.status == self.get_work_status('팔찌 - 승급') or
				self.status == self.get_work_status('가락지 - 승급')
				):

			elapsed_time = self.get_elapsed_time()
			if ( 	elapsed_time >  self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_jangbi', custom_threshold=0)
			self.game_object.get_scene('jangbi_scene').status = self.status

		return self.status

	def chulsuk_bosang_scene(self):

		self.lyb_mouse_click(self.scene_name + '_close_icon')

		return self.status

	def nox_init_screen_scene(self):
		
		self.schedule_list = self.get_game_config('schedule_list')
		if not '게임 시작' in self.schedule_list:
			return 0


		loc_x = -1
		loc_y = -1


		if self.game_object.player_type == 'nox':
			for each_icon in lybgameYeolhyul.LYBYeolhyul.nox_yh_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					break
		elif self.game_object.player_type == 'momo':
			for each_icon in lybgameYeolhyul.LYBYeolhyul.nox_yh_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.6,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
								)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					break

		# if loc_x == -1:
		# 	self.loggingToGUI('테라 아이콘 발견 못함')

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

	def loc_plus(self):

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['item_plus'],
						custom_below_level=(220, 200, 100),
						custom_top_level=(255,255,180),
						custom_threshold=0.7,
						custom_flag=1,
						custom_rect=(360,130,620,260)
						)

		print('[DEBUG] ItemPLus:', (loc_x, loc_y), match_rate)
		if loc_x != -1:
			return loc_x, loc_y

		return -1, -1

	def loc_gate(self):

		custom_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE)) * 0.01

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['item_gate'],
						custom_threshold=custom_threshold,
						custom_flag=1,
						custom_rect=(200,180,240,320)
						)

		print('[DEBUG] ItemGate:', (loc_x, loc_y), match_rate)
		if loc_x != -1:
			return loc_x, loc_y

		return -1, -1

	def loc_jadong(self):

		custom_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_YH_THRESHOLD_STANCE)) * 0.01
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['combat_stance_jadong'],
						custom_threshold=custom_threshold,
						custom_below_level=(80, 80, 80),
						custom_top_level=(255, 255, 190),
						custom_flag=1,
						custom_rect=(5,80,40,110)
						)

		print('[DEBUG] Jadong Stance:', (loc_x, loc_y), match_rate)
		if loc_x != -1:
			return loc_x, loc_y

		return -1, -1















	def get_work_status(self, work_name):
		if work_name in lybgameYeolhyul.LYBYeolhyul.work_list:
			return (lybgameYeolhyul.LYBYeolhyul.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
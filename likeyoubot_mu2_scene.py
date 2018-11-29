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
import likeyoubot_mu2 as lybgamemu2
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBMu2Scene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBMu2Scene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'init_screen_scene':
			rc = self.init_screen_scene()
		elif self.scene_name == 'main_scene':
			rc = self.main_scene()
		elif self.scene_name == 'login_scene':
			rc = self.login_scene()
		elif self.scene_name == 'waiting_scene':
			rc = self.waiting_scene()
		elif self.scene_name == 'jeoljeonmode_scene':
			rc = self.jeoljeonmode_scene()
		elif self.scene_name == 'dungeon_enter_scene':
			rc = self.dungeon_enter_scene()
		elif self.scene_name == 'dungeon_scene':
			rc = self.dungeon_scene()
		elif self.scene_name == 'alrim_scene':
			rc = self.alrim_scene()
		elif self.scene_name == 'mail_scene':
			rc = self.mail_scene()
		elif self.scene_name == 'menu_scene':
			rc = self.menu_scene()
		elif self.scene_name == 'character_scene':
			rc = self.character_scene()
		elif self.scene_name == 'artifact_scene':
			rc = self.artifact_scene()
		elif self.scene_name == 'bosang_scene':
			rc = self.bosang_scene()
		elif self.scene_name == 'yeongum_scene':
			rc = self.yeongum_scene()
			



		else:
			rc = self.else_scene()

		return rc

	def else_scene(self):

		if self.status == 0:
			self.logger.warn('unknown scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def yeongum_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			pb_name = 'yeongum_scene_free'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(100, 270, 540, 320))
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.status = 99999
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def bosang_scene(self):
		self.game_object.current_matched_scene['name'] = ''
		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			is_clicked = self.lyb_mouse_click('bosang_scene_gold_new')
			if is_clicked == True:
				self.game_object.get_scene('yeongum_scene').status = 0
			self.status += 1
		elif self.status == 2:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def artifact_scene(self):

		self.game_object.current_matched_scene['name'] = ''

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 3:
			rank_count = len(lybgamemu2.LYBMu2.item_rank_list)
			i = 0
			for each_rank in lybgamemu2.LYBMu2.item_rank_list:
				cfg_is_checked = self.get_game_config(lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + str(i))

				pb_name = 'artifact_scene_item_rank_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.debug(pb_name + ' ' + str(match_rate))
				if match_rate > 0.9 and cfg_is_checked == True:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
				elif match_rate < 0.9 and cfg_is_checked == False:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
				i += 1
			self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('artifact_scene_bunhe')
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def character_scene(self):

		self.game_object.current_matched_scene['name'] = ''

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('아티팩트 - 분해'):
			self.lyb_mouse_click('character_scene_artifact', custom_threshold=0)
			self.game_object.get_scene('artifact_scene').status = 0
			self.game_object.current_matched_scene['name'] = ''
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def menu_scene(self):

		self.game_object.current_matched_scene['name'] = ''

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('아티팩트 - 분해'):
			self.lyb_mouse_click('menu_scene_character', custom_threshold=0)
			self.game_object.get_scene('character_scene').status = self.status
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def mail_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('mail_scene_all')
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def alrim_scene(self):


		loc_name = 'alrim_inventory_full_loc'
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, loc_name, custom_below_level=100, custom_top_level=255)
		self.logger.debug(loc_name + ' ' + str(match_rate))
		if match_rate > 0.95:
			current_work = self.game_object.get_scene('main_scene').current_work
			if current_work != None:
				self.game_object.get_scene('main_scene').set_option(current_work + '_end_flag', True)
			self.lyb_mouse_click('alrim_inventory_full_cancel')
			return self.status

		loc_name = 'alrim_artifact_confirm_loc'
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, loc_name)
		self.logger.debug(loc_name + ' ' + str(match_rate))
		if match_rate > 0.95:
			self.lyb_mouse_click('alrim_artifact_confirm')
			return self.status

		loc_name = 'alrim_jinhwa_confirm_loc'
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, loc_name)
		self.logger.debug(loc_name + ' ' + str(match_rate))
		if match_rate > 0.95:
			self.lyb_mouse_click('alrim_jinhwa_confirm')
			return self.status

		loc_name = 'alrim_jinhwa2_confirm_loc'
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, loc_name)
		self.logger.debug(loc_name + ' ' + str(match_rate))
		if match_rate > 0.95:
			self.lyb_mouse_click('alrim_jinhwa2_confirm')
			return self.status

		if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
		
		return self.status

	def dungeon_scene(self):

		if self.status % 10 == 0:
			self.game_object.current_matched_scene['name'] = ''

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.auto_on()
			self.status += 1
		elif self.status >= 1 and self. status < 10:
			pb_name = 'dungeon_scene_ready'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(170, 150, 220, 200))
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x - 50, loc_y)
				self.status = 10
			self.status += 1
		elif self.status >= 10 and self.status < 60:
			self.status += 1
		else:						
			self.status = 0

		return self.status

	def dungeon_enter_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('dungeon_enter_scene_join')
			self.status = 0
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def dungeon_end_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def jeoljeonmode_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:
			self.lyb_mouse_drag('jeoljeonmode_scene_drag_left', 'jeoljeonmode_scene_drag_right')
			self.game_object.interval = self.period_bot(2)				
			self.status = 0

		return self.status


	def waiting_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:
			self.status = 0

		return self.status

	def login_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')

		if not '로그인' in self.schedule_list:
			return 0

		elapsedTime = time.time() - self.get_checkpoint('start')
		if elapsedTime > 120:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('login_scene_touch', custom_threshold=0)
			self.status += 1
		elif self.status >= 2 and self.status < 6:
			self.status += 1
		elif self.status == 6:
			self.lyb_mouse_click('login_scene_touch', custom_threshold=0)
			self.status += 1
		elif self.status >= 7 and self.status < 10:
			self.status += 1
		elif self.status >= 10 and self.status < 40:
			self.logger.info('로그인 화면 랙 인식: ' + str(self.status - 10) + '/30')
			self.status += 1
		elif self.status == 40:
			self.game_object.terminate_application()
			self.status += 1
		else:
			# self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def init_screen_scene(self):
		
		self.schedule_list = self.get_game_config('schedule_list')
		if not '게임 시작' in self.schedule_list:
			return 0


		loc_x = -1
		loc_y = -1


		if self.game_object.player_type == 'nox':
			for each_icon in lybgamemu2.LYBMu2.nox_mu2_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				# self.logger.debug(match_rate)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					break
		elif self.game_object.player_type == 'momo':
			for each_icon in lybgamemu2.LYBMu2.momo_mu2_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
								)
				# self.logger.debug(match_rate)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					break

		# if loc_x == -1:
		# 	self.loggingToGUI('테라 아이콘 발견 못함')

		return 0

















































	def main_scene(self):

		if self.game_object.current_schedule_work != self.current_work:
			self.game_object.current_schedule_work = self.current_work

		self.game_object.main_scene = self

		self.schedule_list = self.get_game_config('schedule_list')
		if len(self.schedule_list) == 1:
			self.logger.warn('스케쥴 작업이 없어서 종료합니다.')
			return -1

		if self.status == 0:
			self.status += 1
		elif self.status >= 1 and self.status < 1000:

			self.set_schedule_status()

		elif (	self.status == self.get_work_status('메인 퀘스트') or 
				self.status == self.get_work_status('일일 퀘스트') or 
				self.status == self.get_work_status('길드 퀘스트')
			):

			elapsed_time = self.get_elapsed_time()
			duration_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration'))
			click_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period'))
			quest_number = int(self.get_game_config(lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number')) - 1

			if elapsed_time > self.period_bot(duration_time):
				self.set_option(self.current_work + '_end_flag', True)	

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('ilil_limit_check', 0)
				self.set_option('guild_limit_check', 0)
				self.status = self.last_status[self.current_work] + 1
				return self.status	

			self.game_object.current_matched_scene['name'] = ''

			elapsed_clicked = time.time() - self.get_checkpoint('main_quest_clicked')

			if self.main_quest_pre_process() == True:
				return self.status

			if elapsed_clicked > self.period_bot(3):
				pb_name = 'main_scene_find_path'
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic[pb_name],
					custom_threshold=0.6,
					custom_top_level=(255, 255, 255),
					custom_below_level=(150, 150, 150),
					custom_flag=1,
					custom_rect=(270, 80, 350, 170)
					)
				# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
				self.logger.debug(pb_name + ' ' + str(match_rate))
				if loc_x == -1:
					pb_name = 'main_scene_auto'
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.6,
						custom_top_level=(255, 255, 255),
						custom_below_level=(100, 90, 30),
						custom_flag=1,
						custom_rect=(270, 80, 350, 170)
						)
					self.logger.debug(pb_name + ' ' + str(match_rate))
					if loc_x == -1:

						check_for_click = self.get_option('check_for_click')
						if check_for_click == None:
							check_for_click = 0

						self.logger.warn('퀘스트 수행 멍때림 체크 중...(' + str(check_for_click) + '/5)')
						if check_for_click > 4:
							if self.main_quest_character_move() == True:
								return self.status

							if self.status == self.get_work_status('메인 퀘스트'):
								self.lyb_mouse_click('main_quest_list_' + str(quest_number), custom_threshold=0)
							elif self.status == self.get_work_status('일일 퀘스트'):
								is_clicked = self.main_scene_click_ililquest()
								ilil_limit_check = self.get_option('ilil_limit_check')
								if ilil_limit_check == None:
									ilil_limit_check = 0
								if is_clicked == False:
									self.logger.warn('[일일] 감지 실패: ' + str(ilil_limit_check) + '/5')
									if ilil_limit_check > 5:
										self.set_option(self.current_work + '_end_flag', True)
									else:
										self.set_option('ilil_limit_check', ilil_limit_check + 1)
								else:
									self.set_option('ilil_limit_check', 0)
							elif self.status == self.get_work_status('길드 퀘스트'):
								is_clicked = self.main_scene_click_guildquest()
								guild_limit_check = self.get_option('guild_limit_check')
								if guild_limit_check == None:
									guild_limit_check = 0
								if is_clicked == False:
									self.logger.warn('[길드] 감지 실패: ' + str(guild_limit_check) + '/5')
									if guild_limit_check > 5:
										self.set_option(self.current_work + '_end_flag', True)
									else:
										self.set_option('guild_limit_check', guild_limit_check + 1)
								else:
									self.set_option('guild_limit_check', 0)
							else:
								self.set_option(self.current_work + '_end_flag', True)

							self.set_checkpoint('main_quest_clicked')	
							self.set_option('check_for_click', 0)
							return self.status
						else:
							self.set_option('check_for_click', check_for_click + 1)
					else:
						self.set_option('check_for_click', 0)
				else:
					self.set_option('check_for_click', 0)


			if elapsed_clicked > click_period:
				if self.status == self.get_work_status('메인 퀘스트'):
					self.lyb_mouse_click('main_quest_list_' + str(quest_number), custom_threshold=0)
				elif self.status == self.get_work_status('일일 퀘스트'):
					self.main_scene_click_ililquest()
				elif self.status == self.get_work_status('길드 퀘스트'):
					self.main_scene_click_guildquest()


				self.set_checkpoint('main_quest_clicked')

		elif self.status == self.get_work_status('우편'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_mail')
			self.game_object.get_scene('mail_scene').status =0

		elif self.status == self.get_work_status('무료 교환'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_bosang')
			self.game_object.get_scene('bosang_scene').status =0

		elif self.status == self.get_work_status('아티팩트 - 분해'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_potrait', custom_threshold=0)
			self.game_object.get_scene('menu_scene').status = self.status

		elif self.status == self.get_work_status('알림'):

			try:
				self.game_object.telegram_send(str(self.get_game_config(lybconstant.LYB_DO_STRING_NOTIFY_MESSAGE)))
				self.status = self.last_status[self.current_work] + 1
			except:
				recovery_count = self.get_option(self.current_work + 'recovery_count')
				if recovery_count == None:
					recovery_count = 0

				if recovery_count > 2:
					self.status = self.last_status[self.current_work] + 1
					self.set_option(self.current_work + 'recovery_count', 0)
				else:
					self.logger.error(traceback.format_exc())
					self.set_option(self.current_work + 'recovery_count', recovery_count + 1)

		elif self.status == self.get_work_status('[작업 예약]'):

			self.logger.warn('[작업 예약]')
			self.game_object.wait_for_start_reserved_work = False
			self.status = self.last_status[self.current_work] + 1

		elif self.status == self.get_work_status('[작업 대기]'):
			elapsed_time = self.get_elapsed_time()
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_WAIT_FOR_NEXT))
			if elapsed_time > limit_time:
				self.set_option(self.current_work + '_end_flag', True)
			else:
				self.loggingElapsedTime('[작업 대기]', int(elapsed_time), limit_time, period=10)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

		elif self.status == self.get_work_status('[반복 시작]'):

			self.set_option('loop_start', self.last_status[self.current_work])
			self.status = self.last_status[self.current_work] + 1

		elif self.status == self.get_work_status('[반복 종료]'):

			loop_count = self.get_option('loop_count')
			if loop_count == None:
				loop_count = 1

			self.logger.debug('[반복 종료] ' + str(loop_count) + ' 회 수행 완료, ' +
			 str(int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_LOOP)) - loop_count) + ' 회 남음')
			if loop_count >= int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_LOOP)):
				self.status = self.last_status[self.current_work] + 1
				self.set_option('loop_count', 1)
				self.set_option('loop_start', None)
			else:
				self.status = self.get_option('loop_start')
				# print('DEBUG LOOP STATUS = ', self.status )

				if self.status == None:
					self.logger.debug('[반복 시작] 점을 찾지 못해서 다음 작업을 수행합니다')
					self.status = self.last_status[self.current_work] + 1

				self.set_option('loop_count', loop_count + 1)

		else:
			self.status = self.last_status[self.current_work] + 1


		return self.status













	def main_quest_pre_process(self):

		if self.status == self.get_work_status('메인 퀘스트'):
			pb_name = 'main_quest_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=100, custom_top_level=255)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.7:
				self.set_option(self.current_work + '_end_flag', True)
				return True
		elif self.status == self.get_work_status('길드 퀘스트'):
			pb_name = 'main_quest_guild_share'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.7:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				return True

		pb_name = 'main_quest_complete'
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			self.window_image,
			self.game_object.resource_manager.pixel_box_dic[pb_name],
			custom_threshold=0.7,
			custom_flag=1,
			custom_rect=(90, 100, 130, 250)
			)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if loc_x != -1:
			self.lyb_mouse_click_location(loc_x, loc_y)
			return True

		return False

	def main_scene_click_ililquest(self):

		ilil_pb_list = [
			'main_quest_ilil',
			'main_quest_ilil_0',
			'main_quest_ilil_1',

			]
		for pb_name in ilil_pb_list:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pb_name],
				custom_threshold=0.7,
				custom_flag=1,
				custom_rect=(20, 130, 50, 160)
				)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				return True

		return False


	def main_scene_click_guildquest(self):

		guild_pb_list = [
			'main_quest_guild',
			'main_quest_guild_0',
			'main_quest_guild_1',

			]
		for pb_name in guild_pb_list:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pb_name],
				custom_threshold=0.7,
				custom_flag=1,
				custom_rect=(20, 160, 50, 190)
				)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				return True

		return False

	def main_quest_character_move(self):

		cfg_move_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period'))
		if cfg_move_period == 0:
			return False

		elapsed_move = time.time() - self.get_checkpoint('main_quest_move_checkpoint')

		if elapsed_move < cfg_move_period:
			return False

		self.set_checkpoint('main_quest_move_checkpoint')

		move_index = self.get_option('main_quest_move')
		if move_index == None:
			move_index = 0

		random_direction = int(random.random() * 8)
		self.logger.warn('자동 사냥 랙 방지 움직임: ' + str(lybgamemu2.LYBMu2.character_move_list[move_index]))

		self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(move_index), stop_delay=1)
		self.set_option('main_quest_move', ( move_index + 1 ) % 8)

		return True



	def auto_off(self):

		pb_name = 'sudong'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate < 0.9:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True

		return False

	def auto_on(self):

		pb_name = 'sudong'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate > 0.8:
			sudong_threshold = self.get_option('sudong_threshold')
			if sudong_threshold == None:
				sudong_threshold = 0

			if sudong_threshold > 1:	
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('sudong_threshold', 0)
				return True
			else:
				self.set_option('sudong_threshold', sudong_threshold + 1)
		else:
			self.set_option('sudong_threshold', 0)

		return False

	def get_work_status(self, work_name):
		if work_name in lybgamemu2.LYBMu2.work_list:
			return (lybgamemu2.LYBMu2.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
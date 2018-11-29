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
import likeyoubot_linm as lybgamelinm
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBLinmScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBLinmScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'init_screen_scene':
			rc = self.init_screen_scene()
		elif self.scene_name == 'main_scene':
			rc = self.main_scene()
		elif self.scene_name == 'login_scene':
			rc = self.login_scene()
		elif self.scene_name == 'character_scene':
			rc = self.character_scene()
		elif self.scene_name == 'move_confirm_scene':
			rc = self.move_confirm_scene()
		elif self.scene_name == 'quest_accept_scene':
			rc = self.quest_accept_scene()
		elif self.scene_name == 'death_scene':
			rc = self.death_scene()
		elif self.scene_name == 'inventory_scene':
			rc = self.inventory_scene()
		elif self.scene_name == 'menu_scene':
			rc = self.menu_scene()
		elif self.scene_name == 'mail_scene':
			rc = self.mail_scene()
		elif self.scene_name == 'quest_scene':
			rc = self.quest_scene()

			



		else:
			rc = self.else_scene()

		return rc

	def else_scene(self):

		if self.status == 0:
			self.logger.info('unknown scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def quest_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 100:
			self.set_option('click_level', 0)
			self.status += 1
		elif self.status == 101:
			self.lyb_mouse_click('quest_scene_tab_0', custom_threshold=0)
			self.status += 1
		elif self.status == 102:
			click_level = self.get_option('click_level')
			if click_level > 5:
				self.status = 99999
			else:
				pb_name = 'quest_scene_level_' + str(click_level)
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('click_level', click_level + 1)
				self.set_option('last_status', self.status)
				self.status += 1
		elif self.status >= 103 and self.status < 105:	
			pb_name = 'quest_scene_go'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(300, 110, 360, 140)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
			if loc_x != -1:
				self.status = 106
				return self.status		

			self.status += 1
		elif self.status == 105:
			self.status = self.get_option('last_status')
		elif self.status == 106:
			resource_name_list = [
				'quest_scene_conversation_loc',		
				'quest_scene_meet_loc',				
				'quest_scene_bogo_loc',			
				'quest_scene_enter_loc',				
			]
			for resource_name in resource_name_list:
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
						self.window_image,
						resource_name,
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(370, 120, 620, 140),
						debug=True
						)
				self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
				if loc_x != -1:
					self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_inner_status', 10)
				else:
					self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_inner_status', 20)
				self.status = 99999
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status


	def inventory_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 200:
			self.lyb_mouse_click('inventory_scene_tab_2', custom_threshold=0)
			self.set_option('last_click_loc', (-1, -1))
			self.status += 1
		elif self.status >= 201 and self.status < 210:
			pb_name = self.get_option('search_item_pb_name')
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.85,
						custom_flag=1,
						custom_rect=(440, 100, 630, 290)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.set_option('last_click_loc', (loc_x, loc_y))
				self.status = 210
				return self.status
			else:
				if self.status % 2 == 0:
					self.lyb_mouse_drag('inventory_scene_drag_bot', 'inventory_scene_drag_top', stop_delay=1)
			self.status += 1
		elif self.status == 210:
			(loc_x, loc_y) = self.get_option('last_click_loc')
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def mail_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('mail_scene_receive_all', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def menu_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 3:
			pb_name_list = [
				'menu_scene_new_0',
				'menu_scene_new_1',
				'menu_scene_new_2',
			]
			for pb_name in pb_name_list:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.85,
							custom_flag=1,
							custom_rect=(440, 70, 635, 210)
								)
				self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
					self.game_object.get_scene('quest_scene').status = 0
					self.game_object.get_scene('menu_scene').status = 0
					return True
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def death_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

			if self.get_game_config(lybconstant.LYB_DO_STRING_LINM_NOTIFY + 'character_death') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 캐릭터 사망 감지')
				png_name = self.game_object.save_image('character_death')
				self.game_object.telegram_send('', image=png_name)
				
			self.status = 0

		return self.status

	def quest_accept_scene(self):

		self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
		self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_inner_status', 0)

		return self.status

	def move_confirm_scene(self):

		if self.get_option('free_pass') == True:
			self.set_option('free_pass', False)
			self.lyb_mouse_click('move_confirm_scene_ok', custom_threshold=0)
		else:
			pb_name = 'move_confirm_scene_free'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(390, 260, 440, 290)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + str(match_rate))
			if loc_x != -1:		
				self.lyb_mouse_click('move_confirm_scene_ok', custom_threshold=0)
			else:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
		return self.status

	def character_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			pb_name = 'character_scene_enter'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(500, 330, 590, 375)
							)
			if loc_x != -1:		
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status
			
	def login_scene(self):
		self.game_object.current_matched_scene['name'] = ''

		self.schedule_list = self.get_game_config('schedule_list')

		if not '로그인' in self.schedule_list:
			return 0

		elapsedTime = time.time() - self.get_checkpoint('start')
		if elapsedTime > 300:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('start')			
			if self.get_window_config('multi_account'):
				self.logger.error('구글 멀티 계정 전환 기능을 지원하지 않습니다.')
				self.status += 1
			else:
				self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
			self.status += 1
		elif self.status >= 2 and self.status < 6:
			self.status += 1
		elif self.status == 6:
			self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
			self.status += 1
		elif self.status >= 7 and self.status < 10:
			self.status += 1
		elif self.status >= 10 and self.status < 240:
			if self.status % 5 == 0:
				self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
			self.logger.info('로그인 화면 랙 인식: ' + str(self.status - 10) + '/240')
			self.status += 1
		elif self.status == 240:
			self.game_object.terminate_application()
			self.status += 1
		elif self.status == 300:
			self.game_object.get_scene('connect_account_scene').status = 0
			self.game_object.get_scene('connect_account_2_scene').status = 0
			self.lyb_mouse_click(self.scene_name + '_account', custom_threshold=0)
			self.status += 1
		elif self.status == 301:
			self.status += 1
		elif self.status == 302:
			self.status = 1
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
			for each_icon in lybgamelinm.LYBLinm.linm_icon_list:
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
		else:
			for each_icon in lybgamelinm.LYBLinm.linm_icon_list:
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






















































































	#################################
	#                               #
	#                               #
	#			MAIN SCENE 			#
	#                               #
	#                               #
	#################################
	
	def main_scene(self):

		if self.game_object.current_schedule_work != self.current_work:
			self.game_object.current_schedule_work = self.current_work

		self.game_object.main_scene = self

		is_clicked = self.pre_process_main_scene()
		if is_clicked == True:
			return self.status

		self.schedule_list = self.get_game_config('schedule_list')
		if len(self.schedule_list) == 1:
			self.logger.warn('스케쥴 작업이 없어서 종료합니다.')
			return -1

		if self.status == 0:
			self.status += 1
		elif self.status >= 1 and self.status < 1000:

			self.set_schedule_status()

		elif self.status == self.get_work_status('메인 퀘스트'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(600):
				self.set_option(self.current_work + '_end_flag', True)	

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_inner_status', None)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			inner_status = self.get_option(self.current_work + '_inner_status')
			if inner_status == None:
				inner_status = 0

			self.logger.debug('inner_status: ' + str(inner_status))

			if inner_status == 0:
				if self.pre_process_main_quest() == True:
					return self.status
				else:
					(loc_x, loc_y), match_rate = self.locationOnQuestArea('main_scene_quest_main')
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
					else:
						self.lyb_mouse_click('main_scene_quest_main', custom_threshold=0)
					self.set_option(self.current_work + '_inner_status', inner_status + 1)
			elif inner_status >= 1 and inner_status < 10:

				if self.isSafetyZone() == True:
					self.set_option(self.current_work + '_inner_status', 10)
				else:
					self.lyb_mouse_click('main_scene_quest', custom_threshold=0)
					self.game_object.get_scene('quest_scene').status = 100
					self.set_option(self.current_work + '_inner_status', inner_status + 1)

			elif inner_status >= 10 and inner_status < 15:
				pb_name_list = [
					'main_scene_quest_npc',
					'main_scene_dungeon_npc',
				]
				for pb_name in pb_name_list:
					(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
									self.window_image,
									self.game_object.resource_manager.pixel_box_dic[pb_name],
									custom_threshold=0.8,
									custom_flag=1,
									custom_rect=(190, 70, 510, 260)
									)
					self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						if pb_name == 'main_scene_dungeon_npc':
							self.game_object.get_scene('move_confirm_scene').set_option('free_pass', True)
						self.set_option(self.current_work + '_inner_status', 0)
						return self.status

				self.set_option(self.current_work + '_inner_status', inner_status + 1)

			elif inner_status >= 15 and inner_status < 20:
				self.set_option(self.current_work + '_inner_status', 0)				
			elif inner_status >= 20 and inner_status < 100:

				if self.isAutoOn(limit_count=5) == False:
					self.lyb_mouse_click('main_scene_auto', custom_threshold=0)

				self.set_option(self.current_work + '_inner_status', inner_status + 1)
			else:
				self.set_option(self.current_work + '_inner_status', 0)


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















	def pre_process_main_scene(self):


		pb_name = 'main_scene_potion_empty'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate > 0.98:
			if self.process_charge_potion() == True:
				return True

		pb_name_list = [
			'main_scene_new_0',
			'main_scene_new_1',
		]
		for pb_name in pb_name_list:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.85,
						custom_flag=1,
						custom_rect=(560, 35, 635, 60)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
				self.game_object.get_scene('quest_scene').status = 0
				self.game_object.get_scene('menu_scene').status = 0
				return True
		
		return False

	def pre_process_main_quest(self):
		return False

	def process_charge_potion(self):
		return False

	def locationOnQuestArea(self, pb_name, custom_top_level=-1, custom_below_level=-1):
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic[pb_name],
					custom_threshold=0.85,
					custom_flag=1,
					custom_top_level=custom_top_level,
					custom_below_level=custom_below_level,
					custom_rect=(5, 125, 35, 250)
						)
		self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))

		return (loc_x, loc_y), match_rate

	def isAutoOn(self, limit_count=5):
		return self.isStatusByResource (
			'[자동전투]', 
			'auto_on_loc', 
			0.5, 
			-1, -1, 
			(280, 250, 365, 280),
			limit_count=limit_count,
			average=True
			)

	def isSafetyZone(self):

		resource_name = 'main_scene_safety_zone_loc'
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
				self.window_image,
				resource_name,
				custom_threshold=0.8,
				custom_top_level=(50, 170, 255),
				custom_below_level=(0, 100, 160),
				custom_flag=1,
				custom_rect=(550, 180, 620, 200)
				)
		self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			return True

		return False

	def isStatusByResource(self, log_message, resource_name, custom_threshold, custom_top_level, custom_below_level, custom_rect, limit_count=-1, average=False):
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
				self.window_image,
				resource_name,
				custom_threshold=custom_threshold,
				custom_top_level=custom_top_level,
				custom_below_level=custom_below_level,
				custom_flag=1,
				custom_rect=custom_rect,
				debug=True,
				average=average
				)
		self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			self.set_option(resource_name + 'check_count', 0)
			return True

		check_count = self.get_option(resource_name + 'check_count')
		if check_count == None:
			check_count = 0

		if check_count > limit_count:
			self.set_option(resource_name + 'check_count', 0)
			return False

		self.logger.debug(log_message + '..(' + str(check_count) + '/' + str(limit_count) + ')')
		self.set_option(resource_name + 'check_count', check_count + 1)

		return True

	def get_work_status(self, work_name):
		if work_name in lybgamelinm.LYBLinm.work_list:
			return (lybgamelinm.LYBLinm.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
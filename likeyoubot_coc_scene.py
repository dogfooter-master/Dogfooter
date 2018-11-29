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
import likeyoubot_coc as lybgamecoc
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBCOCScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBCOCScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'init_screen_scene':
			rc = self.init_screen_scene()
		elif self.scene_name == 'main_scene':
			rc = self.main_scene()
		elif self.scene_name == 'chat_scene':
			rc = self.chat_scene()
		elif self.scene_name == 'donate_scene':
			rc = self.donate_scene()
		elif self.scene_name == 'army_scene':
			rc = self.army_scene()
		elif self.scene_name == 'attack_lobby_scene':
			rc = self.attack_lobby_scene()
		elif self.scene_name == 'combat_ready_scene':
			rc = self.combat_ready_scene()


			



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


	def combat_ready_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 10:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def attack_lobby_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status = 10
		elif self.status == 10:

			pb_name = 'attack_lobby_scene_attack'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic[pb_name],
					custom_threshold=0.8,
					custom_flag=1,
					custom_rect=(300, 40, 630, 340)
					)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
			if loc_x != -1:
				self.game_object.get_scene('combat_ready_scene').status = 10
				self.lyb_mouse_click_location(loc_x, loc_y)

		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def army_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('army_train_tab', custom_threshold=0)
			self.status += 1
		elif self.status >= 2 and self.status < 6:
			self.lyb_mouse_click('army_train_scene_golem', custom_threshold=0)
			self.status += 1
		elif self.status >= 6 and self.status < 11:
			self.lyb_mouse_click('army_train_scene_giant', custom_threshold=0)
			self.status += 1
		elif self.status == 11:		
			self.lyb_mouse_click('army_brew_tab', custom_threshold=0)
			self.status += 1
		elif self.status >= 12 and self.status < 20:
			pb_name = 'army_brew_scene_earthquake'
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			self.status += 1		
		elif self.status == 20:
			self.lyb_mouse_click('army_build_siege_machines_tab', custom_threshold=0)
			self.status += 1		
		elif self.status >= 21 and self.status < 25:
			pb_name = 'army_build_siege_machines_scene_sm'
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def donate_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			command = self.get_option('command')
			self.logger.debug('command: ' + str(command))

			if command == None:
				command = 0

			if command == 0:
				pb_name_list = [
					'donate_scene_unit_wallwrecker',
					'donate_scene_unit_golem',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_spell_earthquake',
				]
			elif command == 1:
				# 암거나 부탁드려요
				pb_name_list = [
					'donate_scene_unit_wallwrecker',
					'donate_scene_unit_golem',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_spell_earthquake',
				]
			elif command == 2:	
				# 발키리	
				pb_name_list = [
					'donate_scene_unit_wallwrecker',
					'donate_scene_spell_earthquake',
				]		
			else:
				pb_name_list = [
					'donate_scene_unit_wallwrecker',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_unit_giant',
					'donate_scene_spell_earthquake',
				]

			self.set_option('donate_list', pb_name_list)
			self.status += 1
		elif self.status == 2:
			pb_name_list = self.get_option('donate_list')
			if len(pb_name_list) > 0:
				i = 0
				for pb_name in pb_name_list:
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(260, 50, 600, 290)
							)
					self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						break
					else:
						i += 1

				try:
					for j in range(i + 1):
						pb_name_list.pop(0)
				except:
					self.status = 99999
					return self.status

				self.logger.info(pb_name_list)
				self.set_option('donate_list', pb_name_list)
			else:
				self.status = 99999					
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def chat_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.set_option('last_row', 0)
			self.status += 1
		elif self.status == 1:
			last_row = self.get_option('last_row')
			for i in range(last_row, 4):
				pb_name = 'chat_scene_donate'
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(160, 120 + (60*i) - 40, 240, 120 + (60*i) + 50)
						)
				self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
				if loc_x != -1:
					self.set_option('click_loc', (loc_x, loc_y))					
					adj_x, adj_y = self.game_object.get_player_adjust()
					self.set_option('custom_rect', (20, 120 + (60*i) - 40 - adj_y, 160, 120 + (60*i) + 50 - adj_y))
					self.set_option('last_row', i + 1)
					self.set_option('last_status', self.status)
					self.game_object.get_scene('donate_scene').set_option('command', -1)
					self.status = 10
					return self.status
			self.status = 99999
		elif self.status == 10:
			custom_rect = self.get_option('custom_rect')
			for i in range(3):
				resource_name = 'chat_scene_donate_command_' + str(i) + '_loc'
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
						self.window_image,
						resource_name,
						custom_threshold=0.7,
						custom_top_level=(255, 255, 255),
						custom_below_level=(200, 200, 200),
						custom_flag=1,
						custom_rect=custom_rect	)
				self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
				if loc_x != -1:
					(c_loc_x, c_loc_y) = self.get_option('click_loc')
					self.lyb_mouse_click_location(c_loc_x, c_loc_y)
					self.game_object.get_scene('donate_scene').set_option('command', i)
					self.game_object.get_scene('donate_scene').status = 0
					break

			self.status = self.get_option('last_status')
		elif self.status == 99999:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def init_screen_scene(self):
		
		self.schedule_list = self.get_game_config('schedule_list')
		if not '게임 시작' in self.schedule_list:
			return 0


		loc_x = -1
		loc_y = -1


		if self.game_object.player_type == 'nox':
			for each_icon in lybgamecoc.LYBCOC.coc_icon_list:
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
			for each_icon in lybgamecoc.LYBCOC.coc_icon_list:
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

		elif self.status == self.get_work_status('기부'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)	

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_inner_status', None)
				self.status = self.last_status[self.current_work] + 1
				return self.status		

			self.game_object.get_scene('chat_scene').status = 0
			self.lyb_mouse_click('main_scene_open_chat', custom_threshold=0)


		elif self.status == self.get_work_status('병력'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)	

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status		

			self.game_object.get_scene('army_scene').status = 0
			self.lyb_mouse_click('main_scene_army', custom_threshold=0)

		elif self.status == self.get_work_status('자원'):

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

			if inner_status == 0:
				self.set_option(self.current_work + '_direction', 0)
				self.set_option(self.current_work + '_inner_status', inner_status + 1)
			elif inner_status == 1:
				pb_name = 'main_scene_attack'
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.game_object.get_scene('attack_lobby_scene').status = 10
				self.set_option(self.current_work + '_inner_status', inner_status + 1)
			elif inner_status == 2:
				self.set_option(self.current_work + '_drag_count', 0)
				self.set_option(self.current_work + '_inner_status', inner_status + 1)
			elif inner_status == 3:				
				direction = self.get_option(self.current_work + '_direction')
				if direction > 7:	
					self.set_option(self.current_work + '_end_flag', True)					
				else:
					drag_count = self.get_option(self.current_work + '_drag_count')
					if drag_count > 1:
						self.set_option(self.current_work + '_inner_status', inner_status - 2)
						self.set_option(self.current_work + '_direction', direction + 1)
					else:
						self.logger.debug('자원 탐색 ' + str(lybgamecoc.LYBCOC.move_list[direction]))
						self.lyb_mouse_drag('move_direction_center_' + str(direction), 'move_direction_center', stop_delay=1)
						self.set_option(self.current_work + '_drag_count', drag_count + 1)
						self.set_option(self.current_work + '_inner_status', inner_status + 1)
			elif inner_status == 4:
				pb_name_list = [
					'main_scene_resource_gold',
					'main_scene_resource_elixir',
					'main_scene_resource_dark_elixir',
				]
				self.set_option(self.current_work + '_inner_status', inner_status + 1)
				self.set_option(self.current_work + '_pb_name_list', pb_name_list)
				for pb_name in pb_name_list:
					self.set_option(pb_name + '_find', False)
			elif inner_status >= 5 and inner_status < 10:
				pb_name_list = self.get_option(self.current_work + '_pb_name_list')
				is_complete = True
				for pb_name in pb_name_list:
					if self.get_option(pb_name + '_find') == False:
						is_complete = False

				if is_complete == True:
					self.set_option(self.current_work + '_end_flag', True)	
				else:
					is_found = False
					for pb_name in pb_name_list:
						(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(115, 70, 510, 370)
								)
						self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
						if loc_x != -1:
							self.lyb_mouse_click_location(loc_x, loc_y)
							self.set_option(pb_name + '_find', True)
							is_found = True

					if is_found == False:
						self.set_option(self.current_work + '_inner_status', inner_status - 2)
					else:
						self.set_option(self.current_work + '_inner_status', inner_status + 1)

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

		return False


	def get_work_status(self, work_name):
		if work_name in lybgamecoc.LYBCOC.work_list:
			return (lybgamecoc.LYBCOC.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
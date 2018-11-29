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
import likeyoubot_clans as lybgameclans
from likeyoubot_configure import LYBConstant as lybconstant

import likeyoubot_scene
import time

class LYBClansScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBClansScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'nox_init_screen_scene':
			rc = self.nox_init_screen_scene()
		elif self.scene_name == 'clans_google_play_account_select_scene':
			rc = self.clans_google_play_account_select_scene()
		elif self.scene_name == 'clans_change_account_scene':
			rc = self.clans_change_account_scene()
		elif self.scene_name == 'clans_login_scene':
			rc = self.clans_login_scene()
		elif self.scene_name == 'clans_login_2_scene':
			rc = self.clans_login_2_scene()
		elif self.scene_name == 'clans_character_select_scene':
			rc = self.clans_character_select_scene()
		elif self.scene_name == 'clans_login_ads_scene':
			rc = self.clans_login_ads_scene()
		elif self.scene_name == 'clans_main_scene':
			rc = self.clans_main_scene()
		# elif self.scene_name == 'clans_main_combat_manual_scene':
		# 	rc = self.clans_main_combat_manual_scene()
		# elif self.scene_name == 'clans_main_field_peace_scene':
		# 	rc = self.clans_main_scene(mode='peace')
		# elif self.scene_name == 'clans_main_field_clan_scene':
		# 	rc = self.clans_main_scene(mode='clan')
		# elif self.scene_name == 'clans_main_field_free_scene':
		# 	rc = self.clans_main_scene(mode='free')
		# elif self.scene_name == 'clans_main_skill_scene':
		# 	rc = self.clans_main_scene(mode='skill')
		elif self.scene_name == 'clans_colleague_scene':
			rc = self.clans_colleague_scene()
		elif self.scene_name == 'clans_mission_scene':
			rc = self.clans_mission_scene()
		elif self.scene_name == 'clans_character_information_scene':
			rc = self.clans_character_information_scene()
		elif self.scene_name == 'clans_control_scene':
			rc = self.clans_control_scene()
		elif self.scene_name == 'clans_auto_mode_config_scene':
			rc = self.clans_auto_mode_config_scene()
		elif self.scene_name == 'clans_bonus_scene':
			rc = self.clans_bonus_scene()
		elif self.scene_name == 'clans_achievement_scene':
			rc = self.clans_achievement_scene()
		elif self.scene_name == 'clans_world_map_scene':
			rc = self.clans_world_map_scene()
		elif self.scene_name == 'clans_event_scene':
			rc = self.clans_event_scene()
		elif self.scene_name == 'clans_hero_scene':
			rc = self.clans_hero_scene()
		elif self.scene_name == 'clans_treasure_scene':
			rc = self.clans_treasure_scene()
		elif self.scene_name == 'clans_treasure_search_scene':
			rc = self.clans_treasure_search_scene()
		elif self.scene_name == 'clans_combat_scene':
			rc = self.clans_combat_scene()
		elif self.scene_name == 'clans_party_mission_scene':
			rc = self.clans_party_mission_scene()
		elif self.scene_name == 'clans_arena_scene':
			rc = self.clans_arena_scene()
		elif self.scene_name == 'clans_arena_combat_scene':
			rc = self.clans_arena_combat_scene()
		elif self.scene_name == 'clans_clan_scene':
			rc = self.clans_clan_scene()
		elif self.scene_name == 'clans_clan_bangpawon_scene':
			rc = self.clans_clan_bangpawon_scene()
		elif self.scene_name == 'clans_clan_building_scene':
			rc = self.clans_clan_building_scene()
		elif self.scene_name == 'clans_clan_youngto_scene':
			rc = self.clans_clan_youngto_scene()
		elif self.scene_name == 'clans_clan_chest_scene':
			rc = self.clans_clan_chest_scene()
		elif self.scene_name == 'clans_sooryun_scene':
			rc = self.clans_sooryun_scene()
		elif self.scene_name == 'clans_local_map_scene':
			rc = self.clans_local_map_scene()
		elif self.scene_name == 'clans_gibodang_scene':
			rc = self.clans_gibodang_scene()
		elif self.scene_name == 'clans_dongryo_scene':
			rc = self.clans_dongryo_scene()
		elif self.scene_name == 'clans_sohwan_scene':
			rc = self.clans_sohwan_scene()
		elif self.scene_name == 'tera_murim_mengju_scene':
			rc = self.tera_murim_mengju_scene()
		elif self.scene_name == 'clans_sangdan_scene':
			rc = self.clans_sangdan_scene()
		else:
			rc = 0

		return rc

	def clans_sangdan_scene(self):

		if self.status == 0:
			self.set_option('request_count', 0)

		if self.status >= 0 and self.status < 10:
			item_name = self.get_game_config(lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(self.status))
			print('[CLANS DEBUG]:',	item_name )

			self.loggingToGUI(item_name + ' 탐색')
			item_index = lybgameclans.LYBClans.sangdan_item_list.index(item_name)
			item_pb = 'clans_sangdan_item_' + str(item_index)

			try:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
												self.window_image,
												self.game_object.resource_manager.pixel_box_dic[item_pb],
												custom_flag=1,
												custom_rect=(220, 70, 280, 340)
												)
			except:
				print('[CLANS DEBUG] Exception', item_name)
				# REMOVE ME
				self.status += 1
				return self.status

			print('[CLANS DEBUG]:', item_pb, (loc_x, loc_y), match_rate)
			if loc_x != -1:
				# self.lyb_mouse_click_location(loc_x + 50, loc_y)
				self.set_option('last_status', self.status)
				self.set_option('retry_count', 0)
				self.lyb_mouse_click_location(loc_x + 230, loc_y)
				# self.lyb_mouse_move_location(loc_x + 230, loc_y)
				self.status += 1
			else:
				retry_count = self.get_option('retry_count')
				if retry_count == None:
					retry_count = 0

				if retry_count == 4:
					self.set_option('retry_count', 0)
					self.status += 1
				else:
					if retry_count < 2:
						self.lyb_mouse_drag('clans_sangdan_scene_drag_bottom', 'clans_sangdan_scene_drag_top')
					else:
						self.lyb_mouse_drag('clans_sangdan_scene_drag_top', 'clans_sangdan_scene_drag_bottom')
	
					self.game_object.interval = 1
					self.set_option('retry_count', retry_count+1)
		elif self.status == 10:
			for i in range(3):
				self.lyb_mouse_drag('clans_sangdan_scene_drag_top', 'clans_sangdan_scene_drag_bottom')
				time.sleep(1)
			self.status += 1
		elif self.status == 11:
			for i in range(4):
				self.lyb_mouse_click('clans_sangdan_scene_top_'+str(i))
			self.status = 100
		elif self.status >= 100 and self.status < 130:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic['clans_sangdan_scene_chejip'],
											custom_flag=1,
											custom_rect=(510, 70, 590, 340)
											)
			print('[CLANS DEBUG]: clans_sangdan_scene_chejip', (loc_x, loc_y), match_rate)

			if loc_x != -1:
				# self.lyb_mouse_click_location(loc_x + 50, loc_y)
				self.set_option('last_status', self.status)
				self.set_option('retry_count', 0)
				self.lyb_mouse_click_location(loc_x, loc_y)
				# self.lyb_mouse_move_location(loc_x, loc_y)
				time.sleep(1)
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				self.status += 1
			else:
				retry_count = self.get_option('retry_count')
				if retry_count == None:
					retry_count = 0

				if retry_count == 4:
					self.set_option('retry_count', 0)
					self.status = 110
				else:
					if retry_count < 2:
						self.lyb_mouse_drag('clans_sangdan_scene_drag_bottom', 'clans_sangdan_scene_drag_top')
					else:
						self.lyb_mouse_drag('clans_sangdan_scene_drag_top', 'clans_sangdan_scene_drag_bottom')
	
					self.game_object.interval = 1
					self.set_option('retry_count', retry_count+1)
		elif self.status == 130:
			for i in range(3):
				self.lyb_mouse_drag('clans_sangdan_scene_drag_top', 'clans_sangdan_scene_drag_bottom')
				time.sleep(1)
			self.status += 1
		elif self.status >= 131 and self.status < 998:

			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic['clans_sangdan_scene_jechool'],
											custom_flag=1,
											custom_rect=(510, 70, 590, 340)
											)
			print('[CLANS DEBUG]: clans_sangdan_scene_jechool', (loc_x, loc_y), match_rate)

			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_sangdan_scene_complete_10')
			if match_rate > 0.9:
				self.status = 998
			else:
				self.status += 1

			self.lyb_mouse_drag('clans_sangdan_scene_drag_top', 'clans_sangdan_scene_drag_bottom')
			time.sleep(1)

		elif self.status == 998:
			self.lyb_mouse_click('clans_sangdan_scene_bogo')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_murim_mengju_scene(self):

		self.lyb_mouse_click('tera_murim_mengju_scene_dojun')

		return self.status

	def clans_sohwan_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('clans_sohwan_scene_silver_free')
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('clans_sohwan_scene_wonbo_free')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_dongryo_scene(self):

		if self.status == self.get_work_status('동료 무료 소환'):
			self.lyb_mouse_click('clans_dongryo_scene_sohwan', custom_threshold=0)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_gibodang_scene(self):

		item_count = len(lybgameclans.LYBClans.gibodang_item_list)
		if self.status >= 0 and self.status < item_count:
			print('[CLANS DEBUG]:', 
				lybgameclans.LYBClans.gibodang_item_list[self.status],
				self.get_game_config(lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(self.status)) )
			
			while True:
				if self.status >= item_count:
					return self.status
				if self.get_game_config(lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(self.status)) == True:
					break
				self.status += 1

			self.loggingToGUI(lybgameclans.LYBClans.gibodang_item_list[self.status] + ' 구매 시도')
			item_pb = 'clans_gibodang_item_' + str(self.status)

			if '영혼석 상자' in lybgameclans.LYBClans.gibodang_item_list[self.status]:
				custom_threshold = 0.95
			else:
				custom_threshold = 0.7

			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[item_pb],
											custom_threshold=custom_threshold,
											custom_flag=1,
											custom_rect=(50, 80, 300, 360)
											)
			print('[CLANS DEBUG]:', item_pb, (loc_x, loc_y), match_rate)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x + 50, loc_y)
				self.set_option('last_status', self.status)
				self.set_option('retry_count', 0)
				self.status = 100
			else:
				retry_count = self.get_option('retry_count')
				if retry_count == None:
					retry_count = 0

				if retry_count == 2:
					self.set_option('retry_count', 0)
					self.status += 1
				else:
					if retry_count == 0:
						self.lyb_mouse_drag('clans_gibodang_scene_drag_bottom', 'clans_gibodang_scene_drag_top')
					else:
						self.lyb_mouse_drag('clans_gibodang_scene_drag_top', 'clans_gibodang_scene_drag_bottom')
	
					self.game_object.interval = 1
					self.set_option('retry_count', retry_count+1)

		elif self.status == 100:
			self.lyb_mouse_click('clans_gibodang_scene_number', custom_threshold=0)
			self.status += 1
		elif self.status == 101:
			self.lyb_mouse_click('clans_gibodang_scene_number_9', custom_threshold=0)
			self.lyb_mouse_click('clans_gibodang_scene_number_9', custom_threshold=0)
			self.status += 1
		elif self.status == 102:
			self.lyb_mouse_click('clans_gibodang_scene_gume', custom_threshold=0)
			self.status += 1
		elif self.status == 103:
			self.status = self.get_option('last_status') + 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_local_map_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('안전 지대로 이동'):
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['clans_safetyzone'],
						custom_threshold=0.45,
						custom_flag=1,
						custom_rect=(85, 120, 380, 300)
						)
			print((loc_x, loc_y), match_rate)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x+10, loc_y)
			self.status = 99999
		elif self.status == self.get_work_status('자동 사냥'):
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['clans_local_map_scene_pc'],
						custom_threshold=0.45,
						custom_flag=1,
						custom_rect=(85, 120, 380, 300)
						)
			print((loc_x, loc_y), match_rate)
			if loc_x != -1:
				self.game_object.get_scene('clans_main_scene').set_option('jasa_location', (loc_x, loc_y))
			self.status = 99999
		elif self.status == self.get_work_status('자동 사냥') + 1:
			(loc_x, loc_y) = self.game_object.get_scene('clans_main_scene').get_option('jasa_location')
			self.lyb_mouse_click_location(loc_x, loc_y)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_sooryun_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_clan_chest_scene(self):

		if self.status == self.get_work_status('방파 기부'):
			#방파 기부
			self.lyb_mouse_click('clans_clan_chest_scene_donate_button')
			self.game_object.get_scene('clans_clan_scene').set_option('donate_complete', True)
			self.status = 99999
		elif self.status == self.get_work_status('방파 선물'):
			#방파 선물
			self.lyb_mouse_click('clans_clan_chest_scene_box_exchange_button')
			self.status = 99999
		else:
			self.lyb_mouse_click('clans_clan_chest_scene_close_icon')
			self.status = 0

		return self.status

	def clans_clan_bangpawon_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('clans_clan_scene_jungbo', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def clans_clan_building_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('clans_clan_scene_jungbo', custom_threshold=0)
			self.status += 1
		elif (	self.status == self.get_work_status('방파 기부') or
				self.status == self.get_work_status('방파 선물')
				):
			self.lyb_mouse_click('clans_clan_scene_chest')		
			self.game_object.get_scene('clans_clan_chest_scene').status = self.status
			self.status = 99999
		elif self.status == self.get_work_status('귀보당'):
			self.lyb_mouse_click('clans_clan_scene_gibodang', custom_threshold=0)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def clans_clan_youngto_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('clans_clan_scene_jungbo', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_clan_scene(self):
		
		if self.status == 0:
			self.status = 10
		elif self.status == self.get_work_status('방파 기부'):
			if self.get_option('donate_complete') == True:
				self.status = 99999
			else:
				self.lyb_mouse_click('clans_clan_scene_building_tab', custom_threshold=0)
				self.game_object.get_scene('clans_clan_building_scene').status = self.status
				self.status = 99999
		elif self.status == self.get_work_status('방파 선물'):
			elapsed_time = time.time() - self.get_checkpoint('last_gift')
			if elapsed_time < 3600:
				self.status = 99999
			else:
				self.lyb_mouse_click('clans_clan_scene_building_tab', custom_threshold=0)
				self.game_object.get_scene('clans_clan_building_scene').status = self.status
			self.status = 999999
		elif self.status == self.get_work_status('귀보당'):
			self.lyb_mouse_click('clans_clan_scene_building_tab', custom_threshold=0)
			self.game_object.get_scene('clans_clan_building_scene').status = self.status
			self.status = 99999
		else:
			self.lyb_mouse_click('clans_clan_scene_close_icon')
			self.status = 0

		return self.status

	def clans_arena_combat_scene(self):
		self.status += 1

		if self.status > 999999:
			self.status = 0

		return self.status

	def clans_arena_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		if not '무신전' in self.schedule_list:
			self.status = 99999

		if self.status == 0:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_arena_scene_remain_count')
			if match_rate > 0.9:
				self.status = 99999
			else:
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_arena_scene_reward_notify')
				if match_rate > self.get_window_config('threshold_entry'):
					self.lyb_mouse_click('clans_arena_scene_reward_button')
				self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('clans_arena_scene_refresh_button')
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('clans_arena_scene_challenge_button', custom_threshold=0)
			self.set_checkpoint('challenge_start')
			self.status += 1
		elif self.status == 3:
			elapsed_time = time.time() - self.get_checkpoint('challenge_start')
			if elapsed_time > 10:
				self.status = 0
		else:
			self.lyb_mouse_click('clans_arena_scene_close_icon')
			self.status = 0

		return self.status

	def clans_party_mission_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('clans_party_mission_scene_close_icon')

		return self.status

	def clans_combat_scene(self):

		if self.game_object.get_scene('clans_main_scene').current_work != '메인 퀘스트':
			rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_combat_manual_scene_sudong_icon')
			if rate_match > 0.9:
				self.lyb_mouse_click('clans_main_combat_manual_scene_sudong_icon')

		self.clans_main_scene(mode='combat')

		return self.status

	def clans_treasure_search_scene(self):
		if self.status == 0:
			self.set_checkpoint('start_time')
			self.status += 1
		elif self.status == 1:
			elapsed_time = time.time() - self.get_checkpoint('start_time')
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_treasure_search_scene_remain_0')
			if elapsed_time > 120 or match_rate > self.get_window_config('threshold_entry'):
				self.status = 99999
				return self.status

			self.set_checkpoint('search_treasure')
			self.lyb_mouse_click('clans_treasure_search_scene_button')
			self.status += 1
		elif self.status == 2:
			elapsed_time = time.time() - self.get_checkpoint('search_treasure')
			if elapsed_time > 5:
				self.status = 1
		else:
			self.lyb_mouse_click('clans_treasure_search_scene_close_icon')
			self.game_object.get_scene('clans_treasure_scene').set_option('completed', True)
			self.status = 0

		return self.status

	def clans_treasure_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		if not '보물 탐색' in self.schedule_list:
			self.status = 99999

		if self.status >= 0 and self.status < 6:
			self.set_checkpoint('click_time')
			self.lyb_mouse_click('clans_treasure_scene_entry_' + str(self.status), custom_threshold=0)
			self.last_status['treasure_entry'] = self.status
			self.set_option('completed', False)
			self.status = 10
		elif self.status == 10:
			elapsed_time = time.time() - self.get_checkpoint('click_time')
			if elapsed_time < 5:
				self.status = self.last_status['treasure_entry'] + 1
			else:
				self.status = 99999
		else:
			self.set_option('completed', True)
			self.lyb_mouse_click('clans_treasure_scene_close_icon')
			self.status = 0

		return self.status

	def clans_hero_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')
		if not '영웅 도전' in self.schedule_list:
			self.status = 99999

		if self.status == 0:
			self.lyb_mouse_click('clans_hero_scene_immediate_button', custom_threshold=0)
			self.set_checkpoint('button_press')
			self.set_option('completed', False)
			self.status += 1
		elif self.status == 1:
			elapsed_time = time.time() - self.get_checkpoint('button_press')
			if elapsed_time < 6:
				pass
			elif elapsed_time >= 6 and elapsed_time < 10:
				if self.get_option('remain') == True:
					self.status = 99999
				else:
					self.set_option('remain', True)
					self.status = 0
			else:
				self.set_checkpoint('button_press')
				self.set_option('remain', False)
				# self.status = 0
		else:
			self.lyb_mouse_click('clans_hero_scene_close_icon')
			self.set_option('completed', True)
			self.status = 0

		return self.status

	def clans_event_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')
		search_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_EVENT))

		if self.status == 0:
			self.set_checkpoint('start_time')

			elapsed_time = time.time() - self.get_checkpoint('daily_reward')
			if elapsed_time > int(self.get_game_config(lybconstant.LYB_DO_STRING_DAILY_REWARD)*60):
				self.status = self.get_work_status('임무 보상')
			elif self.get_option('event_tab') == None or self.get_option('event_tab') == 'daily':
				self.lyb_mouse_click('clans_event_scene_daily_tab', custom_threshold=0)

				self.status += 1

				if self.get_option('event') == '영웅 도전':
					self.set_option('click_icon', 'clans_event_scene_hero_icon')
					self.set_option('next_scene', 'clans_hero_scene')
				elif self.get_option('event') == '보물 탐색':
					self.set_option('click_icon', 'clans_event_scene_search_treasure_icon')
					self.set_option('next_scene', 'clans_treasure_scene')				
				elif self.get_option('event') == '무신전':
					self.set_option('click_icon', 'clans_event_scene_arena_icon')
					self.set_option('next_scene', 'clans_arena_scene')			
				else:
					self.status = 99999
		elif self.status == 1:
			if not self.get_option('event') in self.schedule_list:
				self.status = 99999
			elif self.game_object.get_scene(self.get_option('next_scene')).get_option('completed') == True:
				self.status = 99999
			else:
				self.last_status['event_scene'] = self.status
				self.status = 100
		elif self.status == 2:
			self.status = 5
		elif self.status == 5:
			if self.get_option('search_fail') == True:
				self.set_option('search_fail', False)
				elapsed_time = time.time() - self.get_checkpoint('start_time')
				if elapsed_time < search_limit:
					self.status = 1
				else:
					# 가려서 못찾은거라고 판단하고 맨 위 오른쪽을 클릭한다.
					for i in range(4):
						self.lyb_mouse_drag('clans_event_scene_drag_top', 'clans_event_scene_drag_bottom')
					time.sleep(2)
					#화면이 변경되었기 때문에 매칭이 안된다. 무조건 0을 줍시다.
					self.lyb_mouse_click('clans_event_scene_enter_0', custom_threshold=0)
					self.status = 99999

				return self.status

			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic[self.get_option('click_icon')],
				custom_threshold = float(self.game_object.get_window_config('threshold_entry') * 1.1)
				)
			self.loggingToGUI(self.get_option('event') + ' 아이콘 위치:' + str((loc_x, loc_y)))
			if loc_x == -1:
				self.last_status['event_scene'] = 2
				self.status = 200
			else:
				self.lyb_mouse_click_location(loc_x, loc_y + 70)
				self.status = 99999
		elif self.status == 100:
			for i in range(4):
				self.lyb_mouse_drag('clans_event_scene_drag_top', 'clans_event_scene_drag_bottom')
			self.status = self.last_status['event_scene'] + 1
		elif self.status == 200:
			for i in range(2):
				self.lyb_mouse_drag('clans_event_scene_drag_bottom', 'clans_event_scene_drag_top')

			retry_count = self.get_option('search_fail_retry')
			if retry_count == None:
				retry_count = 0

			retry_count += 1
			print('retry_count=', retry_count)
			if retry_count > 4:
				self.set_option('search_fail', True)
				self.set_option('search_fail_retry', 0)
			else:
				self.set_option('search_fail_retry', retry_count)
			
			self.status = self.last_status['event_scene']
		elif self.status == self.get_work_status('임무 보상'):
			self.lyb_mouse_click('clans_event_scene_mission_tab', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('임무 보상') + 1:
			for i in range(5):
				self.lyb_mouse_click('clans_event_scene_mission_rewards_' + str(i), custom_threshold=0)
			self.status = 99999
		elif self.status == self.get_work_status('명상하기'):
			self.lyb_mouse_click('clans_event_scene_daily_tab', custom_threshold=0)
			self.game_object.get_scene('clans_main_scene').set_option('명상하기' + '_event_done', True)
			self.set_option('click_icon', 'clans_event_scene_myungsang')
			self.set_option('event', '명상하기')
			self.last_status['event_scene'] = 1
			self.status = 100
		elif self.status == self.get_work_status('상단 임무'):
			self.lyb_mouse_click('clans_event_scene_daily_tab', custom_threshold=0)
			self.game_object.get_scene('clans_main_scene').set_option(self.game_object.get_scene('clans_main_scene').current_work + '_event_done', True)
			self.set_option('click_icon', 'clans_event_scene_sangdan')
			self.set_option('event', self.game_object.get_scene('clans_main_scene').current_work)
			self.last_status['event_scene'] = 1
			self.status = 100
		elif self.status == self.get_work_status('무림 맹주 도전'):
			self.lyb_mouse_click('clans_event_scene_enter_daily', custom_threshold=0)
			self.status = 99999	
		else:
			self.lyb_mouse_click('clans_event_scene_close_icon')
			self.status = 0

		return self.status

	def clans_world_map_scene(self):
		if self.status == 0:
			self.lyb_mouse_click('clans_world_map_scene_close_icon')

		return self.status

	def clans_achievement_scene(self):
		self.lyb_mouse_click('clans_achievement_scene_close_icon')

		return self.status

	def clans_bonus_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		if not '보너스' in self.schedule_list:
			self.status = 99999

		if self.status == 0:
			self.logging_detect_scene('보너스 화면')
			self.lyb_mouse_drag('clans_bonus_scene_drag_top', 'clans_bonus_scene_drag_bottom')
			self.status += 1
		elif self.status == 1:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_WONBO) == True:
				(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, 
					self.game_object.resource_manager.pixel_box_dic['clans_bonus_daily_wonbo_tab'], 
					custom_threshold 	= float(self.game_object.get_window_config('threshold_entry')))
				if loc_x == -1:
					self.loggingToGUI('일일 원보 탭 감지 불가능 - 임계치를 낮춰보세요.')
					self.status = 5
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status = 5
		elif self.status == 2:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_bonus_daily_wonbo_weekly_button')
			if match_rate < 0.9:
				# 결제를 했다는 의미이므로 클릭
				self.lyb_mouse_click('clans_bonus_daily_wonbo_weekly_button', custom_threshold=0)

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_bonus_daily_wonbo_monthly_button')
			if match_rate < 0.9:
				# 결제를 했다는 의미이므로 클릭
				self.lyb_mouse_click('clans_bonus_daily_wonbo_monthly_button', custom_threshold=0)
			self.status = 5
		elif self.status == 5:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_REWARD) == True:
				(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, 
					self.game_object.resource_manager.pixel_box_dic['clans_bonus_daily_reward_tab'], 
					custom_threshold 	= float(self.game_object.get_window_config('threshold_entry')))
				if loc_x == -1:
					self.loggingToGUI('출석 보상 탭 감지 불가능 - 임계치를 낮춰보세요.')
					self.status = 10
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status = 10
		elif self.status == 6:
			self.lyb_mouse_drag('clans_bonus_daily_reward_drag_top', 'clans_bonus_daily_reward_drag_bottom')
			time.sleep(0.5)
			self.lyb_mouse_drag('clans_bonus_daily_reward_drag_top', 'clans_bonus_daily_reward_drag_bottom')
			time.sleep(0.5)
			self.lyb_mouse_drag('clans_bonus_daily_reward_drag_top', 'clans_bonus_daily_reward_drag_bottom')
			time.sleep(0.5)
			self.status += 1
		elif self.status == 7:
			for i in range(18):
				self.lyb_mouse_click('clans_bonus_daily_reward_day_top_' + str(i), custom_threshold=0)
				time.sleep(0.1)
				self.lyb_mouse_click('clans_bonus_daily_reward_nw', custom_threshold=0)
				time.sleep(0.1)

			self.status += 1
		elif self.status == 8:
			self.lyb_mouse_drag('clans_bonus_daily_reward_drag_bottom', 'clans_bonus_daily_reward_drag_top')
			time.sleep(0.5)
			self.lyb_mouse_drag('clans_bonus_daily_reward_drag_bottom', 'clans_bonus_daily_reward_drag_top')
			time.sleep(0.5)
			self.lyb_mouse_drag('clans_bonus_daily_reward_drag_bottom', 'clans_bonus_daily_reward_drag_top')
			time.sleep(0.5)
			self.status += 1
		elif self.status == 9:
			for i in range(18):
				self.lyb_mouse_click('clans_bonus_daily_reward_day_bottom_' + str(i), custom_threshold=0)
				time.sleep(0.1)
				self.lyb_mouse_click('clans_bonus_daily_reward_nw', custom_threshold=0)
				time.sleep(0.1)


			self.lyb_mouse_drag('clans_bonus_scene_drag_bottom', 'clans_bonus_scene_drag_top')
			self.status = 10
		elif self.status == 10:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BONUS_GOLD_TREE) == True:
				(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, 
					self.game_object.resource_manager.pixel_box_dic['clans_bonus_gold_tree_tab'], 
					custom_threshold 	= float(self.game_object.get_window_config('threshold_entry')))
				if loc_x == -1:
					self.status = 20
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status = 20
		elif self.status == 11:
			self.lyb_mouse_click('clans_bonus_gold_tree_free_button', custom_threshold=0.95)
			self.status = 20
		elif self.status == 20:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BONUS_OFFEXP) == True:
				(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, 
					self.game_object.resource_manager.pixel_box_dic['clans_bonus_offexp_tab'], 
					custom_threshold 	= float(self.game_object.get_window_config('threshold_entry')))
				if loc_x == -1:
					self.status = 30
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status = 30
		elif self.status == 21:
			self.lyb_mouse_click('clans_bonus_offexp_receive_button')
			self.status = 30
		elif self.status == 30:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BONUS_IMMEDIATE) == True:
				(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, 
					self.game_object.resource_manager.pixel_box_dic['clans_bonus_immediate_tab'], 
					custom_threshold 	= float(self.game_object.get_window_config('threshold_entry')))
				if loc_x == -1:
					self.status = 40
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status = 40
		elif self.status == 31:
			self.lyb_mouse_click('clans_bonus_immediate_use_silver_tab')
			self.status += 1
		elif self.status == 32:
			match_rate_confirm = self.game_object.rateMatchedResource(self.window_pixels, 'clans_bonus_immediate_complete_confirm_event')
			if match_rate_confirm > 0.9:
				self.lyb_mouse_click('clans_bonus_immediate_complete_confirm_event_button')
			else:
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_bonus_immediate_complete_button')
				if match_rate > 0.7:
					self.lyb_mouse_click('clans_bonus_immediate_complete_button')
					if self.get_option('immediate_count') == None:
						i_count = 0
					else:
						i_count = self.get_option('immediate_count')

					if i_count > 100:
						self.status = 40
					else:
						self.set_option('immediate_count', i_count + 1)
				else:
					self.status = 40

		else:
			self.lyb_mouse_click('clans_bonus_scene_close_icon')
			self.set_option('completed', True)
			self.status = 0

		return self.status

	def clans_auto_mode_config_scene(self):
		if self.status == 0:
			if self.get_option('request_check_auto_combat') == True:
				combat_mode = int(self.get_game_config(lybconstant.LYB_DO_STRING_MODE_COMBAT))	
				combat_mode_pb =  'clans_auto_mode_config_scene_combat_mode_' + str(combat_mode)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, combat_mode_pb)
				if match_rate > 0.9:
					self.lyb_mouse_click(combat_mode_pb)
				self.status = 10
			else:
				self.status = 99
		elif self.status == 10:
			self.check_combat_skill(lybconstant.LYB_DO_BOOLEAN_0_COMBAT_SKILL, 0)
			self.check_combat_skill(lybconstant.LYB_DO_BOOLEAN_1_COMBAT_SKILL, 1)
			self.check_combat_skill(lybconstant.LYB_DO_BOOLEAN_2_COMBAT_SKILL, 2)
			self.check_combat_skill(lybconstant.LYB_DO_BOOLEAN_3_COMBAT_SKILL, 3)
			self.check_combat_skill(lybconstant.LYB_DO_BOOLEAN_4_COMBAT_SKILL, 4)

			self.set_option('request_check_auto_combat', False)
			self.status = 99
		else:
			self.lyb_mouse_click('clans_auto_mode_config_scene_close_icon')
			self.status = 0

		return self.status

	def clans_control_scene(self):
		if self.status == 0:
			if self.get_option('request_check_auto_combat') == True:
				self.lyb_mouse_click('clans_control_scene_ac_config_button')
				self.set_option('request_check_auto_combat', False)
				self.game_object.get_scene('clans_auto_mode_config_scene').set_option('request_check_auto_combat', True)
			else:
				self.status = 99
		else:
			self.lyb_mouse_click('clans_control_scene_close_icon')
			self.status = 0

		return self.status

	def clans_character_information_scene(self):
		if self.status == 0:
			if self.get_option('request_check_auto_combat') == True:
				self.lyb_mouse_click('clans_character_information_scene_control_tab', custom_threshold=0)
				self.set_option('request_check_auto_combat', False)
				self.game_object.get_scene('clans_control_scene').set_option('request_check_auto_combat', True)
			else:
				self.status = 99999
		elif self.status == 99:
			self.lyb_mouse_click('clans_character_information_scene_logoff')
			self.status = 1000000
			return self.status
		else:
			self.lyb_mouse_click('clans_character_information_scene_close_icon')
			self.status = 0

		return self.status

	def clans_mission_scene(self):
		self.lyb_mouse_click('clans_mission_scene_close_icon')

		return self.status

	def clans_colleague_scene(self):

		self.lyb_mouse_click('clans_colleague_scene_close_icon')
		return self.status

	def clans_main_combat_manual_scene(self):
		self.lyb_mouse_click('clans_main_combat_manual_scene_sudong_icon')

		return self.status































































































	#########################################################
	#														#
	#														#
	#														#
	#						MAIN							#
	#														#
	#														#
	#														#
	#########################################################

	def callback_logoff(self):

		self.game_object.get_scene('clans_character_information_scene').status = 99
		self.lyb_mouse_click('clans_main_scene_portrait')

	def clans_main_scene(self, mode=None):

		if mode == 'combat':
			if self.close_top_menu() == True:
				return self.status

			if self.open_bottom_menu() == True:
				return self.status

			if self.status >= 0 and self.status < 1000:
				pass
			elif (	self.status == self.get_work_status('메인 퀘스트') or 
					self.status == self.get_work_status('메인 퀘스트') + 1):
				pass
			else:
				return self.status

		rc = super(LYBClansScene, self).main_scene()
		if rc < 0:
			return rc

		self.game_object.current_matched_scene['name'] = ''

		config_hp = int(self.get_game_config(lybconstant.LYB_DO_STRING_CHECK_HP))
		if config_hp <= 30:
			config_hp = 20
		elif config_hp > 30 and config_hp <= 60:
			config_hp = 50
		elif config_hp > 60 and config_hp <= 80:
			config_hp = 80
		else:
			config_hp = 100

		if time.time() - self.get_checkpoint('hp_check') > 10:
			match_hp_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_hp_' + str(config_hp))
			if match_hp_rate < 0.4:
				# 설정값보다 HP가 적어졌다.
				match_jump_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_jump_icon')
				if match_jump_rate < 0.5:
					self.lyb_mouse_click('clans_main_scene_change_icon')
					return self.status
				else:
					self.lyb_mouse_click('clans_main_scene_jump_icon')
					if (not 'hp_check' in self.last_status) or self.last_status['hp_check'] == None:
						self.last_status['hp_check'] = self.status

					self.set_checkpoint('hp_check')
					self.set_option('hp_check', True)
					self.status = 10000 + 100
					return self.status

		if self.status == 0:
			self.logging_detect_scene('메인 화면')
			self.set_checkpoint('start')
			self.schedule_list = self.get_game_config('schedule_list')
			self.status += 1
		elif self.status >= 1 and self.status < 1000:
			self.set_schedule_status()
			# s_list_iter = 0
			# s_list_number = len(self.schedule_list)
			# while True:
			# 	self.current_work = self.schedule_list[self.status - 1]
			# 	if self.current_work == '게임 시작':
			# 		pass
			# 	elif self.current_work == '로그인':
			# 		pass
			# 	else:
			# 		break
			# 	self.status += 1
			# 	s_list_iter += 1
			# 	if s_list_iter > s_list_number:
			# 		break

			# if len(self.current_work) < 1:
			# 	is_multi_account = self.get_window_config('multi_account')
			# 	if is_multi_account == True:
			# 		#TODO: 접속 종료
			# 		self.loggingToGUI('다음 계정 작업을 위해 로그오프합니다')
			# 		self.game_object.get_scene('clans_character_information_scene').status = 99
			# 		# aa =self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_main_scene_list_icon_loc')
			# 		# print('LIST: ', int(aa*100), '%')
			# 		self.lyb_mouse_click('clans_main_scene_portrait')
			# 		self.status = 0
			# 	else:
			# 		self.loggingToGUI('지정된 스케줄을 완료해서 처음으로 돌아갑니다')
			# 		# 반복
			# 		self.status = 1
			# 		return self.status
			# else:
			# 	self.loggingStartWork(str(self.status), self.current_work)
			# 	self.set_work_status()
			# 	return self.status

			# self.status ++ 1

		elif self.status == self.get_work_status('메인 퀘스트') or self.status == self.get_work_status('메인 퀘스트') + 1:

			if self.get_option('scene_start_flag') == True:
				self.loggingToGUI('메인 퀘스트 작업 시작')
				self.set_option('scene_start_flag', False)				
				self.set_option(self.current_work + '_end_flag', False)

			if time.time() - self.get_checkpoint('main_quest_wait') > 30:
				self.set_option('wait_for_next', False)
				
			elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')
			
			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST)) * 60
			if (	(elapsed_time > duration_limit) or 
					(self.get_option(self.current_work + '_end_flag') == True) or
					(self.get_checkpoint('main_quest_wait') != 0 and time.time() - self.get_checkpoint('main_quest_wait') > 600) 
					):
				self.loggingToGUI(str(self.current_work) + ' 작업 종료(' \
					+str(elapsed_time)+', ' \
					+str(duration_limit)+',' \
					+str(self.get_option(self.current_work + '_end_flag'))+', '\
					+str(time.time() - self.get_checkpoint('main_quest_wait')))
				self.status = self.last_status[self.current_work] + 1
				self.set_option(self.current_work + '_end_flag', False)
				self.set_checkpoint('main_quest_wait')
				return self.status

			# match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_combat_manual_scene_sudong_icon')
			# if match_rate < 0.5 and self.get_option('wait_for_next') != True:
			# 	self.lyb_mouse_click('clans_main_combat_manual_scene_sudong_icon', custom_threshold=0.0)
			# 	time.sleep(1)

			match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'clans_main_scene_mission_tab_loc')
			if match_rate < 0.5:
				match_rate_2 = self.game_object.rateMatchedResource(self.window_pixels, 'clans_main_scene_party_tab_loc')
				if match_rate_2 > 0.8:
					self.lyb_mouse_click('clans_main_scene_mission_tab', custom_threshold=0.0)
				else:
					match_rate_3 = self.game_object.rateMatchedResource(self.window_pixels, 'clans_main_scene_hide_icon_loc')
					if match_rate_3 > 0.4:
						self.lyb_mouse_click('clans_main_scene_hide_icon', custom_threshold=0.4)
			else:
				match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'clans_main_scene_main_quest_pb_loc', custom_tolerance=100)
				if match_rate > 0.4:
					if self.get_option('wait_for_next') != True:
						self.lyb_mouse_click('clans_main_scene_main_quest_pb', custom_threshold=0.0)
						self.set_checkpoint('main_quest_wait')
						self.set_option('wait_for_next', True)
						self.loggingToGUI('30초 후 또는 이벤트 발생 후 다시 클릭합니다 ['+str(int(match_rate*100))+'%]')
				else:
					self.loggingToGUI('주임무 이미지 매칭률: '+str(int(match_rate*100))+'%')
					self.loggingToGUI('메인 퀘스트 불가능')
					self.set_option(self.current_work + '_end_flag', True)


			if self.status == self.get_work_status('메인 퀘스트'):
				self.status = self.get_work_status('메인 퀘스트') + 1
			else:
				self.status = self.get_work_status('메인 퀘스트')

		elif self.status == self.get_work_status('자동 사냥'):

			if self.close_bottom_menu() == True:
				return self.status

			if self.close_top_menu() == True:
				return self.status

			elapsed_time = self.get_elapsed_time()
			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA)) * 60

			if self.get_option('is_checked_jasa_location') != True:	
				self.set_option('is_checked_jasa_location', True)
				if self.get_option('jasa_location') == None:
					self.lyb_mouse_click('clans_main_scene_map', custom_threshold=0)
					self.game_object.get_scene('clans_local_map_scene').status = self.status
					return self.status
				else:
					self.lyb_mouse_click('clans_main_scene_map', custom_threshold=0)
					self.game_object.get_scene('clans_local_map_scene').status = self.status + 1
					return self.status

			if elapsed_time > duration_limit:
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('is_checked_jasa_location', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_combat_manual_scene_sudong_icon')
			if rate_match > 0.9:
				self.lyb_mouse_click('clans_main_combat_manual_scene_sudong_icon')

		elif self.status == self.get_work_status('보너스'):
			if self.get_option('scene_start_flag') == True:
				self.loggingToGUI('보너스 작업 시작')
				self.set_option('scene_start_flag', False)

			if ((time.time() - self.checkpoint[self.current_work + '_check_start'] > 10) or
				(self.game_object.get_scene('clans_bonus_scene').get_option('completed') == True) or
				(self.get_option('end_flag') == True) ):				
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.status = self.last_status[self.current_work] + 1
				self.set_option('end_flag', False)
				return self.status

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_bonus_icon')
			if match_rate < 0.8:
				# 감춰져있단 뜻이다. 클릭해서 펼치자.
				match_rate_2 = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_hide_3_icon')
				if match_rate_2 < 0.8:
					self.loggingToGUI('보너스 아이콘을 못찾겠음')
					self.set_option('end_flag', True)
				else:
					self.lyb_mouse_click('clans_main_scene_hide_3_icon')
			else:
				self.lyb_mouse_click('clans_main_scene_bonus_icon')
		elif (	self.status == self.get_work_status('무림 맹주 도전')
				):

			if self.open_top_menu() == True:
				return self.status

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('clans_main_scene_event_icon')
			self.game_object.get_scene('clans_event_scene').status = self.status

		elif (  self.status == self.get_work_status('보물 탐색') or
				self.status == self.get_work_status('영웅 도전') or
				self.status == self.get_work_status('무신전') or
				self.status == self.get_work_status('임무 보상') or
				self.status == self.get_work_status('명상하기') or
				self.status == self.get_work_status('상단 임무')
				):
			elapsed_time = self.get_elapsed_time()

			# self.game_object.get_scene('clans_event_scene').status = 10
			self.game_object.get_scene('clans_event_scene').set_option('event_tab', 'daily')
			if self.status == self.get_work_status('보물 탐색'):
				if (	elapsed_time > 5 or 
						self.game_object.get_scene('clans_treasure_scene').get_option('completed') == True
						):
					self.set_option(self.current_work + '_end_flag', True)
				else:
					self.game_object.get_scene('clans_event_scene').set_option('event', self.current_work)
			elif self.status == self.get_work_status('영웅 도전'):
				if (	elapsed_time > 5 or
						self.game_object.get_scene('clans_hero_scene').get_option('completed') == True
						):
					self.set_option(self.current_work + '_end_flag', True)
				else:
					self.game_object.get_scene('clans_event_scene').set_option('event', self.current_work)
			elif self.status == self.get_work_status('무신전'):
				if (	elapsed_time > 5
						):
					self.set_option(self.current_work + '_end_flag', True)
				else:
					self.game_object.get_scene('clans_event_scene').set_option('event', self.current_work)
			elif self.status == self.get_work_status('명상하기'):
				if (	elapsed_time > self.period_bot(120)
						):					
					self.lyb_mouse_click('clans_main_scene_terminate')
					self.set_option(self.current_work + '_event_done', False)
					self.set_option(self.current_work + '_end_flag', True)
				else:
					if (	self.get_option(self.current_work + '_end_flag') != True and
							self.get_option(self.current_work + '_event_done') == True
							):
						self.loggingToGUI(self.current_work + ' 진행 시간: ' + str(int(elapsed_time)) + '초')
						return self.status
				self.game_object.get_scene('clans_event_scene').status = self.status

			elif self.status == self.get_work_status('상단 임무'):
				duration_limit = int(self.get_game_config(lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN)) * 60
				if (	elapsed_time > duration_limit
						):					
					self.set_option(self.current_work + '_event_done', False)
					self.set_option(self.current_work + '_end_flag', True)
				else:
					if (	self.get_option(self.current_work + '_end_flag') != True and
							self.get_option(self.current_work + '_event_done') == True
							):
						self.loggingElapsedTime(self.current_work + ' 진행 시간: ', int(elapsed_time), duration_limit)
				self.game_object.get_scene('clans_event_scene').status = self.status
			else:
				self.game_object.get_scene('clans_event_scene').set_option('event', None)
				self.game_object.get_scene('clans_event_scene').status = self.status

				if elapsed_time > self.period_bot(5):
					self.set_option(self.current_work + '_end_flag', True)


			if self.get_option(self.current_work + '_end_flag') == True:
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.status = self.last_status[self.current_work] + 1
				self.set_option(self.current_work + '_end_flag', False)
				return self.status

			is_clicked = self.lyb_mouse_click('clans_main_scene_event_icon')
			if is_clicked == False:
				is_clicked_hide = self.lyb_mouse_click('clans_main_scene_hide_3_icon')
				if is_clicked_hide == False:
					self.loggingToGUI('이벤트 아이콘을 못찾겠음')
					self.set_option('end_flag', True)
				else:
					self.lyb_mouse_click('clans_main_scene_hide_3_icon')


		elif self.status == self.get_work_status('자동전투 설정'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > 5:
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('clans_main_scene_portrait')
			self.game_object.get_scene('clans_character_information_scene').set_option('request_check_auto_combat', True)

		elif self.status == self.get_work_status('동료 무료 소환'):

			if self.open_bottom_menu() == True:
				return self.status

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('clans_main_scene_dongryo')
			self.game_object.get_scene('clans_dongryo_scene').status = self.status
		
		elif self.status == self.get_work_status('안전 지대로 이동'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > int(self.get_game_config(lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE)):
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.status = self.last_status[self.current_work] + 1
				return self.status
			else:
				self.loggingElapsedTime('[시간 체크] 안전 지대로 이동 중',
					elapsed_time, int(self.get_game_config(lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE)))

			self.lyb_mouse_click('clans_main_scene_map', custom_threshold=0)
			self.game_object.get_scene('clans_local_map_scene').status = self.status

		elif (	self.status == self.get_work_status('방파 기부') or 
				self.status == self.get_work_status('방파 선물') or 
				self.status == self.get_work_status('귀보당')
				):

			if self.open_bottom_menu() == True:
				return self.status

			elapsed_time = self.get_elapsed_time()

			if elapsed_time > self.period_bot(5):
				self.loggingToGUI(str(self.current_work) + ' 작업 종료')
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('clans_main_scene_clan_icon')
			self.game_object.get_scene('clans_clan_scene').status = self.status

			# match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_clan_icon')
			# if match_rate < self.get_window_config('threshold_entry'):
			# 	self.lyb_mouse_click('clans_main_scene_change_2_icon')
			# else:
			# 	self.lyb_mouse_click('clans_main_scene_clan_icon')

		elif self.status == (10000 + 100):
			# 좌선하기
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_combat_manual_scene_sudong_icon')
			if match_rate < 0.5:
				# 자동이면 수동으로 풀고
				self.lyb_mouse_click('clans_main_combat_manual_scene_sudong_icon', custom_threshold=0.0)
			self.lyb_mouse_click('clans_main_scene_rest_icon')
			self.status = 10000 + 102
		elif self.status == (10000 + 102):
			match_hp_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_hp_100')
			if match_hp_rate > 0.9:
				self.lyb_mouse_click('clans_main_scene_character_left', custom_threshold=0)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_combat_manual_scene_sudong_icon')
				if match_rate > 0.6:
					self.lyb_mouse_click('clans_main_combat_manual_scene_sudong_icon', custom_threshold=0.0)
				self.status = self.last_status['hp_check']
				self.last_status['hp_check'] = None
				self.set_option('hp_check', False)
		else:
			self.status = self.last_status[self.current_work] + 1	
						
		return self.status

	def nox_init_screen_scene(self):
		print('DEBUG 1')
		self.schedule_list = self.get_game_config('schedule_list')
		if '게임 시작' in self.schedule_list:
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, self.game_object.resource_manager.pixel_box_dic['clans_icon'])
			# self.loggingToGUI('감지: 리니지2 아이콘('+str(loc_x) + ', '+str(loc_y)+')')
			self.lyb_mouse_click_location(loc_x, loc_y)
		# self.lyb_mouse_drag_location(loc_x, loc_y, loc_x + 100, loc_y, delay=5)
		print('DEBUG 2')
		return 0

	def clans_login_ads_scene(self):
		if self.status == 0:
			self.lyb_mouse_click('clans_login_ads_scene_today')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def clans_character_select_scene(self):
		if self.status == 0:
			self.lyb_mouse_click('clans_character_select_scene_start_game_button')

		return self.status

	def clans_login_2_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')
		if not '로그인' in self.schedule_list:
			return 0

		self.lyb_mouse_click('clans_login_2_scene_game_start_button')
		return self.status

	def clans_login_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		if not '로그인' in self.schedule_list:
			return 0

		if time.time() - self.get_checkpoint('start') > 120:
			self.status = 0

		if self.status >= 0 and self.status < 2:
			if self.status == 0:
				self.set_checkpoint('start')
				self.loggingToGUI('로그인')
				is_multi_account = self.get_window_config('multi_account')
				if is_multi_account == False:
					self.status = 2
					return self.status

				self.set_option('retry_complete_flag', False)

			self.loggingToGUI('계정 변경 재시도: '+str(self.status+1))
			
			self.lyb_mouse_click('clans_login_scene_change_account_button')

			self.status += 1
		elif self.status == 2:
			self.set_option('retry_complete_flag', True)
			self.lyb_mouse_click('clans_login_scene_game_start_button')
			self.status += 1 
			self.set_checkpoint('login_delay')
		elif self.status == 3:
			elapsed_time = time.time() - self.get_checkpoint('login_delay')
			if elapsed_time > 10:
				self.status = 0

		return self.status

	def clans_change_account_scene(self):

		if self.get_checkpoint('defense') == 0:
			elapsed_time = 0
		else:
			elapsed_time = time.time() - self.get_checkpoint('defense')

		self.loggingToGUI('구글 계정 변환 화면이 60초 이상 지속되면 에러로 간주하여 종료합니다: ' + str(int(elapsed_time)) + '초')
		if elapsed_time > 60 and elapsed_time < 70:
			# 녹스 프로그램 중지
			self.game_object.terminate_application()
			self.status = 0
			self.set_option('retry_count', 0)
			return self.status

		if self.status == 0:
			self.set_checkpoint('defense')
			self.status += 1
		elif self.status == 1:
			retry_count = self.get_option('retry_count')
			if retry_count == None:
				retry_count = 0

			(top_loc_x, top_loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['clans_change_account_scene_google_icon']
				)
			if top_loc_x != -1:
				self.loggingToGUI('구글계정연동 이미지 찾기 성공:' + str((top_loc_x, top_loc_y)))
				if retry_count >= 1:
					self.lyb_mouse_click_location(top_loc_x + 130, top_loc_y + 20)
					self.set_option('retry_count', 0)
					self.status += 1
					return self.status
				else:
					self.set_option('retry_count', retry_count + 1)

				self.lyb_mouse_click_location(top_loc_x, top_loc_y)
				self.set_checkpoint('start')
				self.set_option('select_complete_flag', False)
				# self.lyb_mouse_move_location(top_loc_x, top_loc_y)
				self.status += 1
			else:
				duration_fail = self.get_checkpoint('fail_search')
				if duration_fail == None or time.time() - duration_fail > 120:
					duration_fail = time.time()
				elapsed_fail = time.time() - duration_fail
				self.loggingToGUI('구글계정연동 이미지 탐색 실패: 남은 시간('+str(60 - int(elapsed_fail)) +')')

				if elapsed_fail > 60:
					return -1
		elif self.status == 2:
			if self.get_option('select_complete_flag') == True:
				self.status = 0
			if time.time() - self.get_checkpoint('start') > 3:
				# self.lyb_mouse_click('clans_change_account_scene_close_icon')
				self.status = 1

		return self.status



































































































	def clans_google_play_account_select_scene(self):
		self.logging_detect_scene('구글 계정 선택 화면')

		(top_loc_x, top_loc_y) = lybgame.LYBGame.locationOnWindow(
			self.window_image, 
			self.game_object.resource_manager.pixel_box_dic['clans_google_play_letter']
			)
		if self.status == 0:
			(bottom_loc_x, bottom_loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['clans_google_play_add_account_letter']
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

		if self.game_object.get_scene('clans_login_scene').get_option('retry_complete_flag') == True:
			self.status += 1
			self.game_object.get_scene('clans_login_scene').set_option('retry_complete_flag', False) 

		if self.status >= self.google_account_number:
			self.status = 0		
			self.loggingToGUI(str(self.google_account_number)+' 개의 계정 작업 완료')
			self.game_object.get_scene('clans_login_scene').set_option('retry_complete_flag', False)
			return self.status
		else:
			self.loggingToGUI(str(self.status + 1)+' 번째 구글 계정 로그인 시도')
			self.game_object.get_scene('clans_change_account_scene').set_option('select_complete_flag', True)

		if self.status >= 0 and self.status < 5:
			click_loc_x = top_loc_x + 10
			click_loc_y = top_loc_y + self.google_account_height*self.status + self.google_account_height*0.8
			self.lyb_mouse_click_location(click_loc_x, click_loc_y)
			#self.lyb_mouse_move_location(click_loc_x, click_loc_y)
		else:
			if self.just_drag_completed == False:
				self.just_drag_completed = True

				drag_number = self.status - 5

				from_x = top_loc_x + 10
				from_y = top_loc_y + self.google_account_height * 2 + 5

				to_x = top_loc_x + 10
				to_y = top_loc_y + self.google_account_height * 1

				print(from_x, from_y, to_x, to_y)
				for i in range(self.status - 4):
					self.lyb_mouse_drag_location(from_x, from_y, to_x, to_y, delay=1)
				
			else:
				self.just_drag_completed = False
				# 맨아래까지 왔나?
				(bottom_loc_x, bottom_loc_y) = lybgame.LYBGame.locationOnWindow(
						self.window_image, 
						self.game_object.resource_manager.pixel_box_dic['clans_google_play_add_account_letter']
					)
				self.loggingToGUI
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
					# #self.lyb_mouse_move_location(click_loc_x, click_loc_y)
					# if self.game_object.get_scene('clans_change_account_scene').get_option('retry_complete_flag') == True:
					# 	self.status += 1

		return self.status












	def close_top_menu(self):
				
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_inventory')
		if match_rate > 0.8:
			self.lyb_mouse_click('clans_main_scene_hide_3_icon', custom_threshold=0.0)
			return True

		return False

	def open_top_menu(self):
				
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'clans_main_scene_inventory')
		if match_rate > 0.8:
			return False

		self.lyb_mouse_click('clans_main_scene_hide_3_icon', custom_threshold=0.0)

		return True

	def close_bottom_menu(self):
		match_rate = self.game_object.rateMatchedPixelBox(
						self.window_pixels,
						'clans_main_scene_mugong')
		if match_rate < 0.9:
			return False

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic['clans_main_scene_change'],
								custom_below_level=(150, 150, 100),
								custom_top_level=(255, 255, 200),
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(605, 190, 630, 205)
								)

		if match_rate > 0.7:
			self.lyb_mouse_click_location(loc_x, loc_y)
			return True

		return False

	def open_bottom_menu(self):
		match_rate = self.game_object.rateMatchedPixelBox(
						self.window_pixels,
						'clans_main_scene_mugong')
		if match_rate > 0.9:
			return False

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic['clans_main_scene_change'],
								custom_below_level=(150, 150, 100),
								custom_top_level=(255, 255, 200),
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(605, 190, 630, 205)
								)

		if match_rate > 0.7:
			self.lyb_mouse_click_location(loc_x, loc_y)
			return True

		return False

	def check_combat_skill(self, combat_skill, i):

		# for i in range(5):
		combat_skill_pb = 'clans_auto_mode_config_scene_combat_skill_' + str(i)
		is_on_skill = self.get_game_config(combat_skill)
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, combat_skill_pb)
		if is_on_skill == True:
			if match_rate > 0.9:
				self.lyb_mouse_click(combat_skill_pb)
		else:
			if match_rate < 0.9:
				self.lyb_mouse_click(combat_skill_pb, custom_threshold=0)

	def get_work_status(self, work_name):
		if work_name in lybgameclans.LYBClans.work_list:
			return (lybgameclans.LYBClans.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999

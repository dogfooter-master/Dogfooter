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
import likeyoubot_lineage2revolution as lybgamelin2rev
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBLin2RevScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBLin2RevScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'nox_init_screen_scene':
			rc = self.nox_init_screen_scene()
		elif self.scene_name == 'lin2rev_terms_of_use_scene':
			rc = self.lin2rev_terms_of_use_scene()
		elif self.scene_name == 'lin2rev_logo_screen_scene':
			rc = self.lin2rev_logo_screen_scene()
		elif self.scene_name == 'lin2rev_connect_account_scene':
			rc = self.lin2rev_connect_account_scene()
		elif self.scene_name == 'lin2rev_google_play_account_select_scene':
			rc = self.lin2rev_google_play_account_select_scene()
		elif self.scene_name == 'lin2rev_create_character_scene':
			rc = self.lin2rev_create_character_scene()
		elif self.scene_name == 'lin2rev_class_tree_scene':
			rc = self.lin2rev_class_tree_scene()
		elif self.scene_name == 'lin2rev_select_character_scene':
			rc = self.lin2rev_select_character_scene()
		elif self.scene_name == 'lin2rev_main_scene':
			rc = self.lin2rev_main_scene()
		elif self.scene_name == 'lin2rev_episode_clear_scene':
			rc = self.lin2rev_episode_clear_scene()	
		elif self.scene_name == 'lin2rev_inventory_scene':
			rc = self.lin2rev_inventory_scene()		
		elif self.scene_name == 'lin2rev_mail_scene':
			rc = self.lin2rev_mail_scene()	
		elif self.scene_name == 'lin2rev_daily_attendance_scene':
			rc = self.lin2rev_daily_attendance_scene()
		elif self.scene_name == 'lin2rev_list_scene':
			rc = self.lin2rev_list_scene()
		elif self.scene_name == 'lin2rev_shop_scene':
			rc = self.lin2rev_shop_scene()
		elif self.scene_name == 'lin2rev_inventory_scene_consume_item_use_scene':
			rc = self.lin2rev_inventory_scene_consume_item_use_scene()
		elif self.scene_name == 'lin2rev_inventory_scene_consume_item_2_use_scene':
			rc = self.lin2rev_inventory_scene_consume_item_2_use_scene()
		elif self.scene_name == 'lin2rev_config_scene':
			rc = self.lin2rev_config_scene()
		elif self.scene_name == 'lin2rev_quest_scene':
			rc = self.lin2rev_quest_scene()
		elif self.scene_name == 'lin2rev_today_activity_scene':
			rc = self.lin2rev_today_activity_scene()
		elif self.scene_name == 'lin2rev_loading_scene':
			rc = self.lin2rev_loading_scene()
		elif self.scene_name == 'lin2rev_inventory_sell_scene':
			rc = self.lin2rev_inventory_sell_scene()
		elif self.scene_name == 'lin2rev_clan_scene':
			rc = self.lin2rev_clan_scene()
		elif self.scene_name == 'lin2rev_clan_donate_scene':
			rc = self.lin2rev_clan_donate_scene()
		elif self.scene_name == 'lin2rev_friend_scene':
			rc = self.lin2rev_friend_scene()
		else:
			rc = 0

		return rc

	def lin2rev_friend_scene(self):
		if self.status == 0:
			self.lyb_mouse_click('lin2rev_friend_scene_game_friend_tab', custom_threshold=0)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_friend_scene_hi_all')
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('lin2rev_friend_scene_receive_hi_all')
			self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('lin2rev_friend_scene_clean')
			self.status += 1
		elif self.status == 4:
			self.lyb_mouse_click('lin2rev_friend_scene_receive_tab', custom_threshold=0)
			self.status += 1
		elif self.status == 5:
			self.lyb_mouse_click('lin2rev_friend_scene_accept_all')
			self.status += 1
		else:
			self.lyb_mouse_click('lin2rev_friend_scene_close_icon')
			self.status = 0

		return self.status

	def lin2rev_clan_donate_scene(self):
		if self.status == 0:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA) == True:
				self.lyb_mouse_click('lin2rev_clan_donate_scene_adena_tab')
				self.status += 1
			else:
				self.status = 10
		elif self.status == 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_clan_donate_scene_button')
			if match_rate < 0.5:
				self.status = 10
			else:
				donate_num = int(self.get_game_config(lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA))
				self.loggingToGUI('아데나 기부 횟수:' + str(donate_num))
				for i in range(donate_num - 1):
					self.lyb_mouse_click('lin2rev_clan_donate_scene_add')
					time.sleep(0.5)
				self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('lin2rev_clan_donate_scene_button')
			self.status = 10
		elif self.status == 10:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD) == True:
				self.lyb_mouse_click('lin2rev_clan_donate_scene_blood_tab')
				self.status += 1
			else:
				self.status = 20
		elif self.status == 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_clan_donate_scene_button')
			if match_rate < 0.5:
				self.status = 20
			else:
				donate_num = int(self.get_game_config(lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD))
				self.loggingToGUI('피의 증거 기부 횟수:' + str(donate_num))
				for i in range(donate_num - 1):
					self.lyb_mouse_click('lin2rev_clan_donate_scene_add')
					time.sleep(0.5)
				self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('lin2rev_clan_donate_scene_button')
			self.status = 20
		elif self.status == 20:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED) == True:
				self.lyb_mouse_click('lin2rev_clan_donate_scene_red_tab')
				self.status += 1
			else:
				self.status = 99999
		elif self.status == 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_clan_donate_scene_button')
			if match_rate < 0.5:
				self.status = 99999
			else:
				donate_num = int(self.get_game_config(lybconstant.LYB_DO_STRING_CLAN_DONATE_RED))
				self.loggingToGUI('붉은 스타 스톤 기부 횟수:' + str(donate_num))
				for i in range(donate_num - 1):
					self.lyb_mouse_click('lin2rev_clan_donate_scene_add')
					time.sleep(0.5)
				self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('lin2rev_clan_donate_scene_button')
			self.status = 99999
		else:
			self.lyb_mouse_click('lin2rev_clan_donate_scene_close_icon')
			self.status = 0

		return self.status

	def lin2rev_clan_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('lin2rev_clan_scene_information_tab')
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_clan_scene_daily_check_button')
			self.lyb_mouse_click('lin2rev_clan_scene_daily_check_button')
			self.status += 1
		elif self.status == 2:
			if (	self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA) == True or
					self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD) == True or
					self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED) == True
				):
				self.lyb_mouse_click('lin2rev_clan_scene_donate_button')
			self.status += 1
		elif self.status == 3:
			self.status = 10
		elif self.status == 10:
			# 혈맹원 인사
			self.lyb_mouse_click('lin2rev_clan_scene_member_tab')
			self.status += 1
		elif self.status == 11:
			self.lyb_mouse_click('lin2rev_clan_scene_member_member_tab')
			self.status += 1
		elif self.status == 12:
			self.lyb_mouse_click('lin2rev_clan_scene_member_hi_all', custom_threshold=0)
			self.status += 1
		elif self.status == 13:
			self.lyb_mouse_click('lin2rev_clan_scene_member_receive_hi_all', custom_threshold=0)
			self.status = 99999
		else:
			self.lyb_mouse_click('lin2rev_clan_scene_close_icon')
			self.status = 0

		return self.status

	def lin2rev_inventory_sell_scene(self):
		if self.status == 0:
			self.lyb_mouse_click('lin2rev_inventory_sell_scene_sell_button')
			self.status += 1
		else:
			self.lyb_mouse_click('lin2rev_inventory_sell_scene_cancel_button')
			self.status = 0

		return self.status

	def lin2rev_loading_scene(self):

		return self.status

	def lin2rev_today_activity_scene(self):
		if self.status == 0:
			is_reward = self.lyb_mouse_click('lin2rev_today_activity_scene_reward_button')
			if not is_reward == True:
				self.status += 1
		elif self.status == 1:
			for i in range(3):
				self.lyb_mouse_click('lin2rev_today_activity_scene_reward_' + str(i))
			self.status += 1
		else:
			self.lyb_mouse_click('lin2rev_today_activity_scene_close_icon')
			self.status = 0

		return self.status

	def lin2rev_quest_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')
		if self.status == 0:
			if not '일일 퀘스트' in self.schedule_list:
				self.status = 20
			else:
				self.lyb_mouse_click('lin2rev_quest_scene_daily_tab')
				self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_quest_scene_daily_quest_complete_' + str(self.status - 1))
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('lin2rev_quest_scene_daily_quest_complete_' + str(self.status - 1))
			self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('lin2rev_quest_scene_daily_quest_complete_' + str(self.status - 1))
			self.status += 1
		elif self.status == 4:
			self.lyb_mouse_click('lin2rev_quest_scene_daily_quest_' + str(self.status - 4))
			self.status += 1
		elif self.status == 5:
			self.lyb_mouse_click('lin2rev_quest_scene_daily_quest_' + str(self.status - 4))
			self.status += 1
		elif self.status == 6:
			self.lyb_mouse_click('lin2rev_quest_scene_daily_quest_' + str(self.status - 4))
			self.status += 1
		elif self.status == 7:
			self.lyb_mouse_click('lin2rev_quest_scene_reward_1', custom_threshold=0)
			self.lyb_mouse_click('lin2rev_quest_scene_reward_2', custom_threshold=0)
			self.status = 20
		elif self.status == 20:
			if not '주간 퀘스트' in self.schedule_list:
				self.status = 30
			else:
				self.lyb_mouse_click('lin2rev_quest_scene_weekly_tab')
				self.status += 1
		elif self.status == 21:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_quest_scene_weekly_quest_limit')
			self.loggingToGUI('주간 퀘스트 제한 매칭:' + str(int( match_rate * 100)) + '%')
			if match_rate > 0.9:
				self.set_option('weekly_quest_limit', True)
				self.status = 24
			else:
				self.set_option('weekly_quest_limit', False)
				self.lyb_mouse_click('lin2rev_quest_scene_weekly_quest_complete')
				self.status += 1
		elif self.status == 22:	
			self.lyb_mouse_click('lin2rev_quest_scene_weekly_quest')
			self.status += 1
		elif self.status == 23:
			self.lyb_mouse_click('lin2rev_quest_scene_weekly_quest_move')
			self.status += 1
		elif self.status == 24:
			for i in range(7):
				self.lyb_mouse_click('lin2rev_quest_scene_weekly_reward_' + str(i), custom_threshold=0)
			self.status = 30		
		elif self.status == 30:
			self.lyb_mouse_click('lin2rev_quest_scene_close_icon')
			self.status = 0

		return self.status

	def nox_init_screen_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')
		if '게임 시작' in self.schedule_list:
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(self.window_image, self.game_object.resource_manager.pixel_box_dic['lineage2_revolution_icon'])
			# self.loggingToGUI('감지: 리니지2 아이콘('+str(loc_x) + ', '+str(loc_y)+')')
			self.lyb_mouse_click_location(loc_x, loc_y)
		# self.lyb_mouse_drag_location(loc_x, loc_y, loc_x + 100, loc_y, delay=5)
		return 0

	def lin2rev_config_scene(self):
		if self.status == 99:
			self.lyb_mouse_click('lin2rev_config_scene_information_tab', custom_threshold=0)
			#self.lyb_mouse_click('lin2rev_config_scene_information_tab', custom_threshold=0)
			self.status += 1
		elif self.status == 100:
			self.lyb_mouse_click('lin2rev_config_scene_information_logout_button', custom_threshold=0)
			#self.lyb_mouse_click('lin2rev_config_scene_information_logout_button', custom_threshold=0)
			self.status = 1000000
			return self.status
		else:
			self.lyb_mouse_click('lin2rev_config_scene_close_icon')
			self.status = 0

		return self.status


	def lin2rev_inventory_scene_consume_item_2_use_scene(self):
		# 듀란달 합금, 철광석, 원목, ... 설정으로 받자
		if self.status == 0:
			# 설정으로 받자.
			# lin2rev_inventory_scene_consume_item_2_loc_0_icon 부터
			# lin2rev_inventory_scene_consume_item_2_loc_5_icon
			self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_2_loc_0_icon')
			self.status = 1
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_2_loc_confirm_button')
			self.status = 2
		elif self.status == 2:
			# 툴팁이 떠서 두번 눌러야 한다. --;;
			self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_2_loc_confirm_button')
			self.status = 0

		return self.status

	def lin2rev_inventory_scene_consume_item_use_scene(self):
		if self.status == 0:
			# 설정으로 받자.
			# lin2rev_inventory_scene_consume_item_use_scene_weapon_icon
			# lin2rev_inventory_scene_consume_item_use_scene_armor_icon
			# lin2rev_inventory_scene_consume_item_use_scene_ring_icon
			self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_use_scene_weapon_icon')
			self.status = 1
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_use_scene_confirm_button')
			self.status = 2
		elif self.status == 2:
			# 툴팁이 떠서 두번 눌러야 한다. --;;
			self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_use_scene_confirm_button')
			self.status = 0
		return self.status

	def lin2rev_shop_scene(self):
		self.schedule_list = self.get_game_config('schedule_list')
		if self.status == 0: 
			self.lyb_mouse_click('lin2rev_shop_scene_default_tab', custom_tolerance=50, custom_threshold=0.5)
			if self.get_option('is_empty_hp_potion') == True and self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BUY_HP_POTION) == True:
				self.last_status['hp_potion_empty'] = self.status
				self.status = 1000
			elif self.get_option('is_empty_mp_potion') == True and self.get_game_config(lybconstant.LYB_DO_BOOLEAN_BUY_MP_POTION) == True:
				self.last_status['mp_potion_empty'] = self.status
				self.status = 2000
			else:
				self.status = 1
		elif self.status == 1:
			if not '소환 상자' in self.schedule_list:
				self.status = 10
			else:
				rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_shop_default_summon_new_loc')
				if rate > 0.7:
					self.status = 2
				else:
					self.status = 10
		elif self.status == 2:
			self.lyb_mouse_click('lin2rev_shop_default_summon_tab')
			self.status = 3
		elif self.status == 3:
			rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_shop_default_summon_free_box_loc')
			self.loggingToGUI('무료 상자 소환 매칭률: ' + str(int(rate*100)) + '%')
			if rate > 0.9:
				self.status = 4
			else:
				self.status = 10
		elif self.status == 4:
			self.lyb_mouse_click('lin2rev_shop_default_summon_free_box_letter')
			self.status = 10
		elif self.status == 10:
			if not '우정포인트 상자' in self.schedule_list:
				self.status = 20
			else:
				rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_shop_default_friendship_new_loc')
				if rate > 0.7:
					self.status = 11
				else:
					self.status = 20
		elif self.status == 11:
			self.lyb_mouse_click('lin2rev_shop_default_friendship_tab', custom_tolerance=50, custom_threshold=0.5)
			self.status = 12
		elif self.status == 12:
			rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_shop_default_friendship_free_box_loc')
			self.loggingToGUI('무료 매칭률: ' + str(int(rate*100)) + '%')
			if rate > 0.9:
				self.status = 13
			else:
				self.status = 20
		elif self.status == 13:
			self.lyb_mouse_click('lin2rev_shop_default_friendship_free_box_letter', custom_tolerance=50, custom_threshold=0.5)
			self.status = 20
		elif self.status == 20:
			self.lyb_mouse_click('lin2rev_shop_scene_close_icon', custom_tolerance=50, custom_threshold=0.5)
			self.status = 0
		elif self.status == 1000:
			self.lyb_mouse_click('lin2rev_shop_scene_default_consume_tab')
			self.status = 1001
		elif self.status == 1001:
			if self.get_option('hp_potion_remain') == None or self.get_option('hp_potion_remain') < 0:
				self.set_option('hp_potion_remain', int(self.get_game_config(lybconstant.LYB_DO_STRING_NUMBER_HP_POTION)))

			if self.get_option('hp_potion_remain') > 0 :
				# 세계알림때문에 가려진다.
				self.lyb_mouse_click('lin2rev_shop_scene_default_consume_hp_potion_icon', custom_threshold=0)
				self.set_option('hp_potion_remain', int(self.get_option('hp_potion_remain')) - 1)
			else:
				self.set_option('is_empty_hp_potion', False)
				self.status = self.last_status['hp_potion_empty']
		elif self.status == 2000:
			self.lyb_mouse_click('lin2rev_shop_scene_default_consume_tab')
			self.status = 2001
		elif self.status == 2001:
			if self.get_option('mp_potion_remain') == None or self.get_option('mp_potion_remain') < 0:
				self.set_option('mp_potion_remain', int(self.get_game_config(lybconstant.LYB_DO_STRING_NUMBER_MP_POTION)))

			if self.get_option('mp_potion_remain') > 0 :
				self.lyb_mouse_click('lin2rev_shop_scene_default_consume_mp_potion_icon', custom_threshold=0)
				self.set_option('mp_potion_remain', int(self.get_option('mp_potion_remain')) - 1)
			else:
				self.set_option('is_empty_mp_potion', False)
				self.status = self.last_status['mp_potion_empty']

		return self.status

	def lin2rev_list_scene(self):
		if self.status == 99:
			self.lyb_mouse_click('lin2rev_list_scene_config_icon', custom_threshold=0)
			#self.lyb_mouse_click('lin2rev_list_scene_config_icon', custom_threshold=0)
			self.game_object.get_scene('lin2rev_config_scene').status = 99
			self.status = 0
		elif self.status == 200:
			self.lyb_mouse_click('lin2rev_list_scene_challenge_icon', custom_threshold=0)
			self.status += 1
		elif self.status == 201:
			self.lyb_mouse_click('lin2rev_list_scene_quest_icon')
			self.status = 0
		elif self.status == 300:
			self.lyb_mouse_click('lin2rev_list_scene_clan_bottom_icon', custom_threshold=0)
			self.status += 1
		elif self.status == 301:
			self.lyb_mouse_click('lin2rev_list_scene_clan_top_icon')
			self.status = 0
		elif self.status == 400:
			self.lyb_mouse_click('lin2rev_list_scene_friend_icon', custom_threshold=0)
			self.status = 0
		else:
			self.lyb_mouse_click('lin2rev_main_scene_list_scene_cancel', custom_threshold=0)
			self.status = 0

		return self.status

	def lin2rev_daily_attendance_scene(self):

		if time.time() - self.get_checkpoint('start') > 30:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('start')

			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['lin2rev_daily_attendance_tab']
				)
			if loc_x == -1:
				self.status = 10
			else:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_daily_attendance_scene_receive', custom_threshold=0)
			self.status = 10
		elif self.status == 10:
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['lin2rev_weekly_attendance_tab']
				)
			if loc_x == -1:
				self.status = 20
			else:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status += 1
		elif self.status == 11:
			self.lyb_mouse_click('lin2rev_daily_attendance_scene_receive', custom_threshold=0)
			self.status = 20
		elif self.status == 20:
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['lin2rev_monyhly_attendance_newuser_tab']
				)
			if loc_x == -1:
				self.status = 99
			else:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status += 1
		elif self.status == 21:
			self.lyb_mouse_click('lin2rev_daily_attendance_scene_receive', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click('lin2rev_daily_attendance_scene_close_icon', custom_threshold=0.5)
			self.status = 0

		return self.status

	def lin2rev_mail_scene(self):
		if self.status == 0: 
			self.lyb_mouse_click('lin2rev_mail_default_letter', custom_tolerance=50, custom_threshold=0.5)
			rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_mail_default_new_loc')
			if rate > 0.6:
				self.status += 1
			else:
				self.status = 10
		elif self.status == 1:
			self.lyb_mouse_click('lin2rev_mail_scene_receive_all_button')
			self.status = 10


		elif self.status == 10:
			self.lyb_mouse_click('lin2rev_mail_guild_letter', custom_tolerance=50, custom_threshold=0.5)
			self.status += 1
		elif self.status == 11: 
			self.lyb_mouse_click('lin2rev_mail_scene_receive_all_button')
			self.status = 20


		elif self.status == 20:
			self.lyb_mouse_click('lin2rev_mail_account_letter', custom_tolerance=50, custom_threshold=0.5)
			rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_mail_account_new_loc')
			if rate > 0.6:
				self.status += 1
			else:
				self.status = 30
		elif self.status == 21:
			self.lyb_mouse_click('lin2rev_mail_scene_receive_all_button')
			self.status = 30


		elif self.status == 30:
			self.lyb_mouse_click('lin2rev_mail_scene_close_icon', custom_tolerance=50, custom_threshold=0.5)
			self.status = 0

		return self.status

	def lin2rev_inventory_scene(self):
		if time.time() - self.get_checkpoint('start') > 60:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('start')
			
			self.schedule_list = self.get_game_config('schedule_list')

			if '아이템 열기' in self.schedule_list:
				# 한번 클릭으로 동작이 안된다. 리니지2가 좀 이러네...
				self.lyb_mouse_click('lin2rev_inventory_scene_consume_tab', custom_threshold=0.0)
				self.lyb_mouse_click('lin2rev_inventory_scene_consume_tab', custom_threshold=0.0)
				self.status += 1
			else:
				# 상점에 아이템 팔기
				self.status = 4
		elif self.status == 1:
			if time.time() - self.get_checkpoint('start') > 60:
				self.lyb_mouse_click('lin2rev_inventory_scene_close_icon')
				self.status += 1
				return self.status
			rate = self.game_object.rateMatchedResource(
				self.window_pixels, 
				'lin2rev_inventory_scene_consume_item_0_new_icon_loc')
			if rate > 0.5:
				self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_0_new_icon')
			else:
				self.status += 1
		elif self.status == 2:
			self.set_option('check_new_item_index', 0)
			self.status += 1
		elif self.status == 3:
			while self.get_option('check_new_item_index') < 7:
				self.set_option('check_new_item_index', self.get_option('check_new_item_index') + 1)
				try:
					rate = self.game_object.rateMatchedResource(
						self.window_pixels, 
						'lin2rev_inventory_scene_consume_item_check_' + str(self.get_option('check_new_item_index')) + '_icon_loc'
						)
					print('lin2rev_inventory_scene_consume_item_check_' + str(self.get_option('check_new_item_index')) + '_icon_loc', int(rate*100), '%')
					if rate < 0.9:
						self.lyb_mouse_click('lin2rev_inventory_scene_consume_item_check_' + str(self.get_option('check_new_item_index')) + '_icon', custom_threshold=0)
				except:
					self.loggingToGUI('lin2rev_inventory_scene_consume:' + str(sys.exc_info()[0]))
					break
			self.status += 1
		elif self.status == 4: 
			self.lyb_mouse_click('lin2rev_inventory_scene_weapon_tab', custom_threshold=0.0)
			if '자동 장착' in self.schedule_list:
				self.status += 1
			else:
				self.status = 6
		elif self.status == 5:
			self.lyb_mouse_click('lin2rev_inventory_scene_autoequip_button')
			self.status += 1
		elif self.status == 6:
			if '일괄 판매' in self.schedule_list:
				self.lyb_mouse_click('lin2rev_inventory_scene_sell_all_button')
			self.status += 1
		elif self.status == 7:
			self.lyb_mouse_click('lin2rev_inventory_scene_close_icon')
			self.status = 0

		return self.status

	def lin2rev_episode_clear_scene(self):
		self.lyb_mouse_click('lin2rev_episode_clear_scene_button')
		return self.status

	def lin2rev_main_scene(self):
		is_empty_hp_potion = self.check_potion('hp')
		is_empty_mp_potion = self.check_potion('mp')

		if is_empty_hp_potion or is_empty_mp_potion:
			self.game_object.get_scene('lin2rev_shop_scene').set_option('is_empty_hp_potion', is_empty_hp_potion)
			self.game_object.get_scene('lin2rev_shop_scene').set_option('is_empty_mp_potion', is_empty_mp_potion)
			self.lyb_mouse_click('lin2rev_main_scene_shop_icon', custom_tolerance=50, custom_threshold=0.2)
			return self.status

		if self.status == 0:

			self.schedule_list = self.get_game_config('schedule_list')

			if len(self.schedule_list) == 0:
				self.schedule_list.append('메인 퀘스트')

			self.status += 1

		elif self.status >= 1 and self.status < 100:
			s_list_iter = 0
			s_list_number = len(self.schedule_list)
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
					#TODO: 접속 종료
					self.loggingToGUI('다음 계정 작업을 위해 로그오프합니다')
					self.game_object.get_scene('lin2rev_list_scene').status = 99
					# aa =self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_main_scene_list_icon_loc')
					# print('LIST: ', int(aa*100), '%')
					self.lyb_mouse_click('lin2rev_main_scene_list_icon_0', custom_threshold=0.4)
					# CLEAR ALL SCENE INFORMATION = 1000000
					self.status = 0
				else:
					self.loggingToGUI('지정된 스케줄을 완료해서 처음으로 돌아갑니다')
					# 반복
					self.status = 1
					return self.status
			else:
				self.loggingToGUI('스케쥴링 작업 번호 ' + str(self.status) + ':' + self.current_work)
				self.set_work_status()
				return self.status

			self.status += 1

		elif self.status == self.get_work_status('메인 퀘스트') or self.status == self.get_work_status('메인 퀘스트') + 1:
			# 메인 퀘스트 상태
			# 설정값으로 받자. 퀘스트 진행


			# 퀘스트 막혔는 지 확인
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')
				if elapsed_time % 60 == 0:
					self.loggingToGUI('메인 퀘스트 남은 시간: ' + str(elapsed_time))

			quest_stop_letter_rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_main_scene_quest_stop_letter_loc')

			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST)) * 60

			# 설정으로 빼자. 180
			if ( (elapsed_time > duration_limit) or
				 # (elapsed_time > 180) or 
				 (quest_stop_letter_rate > 0.7)
				 ):
				self.loggingToGUI('경과 시간: ' + str(elapsed_time) + ', 레벨 제한 매칭률: ' + str(int(quest_stop_letter_rate*100)) +'%')
				self.status = self.last_status[self.current_work] + 1
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
				return self.status

			custom_tolerance = float(self.get_window_config('pixel_tolerance_entry')) * 1.01 * self.tolerance_weight_factor
			custom_threshold = float(self.get_window_config('threshold_entry')) * 0.99 * self.threshold_weight_factor

			ready_for_quest_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_main_scene_quest_ready_alarm_pb_1', custom_tolerance*2)
			complete_for_quest_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_main_scene_quest_complete_alarm_icon', custom_tolerance)
			tooltip_for_quest_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_main_scene_quest_tooltip_icon', custom_tolerance)
			
			# self.loggingToGUI("%s : %s[%3s%%] %s[%3s%%] %s[%3s%%] " % \
			# 	('메인퀘스트 체크', '준비됨 인식률', \
			# 	str(int(ready_for_quest_rate*100)), '완료됨 인식률', \
			# 	str(int(complete_for_quest_rate*100)), '허용 인식률', \
			# 	str(int(custom_threshold*100)) ))

			if not 'last_quest_move' in self.checkpoint:
				self.checkpoint['last_quest_move'] = time.time()

			self.loggingToGUI('퀘스트 화살표 매칭률: '+str(int(ready_for_quest_rate*100))+'% :: '+str(int(custom_threshold*0.7*100))+'%')
			if ready_for_quest_rate > custom_threshold*0.7:
				self.lyb_mouse_click('lin2rev_main_scene_quest_ready_alarm_pb_0', custom_threshold=0)
				self.checkpoint['last_quest_move'] = time.time()
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
			elif complete_for_quest_rate > custom_threshold:
				self.lyb_mouse_click('lin2rev_main_scene_quest_complete_alarm_icon', custom_tolerance, custom_threshold)
				self.checkpoint['last_quest_move'] = time.time()				
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
			elif tooltip_for_quest_rate > custom_threshold:
				self.lyb_mouse_click('lin2rev_main_scene_quest_tooltip_icon', custom_tolerance*0.5, custom_threshold)
				self.checkpoint['last_quest_move'] = time.time()				
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
			else:
				# 퀘스트 진행이 멈춘 상황을 인지하자.
				print(time.time() - self.checkpoint['last_quest_move'])
				if time.time() - self.checkpoint['last_quest_move'] > 0 and time.time() - self.checkpoint['last_quest_move'] <= 30:
					if int(time.time() - self.checkpoint['last_quest_move']) % 5 == 0:
						self.tolerance_weight_factor *= 1.1
						self.threshold_weight_factor *= 0.9
				elif time.time() - self.checkpoint['last_quest_move'] > int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST_EACH)):
					self.lyb_mouse_click('lin2rev_main_scene_quest_ready_alarm_pb_0', custom_threshold=0)
					self.checkpoint['last_quest_move'] = time.time()
					self.tolerance_weight_factor = 1
					self.threshold_weight_factor = 1
			if self.status == self.get_work_status('메인 퀘스트'):
				self.status = self.get_work_status('메인 퀘스트') + 1
			else:
				self.status = self.get_work_status('메인 퀘스트')

		elif self.status == self.get_work_status('우편함'):

			self.loggingToGUI('우편함 체크')
			if time.time() - self.checkpoint[self.current_work + '_check_start'] > 5:
				self.status = self.last_status[self.current_work] + 1
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
				return self.status

			# 우편함 확인
			custom_tolerance = float(self.get_window_config('pixel_tolerance_entry')) * 1.5 * self.tolerance_weight_factor
			custom_threshold = float(self.get_window_config('threshold_entry')) * 0.6 * self.threshold_weight_factor

			new_message_rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_main_scene_mail_new_loc')
			if new_message_rate > custom_threshold:
				self.lyb_mouse_click('lin2rev_main_scene_mail_icon', custom_tolerance=custom_tolerance, custom_threshold=custom_threshold)
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
			else:
				self.tolerance_weight_factor *= 1.1
				self.threshold_weight_factor *= 0.9
		elif (self.status == self.get_work_status('소환 상자') or self.status == self.get_work_status('우정포인트 상자')):
			if time.time() - self.checkpoint[self.current_work + '_check_start'] > 5:
				self.status = self.last_status[self.current_work] + 1
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
				return self.status

			# 상점 확인
			custom_tolerance = float(self.get_window_config('pixel_tolerance_entry')) * 1.5 * self.tolerance_weight_factor
			custom_threshold = float(self.get_window_config('threshold_entry')) * 0.9 * self.threshold_weight_factor

			new_message_rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_main_scene_shop_new_icon_loc')
			self.loggingToGUI('상점 알림 매칭률: ' + str(int(new_message_rate*100)) + '%')
			if new_message_rate > custom_threshold:
				self.lyb_mouse_click('lin2rev_main_scene_shop_icon', custom_threshold=0)
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
			else:
				self.tolerance_weight_factor *= 1.1
				self.threshold_weight_factor *= 0.9
		elif self.status == self.get_work_status('자동 장착') or self.status == self.get_work_status('일괄 판매'):
			if ( (time.time() - self.checkpoint[self.current_work + '_check_start'] > 5) or
				(time.time() - self.get_checkpoint('inventory_limit') < 60)
				):
				self.status = self.last_status[self.current_work] + 1
				return self.status
			self.lyb_mouse_click('lin2rev_main_scene_inventory_icon', custom_threshold=0)
			self.set_checkpoint('inventory_limit')
		elif self.status == self.get_work_status('아이템 열기'):
			if time.time() - self.checkpoint['아이템 열기' + '_check_start'] > 30:
				self.status = self.last_status['아이템 열기'] + 1
				return self.status
			self.lyb_mouse_click('lin2rev_main_scene_inventory_icon', custom_threshold=0)
		elif self.status == self.get_work_status('혈맹'):
			if time.time() - self.checkpoint[self.current_work + '_check_start'] > 30:
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('lin2rev_main_scene_list_icon_0', custom_threshold=0.0)
			self.game_object.get_scene('lin2rev_list_scene').status = 300

		elif self.status == self.get_work_status('친구 인사'):
			if time.time() - self.checkpoint[self.current_work + '_check_start'] > 30:
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('lin2rev_main_scene_list_icon_0', custom_threshold=0.0)
			self.game_object.get_scene('lin2rev_list_scene').status = 400

		elif self.status == self.get_work_status('일일 퀘스트') or self.status == self.get_work_status('주간 퀘스트'):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')
				if elapsed_time % 60 == 0:
					self.loggingToGUI('주간 퀘스트 남은 시간: ' + str(elapsed_time))

			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_WEEKLY_QUEST)) * 60
			if (	elapsed_time > duration_limit or
					(	self.status == self.get_work_status('주간 퀘스트') and 
						self.game_object.get_scene('lin2rev_quest_scene').get_option('weekly_quest_limit') == True)
					):
				self.status = self.last_status[self.current_work] + 1
				return self.status

			each_elapsed_time = time.time() - self.get_checkpoint('next_weekly_quest')
			each_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_WEEKLY_QUEST_EACH))
				
			if each_elapsed_time < each_limit:
				self.loggingToGUI('주간 퀘스트 진행 중['+str(int(each_elapsed_time/60))+'<'+str(each_limit))
				return self.status
			else:
				self.set_checkpoint('next_weekly_quest')
					
			self.lyb_mouse_click('lin2rev_main_scene_list_icon_0', custom_threshold=0.4)
			self.game_object.get_scene('lin2rev_list_scene').status = 200
			self.set_checkpoint('quest_limit')
		else:
			self.status = self.last_status[self.current_work] + 1

		return self.status


	def lin2rev_select_character_scene(self):
		# TODO: 몇번째 캐릭터를 고를 것인가에 대한 옵션 추가 필요
		self.lyb_mouse_click('lin2rev_select_character_scene_start_button')

		return self.status

	def lin2rev_class_tree_scene(self):		
		self.lyb_mouse_click('lin2rev_class_tree_back_button')

		return self.status

	def lin2rev_create_character_scene(self):
		self.loggingToGUI('최소한 캐릭터를 하나 생성하고 실행해주세요')

		return -1

	def lin2rev_logo_screen_scene(self):

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
				rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_account_change_icon', custom_tolerance=50)
				print('change icon:', int(rate*100), '%')
				is_there = self.lyb_mouse_click('lin2rev_account_change_icon', custom_tolerance=50, custom_threshold=0)
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

	def lin2rev_connect_account_scene(self):
		if self.status == 0:
			self.set_checkpoint('interval_login')
			self.status += 1
		elif self.status == 1:

			print('select_complete_flag:', self.get_option('select_complete_flag'))
			if (self.get_option('select_complete_flag') == True or 
				time.time() - self.get_checkpoint('interval_login') > 100):
				self.lyb_mouse_click('lin2rev_connect_account_close_icon')
				self.game_object.get_scene('lin2rev_logo_screen_scene').set_option('load_complete_flag', True)
				self.set_option('select_complete_flag', False)
				self.status = 0
			else:
				# 회색
				print('DEBUG 00')
				is_logff_status = self.lyb_mouse_click('lin2rev_google_login_letter_0', custom_threshold=0.9)
				if not is_logff_status:
					print('DEBUG 11')
					# 파란색
					self.lyb_mouse_click('lin2rev_google_login_icon')
				else:
					print('DEBUG 12')
					self.set_option('select_complete_flag', False)

		return self.status

	def lin2rev_google_play_account_select_scene(self):
		(top_loc_x, top_loc_y) = lybgame.LYBGame.locationOnWindow(
			self.window_image, 
			self.game_object.resource_manager.pixel_box_dic['lin2rev_google_play_letter']
			)
		self.loggingToGUI('구글 계정 기준점: ' + str((top_loc_x, top_loc_y)))
		if top_loc_x == -1:
			return self.status

		if self.status == 0:
			(bottom_loc_x, bottom_loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image, 
				self.game_object.resource_manager.pixel_box_dic['lin2rev_google_play_add_account_letter']
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
			self.game_object.get_scene('lin2rev_connect_account_scene').set_option('select_complete_flag', True)
		
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
				for i in range(self.status - 4):
					self.lyb_mouse_drag_location(from_x, from_y, to_x, to_y, delay=1)
				
			else:
				self.just_drag_completed = False
				# 맨아래까지 왔나?
				(bottom_loc_x, bottom_loc_y) = lybgame.LYBGame.locationOnWindow(
						self.window_image, 
						self.game_object.resource_manager.pixel_box_dic['lin2rev_google_play_add_account_letter']
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


	def lin2rev_terms_of_use_scene(self):
		#print(self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_terms_of_use_bottom_0'))
		self.lyb_mouse_click('lin2rev_terms_of_use_bottom_0')

		#print(self.game_object.rateMatchedPixelBox(self.window_pixels, 'lin2rev_terms_of_use_bottom_1'))
		self.lyb_mouse_click('lin2rev_terms_of_use_bottom_1')
		return 0
















	def get_work_status(self, work_name):
		if work_name in lybgamelin2rev.LYBLineage2Revolution.work_list:
			return (lybgamelin2rev.LYBLineage2Revolution.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999

	def check_potion(self, potion_type):

		#custom_tolerance = float(self.get_window_config('pixel_tolerance_entry')) * 1.5 * self.tolerance_weight_factor
		#custom_threshold = float(self.get_window_config('threshold_entry')) * 0.9 * self.threshold_weight_factor

		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'lin2rev_main_scene_' + potion_type +'_potion_empty_loc')
		if match_rate > 0.7:
			return True

		return False

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
import traceback

class LYBTeraScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		rc = super(LYBTeraScene, self).process(window_image, window_pixels)
		if rc == 'return':
			return self.status

		rc = 0

		if self.scene_name == 'nox_init_screen_scene':
			rc = self.nox_init_screen_scene()
		elif self.scene_name == 'connect_account_scene':
			rc = self.connect_account_scene()
		elif self.scene_name == 'google_play_account_select_scene':
			rc = self.google_play_account_select_scene()
		elif self.scene_name == 'terms_of_use_scene':
			rc = self.terms_of_use_scene()
		elif self.scene_name == 'logon_screen_scene':
			rc = self.logon_screen_scene()
		elif self.scene_name == 'tera_create_charater_scene':
			rc = self.tera_create_charater_scene()
		elif self.scene_name == 'tera_jiha_arena_main_scene':
			rc = self.tera_jiha_arena_main_scene()
		elif self.scene_name == 'tera_kaia_junjang_main_scene':
			rc = self.tera_jiha_arena_main_scene()
		elif self.scene_name == 'tera_main_scene':
			rc = self.tera_main_scene()
		elif self.scene_name == 'tera_manage_hero_scene':
			rc = self.tera_manage_hero_scene()
		elif self.scene_name == 'tera_inventory_scene':
			rc = self.tera_inventory_scene()
		elif self.scene_name == 'tera_challenge_dokripgun_scene':
			rc = self.tera_challenge_dokripgun_scene()
		elif self.scene_name == 'tera_hero_talent_scene':
			rc = self.tera_hero_talent_scene()
		elif self.scene_name == 'tera_smithy_scene':
			rc = self.tera_smithy_scene()
		elif self.scene_name == 'tera_muhantap_scene':
			rc = self.tera_muhantap_scene()
		elif self.scene_name == 'tera_daily_dungeon_scene':
			rc = self.tera_daily_dungeon_scene()
		elif self.scene_name == 'tera_summon_scene':
			rc = self.tera_summon_scene()
		elif self.scene_name == 'tera_normal_dungeon_scene':
			rc = self.tera_normal_dungeon_scene()
		elif self.scene_name == 'tera_elite_dungeon_scene':
			rc = self.tera_elite_dungeon_scene()
		elif self.scene_name == 'tera_normal_tobul_scene':
			rc = self.tera_normal_tobul_scene()
		elif self.scene_name == 'tera_elite_tobul_scene':
			rc = self.tera_elite_tobul_scene()
		elif self.scene_name == 'tera_gode_dungeon_scene':
			rc = self.tera_gode_dungeon_scene()
		elif self.scene_name == 'tera_rune_scene':
			rc = self.tera_rune_scene()
		elif self.scene_name == 'tera_mail_scene':
			rc = self.tera_mail_scene()
		elif self.scene_name == 'tera_main_menu_scene':
			rc = self.tera_main_menu_scene()
		elif self.scene_name == 'tera_play_time_scene':
			rc = self.tera_play_time_scene()
		elif self.scene_name == 'tera_continous_attendance_scene':
			rc = self.tera_continous_attendance_scene()
		elif self.scene_name == 'tera_monthly_attendance_scene':
			rc = self.tera_monthly_attendance_scene()
		elif self.scene_name == 'tera_launching_special_attendance_scene':
			rc = self.tera_launching_special_attendance_scene()
		elif self.scene_name == 'tera_yamong_attendance_scene':
			rc = self.tera_yamong_attendance_scene()
		elif self.scene_name == 'tera_common_event_scene':
			rc = self.tera_common_event_scene()
		elif self.scene_name == 'tera_guild_scene':
			rc = self.tera_guild_scene()
		elif self.scene_name == 'tera_battle_area_scene':
			rc = self.tera_battle_area_scene()
		elif self.scene_name == 'tera_injang_scene':
			rc = self.tera_injang_scene()
		elif self.scene_name == 'tera_challenge_scene':
			rc = self.tera_challenge_scene()
		elif self.scene_name == 'tera_config_scene':
			rc = self.tera_config_scene()

		elif self.scene_name == 'tera_main_quest_equip_rune_scene':
			rc = self.tera_main_quest_equip_rune_scene()
		elif self.scene_name == 'tera_main_quest_skill_scene':
			rc = self.tera_main_quest_skill_scene()
		elif self.scene_name == 'tera_main_quest_smithy_scene':
			rc = self.tera_main_quest_smithy_scene()
		elif self.scene_name == 'tera_main_quest_smithy_upgrade_scene':
			rc = self.tera_main_quest_smithy_upgrade_scene()
		elif self.scene_name == 'tera_main_quest_smithy_upgrade_scene':
			rc = self.tera_main_quest_smithy_upgrade_scene()
		elif self.scene_name == 'tera_main_quest_talent_scene':
			rc = self.tera_main_quest_talent_scene()
		elif self.scene_name == 'tera_main_quest_dungeon_quest_scene':
			rc = self.tera_main_quest_extra_scene()	
		elif self.scene_name == 'tera_main_quest_injang_scene':
			rc = self.tera_main_quest_extra_scene()	
		elif self.scene_name == 'tera_main_quest_daily_dungeon_scene':
			rc = self.tera_main_quest_extra_scene()	


		elif self.scene_name == 'tera_death_scene':
			rc = self.tera_death_scene()
		elif self.scene_name == 'tera_inventory_not_enough_scene':
			rc = self.tera_inventory_not_enough_scene()
		elif self.scene_name == 'tera_use_box_scene':
			rc = self.tera_use_box_scene()
		elif self.scene_name == 'tera_sell_all_scene':
			rc = self.tera_sell_all_scene()
		elif self.scene_name == 'tera_quest_scene':
			rc = self.tera_quest_scene()
		elif self.scene_name == 'tera_mission_scene':
			rc = self.tera_mission_scene()
		elif self.scene_name == 'tera_achievement_scene':
			rc = self.tera_achievement_scene()
		elif self.scene_name == 'tera_hero_gallery_scene':
			rc = self.tera_hero_gallery_scene()
		elif self.scene_name == 'tera_monster_dogam_scene':
			rc = self.tera_monster_dogam_scene()
		elif self.scene_name == 'tera_raid_scene':
			rc = self.tera_raid_scene()
		elif self.scene_name == 'tera_goods_scene':
			rc = self.tera_goods_scene()
		elif self.scene_name == 'tera_special_shop_scene':
			rc = self.tera_special_shop_scene()
		elif self.scene_name == 'tera_style_scene':
			rc = self.tera_style_scene()
		elif self.scene_name == 'tera_blgamesi_train_scene':
			rc = self.tera_blgamesi_train_scene()
		elif self.scene_name == 'tera_gold_giant_scene':
			rc = self.tera_gold_giant_scene()
		elif self.scene_name == 'tera_chinmildo_npc_0_scene':
			rc = self.tera_chinmildo_npc_0_scene()
		elif self.scene_name == 'tera_chinmildo_npc_1_scene':
			rc = self.tera_chinmildo_npc_1_scene()
		elif self.scene_name == 'tera_chinmildo_npc_2_scene':
			rc = self.tera_chinmildo_npc_2_scene()
		elif self.scene_name == 'tera_chinmildo_npc_3_scene':
			rc = self.tera_chinmildo_npc_3_scene()
		elif self.scene_name == 'tera_chinmildo_npc_4_scene':
			rc = self.tera_chinmildo_npc_4_scene()
		elif self.scene_name == 'tera_hero_information_scene':
			rc = self.tera_hero_information_scene()
		elif self.scene_name == 'tera_chinmildo_npc_gift_confirm_scene':
			rc = self.tera_chinmildo_npc_gift_confirm_scene()
		elif self.scene_name == 'tera_other_player_scene':
			rc = self.tera_other_player_scene()
		elif self.scene_name == 'tera_tutorial_daily_dungeon_scene':
			rc = self.tera_tutorial_daily_dungeon_scene()
		elif self.scene_name == 'tera_friend_scene':
			rc = self.tera_friend_scene()
		elif self.scene_name == 'tera_hero_gallery_each_scene':
			rc = self.tera_hero_gallery_each_scene()
		elif self.scene_name == 'tera_junjang_scene':
			rc = self.tera_junjang_scene()
		elif self.scene_name == 'tera_junjang_0_scene':
			rc = self.tera_junjang_common_scene()
		elif self.scene_name == 'tera_junjang_1_scene':
			rc = self.tera_junjang_common_scene()
		elif self.scene_name == 'tera_junjang_2_scene':
			rc = self.tera_junjang_common_scene()
		elif self.scene_name == 'tera_junjang_common_reward_scene':
			rc = self.tera_junjang_common_reward_scene()
		elif self.scene_name == 'tera_guild_donate_scene':
			rc = self.tera_guild_donate_scene()
		elif self.scene_name == 'tera_confirm_scene':
			rc = self.tera_confirm_scene()
		elif self.scene_name == 'tera_guild_tiaran_tree_scene':
			rc = self.tera_guild_tiaran_tree_scene()
		elif self.scene_name == 'tera_equip_item_scene':
			rc = self.tera_equip_item_scene()
		elif self.scene_name == 'tera_auto_select_scene':
			rc = self.tera_auto_select_scene()
		elif self.scene_name == 'tera_equip_set_scene':
			rc = self.tera_equip_set_scene()
		elif self.scene_name == 'tera_raid_matching_scene':
			rc = self.tera_raid_matching_scene()
		elif self.scene_name == 'tera_bosang_haesu_scene':
			rc = self.tera_bosang_haesu_scene()
		elif self.scene_name == 'tera_gaksung_scene':
			rc = self.tera_gaksung_scene()
		elif self.scene_name == 'tera_item_exchange_event_scene':
			rc = self.tera_item_exchange_event_scene()
		elif self.scene_name == 'tera_dungeon_death_scene':
			rc = self.tera_dungeon_death_scene()
		elif self.scene_name == 'tera_uregesipan_scene':
			rc = self.tera_uregesipan_scene()
		elif self.scene_name == 'tera_world_map_scene':
			rc = self.tera_world_map_scene()
		elif self.scene_name == 'tera_world_map_local_scene':
			rc = self.tera_world_map_local_scene()
		elif self.scene_name == 'tera_world_map_0_scene':
			rc = self.tera_world_map_common_scene()
		elif self.scene_name == 'tera_world_map_1_scene':
			rc = self.tera_world_map_common_scene()
		elif self.scene_name == 'tera_world_map_2_scene':
			rc = self.tera_world_map_common_scene()
		elif self.scene_name == 'tera_world_map_3_scene':
			rc = self.tera_world_map_common_scene()
		elif self.scene_name == 'tera_world_map_4_scene':
			rc = self.tera_world_map_common_scene()
		elif self.scene_name == 'tera_world_map_5_scene':
			rc = self.tera_world_map_common_scene()
		elif self.scene_name == 'tera_channel_scene':
			rc = self.tera_channel_scene()
		elif self.scene_name == 'tera_login_loading_scene':
			rc = self.tera_loading_scene()
		elif self.scene_name == 'tera_init_logo_loading_scene':
			rc = self.tera_loading_scene()
		elif self.scene_name == 'tera_logo_loading_error_scene':
			rc = self.tera_loading_scene()
		elif self.scene_name == 'tera_guild_skill_scene':
			rc = self.tera_guild_skill_scene()
		elif self.scene_name == 'tera_gode_dungeon_reward_scene':
			rc = self.tera_gode_dungeon_reward_scene()
		elif self.scene_name == 'tera_inventory_item_sort_scene':
			rc = self.tera_inventory_item_sort_scene()
		elif self.scene_name == 'tera_smithy_item_sort_scene':
			rc = self.tera_smithy_item_sort_scene()
		elif self.scene_name == 'tera_party_member_scene':
			rc = self.tera_party_member_scene()
		elif self.scene_name == 'tera_jehwa_shop_scene':
			rc = self.tera_jehwa_shop_scene()


		else:
			rc = 0

		return rc

	def tera_jehwa_shop_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_party_member_scene(self):

		if self.status == self.get_work_status('파티원에게 이동'):
			self.lyb_mouse_click('tera_party_member_scene_move')
			self.game_object.get_scene('tera_main_scene').set_option('파티원에게 이동' + '_end_flag', True)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_smithy_item_sort_scene(self):

		if self.status == 0:
			self.status += 1
		elif(	self.status == self.get_work_status('무기 레벨업 - 대장간') or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') or
				self.status == self.get_work_status('장신구 레벨업 - 대장간')
				):
			self.lyb_mouse_click('tera_smithy_item_sort_scene_level')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_inventory_item_sort_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('경험치 부스터 사용'):
			self.lyb_mouse_click('tera_inventory_item_sort_scene_ascending')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_gode_dungeon_reward_scene(self):

		# for i in range(3):
		# 	self.lyb_mouse_click('tera_gode_dungeon_reward_scene_' + str(i*2))
		# 	time.sleep(1)

		if self.status >= 0 and self.status < 3:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['tera_gode_dungeon_reward_scene_reward'],
						custom_threshold=0.7,
						custom_flag=1,
						custom_rect=(340, 120 + 60*self.status, 480, 120 + 60*(self.status + 1)))
			self.logger.warn(str((loc_x, loc_y)) + ':' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status += 1
		else:
			self.status = 0

		self.game_object.interval = self.period_bot(0.1)

		return self.status

	def tera_guild_skill_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0) == True:
				self.lyb_mouse_click('tera_guild_skill_scene_skill_0')
			self.status += 1
		elif self.status == 2:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1) == True:
				self.lyb_mouse_click('tera_guild_skill_scene_skill_1')
			self.status += 1
		elif self.status == 3:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2) == True:
				self.lyb_mouse_click('tera_guild_skill_scene_skill_2')
			self.status += 1
		elif self.status == 4:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3) == True:
				self.lyb_mouse_click('tera_guild_skill_scene_skill_3')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def tera_loading_scene(self):

		match_rate = self.game_object.rateMatchedResource(self.window_pixels, self.scene_name)
		if match_rate < 0.9:
			self.status = 0
			return self.status

		if self.status == 0:
			self.set_checkpoint(self.scene_name +'_start')
			self.status += 1
		elif self.status >= 1 and self.status < 100:
			elapsed_time = time.time() - self.get_checkpoint(self.scene_name +'_start')
			self.logger.debug('로딩 화면 감지: '+str(self.status)+'/90')
			self.logger.debug(str(match_rate) + ', ' + str(self.scene_name) +', ' + str(elapsed_time) + ', ' + str(self.status))

			if self.status >= 90:
				self.game_object.terminate_application()
				self.status = 0
				return self.status

			if elapsed_time > self.period_bot(30):
				self.status = 0
			else:
				self.set_checkpoint(self.scene_name +'_start')
				self.status += 1
		else:
			self.status = 0

		return self.status

	def tera_channel_scene(self):

		if self.status == 0:
			count = self.get_option('count')
			if count == None:
				count = 0
			self.game_object.get_scene('tera_main_scene').set_option('채널 변경' + '_end_flag', True)

			if count > int(self.get_game_config(lybconstant.LYB_DO_STRING_RETRY_CHANNEL)):
				self.status = 99999
			else:
				if time.time() - self.get_checkpoint('channel_clicked') < self.period_bot(8):
					# 채널 변경에 실패한 것이다.
					self.status = 99999
					self.game_object.get_scene('tera_main_scene').set_option('채널 변경' + '_end_flag', False)
				else:
					self.set_option('count', count + 1)
					self.status += 1
		elif self.status == 1:
			self.lyb_mouse_drag('tera_channel_scene_drag_top', 'tera_channel_scene_drag_bottom')
			self.status += 1
		elif self.status == 2:
			if self.get_game_config(lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE) == lybgameTera.LYBTera.channel_favorite[0]:
				self.status = 10
			else:
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_channel_scene_last_ch')
				if match_rate > 0.8:
					self.lyb_mouse_drag('tera_channel_scene_drag_bottom', 'tera_channel_scene_drag_top')
					self.status += 1
				else:
					self.status = 30
		elif self.status == 3:
			self.lyb_mouse_drag('tera_channel_scene_drag_bottom', 'tera_channel_scene_drag_top')
			self.status += 1
		elif self.status == 4:
			self.lyb_mouse_drag('tera_channel_scene_drag_bottom', 'tera_channel_scene_drag_top')
			self.status = 20
		elif self.status == 10:
			self.status += 1
		elif self.status == 11:
			min_channel = 101
			min_loc = (-1, -1)
			anchor_x, anchor_y = self.get_location('tera_channel_scene_anchor_start')

			is_done = False
			for y in range(-1, 3):
				if is_done == True:
					break
				for x in range(4):
					if x == 0 and y == -1:
						continue
					channel_percent = self.hp_status(
						'tera_channel_scene_anchor_start', 
						'tera_channel_scene_anchor_middle', 
						'tera_channel_scene_anchor_end',
						adjust=(90, 70, 60),
						adjust_s=(131*x, 38*y),
						adjust_e=(131*x, 38*y)
						)

					if channel_percent == None:
						if min_channel == 101:
							min_loc = min_loc = (anchor_x + 131*x, anchor_y + 38*y)
							is_done = True
							break
						else:
							continue

					if channel_percent == min_channel:
						rand = random.random()
						if rand < 0.5:
							min_channel = channel_percent
							min_loc = (anchor_x + 131*x, anchor_y + 38*y)	
					elif channel_percent < min_channel:
						min_channel = channel_percent
						min_loc = (anchor_x + 131*x, anchor_y + 38*y)
			self.logger.debug('Channel change 1')

			self.logger.debug('[DEBUG] MinChannel: ' + str(min_loc) + ', MaxChannel: ' + str(min_channel))
			if min_loc[0] != -1:
				# lyb_mouse_click_location2
				self.lyb_mouse_click_location2(min_loc[0], min_loc[1])
				self.set_checkpoint('channel_clicked')
				self.status = 0
			else:
				self.status = 99999
			self.logger.debug('Channel change 2')

		elif self.status == 20:
			self.status += 1
		elif self.status == 21:
			max_channel = -1
			max_loc = (-1, -1)
			anchor_x, anchor_y = self.get_location('tera_channel_scene_anchor_bottom_start')
			for y in range(-3, 1):
				for x in range(4):
					if y == -3:
						adj_y = -2
					elif y == -2:
						adj_y = -1
					else:
						adj_y = 0
					channel_percent = self.hp_status(
						'tera_channel_scene_anchor_bottom_start', 
						'tera_channel_scene_anchor_middle', 
						'tera_channel_scene_anchor_bottom_end',
						adjust=(90, 70, 60),
						adjust_s=(131*x, 38*y + adj_y),
						adjust_e=(131*x, 38*y + adj_y)
						)

					if channel_percent == None or channel_percent == 100:
						continue

					if channel_percent == max_channel:
						rand = random.random()
						if rand < 0.5:
							max_channel = channel_percent
							max_loc = (anchor_x + 131*x, anchor_y + 38*y + adj_y)	
					elif channel_percent > max_channel:
						max_channel = channel_percent
						max_loc = (anchor_x + 131*x, anchor_y + 38*y + adj_y)

			self.logger.debug('MaxChannel:' + str(max_loc) + ', ' + str(max_channel))
			if max_loc[0] != -1:
				# lyb_mouse_click_location2
				self.lyb_mouse_click_location2(max_loc[0], max_loc[1])
				self.set_checkpoint('channel_clicked')
				self.status = 0
			else:
				self.status = 99999
		elif self.status == 30:
			self.status += 1
		elif self.status == 31:
			max_channel = -1
			max_loc = (-1, -1)
			anchor_x, anchor_y = self.get_location('tera_channel_scene_anchor_start')

			for y in range(-1, 3):
				for x in range(4):
					if x == 0 and y == -1:
						continue
					channel_percent = self.hp_status(
						'tera_channel_scene_anchor_start', 
						'tera_channel_scene_anchor_middle', 
						'tera_channel_scene_anchor_end',
						adjust=(90, 70, 60),
						adjust_s=(131*x, 38*y),
						adjust_e=(131*x, 38*y)
						)

					if channel_percent == None or channel_percent == 100:
						continue
					if channel_percent == max_channel:
						rand = random.random()
						if rand < 0.5:
							max_channel = channel_percent
							max_loc = (anchor_x + 131*x, anchor_y + 38*y)	
					elif channel_percent > max_channel:
						max_channel = channel_percent
						max_loc = (anchor_x + 131*x, anchor_y + 38*y)

			self.logger.debug('MaxChannel:' + str(max_loc) + ', ' + str(max_channel))
			if max_loc[0] != -1:
				# lyb_mouse_click_location2
				self.lyb_mouse_click_location2(max_loc[0], max_loc[1])
				self.set_checkpoint('channel_clicked')
				self.status = 0
			else:
				# self.status = 99999
				self.status = 0
		elif self.status == 99998:
			self.status += 1
		else:
			self.set_option('count', 0)
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_world_map_common_scene(self):	

		# tera_world_map_0_scene : 여명의 정원
		# tera_world_map_1_scene : 버려진 평야
		# tera_world_map_2_scene : 엘리누의 언덕
		# tera_world_map_3_scene : 통곡의 해안
		# tera_world_map_4_scene : 제국령 라키타니아
		# tera_world_map_5_scene : 금지된 땅

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('지역 이동'):
			self.game_object.get_scene('tera_world_map_scene').set_option('commit_screen', True)
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 1:
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 2:
			local_index = self.get_option('local_index')
			if local_index == None:
				self.status = 99999
			else:
				self.lyb_mouse_click(self.scene_name + '_local_' + str(local_index), custom_threshold=0)
				self.game_object.get_scene('tera_world_map_local_scene').status = 10
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_world_map_local_scene(self):
		
		if self.status == 0:
			self.status += 1
		elif self.status == 10:
			self.status += 1
		elif self.status == 11:
			self.lyb_mouse_click('tera_world_map_local_scene_move')
			self.game_object.get_scene('tera_main_scene').set_option('move_local', True)
			self.status = 99999
		elif self.status == 777:
			(current_area, current_area_rate) = self.get_current_area( custom_rect=(550, 35, 590, 55))

			self.set_option('current_area', current_area)
			self.set_option('current_area_rate', current_area_rate)
			self.status = 99999
		elif self.status == self.get_work_status('몬스터 추적'):
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 1:
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 2:
			self.lyb_mouse_click('tera_world_map_local_scene_monster', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 3:
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 4:
			self.lyb_mouse_drag('tera_world_map_local_scene_monster_drag_top', 'tera_world_map_local_scene_monster_drag_bottom')
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 5:
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 6:
			self.lyb_mouse_click('tera_world_map_local_scene_monster_list_0', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 7:
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 8:
			self.lyb_mouse_click('tera_world_map_local_scene_monster_chase_0', custom_threshold=0)
			self.game_object.get_scene('tera_main_scene').set_option('chase_monster_commit', True)
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 9:
			self.status += 1
		elif self.status == self.get_work_status('몬스터 추적') + 10:
			self.status = 99999
		elif self.status == self.get_work_status('지역 이동'):
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 1:
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 2:
			self.lyb_mouse_click('tera_world_map_local_scene_worldmap', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_world_map_scene(self):
		
		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('지역 이동'):
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 1:
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 2:
			work_area = self.get_game_config(lybconstant.LYB_DO_STRING_SUB_AREA)	
			area_list = lybgameTera.LYBTera.area_list
			sub_area_dic = lybgameTera.LYBTera.sub_area_dic
			work_area_parent = ''
			work_area_parent_index = -1
			work_area_index = -1

			for area, sub_area_list in sub_area_dic.items():
				if work_area in sub_area_list:
					work_area_parent = area
					work_area_parent_index = area_list.index(area)
					work_area_index = sub_area_list.index(work_area)
					break
			world_map_loc = 'tera_world_map_scene_local_' + str(work_area_parent_index)
			world_map_scene_name = 'tera_world_map_' + str(work_area_parent_index) + '_scene'
			self.lyb_mouse_click(world_map_loc, custom_threshold=0)
			self.game_object.get_scene(world_map_scene_name).status = self.get_work_status('지역 이동')
			self.game_object.get_scene(world_map_scene_name).set_option('local_index', work_area_index)
			self.set_option('commit_screen', False)
			self.status += 1
		elif self.status == self.get_work_status('지역 이동') + 3:
			if self.get_option('commit_screen') == True:
				self.status = 99999
			else:
				self.status -= 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_uregesipan_scene(self):

		if self.status == 0:
			self.status = 99999
		elif self.status == self.get_work_status('지역 퀘스트'):
			self.game_object.get_scene('tera_main_scene').set_option('jiyuk_quest_accept', True)
			self.status = 1
		elif self.status == 1:
			self.lyb_mouse_drag('tera_uregesipan_scene_drag_top', 'tera_uregesipan_scene_drag_bottom')
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('tera_uregesipan_scene_list_0', custom_threshold=0)
			self.status += 1
		elif self.status == 3:
			self.status += 1
		elif self.status == 4:
			self.lyb_mouse_click('tera_uregesipan_scene_list_0', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_dungeon_death_scene(self):

		if self.status == 0:
			self.set_checkpoint('after_death')
			self.status += 1
		elif self.status == 1:
			buhal_count = self.get_option('buhal_count')
			if buhal_count == None:
				buhal_count = 0

			if buhal_count < int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH)):
				self.lyb_mouse_click('tera_dungeon_death_scene_buhal', custom_threshold=0)
				self.set_option('buhal_count', buhal_count + 1)
				self.logger.info('[던전 부활] 부활합니다. '+str(buhal_count+1)+'/'+str(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH)))
				self.status = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint('after_death')
				if elapsed_time > int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH)):
					self.status = 99999
				else:
					self.loggingElapsedTime('[시간 체크] 나가기 버튼 클릭까지 남은 시간', 
						elapsed_time, int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH)) )
		else:
			self.status = 0
			self.lyb_mouse_click(self.scene_name + '_close_icon')

		return self.status

	def tera_item_exchange_event_scene(self):

		if self.status == 0:
			self.lyb_mouse_drag('tera_item_exchange_event_scene_drag_top', 'tera_item_exchange_event_scene_drag_bottom')
			self.status += 1
		elif self.status == 1:
			self.status += 1
		elif self.status == 2:
			self.status += 1
		elif self.status == 3:
			is_clicked = self.lyb_mouse_click('tera_item_exchange_event_scene_exchange_0')
			if is_clicked == False:
				self.status += 1
		elif self.status == 4:
			is_clicked = self.lyb_mouse_click('tera_item_exchange_event_scene_exchange_1')
			if is_clicked == False:
				self.status += 1
		elif self.status == 5:
			is_clicked = self.lyb_mouse_click('tera_item_exchange_event_scene_exchange_2')
			if is_clicked == False:
				self.status += 1
		elif self.status == 6:
			is_clicked = self.lyb_mouse_click('tera_item_exchange_event_scene_exchange_3')
			if is_clicked == False:
				self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0


		return self.status

	def tera_gaksung_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_gaksung')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_gaksung', custom_threshold=0)

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_bosang_haesu_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('tera_bosang_haesu_scene_gold', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_raid_matching_scene(self):

		self.status = 0
		self.set_option('match_canceled', False)

		if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL) == True:
			is_full = False
			# 앞 Lv
			match_rate_0 = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_raid_match_full_party_0', custom_tolerance=50)
			self.logger.debug('match_rate 0: ' + str(match_rate_0))

			# 뒤 Lv
			match_rate_1 = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_raid_match_full_party_1', custom_tolerance=50)
			self.logger.debug('match_rate 1: ' + str(match_rate_1))

			# 앞 각성
			match_rate_2 = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_raid_match_full_party_2_0', custom_tolerance=50)
			self.logger.debug('match_rate 2: ' + str(match_rate_2))

			# 뒤 각성
			match_rate_3 = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_raid_match_full_party_2_1', custom_tolerance=50)
			self.logger.debug('match_rate 3: ' + str(match_rate_3))

			if ( match_rate_0 + match_rate_1 ) / 2 > 0.7:
				is_full = True
			elif ( match_rate_0 + match_rate_3 ) / 2 > 0.7:
				is_full = True
			elif ( match_rate_2 + match_rate_1 ) / 2 > 0.7:
				is_full = True
			elif ( match_rate_2 + match_rate_3 ) / 2 > 0.7:
				is_full = True

			if is_full == False:
				self.logger.info('[파티 매칭] 풀파티 아님: 매칭 취소함')
				self.set_option('match_canceled', True)
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				return self.status

		match_operation = int(self.get_game_config(lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION))
		is_found = False
		is_checked = False
		# print('[DEBUG] match_operation', match_operation)
		for i in range(7):
			# print('[DEBUG] ', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_RAID_MATCH_HERO+str(i)))
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_RAID_MATCH_HERO+str(i)) == False:
				continue

			is_checked = True
			# print('S -- tera_raid_match_class_' + str(i))
			# (loc_x, loc_y), match_rate = self.game_object.locationOnWindowWithRate(
			# 						self.window_image,
			# 						self.game_object.resource_manager.pixel_box_dic['tera_raid_match_class_' + str(i)],
			# 						custom_threshold=int(self.get_game_config(lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD))*0.01,
			# 						# custom_below_level=(200, 9, 0),
			# 						# custom_top_level=(255,100,10),
			# 						# custom_threshold=0.6,
			# 						# custom_flag=1,
			# 						# custom_rect=(50,120,580,254)
			# 						)

			s = time.time()
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['tera_raid_match_class_' + str(i)],
						custom_threshold=int(self.get_game_config(lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD))*0.01,
						custom_flag=1,
						custom_rect=(90,150,545,220)
						)
			e = time.time()
			self.logger.warn('E -- tera_raid_match_class_' + str(i) + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate) + ' ' + str(round(e-s, 2)))
			if loc_x == -1:
				self.logger.warn('[파티 매칭] ' + self.game_object.hero_list[i] + ' 없음')
				if match_operation == 0:
					self.set_option('match_canceled', True)
					self.lyb_mouse_click(self.scene_name + '_close_icon')
					break
			else:
				self.logger.info('[파티 매칭] ' + self.game_object.hero_list[i] + ' 있음')
				if match_operation == 1:
					is_found = True
					break

		if match_operation == 1 and is_checked == True:
			if is_found == False:
				self.set_option('match_canceled', True)
				self.lyb_mouse_click(self.scene_name + '_close_icon')


		return self.status


	def tera_equip_set_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			set_index = int(self.get_game_config(lybconstant.LYB_DO_STRING_LEVELUP_EQUIP_SET))
			self.lyb_mouse_click('tera_equip_set_scene_set_' + str(set_index), custom_threshold=0)
			self.game_object.get_scene('tera_inventory_scene').set_option('select_set', True)
			self.status = 99999
		elif self.status == self.get_work_status('장비 세트'):
			set_index = int(self.get_game_config(lybconstant.LYB_DO_STRING_EQUIP_SET))
			self.lyb_mouse_click('tera_equip_set_scene_set_' + str(set_index), custom_threshold=0)
			self.game_object.get_scene('tera_inventory_scene').set_option('select_set', True)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_jiha_arena_main_scene(self):

		self.game_object.get_scene('tera_jiha_arena_main_scene').set_option('wait_start_flag', False)

		return self.tera_main_scene()

	def tera_auto_select_scene(self):
		if self.status == 0:
			self.status += 1
		elif (	self.status == self.get_work_status('가슴 레벨업') or
				self.status == self.get_work_status('무기 레벨업') or
				self.status == self.get_work_status('신발 레벨업') or
				self.status == self.get_work_status('장갑 레벨업') or
				self.status == self.get_work_status('목걸이 레벨업') or
				self.status == self.get_work_status('반지 레벨업') or
				self.status == self.get_work_status('팔찌 레벨업') or
				self.status == self.get_work_status('귀걸이 레벨업') or
				self.status == self.get_work_status('무기 레벨업 - 대장간') or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') or
				self.status == self.get_work_status('장신구 레벨업 - 대장간')
				):
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			self.logger.debug('옵션: ' + str(work_name))
			if work_name != None and len(work_name) > 0:
				item_loc = work_name.split()[0]
				self.logger.debug('자동 선택 아이템 레벨업 부위: ' + item_loc)

				if item_loc == '방어구':
					item_loc = '가슴'
				elif item_loc == '장신구':
					item_loc = '목걸이'

				item_loc_index = lybgameTera.LYBTera.item_loc_list.index(item_loc)
				option_iterator = self.get_option('option_iterator')
				if option_iterator == None:
					option_iterator = 0

				if option_iterator < len(lybgameTera.LYBTera.item_levelup_option_list):
					option_config = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(item_loc_index) + str(option_iterator))
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_auto_select_scene_option_' + str(option_iterator))
					if option_config == True:
						if match_rate > 0.7:
							self.lyb_mouse_click('tera_auto_select_scene_option_' + str(option_iterator), custom_threshold=0)
					else:
						if match_rate < 0.7:
							self.lyb_mouse_click('tera_auto_select_scene_option_' + str(option_iterator), custom_threshold=0)

					self.set_option('option_iterator', option_iterator + 1)
				else:
					self.set_option('option_iterator', 0)
					self.status = 99990
			else:
				self.status = 99999
		elif self.status == 99990:
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			self.logger.debug('등급: ' + str(work_name))
			if work_name != None and len(work_name) > 0:
				item_loc = work_name.split()[0]
				self.logger.debug('자동 선택 아이템 레벨업 부위: ' + item_loc)

				if item_loc == '방어구':
					item_loc = '가슴'
				elif item_loc == '장신구':
					item_loc = '목걸이'

				item_loc_index = lybgameTera.LYBTera.item_loc_list.index(item_loc)

				# rank_config = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(item_loc_index))
				rank_iterator = self.get_option('rank_iterator')
				if rank_iterator == None:
					rank_iterator = 0
				self.logger.debug('아이템 등급: ' + str(lybgameTera.LYBTera.item_rank_list[rank_iterator]))
				self.lyb_mouse_click('tera_auto_select_scene_rank_' + str(rank_iterator))
				self.status = 99999
			else:
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_equip_item_scene(self):

		if self.status == 0:
			self.status += 1
		elif (	self.status == self.get_work_status('가슴 레벨업') or
				self.status == self.get_work_status('무기 레벨업') or
				self.status == self.get_work_status('신발 레벨업') or
				self.status == self.get_work_status('장갑 레벨업') or
				self.status == self.get_work_status('목걸이 레벨업') or
				self.status == self.get_work_status('반지 레벨업') or
				self.status == self.get_work_status('팔찌 레벨업') or
				self.status == self.get_work_status('귀걸이 레벨업')
				):
			self.lyb_mouse_click('tera_equip_item_scene_smithy')
			self.game_object.get_scene('tera_smithy_scene').status = self.status
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status	

	def tera_guild_tiaran_tree_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_drag('tera_guild_tiaran_tree_scene_drag_top', 'tera_guild_tiaran_tree_scene_drag_bottom')
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('tera_guild_tiaran_tree_scene_reward')
			self.status += 1
		elif self.status == 3:
			# print('tera_guild_tiaran_tree_scene_give_' + str(self.get_game_config(lybconstant.LYB_DO_STRING_TIARAN_GIVE)))
			self.logger.debug(str(int(self.get_game_config(lybconstant.LYB_DO_STRING_TIARAN_GIVE)) + 1)  + ' 번째 클릭')
			self.lyb_mouse_click('tera_guild_tiaran_tree_scene_give_' + str(self.get_game_config(lybconstant.LYB_DO_STRING_TIARAN_GIVE)))
			self.status = 99999
		else:
			self.game_object.get_scene('tera_main_scene').set_option('guild_village_done', True)
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status	

	def tera_confirm_scene(self):

		current_work = self.game_object.get_scene('tera_main_scene').current_work

		if current_work != None:
			self.logger.debug('확인 창 작업: ' + str(current_work))
			if '길드 스킬' in current_work:
				match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'tera_guild_skill_scene')
				if match_rate > 0.9:
					self.logger.debug('길드 스킬 화면('+str(int(match_rate*100))+'%)')
					return self.tera_guild_skill_scene()
			elif '채널' in current_work:
				match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'tera_channel_scene')
				if match_rate > 0.9:
					self.logger.debug('채널 변경 화면('+str(int(match_rate*100))+'%)')
					return self.tera_channel_scene()

		self.lyb_mouse_click(self.scene_name + '_close_icon')

		return self.status	

	def tera_junjang_common_reward_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('tera_junjang_common_reward_scene_receive')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status	

	def tera_junjang_common_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_junjang_common')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_junjang_common', custom_threshold=0)

		if self.status == 0:
			self.set_option('limit_count', 10)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('tera_junjang_common_scene_weekly_reward')
			self.status += 1		
		elif self.status == 2:
			self.status += 1
		elif self.status == 3:
			limit_count = self.get_option('limit_count')
			self.logger.debug('전장 참여 시도 횟수: ' + str(limit_count) + ' / 10 회')
			if limit_count < 1:
				self.status = 99999
			else:
				match_rate_limit = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_junjang_common_scene_limit')
				self.logger.warn('횟수 소진? ' + str(match_rate_limit))
				if match_rate_limit > 0.9:
					self.status = 99999
				else:
					# elapsed_time = time.time() - self.get_checkpoint('press_matching')
					# if elapsed_time > int(self.get_game_config(lybconstant.LYB_DO_STRING_WAIT_MATCHING)):
					self.lyb_mouse_click('tera_junjang_common_scene_matching')
					self.set_checkpoint('press_matching')
					self.game_object.get_scene('tera_jiha_arena_main_scene').set_option('wait_start_flag', True)
					self.game_object.get_scene('tera_jiha_arena_main_scene').status = self.get_work_status('지하 결투장')
					self.set_option('limit_count', limit_count - 1)
					self.status += 1
					# print('DEBUG1:', self.status)
		elif self.status == 4:
			# print('DEBUG2:', self.game_object.get_scene('tera_jiha_arena_main_scene').get_option('wait_start_flag'))
			if self.game_object.get_scene('tera_jiha_arena_main_scene').get_option('wait_start_flag') == False:
				self.status = 3
			elapsed_time = time.time() - self.get_checkpoint('press_matching')
			if elapsed_time > int(self.get_game_config(lybconstant.LYB_DO_STRING_WAIT_MATCHING)):
				self.status = 3
		else:
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			if work_name != None and len(work_name) > 0 and (('지하 결투장' in work_name) or ('길드 대전' in work_name)):
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)

			self.lyb_mouse_click('tera_junjang_scene_close_icon')
			self.status = 0

		return self.status	

	def tera_junjang_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_junjang')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_junjang', custom_threshold=0)

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('지하 결투장'):
			self.lyb_mouse_click('tera_junjang_scene_enter_0')
			self.status = 99999
		# elif self.status == self.get_work_status('카이아의 전장'):
			# self.lyb_mouse_click('tera_junjang_scene_enter_1')
			# self.status = 99999
		elif self.status == self.get_work_status('길드 대전'):
			self.lyb_mouse_click('tera_junjang_scene_enter_2')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_hero_gallery_each_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_each_hero')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_each_hero', custom_threshold=0)
			return self.status
			
		work_name = self.game_object.get_scene('tera_main_scene').current_work
		if work_name != None and len(work_name) > 0 and '영웅 변경' in work_name:
			self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)


		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('영웅 변경'):
			self.status += 1
		elif self.status == self.get_work_status('영웅 변경') + 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_hero_gallery_each_scene_current')
			if match_rate > 0.9:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			else:
				self.lyb_mouse_click('tera_hero_gallery_each_scene_change', custom_threshold=0)
			self.status += 1
		elif (	self.status == self.get_work_status('영웅 변경 - 솔') or
				self.status == self.get_work_status('영웅 변경 - 올렌더') or
				self.status == self.get_work_status('영웅 변경 - 레인') or
				self.status == self.get_work_status('영웅 변경 - 라브랭') or
				self.status == self.get_work_status('영웅 변경 - 리벨리아') or
				self.status == self.get_work_status('영웅 변경 - 리나') or
				self.status == self.get_work_status('영웅 변경 - 카야')
			):

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_hero_gallery_each_scene_current')
			if match_rate > 0.9:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				self.status = 99999
			else:


				self.lyb_mouse_click('tera_hero_gallery_each_scene_change', custom_threshold=0)
				self.set_checkpoint('press_change')
				self.status = 1000
		elif self.status == 1000:
			elapsed_time = time.time() - self.get_checkpoint('press_change')
			if elapsed_time > 10:
				self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def tera_friend_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_friend')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_friend', custom_threshold=0)
			return self.status

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('우정 포인트'):
			self.lyb_mouse_click('tera_friend_scene_send_all', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('우정 포인트') + 1:
			self.status = 99999
		elif self.status == self.get_work_status('친구 관리'):
			self.lyb_mouse_click('tera_friend_scene_manage', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('친구 관리') + 1:
			self.lyb_mouse_click('tera_friend_scene_surak_degi', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('친구 관리') + 2:
			# print('[DEBUG FRIEND]', self.game_object.get_friend_delete())
			if self.game_object.get_friend_delete() != True:
				is_clicked = self.lyb_mouse_click('tera_friend_scene_ok')
			else:
				is_clicked = self.lyb_mouse_click('tera_friend_scene_delete')
				self.game_object.set_friend_delete(False)

			if is_clicked < 0.5:
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_tutorial_daily_dungeon_scene(self):
		if self.status >= 0 and self.status < 30:
			elapsed_time = time.time() - self.get_checkpoint('tutorial_interval')
			if elapsed_time > 30:
				self.status = 0
			self.set_checkpoint('tutorial_interval')
			# self.logger.info('튜토리얼 스킵 대기 중입니다.'+str(self.status)+' / 30')
			# print('[DEBUG] tera_tutorial_daily_dungeon_scene:', self.status, '/ 30')
			self.status += 1
		else:
			# return -1
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def tera_other_player_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_chinmildo_npc_gift_confirm_scene(self):

		self.game_object.interval = self.period_bot(0.5)

		if self.status == 0:
			self.status += 1
		elif self.status == 1:

			# 테라M 버그 수정됨
			self.lyb_mouse_click('tera_chinmildo_npc_gift_confirm_scene_max')
			self.status += 1

			# 테라가 자꾸 다운되서 삭제함, 룬만...낱개로
			# if self.get_option('sell_each') != True:
			# 	self.lyb_mouse_click('tera_chinmildo_npc_gift_confirm_scene_max')
			# 	self.status += 1
			# else:
			# 	self.lyb_mouse_click('tera_chinmildo_npc_gift_confirm_scene_button')
			# 	self.status = 0
		else:
			self.lyb_mouse_click('tera_chinmildo_npc_gift_confirm_scene_button')
			self.status = 0

		return self.status

	def tera_hero_information_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 10:
			self.status += 1
		elif self.status == 11:
			self.status = self.get_option('last_delay_status')
		elif (	self.status == self.get_work_status('친밀도') or
				self.status == self.get_work_status('글로리아로 이동') or
				self.status == self.get_work_status('아이샤로 이동') or
				self.status == self.get_work_status('오르단으로 이동') or
				self.status == self.get_work_status('블가메시로 이동') or
				self.status == self.get_work_status('야몽으로 이동') 
				):
			self.lyb_mouse_click('tera_hero_information_scene_chinmildo', custom_threshold=0)
			self.set_option('last_delay_status', self.status + 1)
			self.status = 10
		elif (	self.status == self.get_work_status('친밀도') + 1 or
				self.status == self.get_work_status('글로리아로 이동') + 1 or
				self.status == self.get_work_status('아이샤로 이동') + 1 or
				self.status == self.get_work_status('오르단으로 이동') + 1 or
				self.status == self.get_work_status('블가메시로 이동') + 1 or
				self.status == self.get_work_status('야몽으로 이동') + 1
				):

			if self.status == self.get_work_status('글로리아로 이동') + 1:
				npc_iterator_max = 0
				self.set_option('npc_iterator', 0)
			elif self.status == self.get_work_status('아이샤로 이동') + 1:
				npc_iterator_max = 1
				self.set_option('npc_iterator', 1)
			elif self.status == self.get_work_status('오르단으로 이동') + 1:
				npc_iterator_max = 2
				self.set_option('npc_iterator', 2)
			elif self.status == self.get_work_status('블가메시로 이동') + 1:
				npc_iterator_max = 3
				self.set_option('npc_iterator', 3)
			elif self.status == self.get_work_status('야몽으로 이동') + 1:
				npc_iterator_max = 4
				self.set_option('npc_iterator', 4)
			else:
				npc_iterator_max = 4

			npc_iterator = self.get_option('npc_iterator')
			# print('==================================== DEBUG9: npc_iterator', npc_iterator, npc_iterator_max)
			if npc_iterator == None:
				self.set_option('npc_iterator', 0)
				npc_iterator = 0
			elif npc_iterator > npc_iterator_max:
				self.game_object.get_scene('tera_main_scene').set_option('친밀도'+'_end_flag', True)
				self.game_object.get_scene('tera_main_scene').set_option('글로리아로 이동'+'_end_flag', True)
				self.game_object.get_scene('tera_main_scene').set_option('아이샤로 이동'+'_end_flag', True)
				self.game_object.get_scene('tera_main_scene').set_option('오르단으로 이동'+'_end_flag', True)
				self.game_object.get_scene('tera_main_scene').set_option('블가메시로 이동'+'_end_flag', True)
				self.game_object.get_scene('tera_main_scene').set_option('야몽으로 이동'+'_end_flag', True)
				self.set_option('running', False)
				self.set_option('npc_iterator', 0)
				self.checkpoint['is_clicked'] = 0
				self.status = 99999
			else:
				if self.get_checkpoint('is_clicked') == 0:
					elapsed_time = 0
				else:
					elapsed_time = time.time() - self.get_checkpoint('is_clicked')

				is_npc_go = False
				if (	self.status == self.get_work_status('글로리아로 이동') + 1 or
						self.status == self.get_work_status('아이샤로 이동') + 1 or
						self.status == self.get_work_status('오르단으로 이동') + 1 or
						self.status == self.get_work_status('블가메시로 이동') + 1 or
						self.status == self.get_work_status('야몽으로 이동') + 1
					):
					is_npc_go = True
					# self.set_option('npc_iterator', npc_iterator + 1)
				else:
					i = 0
					for each_gift in lybgameTera.LYBTera.gift_item_list:
						is_gift = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CHINMILDO_NPC_GIFT + str(npc_iterator) + str(i))
						is_npc_go = is_npc_go or is_gift
						i += 1

				if is_npc_go == False or ( elapsed_time != 0 and (
					elapsed_time < 5 or ( elapsed_time > 120 and elapsed_time < 150 ) ) ) :
					self.logger.debug(lybgameTera.LYBTera.chinmildo_npc_list[npc_iterator] + ' 패스')
					self.set_option('npc_iterator', npc_iterator + 1)
				else:
					self.lyb_mouse_click('tera_hero_information_scene_chinmildo_' + str(npc_iterator), custom_threshold=0)
					self.logger.debug(lybgameTera.LYBTera.chinmildo_npc_list[npc_iterator] + ' 이동')
					self.set_checkpoint('is_clicked')
					self.set_option('running', True)
					self.game_object.get_scene('tera_chinmildo_npc_' + str(npc_iterator) + '_scene').status = self.status - 1
					self.game_object.get_scene('tera_chinmildo_npc_' + str(npc_iterator) + '_scene').set_option('my_index', npc_iterator)

		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_chinmildo_npc_0_scene(self):

		return self.tera_chinmildo_npc_scene()

	def tera_chinmildo_npc_1_scene(self):

		return self.tera_chinmildo_npc_scene()
		
	def tera_chinmildo_npc_2_scene(self):

		return self.tera_chinmildo_npc_scene()
		
	def tera_chinmildo_npc_3_scene(self):

		return self.tera_chinmildo_npc_scene()
		
	def tera_chinmildo_npc_4_scene(self):

		return self.tera_chinmildo_npc_scene()

	def tera_chinmildo_npc_scene(self):
		self.game_object.interval = self.period_bot(0.5)

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_chinmildo_npc_scene' + '_red_gem')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_chinmildo_npc_scene' + '_red_gem', custom_threshold=0)


		# FIXME
		# if self.get_option('TEST') != True:
		# 	self.status = self.get_work_status('친밀도')
		# 	self.set_option('my_index', 2)
		# 	self.set_option('TEST', True)

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('친밀도'):
			npc_index = self.get_option('my_index')
			self.game_object.get_scene('tera_hero_information_scene').set_option('running', False)
			npc_iterator = self.game_object.get_scene('tera_hero_information_scene').get_option('npc_iterator')
			if npc_iterator == None:
				npc_iterator = 0

			gift_index = self.get_option('gift_index')
			if gift_index == None:
				gift_index = 0
				self.set_option('gift_index', 0)
			
			if gift_index == 3:
				self.game_object.get_scene('tera_chinmildo_npc_gift_confirm_scene').set_option('sell_each', True)
			else:
				self.game_object.get_scene('tera_chinmildo_npc_gift_confirm_scene').set_option('sell_each', False)

			if gift_index > len(lybgameTera.LYBTera.gift_item_list) - 1:
				self.status = 99999
				self.game_object.get_scene('tera_hero_information_scene').set_option('npc_iterator', npc_iterator + 1)
				self.set_option('gift_index', 0)
			else:
				is_gift = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_CHINMILDO_NPC_GIFT + str(npc_index) + str(gift_index))
				if is_gift == True:
					gift_index = self.get_option('gift_index')
					if gift_index == None:
						gift_index = 0

					self.lyb_mouse_click('tera_chinmildo_npc_gift_' + str(gift_index), custom_threshold=0)
					self.logger.debug(lybgameTera.LYBTera.gift_item_list[gift_index] + ' 탭 클릭')
					self.set_option('gift_index', gift_index+1)
					self.status += 1
				else:
					self.set_option('gift_index', gift_index + 1)		
		elif self.status == self.get_work_status('친밀도') + 1:
			drag_count = self.get_option('drag_count')
			drag_max_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG))
			if drag_count == None:
				drag_count = 0

			# print('DRAG', drag_count)
			if drag_count < drag_max_count:
				self.logger.debug('[친밀도   ] 화면 아래로 드래그 ' + str(drag_count) + '/' + str(drag_max_count))				
				self.lyb_mouse_drag('tera_chinmildo_drag_bottom', 'tera_chinmildo_drag_top')
				self.set_option('drag_count', drag_count + 1)
				self.set_option('current_pos', 'bottom')
			elif drag_count > drag_max_count and drag_count <= drag_max_count * 2 + 1:
				self.logger.debug('[친밀도   ] 화면 위로 드래그 ' + str(drag_count) + '/' + str(drag_max_count*2 + 1))				
				self.lyb_mouse_drag('tera_chinmildo_drag_top', 'tera_chinmildo_drag_bottom')
				self.set_option('drag_count', drag_count + 1)
				self.set_option('current_pos', 'top')
			else:
				self.set_option('drag_count', drag_count + 1)
				self.status += 1
			
		elif self.status == self.get_work_status('친밀도') + 2:
			rank = self.get_game_config(lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK)
			rank_index = lybgameTera.LYBTera.item_rank_list.index(rank)
			drag_max_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG))

			gift_capacity = self.get_option('gift_capacity')
			if gift_capacity == None:
				gift_capacity = 0

			item_width_iterator = self.get_option('item_width_iterator')
			if item_width_iterator == None:
				item_width_iterator = 0

			item_height_iterator = self.get_option('item_height_iterator')
			if item_height_iterator == None:
				item_height_iterator = 0

			rank_iterator = self.get_option('rank_iterator')
			if rank_iterator == None:
				rank_iterator = 0

			# print('item_width_iterator:', item_width_iterator, 'item_height_iterator:', item_height_iterator, 'drag_count', self.get_option('drag_count'))
			# print('gift_capacity:', gift_capacity)
			if gift_capacity > 4:
				self.status += 1

				return self.status

			if item_width_iterator > 4:
				self.set_option('item_width_iterator', 0)
				self.set_option('item_height_iterator', item_height_iterator + 1)
				self.status += 1

				return self.status		

			if item_height_iterator > 2:
				self.set_option('item_height_iterator', 0)
				self.set_option('item_width_iterator', 0)

				if gift_capacity > 0:
					self.status += 1
				else:
					if self.get_option('drag_count') == drag_max_count + 1:
						self.status -= 1
					elif self.get_option('drag_count') > (drag_max_count*2 - 1):
						self.set_option('drag_count', 0)
						self.status = self.get_work_status('친밀도')

				return self.status

			# print('rank_iterator:', rank_iterator, self.get_option('is_there'))
			if rank_iterator >= len(lybgameTera.LYBTera.item_rank_list):
				self.set_option('rank_iterator', 0)

				# 영웅 전설 신화 추가한 다음에 여기 주석 풀자
				if self.get_option('is_there') != True:
					self.set_option('item_width_iterator', 0)
					self.set_option('item_height_iterator', item_height_iterator + 1)

				return self.status

			

			

			# print('DEBUG0: anchor ===> ', (comp_x, comp_y))
			# print('current_pos=', self.get_option('current_pos'), 'rank_iterator=', rank_iterator)


			if self.get_option('give_count') != None and self.get_option('give_count') > 100:
				self.status = self.get_work_status('친밀도')
				return self.status
			else:
				comp_pb = 'tera_chinmildo_compare_anchor_' + self.get_option('current_pos')
				# print('DEBUG4:', comp_pb)
				(comp_x, comp_y) = self.get_location(comp_pb)

				item_pb = 'tera_chinmildo_item_class_' + str(rank_iterator)
				item_rank = lybgameTera.LYBTera.item_rank_list[rank_iterator]
				loc_x = comp_x + item_width_iterator * 62 # 테라 친밀도 정사각형 넓이 간격

				if self.get_option('current_pos') == 'top':
					loc_y = comp_y + item_height_iterator * 62 # 테라 친밀도 정사각형 높이 간격
				else:
					loc_y = comp_y - item_height_iterator * 62 # 테라 친밀도 정사각형 높이 간격

				is_matched = False
				self.set_option('is_there', False)
				for i in range(-3,4):
					is_matched_each = self.game_object.isMatchedCenterPixelBox(
						self.window_pixels,
						item_pb,
						custom_x = loc_x,
						custom_y = loc_y + i,
						custom_tolerance = int(int(self.get_window_config('pixel_tolerance_entry')) * 1.5)
						)
					# print('DEBUG0:', (loc_x, loc_y + i), is_matched_each)

					is_matched = is_matched or is_matched_each

				if rank_iterator <= rank_index:
					self.logger.debug('[친밀도   ] 검사 ' + item_rank + ' ' + 
						str(item_width_iterator + 5*item_height_iterator) + '/15 ' + str((loc_x, loc_y)) + ' ' + str(is_matched))
				else:
					self.logger.debug('[친밀도   ] 패스 ' + item_rank + ' ' + 
						str(item_width_iterator + 5*item_height_iterator) + '/15 ' + str((loc_x, loc_y)) + ' ' + str(is_matched))


				if is_matched == True:
					if rank_iterator <= rank_index:
						# lyb_mouse_click_location2
						self.lyb_mouse_click_location(loc_x, loc_y)
						gift_capacity += 1
						self.set_option('gift_capacity', gift_capacity)
					self.set_option('item_width_iterator', item_width_iterator + 1)
					self.set_option('rank_iterator', 0)
					self.set_option('is_there', True)
				else:
					self.set_option('rank_iterator' , rank_iterator + 1)
					# 전부 다 검색하게 하려고

				# print('DEBUG2:', (loc_x, loc_y), item_match_rate)

				# if loc_x != -1:
				# 	self.lyb_mouse_click_location(loc_x, loc_y)
				# 	self.status += 1
				# else:
				# 	if self.get_option('drag_count') != None and self.get_option('drag_count') > 2:
				# 		self.set_option('item_iterator', item_iterator - 1)
				# 		for i in range(self.get_option('drag_count')):
				# 			self.lyb_mouse_drag('tera_chinmildo_drag_top', 'tera_chinmildo_drag_bottom')
				# 			time.sleep(1)
				# 		self.set_option('drag_count', 0)
				# 	else:
				# 		drag_count = self.get_option('drag_count')
				# 		if drag_count == None:
				# 			drag_count = 0

				# 		self.lyb_mouse_drag('tera_chinmildo_drag_bottom', 'tera_chinmildo_drag_top')
				# 		time.sleep(1)
				# 		self.set_option('drag_count', drag_count + 1)

				# self.loggingToGUI('친밀도 점수 ' + str(self.game_object.item_rank_list[item_iterator]) + ' 점 인식률: ' +
				# 	str(int(item_match_rate*100)) + ' / ' + str(int(chinmildo_threshold*100)) + ' %')

				# print('DEBUG2-1: ', str(self.game_object.item_rank_list[item_iterator]))
				# print('DEBUG3')

			# print('DEBUG: ', item_iterator, gift_capacity)

			# item_rank = self.get_option('item_rank')
			# if item_rank == None:
			# 	item_rank = 0

			# rank = self.get_game_config(lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK)
			# rank_index = lybgameTera.LYBTera.item_rank_list.index(rank)

			# if item_rank <= rank_index:
			# 	self.loggingToGUI(lybgameTera.LYBTera.item_rank_list[item_rank] + ' 찾는 중')
			# 	(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
			# 		self.window_image, 
			# 		self.game_object.resource_manager.pixel_box_dic['tera_chinmildo_item_class_'+str(item_rank)])

			# 	print('DEBUG CHINMILDO 0:', item_rank, loc_x, loc_y)
			# 	print('DEBUG CHINMILDO 0:', self.get_option('drag_count'))

			# 	if ( 	loc_x == -1 or 
			# 			( self.get_option('give_count') != None and self.get_option('give_count') > 20)
			# 			):
			# 		if self.get_option('drag_count') == None or self.get_option('drag_count') < 1:
			# 			self.status += 2
			# 		else:
			# 			self.set_option('item_rank', item_rank + 1)
			# 			self.set_option('give_count', 0)
			# 			if self.get_option('drag_count') != None and self.get_option('drag_count') > 0:
			# 				for i in range(self.get_option('drag_count')):
			# 					self.lyb_mouse_drag('tera_chinmildo_drag_top', 'tera_chinmildo_drag_bottom')
			# 					time.sleep(1)
			# 				self.set_option('drag_count', 0)
			# 	else:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.status += 1
			# else:
			# 	self.status = self.get_work_status('친밀도')
			# 	self.set_option('item_rank', 0)
		elif self.status == self.get_work_status('친밀도') + 3:
			drag_max_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG))
			give_count = self.get_option('give_count')
			if give_count == None:
				give_count = 0

			is_debug_mode = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO)

			self.logger.debug('선물 하기 디버깅 모드: ' + str(is_debug_mode) + ', 선물 횟수: ' + str(give_count))

			if is_debug_mode == False:
				if self.get_option('gift_capacity') != None and self.get_option('gift_capacity') > 0:
					self.set_option('give_count', give_count + 1)
					self.lyb_mouse_click('tera_chinmildo_npc_scene_give')
					self.set_option('item_width_iterator', 0)
					self.set_option('item_height_iterator', 0)
					self.set_option('gift_capacity', 0)
					if self.get_option('drag_count') <= drag_max_count + 1 :
						# 아래 쪽 하는 중에 선물하기를 누르면 화면이 초기화 된다.
						self.set_option('drag_count', 0)
					else:
						self.set_option('drag_count', (drag_max_count*2) - 1)

					self.status = self.get_work_status('친밀도') + 1
					return self.status

			self.status -= 1
		# elif self.status == self.get_work_status('친밀도') + 3:
		# 	drag_count = self.get_option('drag_count')
		# 	if drag_count == None:
		# 		drag_count = 0
		# 	print('DEBUG CHINMILDO 3:', drag_count)
		# 	self.lyb_mouse_drag('tera_chinmildo_drag_bottom', 'tera_chinmildo_drag_top')
		# 	time.sleep(1)
		# 	self.set_option('drag_count', drag_count + 1)
		# 	self.status -= 2
		else:
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			if (	work_name != None and len(work_name) > 0 and 
					('친밀도' in work_name or '이동' in work_name)
					):
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)
			self.lyb_mouse_click('tera_chinmildo_npc_scene' + '_close_icon')
			self.status = 0

		return self.status

	def tera_style_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_style')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_style', custom_threshold=0)

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click('tera_style_scene_close' + '_icon')
			self.status = 0

		return self.status

	def tera_special_shop_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('길드 상점 - 경험치'):
			self.game_object.interval = self.period_bot(3)
			self.status += 1
		elif self.status == self.get_work_status('길드 상점 - 경험치') + 1:
			self.lyb_mouse_click('tera_special_shop_scene_guild_token', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('길드 상점 - 경험치') + 2:
			exp_potion_iterator = self.get_option('exp_potion_iterator')
			if exp_potion_iterator == None:
				exp_potion_iterator = 0

			print('[DEBUG] Guild Exp Potion', exp_potion_iterator)
			if exp_potion_iterator < int(self.get_game_config(lybconstant.LYB_DO_STRING_GUILD_EXP_POTION)):
				self.set_option('exp_potion_iterator', exp_potion_iterator+1)
				pb_name = 'tera_special_shop_scene_guild_token_exp'
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.9,
										custom_flag=1,
										custom_rect=(120,110,630,380)
										)	
				self.logger.debug(str(pb_name) + ':' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.set_option('exp_potion_iterator', 0)
				self.status = 99999
		elif self.status == self.get_work_status('길드 상점 - 대량의 경험치'):
			self.game_object.interval = self.period_bot(3)
			self.status += 1
		elif self.status == self.get_work_status('길드 상점 - 대량의 경험치') + 1:
			self.lyb_mouse_click('tera_special_shop_scene_guild_token', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('길드 상점 - 대량의 경험치') + 2:
			pb_name = 'tera_special_shop_scene_guild_token_big_exp'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
									self.window_image,
									self.game_object.resource_manager.pixel_box_dic[pb_name],
									custom_threshold=0.9,
									custom_flag=1,
									custom_rect=(120,110,630,380)
									)	
			self.logger.debug(str(pb_name) + ':' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status = 99999
		elif self.status == self.get_work_status('경험치 부스터 구매'):
			self.set_option('exp_booster_iterator', 0)
			self.status += 1
		elif self.status == self.get_work_status('경험치 부스터 구매') + 1:
			self.lyb_mouse_click('tera_special_shop_scene_somopum', custom_threshold=0)
			self.set_option('exp_find_limit', 0)
			self.status += 2
		elif self.status == self.get_work_status('경험치 부스터 구매') + 2:
			self.lyb_mouse_drag('tera_special_shop_scene_drag_bottom', 'tera_special_shop_scene_drag_top')
			self.game_object.interval = self.period_bot(3)
			self.status += 1
		elif self.status == self.get_work_status('경험치 부스터 구매') + 3:
			self.logger.debug('exp_booster_iterator: '+str(self.get_option('exp_booster_iterator')))
			if self.get_option('exp_booster_iterator') == 0:
				game_config = lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1
				pb_name = 'tera_somopum_exp_1'
			elif self.get_option('exp_booster_iterator') == 1:
				game_config = lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2
				pb_name = 'tera_somopum_exp_2'
			else:
				game_config = lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5
				pb_name = 'tera_somopum_exp_5'


			if self.get_game_config(game_config) == True:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.9,
										custom_flag=1,
										custom_rect=(120,110,630,380)
										)	
				self.logger.debug(str(pb_name) + ':' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)))
				if loc_x == -1:
					if self.get_option('exp_find_limit') > 10:
						self.set_option('exp_find_limit', 0)
						self.status += 1
					else:
						exp_find_limit = self.get_option('exp_find_limit')
						self.set_option('exp_find_limit', exp_find_limit + 1)
						self.status -= 1
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status += 1

			# self.lyb_mouse_click('tera_special_shop_scene_buy_0', custom_threshold=0)
			# self.status += 1
		elif self.status == self.get_work_status('경험치 부스터 구매') + 4:
			exp_booster_iterator = self.get_option('exp_booster_iterator')
			if exp_booster_iterator == 2:
				self.status = 99999
			else:
				self.set_option('exp_booster_iterator', exp_booster_iterator + 1)
				self.status = self.get_work_status('경험치 부스터 구매') + 2
		# elif self.status == self.get_work_status('경험치 부스터 구매') + 5:
		# 	if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2) == True:
		# 		self.lyb_mouse_click('tera_special_shop_scene_buy_0', custom_threshold=0)
		# 	self.status += 1
		# elif self.status == self.get_work_status('경험치 부스터 구매') + 6:
		# 	if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5) == True:
		# 		self.status += 1
		# 	else:
		# 		self.status = 99999
		# elif (	self.status >= self.get_work_status('경험치 부스터 구매') + 7 and
		# 		self.status <= self.get_work_status('경험치 부스터 구매') + 11
		# 		):
		# 	self.lyb_mouse_drag('tera_special_shop_scene_drag_bottom', 'tera_special_shop_scene_drag_top')
		# 	self.game_object.interval = self.period_bot(3)
		# 	self.status += 1
		# elif self.status == self.get_work_status('경험치 부스터 구매') + 12:
		# 	self.lyb_mouse_click('tera_special_shop_scene_buy_1')
		# 	self.status = 99999

		elif self.status == self.get_work_status('골드 부스터 구매'):
			self.set_option('gold_booster_iterator', 0)
			self.status += 1
		elif self.status == self.get_work_status('골드 부스터 구매') + 1:
			self.lyb_mouse_click('tera_special_shop_scene_somopum', custom_threshold=0)
			self.set_option('gold_find_limit', 0)
			self.status += 2
		elif self.status == self.get_work_status('골드 부스터 구매') + 2:
			self.lyb_mouse_drag('tera_special_shop_scene_drag_bottom', 'tera_special_shop_scene_drag_top')
			self.game_object.interval = self.period_bot(3)
			self.status += 1
		elif self.status == self.get_work_status('골드 부스터 구매') + 3:
			self.logger.debug('gold_booster_iterator: '+str(self.get_option('gold_booster_iterator')))
			if self.get_option('gold_booster_iterator') == 0:
				game_config = lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1
				pb_name = 'tera_somopum_gold_1'
			elif self.get_option('gold_booster_iterator') == 1:
				game_config = lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2
				pb_name = 'tera_somopum_gold_2'
			else:
				game_config = lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5
				pb_name = 'tera_somopum_gold_5'

			self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')

			if self.get_game_config(game_config) == True:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.9,
										custom_flag=1,
										custom_rect=(120,110,630,380)
										)	
				self.logger.debug(str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)))
				if loc_x == -1:
					if self.get_option('gold_find_limit') > 10:
						self.set_option('gold_find_limit', 0)
						self.status += 1
					else:
						gold_find_limit = self.get_option('gold_find_limit')
						self.set_option('gold_find_limit', gold_find_limit + 1)
						self.status -= 1
				else:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
			else:
				self.status += 1

			# self.lyb_mouse_click('tera_special_shop_scene_buy_0', custom_threshold=0)
			# self.status += 1
		elif self.status == self.get_work_status('골드 부스터 구매') + 4:
			gold_booster_iterator = self.get_option('gold_booster_iterator')
			if gold_booster_iterator == 2:
				self.status = 99999
			else:
				self.set_option('gold_booster_iterator', gold_booster_iterator + 1)
				self.status = self.get_work_status('골드 부스터 구매') + 2

		# elif self.status == self.get_work_status('골드 부스터 구매'):
		# 	self.status += 1
		# elif self.status == self.get_work_status('골드 부스터 구매') + 1:
		# 	self.lyb_mouse_click('tera_special_shop_scene_somopum', custom_threshold=0)
		# 	self.status += 1
		# elif (	self.status >= self.get_work_status('골드 부스터 구매') + 2 and
		# 		self.status <= self.get_work_status('골드 부스터 구매') + 7
		# 		):
		# 	self.lyb_mouse_drag('tera_special_shop_scene_drag_bottom', 'tera_special_shop_scene_drag_top')
		# 	self.game_object.interval = self.period_bot(3)
		# 	self.status += 1
		# elif self.status == self.get_work_status('골드 부스터 구매') + 8:
		# 	if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1) == True:
		# 		self.lyb_mouse_click('tera_special_shop_scene_buy_2')
		# 	self.status += 1
		# elif (	self.status >= self.get_work_status('골드 부스터 구매') + 9 and
		# 		self.status <= self.get_work_status('골드 부스터 구매') + 14
		# 		):
		# 	self.lyb_mouse_drag('tera_special_shop_scene_drag_bottom', 'tera_special_shop_scene_drag_top')
		# 	self.game_object.interval = self.period_bot(3)
		# 	self.status += 1
		# elif self.status == self.get_work_status('골드 부스터 구매') + 15:
		# 	if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2) == True:
		# 		self.lyb_mouse_click('tera_special_shop_scene_buy_3')
		# 	self.status += 1
		# elif (	self.status >= self.get_work_status('골드 부스터 구매') + 16 and
		# 		self.status <= self.get_work_status('골드 부스터 구매') + 21
		# 		):
		# 	self.lyb_mouse_drag('tera_special_shop_scene_drag_bottom', 'tera_special_shop_scene_drag_top')
		# 	self.game_object.interval = self.period_bot(3)
		# 	self.status += 1
		# elif self.status == self.get_work_status('골드 부스터 구매') + 22:
		# 	if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5) == True:
		# 		self.lyb_mouse_click('tera_special_shop_scene_buy_4')
		# 	self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def tera_goods_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click('tera_goods_scene_close' + '_icon')
			self.status = 0

		return self.status

	def tera_raid_scene(self):

		# if self.get_option('delay_complete') != True:
		# 	self.set_option('delay_complete', True)
		# 	return self.status

		if (	self.status == self.get_work_status('독립군 보급 기지') or
				self.status == self.get_work_status('후카족 마을 수복전') or
				self.status == self.get_work_status('밤피르의 저택') or
				self.status == self.get_work_status('달의 호수 쟁탈전') or
				self.status == self.get_work_status('황금의 미궁') or
				self.status == self.get_work_status('왕자의 궁전') or
				self.status == self.get_work_status('불의 제단')
			):
			if self.game_object.get_scene('tera_main_scene').get_option('elite_mode') != True:
				self.lyb_mouse_click('tera_raid_scene_normal_dungeon', custom_threshold=0)
			else:
				self.lyb_mouse_click('tera_raid_scene_elite_dungeon_80', custom_threshold=0)

			self.status = 99999
		elif (	self.status == self.get_work_status('벤튤라') or
				self.status == self.get_work_status('데미안') or
				self.status == self.get_work_status('그림자 기수') or
				self.status == self.get_work_status('굴') or
				self.status == self.get_work_status('티라누스') or
				self.status == self.get_work_status('라우라바') 
			):
			if self.game_object.get_scene('tera_main_scene').get_option('elite_mode') != True:
				self.lyb_mouse_click('tera_raid_scene_normal_tobul', custom_threshold=0)
			else:
				self.lyb_mouse_click('tera_raid_scene_elite_tobul', custom_threshold=0)

			self.status = 99999
		elif (	self.status == self.get_work_status('고대 던전 입구') or
				self.status == self.get_work_status('고대 던전 1구역') or
				self.status == self.get_work_status('고대 던전 2구역')
			):
			self.lyb_mouse_click('tera_raid_scene_gode_dungeon', custom_threshold=0)
			self.game_object.get_scene('tera_gode_dungeon_scene').status = self.status
			self.status = 99999
		elif self.status == self.get_work_status('카이아의 던전'):
			self.lyb_mouse_click('tera_raid_scene_kaia_dungeon', custom_threshold=0)
			self.game_object.get_scene('tera_kaia_dungeon_scene').status = self.status
			self.status = 99999			
		elif self.status == 99990:
			self.status += 1
		elif self.status == 99991:
			self.status += 1
		elif self.status == 99999:
			self.status = 99990
		else:
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			if work_name != None and self.get_work_status(work_name) > self.get_work_status('몬스터 도감'):
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_end', True)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', False)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)

			# self.set_option('delay_complete', False)
			self.lyb_mouse_click('tera_raid_scene' + '_close_icon')
			self.status = 0

		return self.status


	def tera_monster_dogam_scene(self):

		if self.status == 0:
			is_clicked = self.lyb_mouse_click('tera_monster_dogam_reward_0')
			if is_clicked == False:
				self.lyb_mouse_click('tera_monster_dogam_active')
			self.status += 1
		elif self.status == self.get_work_status('몬스터 도감'):
			if self.get_option('retry_complete_flag') != True:
				self.set_option('retry_complete_flag', True)
				self.lyb_mouse_click(self.scene_name + '_close_icon')
			else:
				self.status = 1100
		elif self.status == 1100:
			self.game_object.get_scene('tera_main_scene').set_option('dogam_opened', True)
			self.set_option('retry_complete_flag', False)
			rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_monster_dogam_reward_0')
			if rate_match > 0.8:
				self.lyb_mouse_click('tera_monster_dogam_reward_0', custom_threshold=0.8)
			else:
				self.status = 1101
		elif self.status == 1101:
			rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_monster_dogam_active')
			if rate_match > 0.8:
				self.lyb_mouse_click('tera_monster_dogam_active', custom_threshold=0.8)
			else:
				self.status += 1
		elif self.status == 1102:
			is_clicked = self.lyb_mouse_click('tera_monster_dogam_chase_0')
			if is_clicked == False:
				self.game_object.get_scene('tera_main_scene').set_option('몬스터 도감' + '_end_flag', True)
				self.status = 99999
			else:
				self.set_checkpoint('dogam_chase')
				self.status += 1
		elif self.status == 1103:
			self.status += 1
		elif self.status == 1104:
			self.status = self.get_work_status('몬스터 도감')
		else:
			self.lyb_mouse_click('tera_monster_dogam_scene' + '_close_icon')
			self.status = 0

		return self.status

	# def tera_monster_dogam_scene(self):

	# 	area_list = lybgameTera.LYBTera.area_list
	# 	sub_area_dic = lybgameTera.LYBTera.sub_area_dic
	# 	work_area = self.get_game_config(lybconstant.LYB_DO_STRING_DOGAM_AREA)
	# 	match_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD)) * 0.01

	# 	if match_threshold > 1:
	# 		match_threshold = 1
	# 	elif match_threshold < 0:
	# 		match_threshold = 0

	# 	# print('dogam status=', self.status, match_threshold)

	# 	red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_monster_dogam')
	# 	if red_gem > 0.2:
	# 		self.lyb_mouse_click('tera_red_gem_monster_dogam', custom_threshold=0.2)

	# 	work_name = self.game_object.get_scene('tera_main_scene').current_work 
	# 	if work_name != None and work_name != '몬스터 도감':
	# 		rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_monster_dogam_reward_0')
	# 		if rate_match > 0.8:
	# 			self.lyb_mouse_click('tera_monster_dogam_reward_0', custom_threshold=0.8)
	# 		else:
	# 			self.status = 99999

	# 	if self.status == 0:
	# 		self.game_object.get_scene('tera_main_scene').set_option('dogam_opened', True)

	# 		work_area_parent = area_list[0]
	# 		work_area_parent_index = 0
	# 		work_area_index = 0

	# 		for area, sub_area_list in sub_area_dic.items():
	# 			if work_area in sub_area_list:
	# 				work_area_parent = area
	# 				work_area_parent_index = area_list.index(area)
	# 				work_area_index = sub_area_list.index(work_area)
	# 				break

	# 		self.loggingToGUI('몬스터 도감 작업할 지역: ' + work_area_parent + '-' + work_area + '(' + str(work_area_parent_index) + ':' + str(work_area_index) +')')

	# 		self.status = work_area_parent_index
	# 		self.set_option('sub_area_iterator', work_area_index)
	# 		self.set_option('init_done', True)
	# 		self.status += 1
	# 	elif self.status >= 1 and self.status < len(area_list) + 1:

	# 		iterator = self.status - 1

	# 		for i in range(len(area_list)):
	# 			print("[DEBUG] 몬스터 도감 - ", i, area_list[i])

	# 		area_name = 'tera_monster_dogam_left_area_' + str(iterator)
			
	# 		# (loc_x, loc_y), dogam_rate = lybgame.LYBGame.locationOnWindowWithRate(
	# 		# 	self.window_image,
	# 		# 	self.game_object.resource_manager.pixel_box_dic[area_name],
	# 		# 	custom_threshold=match_threshold,
	# 		# 	custom_below_level=(10, 10, 10),
	# 		# 	custom_top_level=(255,255,255)
	# 		# 	)
	# 		(loc_x, loc_y), dogam_rate = self.game_object.locationOnWindowPart(
	# 						self.window_image,
	# 						self.game_object.resource_manager.pixel_box_dic[area_name],
	# 						custom_below_level=(100, 100, 100),
	# 						custom_top_level=(255,255,255),
	# 						custom_threshold=match_threshold,
	# 						custom_flag=1,
	# 						custom_rect=(25,140,45,380)
	# 						)
	# 		print(area_list[iterator],':', (loc_x, loc_y), dogam_rate)
	# 		self.loggingToGUI(area_list[iterator] + ' 매칭률: ' + str(int(dogam_rate * 100)) + ' / ' + str(int(match_threshold*100)) + ' %')
			
	# 		if loc_x == -1:
	# 			drag_count = self.get_option('drag_count')
	# 			if drag_count == None:
	# 				drag_count = 0

	# 			if drag_count > 2:
	# 				self.status += 1
	# 				for i in range(drag_count):
	# 					self.lyb_mouse_drag('tera_monster_dogam_scene_drag_top', 'tera_monster_dogam_scene_drag_bottom')
	# 					time.sleep(1)
	# 				self.set_option('drag_count', 0)
	# 				self.loggingToGUI(str(area_list[iterator]) + '을 찾지 못했습니다.')
	# 			else:
	# 				self.lyb_mouse_drag('tera_monster_dogam_scene_drag_bottom', 'tera_monster_dogam_scene_drag_top')
	# 				time.sleep(1)
	# 				self.set_option('drag_count', drag_count + 1)
	# 		else:
	# 			self.loggingToGUI(area_list[iterator] + ' 발견됨')
	# 			self.lyb_mouse_click_location(loc_x+40, loc_y)
	# 			self.last_status['dogam'] = self.status
	# 			self.status = 100 + iterator
	# 	elif self.status == (100 + area_list.index('여명의 정원')):
	# 		self.set_option('iterator_list', sub_area_dic['여명의 정원'])
	# 		self.set_option('iterator_start', 0)
	# 		self.set_option('iterator_len', len(sub_area_dic['여명의 정원']))
	# 		self.status = 1000
	# 	elif self.status == (100 + area_list.index('버려진 평야')):
	# 		self.set_option('iterator_list', sub_area_dic['버려진 평야'])
	# 		self.set_option('iterator_start', len(sub_area_dic['여명의 정원']))
	# 		self.set_option('iterator_len', len(sub_area_dic['버려진 평야']))
	# 		self.status = 1000
	# 	elif self.status == (100 + area_list.index('엘리누의 언덕')):
	# 		self.set_option('iterator_list', sub_area_dic['엘리누의 언덕'])
	# 		self.set_option('iterator_start', len(sub_area_dic['여명의 정원']) + len(sub_area_dic['버려진 평야']))
	# 		self.set_option('iterator_len', len(sub_area_dic['엘리누의 언덕']))
	# 		self.status = 1000
	# 	elif self.status == (100 + area_list.index('통곡의 해안')):
	# 		self.set_option('iterator_list', sub_area_dic['통곡의 해안'])
	# 		self.set_option('iterator_start', len(sub_area_dic['여명의 정원']) + 
	# 			len(sub_area_dic['버려진 평야']) + 
	# 			len(sub_area_dic['엘리누의 언덕']))
	# 		self.set_option('iterator_len', len(sub_area_dic['통곡의 해안']))
	# 		self.status = 1000
	# 	elif self.status == (100 + area_list.index('제국령 라키타니아')):
	# 		self.set_option('iterator_list', sub_area_dic['제국령 라키타니아'])
	# 		self.set_option('iterator_start', len(sub_area_dic['여명의 정원']) + 
	# 			len(sub_area_dic['버려진 평야']) + 
	# 			len(sub_area_dic['엘리누의 언덕']) + 
	# 			len(sub_area_dic['통곡의 해안']))
	# 		self.set_option('iterator_len', len(sub_area_dic['제국령 라키타니아']))
	# 		self.status = 1000
	# 	elif self.status == (100 + area_list.index('금지된 땅')):
	# 		self.set_option('iterator_list', sub_area_dic['금지된 땅'])
	# 		self.set_option('iterator_start', len(sub_area_dic['여명의 정원']) + 
	# 			len(sub_area_dic['버려진 평야']) + 
	# 			len(sub_area_dic['엘리누의 언덕']) + 
	# 			len(sub_area_dic['통곡의 해안']) + 
	# 			len(sub_area_dic['제국령 라키타니아']))
	# 		self.set_option('iterator_len', len(sub_area_dic['금지된 땅']))
	# 		self.status = 1000
	# 	elif self.status == 1000:
			
	# 		sub_iterator = self.get_option('sub_area_iterator')
	# 		if sub_iterator == None:
	# 			sub_iterator = 0
	# 			self.set_option('sub_area_iterator', 0)

	# 		sub_area_list = self.get_option('iterator_list')
	# 		sub_area_start = self.get_option('iterator_start')

	# 		# print('DEBUG1 sub_iterator:', sub_iterator, 'len:', self.get_option('iterator_len'))
	# 		if sub_iterator >= self.get_option('iterator_len'):
	# 			self.status = self.last_status['dogam'] + 1
	# 			self.set_option('sub_area_iterator', 0)
	# 		else:
	# 			sub_area_name = 'tera_monster_dogam_area_' + str(sub_area_start + sub_iterator)
	# 			self.loggingToGUI(sub_area_list[sub_iterator] + ' 체크')

	# 			(loc_x, loc_y), dogam_rate = lybgame.LYBGame.locationOnWindowWithRate(
	# 				self.window_image,
	# 				self.game_object.resource_manager.pixel_box_dic[sub_area_name],
	# 				custom_threshold=match_threshold,
	# 				custom_below_level=(30, 30, 30),
	# 				custom_top_level=(255,255,255)
	# 				)
	# 			# print(sub_area_list[sub_iterator] ,':', (loc_x, loc_y))
	# 			self.loggingToGUI(sub_area_list[sub_iterator] + ' 매칭률: ' + str(int(dogam_rate * 100)) + ' / ' + str(int(match_threshold*100)) + ' %')
				
	# 			if loc_x == -1:
	# 				sub_drag_count = self.get_option('sub_drag_count')
	# 				if sub_drag_count == None:
	# 					sub_drag_count = 0

	# 				if sub_drag_count > 2:
	# 					self.status += 1
	# 					for i in range(sub_drag_count):
	# 						self.lyb_mouse_drag('tera_monster_dogam_scene_drag_top', 'tera_monster_dogam_scene_drag_bottom')
	# 						time.sleep(1)
	# 					self.set_option('sub_drag_count', 0)
	# 					self.loggingToGUI(str(sub_area_list[sub_iterator]) + '을 찾지 못했습니다.')
	# 					self.set_option('sub_area_iterator', sub_iterator + 1)
	# 				else:
	# 					self.lyb_mouse_drag('tera_monster_dogam_scene_drag_bottom', 'tera_monster_dogam_scene_drag_top')
	# 					time.sleep(1)
	# 					self.set_option('sub_drag_count', sub_drag_count + 1)
	# 			else:
	# 				self.loggingToGUI(sub_area_list[sub_iterator] + ' 발견됨')
	# 				self.lyb_mouse_click_location(130, loc_y)
	# 				self.status = 1100
	# 	elif self.status == 1100:
	# 		rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_monster_dogam_reward_0')
	# 		if rate_match > 0.8:
	# 			self.lyb_mouse_click('tera_monster_dogam_reward_0', custom_threshold=0.8)
	# 		else:
	# 			self.status += 1
	# 	elif self.status == 1101:
	# 		rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_monster_dogam_active')
	# 		if rate_match > 0.8:
	# 			self.lyb_mouse_click('tera_monster_dogam_active', custom_threshold=0.8)
	# 		else:
	# 			self.status += 1
	# 	elif self.status == 1102:
	# 		is_clicked = self.lyb_mouse_click('tera_monster_dogam_chase_0')
	# 		if is_clicked == False:
	# 			sub_area_iterator = self.get_option('sub_area_iterator')
	# 			self.set_option('sub_area_iterator', sub_area_iterator + 1)
	# 			self.status = 1000
	# 		else:
	# 			self.set_checkpoint('dogam_chase')
	# 			self.status += 1
	# 	elif self.status == 1103:
	# 		self.status += 1
	# 	elif self.status == 1104:
	# 		self.status = 1100
	# 	else:
	# 		self.lyb_mouse_click('tera_monster_dogam_scene' + '_close_icon')
	# 		self.status = 0

	# 	return self.status

	def tera_achievement_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_no_red_gem_achievement')
		if red_gem < 0.8:
			self.lyb_mouse_click('tera_no_red_gem_achievement', custom_threshold=0)

		if self.status >= 0 and self.status < 5:
			self.lyb_mouse_click('tera_achievement_scene_tab_' + str(self.status))
			self.last_status['achievement'] = self.status
			self.status = 100
		elif self.status == 5:
			self.lyb_mouse_click('tera_achievement_scene_upgrade')
			self.status = 99999
		elif self.status == 100:
			is_clicked = self.lyb_mouse_click('tera_achievement_scene_receive')
			if is_clicked == False:
				self.status = self.last_status['achievement'] + 1
		else:
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			if work_name != None and len(work_name) > 0 and '업적' in work_name:
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)

			self.status = 0
			self.lyb_mouse_click('tera_achievement_scene' + '_close_icon')

		return self.status

	def tera_mission_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_mission')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_mission', custom_threshold=0.2)

		if self.status >= 0 and self.status < 3:
			self.lyb_mouse_click('tera_mission_scene_tab_' + str(self.status))
			self.last_status['mission'] = self.status
			self.status = 100
		elif self.status == 3:
			self.lyb_mouse_click('tera_achievement_scene_upgrade')
			self.status = 99999
		elif self.status == 100:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_mission_scene_receive_top')
			if match_rate < 0.9:
				self.lyb_mouse_click('tera_mission_scene_receive_top', custom_threshold=0)
			self.status += 1
		elif self.status == 101:
			is_clicked = self.lyb_mouse_click('tera_mission_scene_receive_bottom')
			if is_clicked == False:
				self.status = self.last_status['mission'] + 1
		else:
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			if work_name != None and len(work_name) > 0 and '임무' in work_name:
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)
			self.status = 0
			self.lyb_mouse_click('tera_mission_scene' + '_close_icon')

		return self.status

	def tera_hero_gallery_scene(self):

		self.game_object.current_matched_scene['name'] = ''

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_hero_gallery')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_hero_gallery', custom_threshold=0.2)
			return self.status

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('영웅 변경'):
			hero_change_iterator = self.get_option('hero_change_iterator')
			if hero_change_iterator == None:
				self.game_object.get_scene('tera_main_scene').set_option('hero_change_do', True)
				hero_change_iterator = 0
			elif hero_change_iterator > len(self.game_object.hero_list) - 1:
				self.set_option('hero_change_iterator', 0)
				self.game_object.get_scene('tera_main_scene').set_option('hero_change_do', False)
				hero_change_iterator = 0

			self.logger.info(str(hero_change_iterator + 1) + ' 번째 영웅 변경합니다.')
			self.lyb_mouse_click('tera_hero_gallery_scene_hero_' + str(hero_change_iterator), custom_threshold=0)
			self.game_object.get_scene('tera_hero_gallery_each_scene').status = self.status
			self.set_option('hero_change_iterator', hero_change_iterator + 1)
		elif (	self.status == self.get_work_status('영웅 변경 - 솔') or
				self.status == self.get_work_status('영웅 변경 - 올렌더') or
				self.status == self.get_work_status('영웅 변경 - 레인') or
				self.status == self.get_work_status('영웅 변경 - 라브랭') or
				self.status == self.get_work_status('영웅 변경 - 리벨리아') or
				self.status == self.get_work_status('영웅 변경 - 리나') or
				self.status == self.get_work_status('영웅 변경 - 카야')
			):
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			# print('DEBUG hero change:', work_name)
			if work_name != None and len(work_name) > 0:
				hero_change_iterator = self.game_object.hero_list.index(work_name.replace('영웅 변경 - ', '', 1))
				# print('DEBUG hero_change_iterator=', hero_change_iterator)

				self.logger.info(str(hero_change_iterator + 1) + ' 번째 영웅 변경합니다.')
				self.lyb_mouse_click('tera_hero_gallery_scene_hero_' + str(hero_change_iterator), custom_threshold=0)
				self.game_object.get_scene('tera_hero_gallery_each_scene').status = self.status
				self.status = 0
			else:
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_quest_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_quest')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_quest', custom_threshold=0.2)

		if self.status == self.get_work_status('임무 보상'):
			self.lyb_mouse_click('tera_quest_scene_mission_tab')
			self.status = 99999
		elif self.status == self.get_work_status('업적 보상'):
			self.lyb_mouse_click('tera_quest_scene_achievement_tab')
			self.status = 99999
		else:
		 	self.lyb_mouse_click('tera_quest_scene' + '_close_icon')
		 	self.status = 0

		return self.status

	def tera_sell_all_scene(self):

		if self.status == 0:
			self.status += 1
		elif  self.status == 1:
			self.status += 1
		elif  self.status == 2:
			self.lyb_mouse_click('tera_sell_all_scene_button')
			self.status += 1
		else:
			self.lyb_mouse_click('tera_inventory_scene_close_icon')
			self.status = 0

		return self.status

	def tera_use_box_scene(self):

		full_scene = self.game_object.get_scene('tera_inventory_not_enough_scene')
		inven_scene = self.game_object.get_scene('tera_inventory_scene')

		if  full_scene.get_option('inventory_full') == True:
			# full_scene.set_option('inventory_full', False)
			# inven_scene.status = self.get_work_status('일괄 판매')

			self.lyb_mouse_click('tera_use_box_scene_close_icon')
		else:
			self.lyb_mouse_click('tera_use_box_scene_button')

		return self.status

	def tera_inventory_not_enough_scene(self):

		self.lyb_mouse_click('tera_inventory_not_enough_scene_button')
		self.set_option('inventory_full', True)

		return self.status

	def tera_death_scene(self):
		
		if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_STOP_WORKING) == True:
			self.logger.warn('캐릭터가 사망하여 다음 스케쥴 작업을 진행합니다.')
			self.game_object.get_scene('tera_main_scene').set_option('hero_death', True)
			# self.game_object.get_scene('tera_main_scene').set_checkpoint('wait_penaltry')

		self.lyb_mouse_click('tera_death_scene_mudum_buhal')

		return self.status

	def tera_main_quest_equip_rune_scene(self):
		# 메인퀘스트 중에 장착 퀘스트
		if self.status == 0:
			self.set_tutorial(True)
			self.status += 1
		else:
			self.status = 1

		self.lyb_mouse_click('tera_main_quest_equip_rune_scene_button')

		return self.status

	def tera_main_quest_smithy_scene(self):
		# 메인퀘스트 중에 스킬 퀘스트
		if self.status == 0:
			self.set_tutorial(True)

			self.status += 1
		else:
			self.status = 1

		self.lyb_mouse_click('tera_main_quest_smithy_scene'+'_button')

		return self.status

	def tera_main_quest_smithy_upgrade_scene(self):
		# 메인퀘스트 중에 스킬 퀘스트
		if self.status == 0:
			self.set_tutorial(True)
			self.status += 1
		else:
			self.status = 1

		self.lyb_mouse_click('tera_main_quest_smithy_upgrade_scene'+'_button')

		return self.status

	def tera_main_quest_skill_scene(self):
		# 메인퀘스트 중에 스킬 퀘스트
		if self.status == 0:
			self.set_tutorial(True)
			self.status += 1
		else:
			self.status = 1

		self.lyb_mouse_click('tera_main_quest_skill_scene_button')

		return self.status


	def tera_main_quest_talent_scene(self):
		# 메인퀘스트 중에 스킬 퀘스트
		if self.status == 0:
			self.set_tutorial(True)
			self.status += 1
		else:
			self.status = 1

		self.lyb_mouse_click('tera_main_quest_talent_scene' + '_button')

		return self.status

	def tera_main_quest_extra_scene(self):
		# 메인퀘스트 중에 스킬 퀘스트
		if self.status == 0:
			self.set_tutorial(True)
			self.status += 1
		else:
			self.status = 1

		self.lyb_mouse_click(self.scene_name + '_button')

		return self.status

	def tera_config_scene(self):

		if self.status == self.get_work_status('로그인'):
			self.lyb_mouse_click('tera_config_scene_information_tab', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('로그인') + 1:
			self.lyb_mouse_click('tera_config_scene_select_server_button')
			# 클리어 씬 = 1000000
			self.status = 1000000
		elif self.status == self.get_work_status('설정 - 파티 초대 거절'):
			self.lyb_mouse_click('tera_config_scene_game_tab', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('설정 - 파티 초대 거절') + 1:
			# print('[DEBUG]', self.get_game_config(lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY))
			bool_index = lybgameTera.LYBTera.game_config_boolean_list.index(self.get_game_config(lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY))
			# print('[DEBUG]', bool_index)
			pb_name = 'tera_game_config_invite_party_' + str(bool_index)
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			print('[DEBUG]', pb_name, match_rate)
			if match_rate < 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
			self.status = 99999
		else:
			self.lyb_mouse_click('tera_config_scene_close_icon')
			self.status = 0

		return self.status


	def tera_challenge_scene(self):

		if self.status == self.get_work_status('독립군 장비 보급'):
			self.lyb_mouse_click('tera_challenge_scene_dokripgun', custom_threshold=0)
			self.set_checkpoint('challenge_enter')
			self.set_option('work_name', '독립군 장비 보급')
			self.status = 99999
		elif self.status == self.get_work_status('무한의 탑'):
			self.lyb_mouse_click('tera_challenge_scene_muhantap', custom_threshold=0)
			self.set_checkpoint('challenge_enter')
			self.set_option('work_name', '무한의 탑')
			self.status = 99999
		elif self.status == self.get_work_status('요일 던전'):
			self.lyb_mouse_click('tera_challenge_scene_daily_dungeon', custom_threshold=0)
			self.set_checkpoint('challenge_enter')
			self.set_option('work_name', '요일 던전')
			self.status = 99999
		elif self.status == self.get_work_status('블가메시의 훈련'):
			self.lyb_mouse_click('tera_challenge_scene_blgamesi_train', custom_threshold=0)
			self.set_checkpoint('challenge_enter')
			self.set_option('work_name', '블가메시의 훈련')
			self.status = 99999
		elif self.status == self.get_work_status('황금 거인 강탈'):
			self.lyb_mouse_click('tera_challenge_scene_gold_giant', custom_threshold=0)
			self.set_checkpoint('challenge_enter')
			self.set_option('work_name', '황금 거인 강탈')
			self.status = 99999
		else:
			elapsed_time = time.time() - self.get_checkpoint('challenge_enter')
			# print(elapsed_time)
			if elapsed_time < 5:
				work_name = self.get_option('work_name')
				if work_name != None and len(work_name) > 0 and (self.get_work_status(work_name) > self.get_work_status('몬스터 도감')):
					self.logger.warn(work_name + ' 입장 불가')
					self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_end', True)
					self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', False)
					self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)

			self.lyb_mouse_click('tera_challenge_scene' + '_close_icon')
			self.status = 0

		return self.status

	def tera_injang_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_injang')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_injang', custom_threshold=0.2)
		
		# print('DEBUG injang:', self.get_tutorial())
		if self.get_tutorial() == True:
			self.status = 500

		if self.status == 0:
			self.status += 1
		elif self.status == 500:
			self.lyb_mouse_click('tera_injang_make', custom_threshold=0)
			self.set_tutorial(False)
			self.status += 1
		elif self.status == 501:
			self.status += 1
		elif self.status == 502:
			self.lyb_mouse_click('tera_injang_make', custom_threshold=0)
			self.status += 1
		elif self.status == 503:
			self.lyb_mouse_click('tera_injang_equip', custom_threshold=0)
			self.status = 99999	
		else:
			self.lyb_mouse_click('tera_injang_scene' + '_close_icon')
			self.status = 0

		return self.status

	def tera_battle_area_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_battle')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_battle', custom_threshold=0.2)
		
		if self.get_tutorial() == True:
			self.status = 500

		if self.status == 0:
			self.status += 1
		elif self.status == 500:
			self.lyb_mouse_click('tera_battle_area_enter', custom_threshold=0)
			self.set_tutorial(False)
			self.game_object.get_scene('tera_main_scene').set_option('battle_area', True)
			self.game_object.get_scene('tera_main_scene').set_checkpoint('battle_area')
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_guild_donate_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.logger.debug(str(int(self.get_game_config(lybconstant.LYB_DO_STRING_GUILD_DONATE)) + 1) + ' 번째에 기부')
			is_clicked = self.lyb_mouse_click('tera_guild_donate_scene_donate_' + str(self.get_game_config(lybconstant.LYB_DO_STRING_GUILD_DONATE)))
			if is_clicked == False:
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_guild_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_guild')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_guild', custom_threshold=0.2)

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('길드 출석'):
			self.logger.info('길드 출석')
			self.lyb_mouse_click('tera_guild_scene_information', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('길드 출석') + 1:
			self.lyb_mouse_click('tera_guild_scene_check', custom_threshold=0)
			self.status = 99999
		elif self.status == self.get_work_status('길드 보상'):
			self.logger.info('길드 보상')
			self.lyb_mouse_click('tera_guild_scene_information', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('길드 보상') + 1:
			self.lyb_mouse_click('tera_guild_scene_reward', custom_threshold=0)
			self.status = 99999
		elif self.status == self.get_work_status('길드 기부'):
			self.logger.info('길드 기부')
			self.lyb_mouse_click('tera_guild_donate', custom_threshold=0)
			self.status = 99999
		elif self.status == self.get_work_status('길드 업적'):
			self.logger.info('길드 업적')
			self.lyb_mouse_click('tera_guild_scene_achievement_0', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('길드 업적') + 1:
			is_clicked = self.lyb_mouse_click('tera_guild_scene_achievement_reward')
			if is_clicked == False:
				self.status = 99999
		elif self.status == self.get_work_status('길드 마을'):
			self.logger.info('길드 마을')
			self.lyb_mouse_click('tera_guild_scene_village', custom_threshold=0)
			self.game_object.get_scene('tera_main_scene').set_option('guild_village', True)
			self.status = 99999
		elif self.status == self.get_work_status('길드 상점 - 경험치'):
			self.logger.info('길드 상점 - 경험치')
			self.lyb_mouse_click('tera_guild_scene_shop', custom_threshold=0)
			self.game_object.get_scene('tera_special_shop_scene').status = self.status
			self.status = 99999
		elif self.status == self.get_work_status('길드 상점 - 대량의 경험치'):
			self.logger.info('길드 상점 - 대량의 경험치')
			self.lyb_mouse_click('tera_guild_scene_shop', custom_threshold=0)
			self.game_object.get_scene('tera_special_shop_scene').status = self.status
			self.status = 99999
		elif self.status == self.get_work_status('길드 스킬'):
			self.logger.info('길드 스킬')
			self.lyb_mouse_click('tera_guild_scene_skill', custom_threshold=0)
			self.status = 99999
		else:			
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_yamong_attendance_scene(self):
		return self.tera_common_event_scene()

	def tera_launching_special_attendance_scene(self):
		return self.tera_common_event_scene()

	def tera_monthly_attendance_scene(self):
		return self.tera_common_event_scene()

	def tera_continous_attendance_scene(self):
		return self.tera_common_event_scene()

	def tera_play_time_scene(self):
		return self.tera_common_event_scene()

	def tera_common_event_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status >= 1 and self.status < 10:
			pb_name = 'tera_common_event_scene_new'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[pb_name],
											custom_threshold=0.8,
											custom_flag=1,
											custom_rect=(100, 50, 130, 360)
											)
			self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.set_option('last_status', self.status + 1)
				self.status += 10
			else:
				self.status = 99999
		elif self.status >= 11 and self.status < 20:
			self.lyb_mouse_click(self.scene_name + '_center', custom_threshold=0)
			self.status = self.get_option('last_status')
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_main_menu_scene(self):
		# 1 ~ 100 은 예약된 번호다. 스케쥴링 번호.. 쓰지말것
		# print('XXX:', self.status)
		self.game_object.current_matched_scene['name'] = ''
		if self.status == 0:
			self.status += 1			
		elif (	self.status == self.get_work_status('요일 던전') or
				self.status == self.get_work_status('독립군 장비 보급') or
				self.status == self.get_work_status('무한의 탑') or
				self.status == self.get_work_status('블가메시의 훈련') or
				self.status == self.get_work_status('황금 거인 강탈')
				):
			# 요일 던전
			is_clicked = self.lyb_mouse_click('tera_main_menu_scene_challenge')
			if is_clicked == False:
				self.logger.warn('도전 던전 미오픈 또는 인식 불가 (이미지 인식 허용치를 낮춰주세요)')
				work_name = self.game_object.get_scene('tera_main_scene').current_work
				self.game_object.get_scene('tera_main_scene').set_option( work_name + '_dungeon_done', True)
				self.game_object.get_scene('tera_main_scene').set_option( work_name + '_dungeon_end', True)
			else:
				self.game_object.get_scene('tera_challenge_scene').status = self.status
			self.status = 99999
		elif (	self.status == self.get_work_status('독립군 보급 기지') or
				self.status == self.get_work_status('후카족 마을 수복전') or
				self.status == self.get_work_status('밤피르의 저택') or
				self.status == self.get_work_status('달의 호수 쟁탈전') or
				self.status == self.get_work_status('황금의 미궁') or
				self.status == self.get_work_status('왕자의 궁전') or
				self.status == self.get_work_status('불의 제단') or
				self.status == self.get_work_status('벤튤라') or
				self.status == self.get_work_status('데미안') or
				self.status == self.get_work_status('그림자 기수') or
				self.status == self.get_work_status('굴') or
				self.status == self.get_work_status('티라누스') or
				self.status == self.get_work_status('라우라바') or
				self.status == self.get_work_status('고대 던전 입구') or
				self.status == self.get_work_status('고대 던전 1구역') or
				self.status == self.get_work_status('고대 던전 2구역')
				):
			is_clicked = self.lyb_mouse_click('tera_main_menu_scene_raid')
			if is_clicked == False:
				self.logger.warn('레이드 던전 미오픈 또는 인식 불가 (이미지 인식 허용치를 낮춰주세요)')
				work_name = self.game_object.get_scene('tera_main_scene').current_work
				self.game_object.get_scene('tera_main_scene').set_option( work_name + '_dungeon_done', True)
				self.game_object.get_scene('tera_main_scene').set_option( work_name + '_dungeon_end', True)
			else:
				self.game_object.get_scene('tera_raid_scene').status = self.status
			self.status = 99999
		elif (	self.status == self.get_work_status('로그인') or
				self.status == self.get_work_status('설정 - 파티 초대 거절')
			):
			self.lyb_mouse_click('tera_main_menu_scene_config', custom_threshold=0)
			self.game_object.get_scene('tera_config_scene').status = self.status
		elif (	self.status == self.get_work_status('임무 보상') or
				self.status == self.get_work_status('업적 보상')
				):
			self.lyb_mouse_click('tera_main_menu_scene_quest', custom_threshold=0)
			self.game_object.get_scene('tera_quest_scene').status = self.status
			self.status = 99999
		elif self.status == self.get_work_status('보상 회수'):
			self.lyb_mouse_click('tera_main_menu_scene_bosang', custom_threshold=0)
			self.status = 99999
		elif (	self.status == self.get_work_status('길드 출석') or
				self.status == self.get_work_status('길드 보상') or
				self.status == self.get_work_status('길드 업적') or
				self.status == self.get_work_status('길드 기부') or
				self.status == self.get_work_status('길드 마을') or
				self.status == self.get_work_status('길드 상점 - 경험치') or
				self.status == self.get_work_status('길드 상점 - 대량의 경험치') or
				self.status == self.get_work_status('길드 스킬') 
				):
			self.lyb_mouse_click('tera_main_menu_scene_guild')
			self.game_object.get_scene('tera_guild_scene').status = self.status
			self.status = 99999
		elif self.status == self.get_work_status('몬스터 도감'):
			self.game_object.get_scene('tera_monster_dogam_scene').status = self.status
			self.lyb_mouse_click('tera_main_menu_scene_dogam', custom_threshold=0)
		elif (	self.status == self.get_work_status('영웅 변경') or
				self.status == self.get_work_status('영웅 변경 - 솔') or
				self.status == self.get_work_status('영웅 변경 - 올렌더') or
				self.status == self.get_work_status('영웅 변경 - 레인') or
				self.status == self.get_work_status('영웅 변경 - 라브랭') or
				self.status == self.get_work_status('영웅 변경 - 리벨리아') or
				self.status == self.get_work_status('영웅 변경 - 리나') or
				self.status == self.get_work_status('영웅 변경 - 카야')
				):
			self.lyb_mouse_click('tera_main_menu_scene_hero_gallery', custom_threshold=0)
			self.game_object.get_scene('tera_hero_gallery_scene').status = self.status
		elif (	self.status == self.get_work_status('지하 결투장')
				# self.status == self.get_work_status('카이아의 전장')
				):
			is_clicked = self.lyb_mouse_click('tera_main_menu_scene_junjang')
			if is_clicked == False:
				self.logger.warn('전장 인식 불가 (이미지 인식 허용치를 낮춰주세요)')
			else:
				self.game_object.get_scene('tera_junjang_scene').status = self.status
			self.status = 99999
			# print('DEBUG:', self.status)
		elif(	self.status == self.get_work_status('무기 레벨업 - 대장간') or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') or
				self.status == self.get_work_status('장신구 레벨업 - 대장간')
				):
			self.lyb_mouse_click('tera_main_menu_scene_dejanggan', custom_threshold=0)
			self.game_object.get_scene('tera_smithy_scene').status = self.status
		elif self.status == 99995:
			self.status += 1
		elif self.status == 99996:
			self.status += 1
		elif self.status == 99997:
			self.status += 1
		elif self.status == 99998:
			self.lyb_mouse_click('tera_main_menu_scene' + '_close_icon', custom_threshold=0.2)
			self.status = 0
		else:
			# 메인메뉴화면은 겹쳐보여서 스레숄드를 줘야함.
			self.status = 99995

		return self.status

	def tera_mail_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_mail')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_mail', custom_threshold=0.2)

		if self.status == 0:
			self.lyb_mouse_click('tera_mail_scene_receive_all_button')
			self.status += 1
		else:
			self.lyb_mouse_click('tera_mail_scene' + '_close_icon')
			self.status = 0

		return self.status

	def tera_rune_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_rune')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_rune', custom_threshold=0.2)

		if self.get_tutorial() == True:
			self.status = 500

		if self.status == 0:
			self.status += 1
		elif self.status == 500:
			self.lyb_mouse_click('tera_rune_scene_attack_tab', custom_threshold=0)
			self.set_tutorial(False)
			self.status += 1
		elif self.status == 501:
			self.lyb_mouse_click('tera_rune_scene_item_0', custom_threshold=0)
			self.status = 99999			
		else:
			self.lyb_mouse_click('tera_rune_scene' + '_close_icon')
			self.status = 0

		return self.status

	def tera_dungeon_scene_common(self):

		party_member_mode = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE)			
		work_name = self.game_object.get_scene('tera_main_scene').current_work

		# print('DEBUG: current work ==>', work_name)
		# print('DEBUG: tutorial ==>', self.get_tutorial())
		# print( lybgameTera.LYBTera.tobul_list )

		if self.get_tutorial() == True:
			if work_name == None or len(work_name) < 1 or work_name == '메인 퀘스트':
				work_name = '독립군 보급 기지'			
		else:
			if work_name == None:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				self.status = 0
				return self.status

		if work_name == '랜덤 퀘스트':
			click_enter_pb = 'tera_normal_dungeon_party_matching'
			self.status = 3
		else:
			if (	not work_name in lybgameTera.LYBTera.dungeon_list and
					not work_name in lybgameTera.LYBTera.tobul_list
					):
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				self.status = 0
				return self.status

			if ( 	self.scene_name == 'tera_normal_dungeon_scene' or
					self.scene_name == 'tera_elite_dungeon_scene' 
				):
				

				red_gem_pb = 'tera_red_gem_normal_dungeon'
				click_select_pb = 'tera_normal_dungeon_'
				if self.scene_name == 'tera_elite_dungeon_scene':
					click_select_pb = 'tera_elite_dungeon_'
				click_reward_pb = 'tera_normal_dungeon_scene_reward'

				try:
					dungeon_index = lybgameTera.LYBTera.dungeon_list.index(work_name)
				except:
					self.logger.error(traceback.format_exc())
					return self.status
					
				# print(work_name, self.get_game_config(lybconstant.LYB_DO_STRING_TYPE_ENTER_DUNGEON + str(dungeon_index)))
				if int(self.get_game_config(lybconstant.LYB_DO_STRING_TYPE_ENTER_DUNGEON + str(dungeon_index))) == 0:
					click_enter_pb = 'tera_raid_immediate_enter'
				else:
					click_enter_pb = 'tera_normal_dungeon_party_matching'
				count_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_LIMIT_COUNT_DUNGEON + str(dungeon_index)))
			elif (	self.scene_name == 'tera_normal_tobul_scene' or
					self.scene_name == 'tera_elite_tobul_scene'
					):

				red_gem_pb = 'tera_red_gem_normal_tobul'
				click_select_pb = 'tera_normal_tobul_'
				if self.scene_name == 'tera_elite_tobul_scene':
					click_select_pb = 'tera_elite_tobul_'

				click_reward_pb = 'tera_normal_tobul_scene_reward'

				try:
					dungeon_index = lybgameTera.LYBTera.tobul_list.index(work_name)
				except:
					self.logger.error(traceback.format_exc())
					return self.status

				if int(self.get_game_config(lybconstant.LYB_DO_STRING_TYPE_ENTER_TOBUL + str(dungeon_index))) == 0:
					click_enter_pb = 'tera_raid_immediate_enter'
				else:
					click_enter_pb = 'tera_normal_dungeon_party_matching'

				count_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_LIMIT_COUNT_TOBUL + str(dungeon_index)))
			elif self.scene_name == 'tera_kaia_dungeon_scene':

				red_gem_pb = 'tera_red_gem_normal_tobul'
				click_select_pb = 'tera_normal_dungeon_0'
				click_reward_pb = 'tera_kaia_dungeon_reward'
				try:
					dungeon_index = lybgameTera.LYBTera.tobul_list.index(work_name)
				except:					
					self.logger.error(traceback.format_exc())
					return self.status
				click_enter_pb = 'tera_kaia_dungeon_party_matching'

				count_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_LIMIT_COUNT_TOBUL + str(dungeon_index)))

			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DUNGEON)) * 60

			# print('DEBUG: count_limit ==>', count_limit)

			red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, red_gem_pb)
			if red_gem > 0.2:
				self.lyb_mouse_click(red_gem_pb, custom_threshold=0.2)

			if self.get_tutorial() == True:
				pass
			else:
				if self.is_there_in_schedule_list(work_name) == False:
					self.status = 99999

				if self.game_object.get_scene('tera_main_scene').get_option(work_name + '_end_flag') == True:
					self.status = 99999
			
		if self.status == 0:
			# 개별 진행 시간 체크를 위해
			self.set_checkpoint('start')
			self.set_option('retry_count', 0)
			self.status += 1

		if self.status == 1:
			retry_count = self.get_option('retry_count')
			if retry_count == None:
				retry_count = 0
			retry_count_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER))
			self.logger.warn('[던전     ] 재시도 횟수:' + str(retry_count) + ' / ' + str(retry_count_limit))

			if retry_count != None and retry_count > retry_count_limit:
				# self.game_object.terminate_application()
				self.status = 99999
				# return 1000000
			else:
				self.lyb_mouse_click(click_reward_pb, custom_threshold=0)
				self.status += 1
		elif self.status == 2:

			# 전체 진행 시간 체크
			if self.game_object.get_scene('tera_main_scene').get_checkpoint(work_name + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.game_object.get_scene('tera_main_scene').get_checkpoint(work_name + '_check_start')
			self.logger.info('[던전     ] ' + work_name + ' 작업 경과 시간:' + str(int(elapsed_time)) + ' / ' + str(duration_limit) + '초')

			enter_count = self.game_object.get_scene('tera_main_scene').get_option(work_name + '_enter_count')
			if enter_count == None:
				enter_count = 0

			self.logger.debug('[던전     ] ' + work_name + ' 횟수:' + str(enter_count) + ' / ' + str(count_limit))
			if enter_count >= count_limit:
				self.status = 99999
			elif elapsed_time > duration_limit:
				self.status = 99999
			else:
				is_clicked = self.lyb_mouse_click(click_select_pb + str(dungeon_index), custom_threshold=0)
				if is_clicked == False:
					self.status = 99999
				else:				
					self.status += 1

		elif self.status == 3:

			retry_count = self.get_option('retry_count')
			if retry_count == None:
				retry_count = 0

			if party_member_mode == True:
				self.logger.info('던전 파티원 모드')
				is_clicked = True
			else:
				is_clicked = self.lyb_mouse_click(click_enter_pb)

			if is_clicked == False:
				if retry_count == 0:
					self.lyb_mouse_click(click_enter_pb, custom_threshold=0)

				self.set_option('retry_count', retry_count + 1)

				self.logger.warn(work_name + '파티 매칭 버튼 클릭에 실패했습니다. 재시도합니다. '+str(retry_count+1))
				self.status = 10
				# self.status = 99999
			else:
				self.logger.info('[' + work_name + '] 파티 매칭을 클릭했습니다.')
				self.status += 1
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', True)
				self.game_object.get_scene('tera_main_scene').set_option('wait_start_flag', True)
				self.game_object.get_scene('tera_raid_matching_scene').set_option('match_canceled', False)
				self.set_checkpoint('waiting_time')
				self.set_option('retry_count', 0)

		elif self.status == 4:
			self.game_object.interval = 0.01		

			if self.game_object.get_scene('tera_main_scene').get_option('wait_start_flag') != True:
				self.status = 10
			else:
				if self.game_object.get_scene('tera_raid_matching_scene').get_option('match_canceled') == True:
					self.status = 10
				else:
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, click_enter_pb)
					if match_rate > 0.9:
						self.lyb_mouse_click(self.scene_name + '_close_icon')
						self.status = 10

					elapsed_waiting_time = time.time() - self.get_checkpoint('waiting_time')
					wait_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_WAIT_MATCHING))
					if elapsed_waiting_time > wait_limit:
						retry_count = self.get_option('retry_count')
						if retry_count == None:
							retry_count = 0
						self.set_option('retry_count', retry_count + 1)

						self.logger.info(work_name + ' 매칭 대기시간 초과로 입장을 실패했습니다. 재시도합니다. '+str(retry_count+1))
						self.game_object.get_scene('tera_main_scene').set_option('wait_start_flag', False)
						self.lyb_mouse_click(click_enter_pb, custom_threshold=0)
					else:
						self.loggingElapsedTime(work_name + ' 매칭 대기 중', int(elapsed_waiting_time), int(wait_limit), period=3)

		elif self.status == 10:
			self.game_object.get_scene('tera_main_scene').checkpoint[work_name + '_check_start_each'] = 0
			self.status = 1
		elif self.status == 500:
			self.lyb_mouse_click(click_select_pb + str(0), custom_threshold=0)
			time.sleep(1)
			self.lyb_mouse_click('tera_normal_dungeon_party_matching', custom_threshold=0)
			self.set_tutorial(False)
			self.status += 1
		else:
			if work_name != None and len(work_name) > 0 and (self.get_work_status(work_name) > self.get_work_status('몬스터 도감')):
				self.game_object.get_scene('tera_main_scene').checkpoint[work_name + '_check_start_each'] = 0
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_enter_count', 0)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_end', True)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', False)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tera_kaia_dungeon_scene(self):
		return self.tera_dungeon_scene_common()

	def tera_normal_dungeon_scene(self):
		return self.tera_dungeon_scene_common()

	def tera_normal_tobul_scene(self):
		return self.tera_dungeon_scene_common()


	def tera_elite_dungeon_scene(self):
		return self.tera_dungeon_scene_common()

	def tera_elite_tobul_scene(self):
		return self.tera_dungeon_scene_common()

	def tera_gode_dungeon_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_gode_dungeon')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_gode_dungeon', custom_threshold=0.2)

		work_name = self.game_object.get_scene('tera_main_scene').current_work
		if (	work_name != None and len(work_name) > 0 and 
					(self.get_work_status(work_name) > self.get_work_status('몬스터 도감'))
					):
			if self.game_object.get_scene('tera_main_scene').get_option(work_name + '_end_flag') == True:
				self.status = 99999

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('고대 던전 입구'):
			self.lyb_mouse_click('tera_gode_dungeon_scene_list_0', custom_threshold=0)
			self.status = 100
		elif self.status == self.get_work_status('고대 던전 1구역'):
			self.lyb_mouse_click('tera_gode_dungeon_scene_list_1', custom_threshold=0)
			self.status = 100
		elif self.status == self.get_work_status('고대 던전 2구역'):
			self.lyb_mouse_click('tera_gode_dungeon_scene_list_2', custom_threshold=0)
			self.status = 100
		elif self.status == 100:

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_gode_dungeon_scene_limit')
			self.logger.warn('고대 던전 남은 횟수 0? ' + str(match_rate))
			if match_rate > 0.9:
				self.status = 99999
			else:
				is_clicked = self.lyb_mouse_click('tera_gode_dungeon_scene_enter')
				if is_clicked == False:
					self.status = 99999
				else:
					self.status += 1
					self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', True)
					self.game_object.get_scene('tera_main_scene').set_option('wait_start_flag', True)
					self.game_object.get_scene('tera_raid_matching_scene').set_option('match_canceled', False)
					self.set_checkpoint('waiting_time')
					self.set_option('retry_count', 0)

		elif self.status == 101:
			self.game_object.interval = 0.01		

			if self.game_object.get_scene('tera_main_scene').get_option('wait_start_flag') != True:
				self.status = 110
			else:
				if self.game_object.get_scene('tera_raid_matching_scene').get_option('match_canceled') == True:
					self.status = 110
				else:
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_gode_dungeon_scene_enter')
					if match_rate > 0.9:
						self.lyb_mouse_click(self.scene_name + '_close_icon')
						self.status = 110

					elapsed_waiting_time = time.time() - self.get_checkpoint('waiting_time')
					wait_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_WAIT_MATCHING))
					if elapsed_waiting_time > wait_limit:
						retry_count = self.get_option('retry_count')
						if retry_count == None:
							retry_count = 0
						self.set_option('retry_count', retry_count + 1)

						self.logger.warn(work_name + ' 매칭 대기시간 초과로 입장을 실패했습니다. 재시도합니다. '+str(retry_count+1))
						self.game_object.get_scene('tera_main_scene').set_option('wait_start_flag', False)
						self.lyb_mouse_click('tera_gode_dungeon_scene_enter', custom_threshold=0)
					else:
						self.logger.debug(work_name + ' 매칭 대기 중 ' + str(int(elapsed_waiting_time)) + ' / ' + str(int(wait_limit)) + ' 초')

		elif self.status == 110:
			self.game_object.get_scene('tera_main_scene').checkpoint[work_name + '_check_start_each'] = 0
			self.status = 100
		else:
			if (	work_name != None and len(work_name) > 0 and 
					(self.get_work_status(work_name) > self.get_work_status('몬스터 도감'))
					):
				self.game_object.get_scene('tera_main_scene').checkpoint[work_name + '_check_start_each'] = 0
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_end', True)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', False)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def tera_summon_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_summon')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_summon', custom_threshold=0.2)

		if self.get_tutorial() == True:
			self.set_tutorial(False)
			self.status = self.get_work_status('무료 소환')

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('무료 소환'):
			self.status += 1
		elif self.status == self.get_work_status('무료 소환') + 1:
			self.lyb_mouse_click('tera_summon_scene_normal_summon', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('무료 소환') + 2:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_summon_scene_free')
			if match_rate > 0.98:
				self.lyb_mouse_click('tera_summon_scene_free', custom_threshold=0.98)
			self.status = 99999
		elif (	self.status == self.get_work_status('경험치 부스터 구매') or 
				self.status == self.get_work_status('골드 부스터 구매')
				):
			self.lyb_mouse_click('tera_summon_scene_special', custom_threshold=0)
			self.game_object.get_scene('tera_special_shop_scene').status = self.status
			self.status = 0
		else:
			self.lyb_mouse_click('tera_summon_scene' + '_close_icon')

		return self.status

	def tera_challenge_scene_common(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_dojun')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_dojun', custom_threshold=0.2)


		# print('DEBUG [ 요일 던전 ]:', self.status)
		difficulty_list = [
				'쉬움',
				'보통',
				'어려움',
				'매우 어려움',
				]
		if self.scene_name == 'tera_daily_dungeon_scene':
			work_name = '요일 던전'
		elif self.scene_name == 'tera_challenge_dokripgun_scene':
			work_name = '독립군 장비 보급'
		elif self.scene_name == 'tera_blgamesi_train_scene':
			work_name = '블가메시의 훈련'
		elif self.scene_name == 'tera_gold_giant_scene':
			work_name = '황금 거인 강탈'

		challenge_index = lybgameTera.LYBTera.challenge_list.index(work_name)
		config_name = lybconstant.LYB_DO_STRING_MODE_DIFFICULTY + str(challenge_index)

		difficulty = self.get_game_config(config_name)

		# if self.get_option('difficulty') == None:
		# 	difficulty = self.get_game_config(config_name)
		# else:
		# 	difficulty = self.get_option('difficulty')

		click_difficulty_pb = self.scene_name + '_difficulty_' + str(difficulty)	
		click_enter_pb = 'tera_challenge_scene_enter_possible'
		enter_limit_pb = self.scene_name + '_enter_limit'

		duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DUNGEON)) * 60	
		
		if self.get_tutorial() == True:			
			if len(work_name) < 1:
				self.status = 500
		else:
			if self.is_there_in_schedule_list(work_name) == False:
				self.status = 99999

			if self.game_object.get_scene('tera_main_scene').get_option(work_name + '_end_flag') == True:
				self.status = 99999

		self.logger.debug('[도전 던전] ' + str(work_name) + ' ' + str(self.status))

		if self.status == 0:
			# 개별 진행 시간 체크를 위해
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click(click_difficulty_pb, custom_threshold=0)
			self.status += 1
		elif self.status == 2:

			# 전체 진행 시간 체크
			if self.game_object.get_scene('tera_main_scene').get_checkpoint(work_name + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.game_object.get_scene('tera_main_scene').get_checkpoint(work_name + '_check_start')

			# print(elapsed_time, duration_limit)

			if elapsed_time > duration_limit:
				self.status = 99999
			else:
				is_matched = self.game_object.rateMatchedPixelBox(self.window_pixels, enter_limit_pb)
				# print('enter_limit_pb:', is_matched)
				if is_matched > 0.9:
					self.logger.warn(work_name + '입장을 실패했습니다.')
					self.set_option('difficulty', int(difficulty))
					self.status = 99999
				else:
					# is_possible = self.game_object.rateMatchedPixelBox(self.window_pixels, click_enter_pb, custom_tolerance=100)

					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[click_enter_pb],
											custom_threshold=0.7,
											custom_flag=1,
											custom_rect=(300, 300, 630, 380)
											)
					self.logger.debug(click_enter_pb + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', True)
						self.game_object.get_scene('tera_main_scene').set_option('wait_start_flag', True)
						self.set_checkpoint('waiting_time')
						self.set_option('difficulty', int(difficulty))
						self.status += 1
					else:
						custom_difficulty = self.get_option('difficulty')
						if custom_difficulty == None:
							custom_difficulty = int(difficulty)

						custom_difficulty -= 1

						if custom_difficulty > -1:
							self.logger.warn('도전 던전 난이도를 낮춥니다. ' + 
								difficulty_list[custom_difficulty + 1] + ' > ' + 
								difficulty_list[custom_difficulty])
							click_difficulty_pb = self.scene_name + '_difficulty_' + str(custom_difficulty)
							self.lyb_mouse_click(click_difficulty_pb, custom_threshold=0)
							self.set_option('difficulty', custom_difficulty)
						else:
							self.set_option('difficulty', 0)
							self.status = 99999
		elif self.status == 3:

			if self.game_object.get_scene('tera_main_scene').get_option('wait_start_flag') != True:
				self.status = 10
			else:
				elapsed_waiting_time = time.time() - self.get_checkpoint('waiting_time')
				wait_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_WAIT_MATCHING))
				# print('DEBUGXXXX:', elapsed_waiting_time, wait_limit)
				if elapsed_waiting_time > wait_limit:
					self.game_object.get_scene('tera_main_scene').set_option('wait_start_flag', False)
					self.status = 99999
				else:
					self.logger.warn(work_name + ' 랙걸림? ' + str(int(elapsed_waiting_time)) + ' / ' + str(int(wait_limit)) + ' 초')

		elif self.status == 10:
			self.game_object.get_scene('tera_main_scene').checkpoint[work_name + '_check_start_each'] = 0
			self.status = 1
		elif self.status == 500:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[click_enter_pb],
						custom_threshold=0.7,
						custom_flag=1,
						custom_rect=(300, 300, 630, 380)
						)
			self.logger.debug(click_enter_pb + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.lyb_mouse_click(click_enter_pb, custom_threshold=0)
			self.set_tutorial(False)
			self.status = 99999
		else:
			if work_name != None and len(work_name) > 0 and (self.get_work_status(work_name) > self.get_work_status('몬스터 도감')):
				self.game_object.get_scene('tera_main_scene').checkpoint[work_name + '_check_start_each'] = 0
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_end', True)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_dungeon_done', True)
				self.game_object.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def tera_challenge_dokripgun_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_dokripgun')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_dokripgun', custom_threshold=0.2)

		return self.tera_challenge_scene_common()	

	def tera_gold_giant_scene(self):
		return self.tera_challenge_scene_common()

	def tera_blgamesi_train_scene(self):
		return self.tera_challenge_scene_common()

	def tera_daily_dungeon_scene(self):

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_daily_dungeon')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_daily_dungeon', custom_threshold=0.2)

		return self.tera_challenge_scene_common()

	def tera_muhantap_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_muhantap')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_muhantap', custom_threshold=0.2)


		if self.game_object.get_scene('tera_main_scene').get_option('무한의 탑'+'_end_flag') == True:
			self.status = 99999

		# 테라 무한의 탑
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG) == True:
				self.status = 100
			else:
				is_matched = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_muhantap_scene_limit_count')
				if is_matched > 0.99:
					self.status = 100
				else:
					is_matched = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_muhantap_scene_enter_possible')
					# print('[DEBUG] tera_muhantap_scene_enter_possible', is_matched)
					if is_matched > 0.8:
						self.lyb_mouse_click('tera_muhantap_scene_enter_possible')
						self.game_object.get_scene('tera_main_scene').set_option('무한의 탑'+ '_dungeon_done', True)
					else:
						self.status = 100
		elif self.status == 100:
			self.lyb_mouse_click('tera_challenge_scene_sotang')
			self.status = 99999
		else:
			self.game_object.get_scene('tera_main_scene').set_option('무한의 탑'+ '_dungeon_end', True)
			self.game_object.get_scene('tera_main_scene').set_option('무한의 탑' + '_dungeon_done', True)			
			self.lyb_mouse_click('tera_muhantap_scene_close_icon')
			self.status = 0

		return self.status

	def tera_smithy_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_smithy')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_smithy', custom_threshold=0.2)


		if self.get_tutorial() == True:
			self.status = 500
		

		if self.status == 0:
			self.status += 1
		elif self.status == 500:
			self.lyb_mouse_click('tera_smithy_scene_weapon_tab', custom_threshold=0)
			self.set_tutorial(False)
			self.status += 1
		elif self.status == 501:
			self.lyb_mouse_click('tera_smithy_scene_item_0', custom_threshold=0)
			self.status += 1
		elif self.status == 502:
			self.lyb_mouse_click('tera_smithy_scene_item_1', custom_threshold=0)
			self.status += 1
		elif self.status == 503:
			self.lyb_mouse_click('tera_smithy_scene_item_levelup', custom_threshold=0)
			self.status = 99999	

		elif (	self.status == self.get_work_status('가슴 레벨업') or
				self.status == self.get_work_status('무기 레벨업') or
				self.status == self.get_work_status('신발 레벨업') or
				self.status == self.get_work_status('장갑 레벨업') or
				self.status == self.get_work_status('목걸이 레벨업') or
				self.status == self.get_work_status('반지 레벨업') or
				self.status == self.get_work_status('팔찌 레벨업') or
				self.status == self.get_work_status('귀걸이 레벨업')
				):
			self.lyb_mouse_click('tera_smithy_scene_auto_select', custom_threshold=0)
			self.game_object.get_scene('tera_auto_select_scene').status = self.status
			self.set_option('last_status', self.status)
			self.status = 99990

		elif(	self.status == self.get_work_status('무기 레벨업 - 대장간') or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') or
				self.status == self.get_work_status('장신구 레벨업 - 대장간')
				):
			s_index = (self.status - self.get_work_status('무기 레벨업 - 대장간')) / 1000
			self.set_option('dejangan_item_start_y', None)
			self.lyb_mouse_click('tera_smithy_scene_tab_' + str(int(s_index)), custom_threshold=0)
			self.status += 1
		elif(	self.status == self.get_work_status('무기 레벨업 - 대장간') + 1 or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') + 1 or
				self.status == self.get_work_status('장신구 레벨업 - 대장간') + 1
				):
			self.lyb_mouse_click('tera_smithy_scene_sort', custom_threshold=0)
			self.game_object.get_scene('tera_smithy_item_sort_scene').status = self.status - 1
			self.status += 1
		elif(	self.status == self.get_work_status('무기 레벨업 - 대장간') + 2 or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') + 2 or
				self.status == self.get_work_status('장신구 레벨업 - 대장간') + 2
				):
			start_x = 345

			start_y = self.get_option('dejangan_item_start_y')
			if start_y == None:
				start_y = 120
			
			end_x = 600
			end_y = 345

			item_rank = int(self.get_game_config(lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK))
			item_rank_pb = self.get_center_pixel_info('tera_smithy_scene_item_rank_' + str(item_rank))
		
			# print('[DEBUG]:', start_x, start_y, end_x, start_y + 60, item_rank_pb[1])
			(loc_x, loc_y) = self.find_item_loc(start_x, start_y, end_x, start_y + 60, item_rank_pb[1])
			if loc_x == -1:
				start_y += 60

				if start_y > end_y:
					drag_count = self.get_option('smithy_drag_count')
					if drag_count == None:
						drag_count = 0
					self.lyb_mouse_drag('tera_smithy_scene_tab_drag_bottom', 'tera_smithy_scene_tab_drag_top')
					start_y = None

					drag_count += 1
					if drag_count > int(self.get_game_config(lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG)):
						self.status = 99999
					else:
						self.set_option('smithy_drag_count', drag_count)

				self.set_option('dejangan_item_start_y', start_y)
			else:
				# print('[DEBUG]: Clicked', loc_x, loc_y)
				self.lyb_mouse_click_location2(loc_x, loc_y)
				self.status += 1
		elif(	self.status == self.get_work_status('무기 레벨업 - 대장간') + 3 or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') + 3 or
				self.status == self.get_work_status('장신구 레벨업 - 대장간') + 3
				):

			self.lyb_mouse_click('tera_smithy_scene_auto_select', custom_threshold=0)
			self.game_object.get_scene('tera_auto_select_scene').status = self.status - 3
			self.set_option('last_status', self.status)
			self.status = 99990
		elif self.status == 99990:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_smithy_scene_gold')
			if match_rate > 0.8:
				self.lyb_mouse_click('tera_smithy_scene_item_levelup', custom_threshold=0)
				self.status += 1
			else:
				rank_iterator = self.game_object.get_scene('tera_auto_select_scene').get_option('rank_iterator')
				if rank_iterator == None:
					rank_iterator = 0

				work_name = self.game_object.get_scene('tera_main_scene').current_work
				if work_name == None or len(work_name) < 1 or (not '레벨업' in work_name):
					self.status = 99999
				else:
					item_loc = work_name.split()[0]
					self.logger.debug('자동 선택 아이템 레벨업 부위: ' + item_loc)

					if item_loc == '방어구':
						item_loc = '가슴'
					elif item_loc == '장신구':
						item_loc = '목걸이'

					item_loc_index = lybgameTera.LYBTera.item_loc_list.index(item_loc)

					rank_config = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(item_loc_index))
					# print('rank_iterator', rank_iterator, 'rank_config', rank_config)
					if rank_iterator >= int(rank_config):
						self.game_object.get_scene('tera_auto_select_scene').set_option('rank_iterator', None)
						self.status = 99999
					else:
						self.game_object.get_scene('tera_auto_select_scene').set_option('rank_iterator', rank_iterator + 1)
						self.status += 1
		elif self.status == 99991:
			self.status += 1
		elif self.status == 99992:
			self.status = self.get_option('last_status')
		else:
			self.lyb_mouse_click('tera_smithy_scene' + '_close_icon')
			self.status = 0

		return self.status

	def tera_hero_talent_scene(self):
		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_talent')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_talent', custom_threshold=0.2)

		if self.get_tutorial() == True:
			self.status = 500
		
		if self.status == 0:
			self.status += 1
		elif self.status == 500:
			self.lyb_mouse_click('tera_hero_talent_scene_1_tab', custom_threshold=0)
			self.set_tutorial(False)
			self.status += 1
		elif self.status == 501:
			self.lyb_mouse_click('tera_hero_talent_scene_level5', custom_threshold=0)
			self.status += 1
		elif self.status == 502:
			self.lyb_mouse_click('tera_hero_talent_scene_apply', custom_threshold=0)
			self.status += 1
		elif self.status == 503:
			self.lyb_mouse_click('tera_hero_talent_scene_save', custom_threshold=0)
			self.status = 99999	
		elif self.status == 600:
			self.lyb_mouse_drag('tera_hero_talent_scene_drag_top', 'tera_hero_talent_scene_drag_bottom', delay=1)
			time.sleep(1)
			elapsed_time = time.time() - self.get_checkpoint('hero_talent')
			# print('elapsed_time', int(elapsed_time))
			if elapsed_time > 10:
				# self.set_option('top_drag_complete', True)
				self.status = self.last_status['talent_drag']
				self.set_checkpoint('hero_talent')
		elif self.status == 601:
			self.lyb_mouse_drag('tera_hero_talent_scene_drag_bottom', 'tera_hero_talent_scene_drag_top', delay=1)
			time.sleep(1)
			self.status = self.last_status['talent_drag']
		elif self.status == self.get_work_status('영웅 특성'):
			# self.set_option('top_drag_complete', False)
			self.set_checkpoint('hero_talent')
			iterator = self.get_option('talent_iterator')
			if iterator == None:
				iterator = -1
			elif iterator > 14:
				self.logger.debug('Lv. ' + str((iterator+1) * 5) + '까지 특성 찍기를 완료했습니다.')
				self.set_option('talent_iterator', None)
				self.lyb_mouse_click('tera_hero_talent_scene_save', custom_threshold=0)
				self.status = 99999
				return self.status
			
			iterator += 1

			self.set_option('talent_iterator', iterator)
			# if iterator == 0:
			# 	self.last_status['talent_drag'] = self.status + 1
			# 	self.status = 600
			# else:
			self.status += 1
		elif self.status == self.get_work_status('영웅 특성') + 1:
			iterator = self.get_option('talent_iterator')
			level_name = 'tera_hero_talent_level_' + str(iterator)
			talent_index = int( self.get_game_config(lybconstant.LYB_DO_STRING_HERO_TALENT_LEVEL + str(iterator)) )

			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[level_name],
				custom_threshold=0.7
				)
			# print('Lv.', (iterator+1) * 5 ,':', (loc_x, loc_y))
			if loc_x == -1:
				# if self.get_option('top_drag_complete') != True:
				# 	self.last_status['talent_drag'] = self.status
				# 	self.status = 600
				# else:
				elapsed_time = time.time() - self.get_checkpoint('hero_talent')
				# print('elapsed_time down', elapsed_time)
				if elapsed_time > 20:
					self.logger.warn('Lv. ' + str((iterator+1)*5) + ' 특성을 찾지 못했습니다.')
					self.status = self.get_work_status('영웅 특성')
				else:
					self.last_status['talent_drag'] = self.status
					self.status = 601
			else:
				self.lyb_mouse_click_location(loc_x - 140*(2-talent_index), loc_y)
				time.sleep(1)
				is_clicked = self.lyb_mouse_click('tera_hero_talent_scene_apply', custom_threshold=0.9)
				# print(is_clicked, self.get_option('talent_iterator'))
				if is_clicked == False:
					self.set_option('talent_iterator', 15)
				
				self.status = self.get_work_status('영웅 특성')

			# for i in range(16):
			# 	print(i, lybconstant.LYB_DO_STRING_HERO_TALENT_LEVEL+str(i), self.get_game_config(lybconstant.LYB_DO_STRING_HERO_TALENT_LEVEL + str(i)))
		else:
			self.lyb_mouse_click('tera_hero_talent_scene' + '_close_icon')
			self.status = 0

		return self.status


	def tera_inventory_scene(self):

		box_list = [

				'연마제 상자',
				'일반 룬 상자',
				'고급 장비 상자 ',
				'골드 상자',
				'고급 강화 재료 상자',
				'고급 장신구 상자',
				'방어구 연마제 상자',
				'희귀 스킨 상자',
				'희귀 크리스탈 상자',
				'보석 상자',
				'강화 재료 상자'

			]

		red_gem = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_red_gem_0')
		if red_gem > 0.2:
			self.lyb_mouse_click('tera_red_gem_0', custom_threshold=0.2)
			return self.status

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('자동 장착'):
			self.lyb_mouse_click('tera_inventory_scene_auto_equip')
			self.status = 99999
		elif (	self.status == self.get_work_status('소모품 상자 열기') or
				self.status == self.get_work_status('경험치 부스터 사용') or
				self.status == self.get_work_status('골드 부스터 사용') 
				):

			self.lyb_mouse_click('tera_inventory_scene_consume_tab')
			self.set_checkpoint('start_consume')
			self.status += 1
		elif self.status == self.get_work_status('소모품 상자 열기') + 1:
			elapsed_time = time.time() - self.get_checkpoint('start_consume')
			if elapsed_time > 60:
				self.status = 99999
				return self.status

			box_iterator = self.get_option('box_iterator')
			if box_iterator == None:
				box_iterator = 0
				self.set_option('box_iterator', 0)

			if box_iterator >= len(box_list) - 1:
				box_iterator = 0
				self.set_option('box_iterator', 0)
				self.status = 99999
			else:
				box_name = 'tera_consume_box_' + str(box_iterator)
				self.logger.info(box_list[box_iterator] + ' 체크')
				(loc_x, loc_y) = self.game_object.locationOnWindow(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic[box_name],
					custom_threshold=0.7
					)
				# print(box_name,':', (loc_x, loc_y))
				if loc_x == -1:
					if self.get_option('is_drag') == True:
						self.set_option('box_iterator', box_iterator + 1)
						self.lyb_mouse_drag('tera_inventory_scene_drag_top', 'tera_inventory_scene_drag_bottom')
						self.set_option('is_drag', False)
					else:
						self.set_option('is_drag', True)
						self.lyb_mouse_drag('tera_inventory_scene_drag_bottom', 'tera_inventory_scene_drag_top')
				else:
					self.logger.debug(box_list[box_iterator] + ' 발견됨')
					self.lyb_mouse_click_location(loc_x, loc_y)
		elif (	self.status == self.get_work_status('경험치 부스터 사용') + 1 or
				self.status == self.get_work_status('골드 부스터 사용') + 1
				):
			self.set_option('exp_drag_count', 0)
			self.lyb_mouse_click('tera_inventory_scene_sort')
			self.game_object.get_scene('tera_inventory_item_sort_scene').status = self.get_work_status('경험치 부스터 사용')

			if self.status == self.get_work_status('경험치 부스터 사용') + 1:
				self.set_option('item_1', 'tera_item_exp_1')
				self.set_option('item_2', 'tera_item_exp_2')
				self.set_option('item_5', 'tera_item_exp_5')
			else:
				self.set_option('item_1', 'tera_item_gold_1')
				self.set_option('item_2', 'tera_item_gold_2')
				self.set_option('item_5', 'tera_item_gold_5')

			self.status += 1
		elif (	self.status == self.get_work_status('경험치 부스터 사용') + 2 or
				self.status == self.get_work_status('골드 부스터 사용') + 2
				):
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[self.get_option('item_1')],
											custom_flag=1,
											custom_rect=(325,115,640,340)
											)
			# print('[DEBUG] item_1', (loc_x, loc_y), match_rate)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 99999
				return self.status

			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[self.get_option('item_2')],
											custom_flag=1,
											custom_rect=(325,115,640,340)
											)
			# print('[DEBUG] item_2', (loc_x, loc_y), match_rate)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 99999
				return self.status

			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[self.get_option('item_5')],
											custom_flag=1,
											custom_rect=(325,115,640,340)
											)
			# print('[DEBUG] item_5', (loc_x, loc_y), match_rate)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 99999
				return self.status
			self.status += 1
		elif (	self.status == self.get_work_status('경험치 부스터 사용') + 3 or
				self.status == self.get_work_status('골드 부스터 사용') + 3
				):
			exp_drag_count = self.get_option('exp_drag_count')
			if exp_drag_count == None:
				exp_drag_count = 0

			if exp_drag_count >= int(self.get_game_config(lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT)):
				self.status = 99999
			else:
				exp_drag_count += 1
				self.logger.debug('부스터 아이템 탐색 드래그 횟수: ' + str(exp_drag_count) + 
					'/' + str(self.get_game_config(lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT)))
				self.set_option('exp_drag_count', exp_drag_count)
				self.lyb_mouse_drag('tera_inventory_scene_drag_bottom', 'tera_inventory_scene_drag_top')
				self.game_object.interval = self.period_bot(3)
				self.status -= 1
		elif (	self.status == self.get_work_status('경험치 부스터 사용') + 4 or
				self.status == self.get_work_status('골드 부스터 사용') + 4
				):
			self.status = 99999
		elif self.status == self.get_work_status('일괄 판매'):
			self.lyb_mouse_click('tera_inventory_scene_sell')
			self.game_object.get_scene('tera_sell_all_scene').status = 0
			self.status = 99999
		elif (	self.status == self.get_work_status('가슴 레벨업') or
				self.status == self.get_work_status('무기 레벨업') or
				self.status == self.get_work_status('신발 레벨업') or
				self.status == self.get_work_status('장갑 레벨업') or
				self.status == self.get_work_status('목걸이 레벨업') or
				self.status == self.get_work_status('반지 레벨업') or
				self.status == self.get_work_status('팔찌 레벨업') or
				self.status == self.get_work_status('귀걸이 레벨업')
				):
			work_name = self.game_object.get_scene('tera_main_scene').current_work
			if work_name == None or len(work_name) < 1:
				self.logger.warn('비정상: ' + str(self.status))
				self.status = 99999
			else:
				if self.get_option('select_set') == True:
					item_loc = work_name.split()[0]
					self.logger.debug('아이템 레벨업 부위: ' + item_loc)
					item_loc_index = lybgameTera.LYBTera.item_loc_list.index(item_loc)
					# print('item_loc_index:', item_loc_index)
					# 장비 부위를 고른다
					self.lyb_mouse_click('tera_inventory_scene_item_locate_' + str(item_loc_index), custom_threshold=0)
					self.game_object.get_scene('tera_equip_item_scene').status = self.status
					self.set_option('select_set', False)
					self.status = 99999
				else:
					self.lyb_mouse_click('tera_inventory_scene_equip_set')		
					self.set_option('select_set', False)
		elif self.status == self.get_work_status('장비 세트'):
			if self.get_option('select_set') == True:
				self.set_option('select_set', False)
				self.status = 99999
			else:
				self.game_object.get_scene('tera_equip_set_scene').status = self.get_work_status('장비 세트')
				self.lyb_mouse_click('tera_inventory_scene_equip_set')	
				self.set_option('select_set', False)

		elif (	self.status == self.get_work_status('무기 레벨업 - 대장간') or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') or
				self.status == self.get_work_status('장신구 레벨업 - 대장간')
				):
			tab_index = int((self.status - self.get_work_status('무기 레벨업 - 대장간')) / 1000)
			self.lyb_mouse_click('tera_inventory_scene_tab_' + str(tab_index), custom_threshold=0)
			self.status = 99999
		elif self.status == 99999:
			self.status += 1
		elif self.status == 100000:
			self.status += 1
		elif self.status == 100001:
			self.status += 1
		else:
			self.lyb_mouse_click('tera_inventory_scene_close_icon')
			self.status += 1

		return self.status

	def tera_manage_hero_scene(self):

		if self.get_tutorial() == True:
			self.status = 500

		if self.status == 0:
			self.status += 1
		elif self.status == 500:
			self.lyb_mouse_click('tera_manage_hero_scene_attack', custom_threshold=0)
			self.set_tutorial(False)
			self.status += 1
		elif self.status == 501:
			self.lyb_mouse_click('tera_manage_hero_scene_plus', custom_threshold=0)
			self.status += 1
		elif self.status == 502:
			self.lyb_mouse_click('tera_manage_hero_scene_save', custom_threshold=0)
			self.status = 99999	
		elif self.status == self.get_work_status('영웅 특성'):
			self.lyb_mouse_click('tera_hero_talent_tab', custom_threshold=0)
			self.game_object.get_scene('tera_hero_talent_scene').status = self.status
			self.status = 99999		
		elif self.status == self.get_work_status('영웅 스킬'):
			self.lyb_mouse_click('tera_hero_skill_tab', custom_threshold=0)
			self.status += 1	
		elif self.status == self.get_work_status('영웅 스킬') + 1:
			skill_iterator = self.get_option('skill_iterator')
			if skill_iterator == None:
				skill_iterator = 0

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_manage_hero_scene_skill_point_0')
			# print('0?: ', match_rate)
			if match_rate > 0.9:
				self.logger.warn('스킬 포인트 부족')
				skill_iterator = 8

			if skill_iterator > 7:
				self.set_option('skill_iterator', 0)
				self.status = 99999
			else:
				self.set_option('skill_iterator', skill_iterator + 1)

				skill_checkbox = lybconstant.LYB_DO_BOOLEAN_HERO_SKILL + str(skill_iterator)
				is_checked = self.get_game_config(skill_checkbox)

				# print(skill_iterator, skill_checkbox, is_checked)
				if is_checked:
					self.lyb_mouse_click('tera_manage_hero_scene_skill_' + str(skill_iterator), custom_threshold=0)
					self.status += 1
		elif self.status == self.get_work_status('영웅 스킬') + 2:	
			self.lyb_mouse_click('tera_manage_hero_scene_max')	
			self.status += 1
		elif self.status == self.get_work_status('영웅 스킬') + 3:	
			self.lyb_mouse_click('tera_manage_hero_scene_save')	
			self.status = self.get_work_status('영웅 스킬') + 1
		else:
			self.lyb_mouse_click('tera_manage_hero_scene' + '_close_icon')
			self.status = 0

		return self.status



































































































































	# +-------------------------+
	# |							|
	# |							|
	# |			MAIN			|
	# |							|
	# |							|
	# +-------------------------+

	def tera_main_scene(self):
		# print('DEBUG ------------', self.current_work, ':', self.get_option('자동 장착' + '_end_flag'))
		# self.loggingToGUI('메인 화면 체크: ' + str(self.status) + ' ' + str(self.current_work))
		# print('[DEBUG] tera_main_scene:', self.current_work, self.status)

		self.update_skill_time()

		if self.game_object.current_schedule_work != self.current_work:
			self.game_object.current_schedule_work = self.current_work

		self.game_object.main_scene = self
			
		self.schedule_list = self.get_game_config('schedule_list')
		if len(self.schedule_list) == 1:
			self.logger.warn('스케쥴 작업이 없어서 종료합니다.')
			return -1

		if self.is_full_inventory() == True:	
			is_checked = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL)
			self.logger.warn('가방이 가득 찼습니다. 작업 중지 설정값: ' + str(is_checked))

			telegram_elapsed_time = time.time() - self.get_checkpoint('telegram_inventory_check_time')
			if telegram_elapsed_time > 180:
				self.set_checkpoint('telegram_inventory_check_time')
				if self.game_object.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full') == True:
					send_text = self.game_object.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full')
					if len(send_text) < 1:
						send_text = '인벤토리가 가득찼습니다'

					self.game_object.telegram_send(send_text)

			if is_checked:
				self.logger.warn('[디버깅   ] 인벤풀: ' + str(self.status) + ':' + str(self.current_work))

				if self.current_work != None:

					if (	self.current_work == '일괄 판매' or
							self.current_work == '친밀도' or
							self.current_work == '가슴 레벨업' or
							self.current_work == '무기 레벨업' or
							self.current_work == '신발 레벨업' or
							self.current_work == '장갑 레벨업' or
							self.current_work == '목걸이 레벨업' or
							self.current_work == '반지 레벨업' or
							self.current_work == '팔찌 레벨업' or
							self.current_work == '귀걸이 레벨업' or
							self.current_work == '무기 레벨업 - 대장간' or
							self.current_work == '방어구 레벨업 - 대장간' or
							self.current_work == '장신구 레벨업 - 대장간'
							):
						# print('DEBUG2')
						self.logger.info('가방이 가득찼지만 [일괄 판매], [친밀도], [장비 레벨업] 관련 작업은 수행 가능합니다.')

					else:
						if len(self.current_work) > 0:
							self.set_option(self.current_work +'_end_flag', True)

		if self.is_new_event_bosang():
			return self.status

		# if self.is_full_inventory() == True:
		# 	if self.get_option('full_inventory') != True:
		# 		self.loggingToGUI('가방이 가득찼습니다. 일괄 판매 작업을 시작합니다.')
		# 		self.last_status['full_inventory'] = self.status
		# 		self.set_option('full_inventory_last_current_work', self.current_work)
		# 		self.set_option('full_inventory', True)
		# 		self.current_work = '일괄 판매'
		# 		self.set_work_status()

		if self.current_work != None:
			if (	'퀘스트' in self.current_work or
					(	self.status > self.get_work_status('몬스터 도감') and
						self.status < self.get_work_status('[반복 시작]')
						)
					):
				if self.is_open_map() == True:
					self.lyb_mouse_click('tera_main_scene_plus', custom_threshold=0)
					return self.status

		if self.current_work != None and self.get_option('wait_start_flag') == True:
			self.logger.info('던전 진입 완료')
			self.set_option('wait_start_flag', False)
			enter_count = self.get_option(self.current_work + '_enter_count')
			if enter_count == None:
				enter_count = 0

			self.set_option(self.current_work + '_enter_count', enter_count + 1)
			self.set_checkpoint(self.current_work + '_check_start_each')
			self.set_option('count_error_dungeon', 0)
			self.game_object.interval = int(self.get_game_config(lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START))
			self.set_option('tracking_count', 0)
			self.game_object.get_scene('tera_dungeon_death_scene').status = 0


		# if time.time() - self.get_checkpoint('wait_penaltry') < 600:
		# 	self.loggingToGUI('부활 후유증때문에 10분(600초)간 대기 중입니다. 경과 시간: ' + 
		# 		str(int(time.time() - self.get_checkpoint('wait_penaltry'))) + '초')
		# 	return self.status


		if self.get_option('guild_village') == True:

			if self.get_checkpoint('guild_village') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint('guild_village')

			self.logger.debug('길드 마을 체류 시간: '+str(int(elapsed_time))+' 초')

			if ( 	self.get_option('guild_village_done') == True or
					elapsed_time > 60 
					):
				self.lyb_mouse_click('tera_main_scene_out_field', custom_threshold=0)
				self.set_option('guild_village', False)
				self.set_option('guild_village_running', False)
				self.set_option('guild_village_done', False)
				self.checkpoint['guild_village'] = 0
				return self.status

			if self.get_option('guild_village_running') == True:
				return self.status

			self.set_checkpoint('guild_village')
			self.set_option('guild_village_running', True)
			(x, y) = self.location_etc_quest()
			# print('[길드]:', (x, y))
			if x != -1:
				self.lyb_mouse_click_location(x,y)
				# self.lyb_mouse_click('tera_main_scene_quest_top', custom_threshold=0)
				return self.status

		max_play_stance = {}
		max_play_stance['name'] = ''
		max_play_stance['value'] = 0

		manual_play = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_sudong', custom_tolerance=100)
		if max_play_stance['value'] < manual_play:
			max_play_stance['name'] = 'manual_play'
			max_play_stance['value'] = manual_play

		half_auto_play = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_banjadong', custom_tolerance=100)
		if max_play_stance['value'] < half_auto_play:
			max_play_stance['name'] = 'half_auto_play'
			max_play_stance['value'] = half_auto_play

		auto_play = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_jadong', custom_tolerance=100)
		if max_play_stance['value'] < auto_play:
			max_play_stance['name'] = 'auto_play'
			max_play_stance['value'] = auto_play

		maul_play = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_maul',custom_tolerance=100)
		if max_play_stance['value'] < maul_play:
			max_play_stance['name'] = 'maul_play'
			max_play_stance['value'] = maul_play


		dogam_stance_name = self.get_game_config(lybconstant.LYB_DO_STRING_DOGAM_STANCE)
		dogam_stance_index = lybgameTera.LYBTera.dogam_stance_list.index(dogam_stance_name)


		tracking_match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'tera_main_scene_tracking_icon_loc')
		# self.logger.debug('추적 매칭률: '+str(int(tracking_match_rate*100))+'%')
		if tracking_match_rate < 0.7:
			quest_top_main = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_quest_top', custom_tolerance=100)
			quest_sub = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_quest_sub', custom_tolerance=100)
			quest_complete = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_quest_complete', custom_tolerance=100)
			quest_challenge = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_quest_challenge', custom_tolerance=100)
			quest_dungeon = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_dungeon', custom_tolerance=100)
			quest_tobul = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_tobul', custom_tolerance=100)
			# quest_talent = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_talent', custom_tolerance=100)
			# quest_buhal = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_buhal', custom_tolerance=100)
			# quest_skill = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_skill', custom_tolerance=100)
			# quest_reward = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_reward', custom_tolerance=100)


			out_field = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_out', custom_tolerance=100)
		
			# self.loggingToGUI(
			# 	'추'+str(int(tracking_match_rate*100))+
			# 	'메'+str(int(quest_top_main*100))+
			# 	'서'+str(int(quest_sub*100))+
			# 	'완'+str(int(quest_complete*100))+
			# 	'도'+str(int(quest_challenge*100))+
			# 	'던'+str(int(quest_dungeon*100))+
			# 	'토'+str(int(quest_tobul*100))+
			# 	'특'+str(int(quest_talent*100))+
			# 	'부'+str(int(quest_buhal*100))+
			# 	'스'+str(int(quest_skill*100))+
			# 	'보'+str(int(quest_reward*100))+
			# 	'나'+str(int(out_field*100))
			# 	)
			
			# 메인퀘스트 중일때는 메인과 서브만 진행

			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU) == True:
				(loc_x, loc_y) = self.loc_buhal_quest()
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status

			if self.is_main_quest():
				if self.get_option('hero_death') != True:
					s_time = time.time()
					(x, y) = self.loc_quest()
					e_time = time.time()
					# print('[DEBUG] Elapsed Time MAIN QUEST:', round(e_time - s_time, 5))

					# (x, y) = self.location_main_quest()
					self.logger.debug('[메인]: ' + str((x, y)))
					if x != -1:
						self.lyb_mouse_click_location(x,y)
						# self.lyb_mouse_click('tera_main_scene_quest_top', custom_threshold=0)
						return self.status
				# quest_sub > 0.9 or quest_complete > 0.9 or quest_top_main > 0.9
			elif self.is_boss_quest():
				(loc_x, loc_y) = self.loc_boss_quest()
				if loc_x != -1:
					self.logger.debug('[보스]: ' + str((loc_x, loc_y)))
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status
				else:
					is_clicked = self.set_combat_stance(max_play_stance['name'], max_play_stance['value'], ['auto_play', 'tracking_match_rate'])
					if is_clicked:
						return self.status
			elif self.current_work != None and len(self.current_work) > 0:
				# print('-----::----', self.get_elapsed_time(), self.period_bot(10))
				if self.get_elapsed_time() > self.period_bot(10):
					if self.status == self.get_work_status('무한의 탑'):
						# [던전] 표시가 없다.
						# print('DEBUG111111')
						pass
					elif self.status > self.get_work_status('몬스터 도감'):

						tracking_count = self.get_option('tracking_count')
						if tracking_count == None:
							tracking_count = 0

						tracking_limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_TRACKING))

						if self.get_checkpoint(self.current_work + '_check_start_each') == None:
							each_elapsed_time = 0
						else:
							each_elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start_each')
						self.logger.debug('TimeCheckTracking' + 
							' W:' + str(self.current_work) + 
							' E:' + str(each_elapsed_time) +
							' T:' + str(tracking_count) + 
							' L:' + str(tracking_limit_count) + 
							' S:' + str(self.get_option(self.current_work + '_end_flag')))

						if (	each_elapsed_time < self.period_bot(10) or
								tracking_count >= tracking_limit_count
								):	
								self.logger.debug('Tracking click permission ok')
						elif self.get_option(self.current_work + '_end_flag') == True:
							self.logger.debug('end:' + str(self.current_work))
						else:
							self.set_option('tracking_count', tracking_count + 1)	
							return self.status
						# print('------------------------------------------', self.current_work, self.get_elapsed_time())
						s_time = time.time()
						(loc_x, loc_y) = self.loc_dungeon()
						e_time = time.time()
						# print('[DEBUG] Elapsed Time DUNGEON QUEST:', round(e_time - s_time, 5))
						if loc_x != -1:
						# if (	quest_challenge > 0.9 or 
						# 		quest_dungeon > 0.9 or
						# 		quest_tobul > 0.9 or
						# 		quest_complete > 0.9
						# 	):
							# self.lyb_mouse_click('tera_main_scene_quest_top', custom_threshold=0)


					
							self.set_option('tracking_count', 0)
							self.lyb_mouse_click_location(loc_x, loc_y)

							return self.status
						else:
							period_dungeon = self.get_checkpoint('period_dungeon')
							count_error_dungeon = self.get_option('count_error_dungeon')
							if count_error_dungeon == None:
								count_error_dungeon = 0

							if period_dungeon != 0:
								self.loggingElapsedTime('던전 진행 중 이상 상태 체크', int(time.time() - period_dungeon), count_error_dungeon, period=5)
								if (	time.time() - period_dungeon < self.period_bot(30) and 
										self.get_option(self.current_work + '_dungeon_end') != True
									 	):
									if count_error_dungeon > 10:
										self.set_option(self.current_work + '_dungeon_done', False)
									self.set_option('count_error_dungeon', count_error_dungeon + 1)


								if count_error_dungeon > 20:
									self.logger.warn('던전 진행 중 이상 상태 감지 게임 재시작')
									self.game_object.terminate_application()
									return 1000000

							self.set_checkpoint('period_dungeon')
				
					if out_field > 0.3:
						# 던전 전투 중이라는 의미
						# self.loggingToGUI('수: '+str(int(manual_play*100))+\
						# 	' 반: ' + str(int(half_auto_play*100))+\
						# 	' 마: ' + str(int(maul_play*100))+\
						# 	' 자: ' + str(int(auto_play*100)))
						if self.status == self.get_work_status('몬스터 도감'):
						 	if dogam_stance_index == 3:
						 		self.checkpoint['last_dogam_check_time'] = 0
						elif self.status > self.get_work_status('몬스터 도감'):
							if manual_play > 0.9:
								time.sleep(1)
								self.lyb_mouse_click('tera_main_scene_sudong', custom_threshold=0)
							elif half_auto_play > 0.9:
								time.sleep(1)
								self.lyb_mouse_click('tera_main_scene_banjadong', custom_threshold=0)
								time.sleep(1)
			elif self.scene_name == 'tera_jiha_arena_main_scene':
				pass
			elif self.scene_name == 'tera_kaia_junjang_main_scene':
				pass
			else:
				pass
				# is_clicked = self.set_combat_stance(max_play_stance['name'], max_play_stance['value'], ['manual_play', 'maul_play'])
				# if is_clicked:
				# 	stance_change_count = self.get_option('stance_change_count')
				# 	if stance_change_count == None:
				# 		stance_change_count = 0

				# 	# print('stance_change_count', stance_change_count)
				# 	if stance_change_count < 1:
				# 		self.set_option('stance_change_count', stance_change_count + 1)
				# 		return self.status
				# 	else:
				# 		self.set_option('stance_change_count', 0)

		else:
			if self.is_main_quest():
				self.logger.debug('메인 퀘스트 진행 중')
				(loc_x, loc_y) = self.loc_talent_quest()
				if loc_x != -1:
					self.game_object.get_scene('tera_hero_talent_scene').status = self.get_work_status('영웅 특성')
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status

				(loc_x, loc_y) = self.loc_skill_quest()
				if loc_x != -1:
					self.game_object.get_scene('tera_manage_hero_scene').status = self.get_work_status('영웅 스킬')
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status

				(loc_x, loc_y) = self.loc_equip_quest()
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status

				(loc_x, loc_y) = self.loc_bosang_quest()
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status

		if max_play_stance['value'] < tracking_match_rate:
			max_play_stance['name'] = 'tracking_match_rate'
			max_play_stance['value'] = tracking_match_rate


		# print('[DEBUG] CP1 - ', self.status)
		# 지역 인식은 던전에서 하지 말자.
		if (	self.status == self.get_work_status('메인 퀘스트') or
				self.status == self.get_work_status('지하 결투장')
				):
			# print('[DEBUG] AreaDetected:', self.status)
			# s = time.time()
			(current_area, current_area_rate) = self.get_current_area()
			# print('[DEBUG] Area:', (current_area, current_area_rate))
			# print((current_area, current_area_rate))
			if current_area_rate > int(self.get_game_config(lybconstant.LYB_DO_STRING_AREA_THRESHOLD)) * 0.01:

				if '분쟁' in current_area:
					duration_battle = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_BATTLE))
					if self.get_checkpoint('battle_area') == 0:
						self.set_checkpoint('battle_area')

					elapsed_time_battle = time.time() - self.get_checkpoint('battle_area')
					battle_area_elapsed_time = time.time() - self.get_checkpoint('battle_area')
					self.loggingElapsedTime('분쟁 구역 진행 중', int(battle_area_elapsed_time), duration_battle, period=5)
					if battle_area_elapsed_time > duration_battle:
						self.lyb_mouse_click('tera_main_scene_out_field', custom_threshold=0)
						return self.status
				else:
					self.set_option('battle_area', False)
					self.checkpoint['battle_area'] = 0
					if '무한의탑' in current_area:
						is_clicked = self.set_combat_stance(max_play_stance['name'], max_play_stance['value'], ['auto_play', 'tracking_match_rate'])
						if is_clicked:
							return self.status
					elif (	'지하결투장' in current_area or 
							'카이아의전장' in current_area
							):
						is_clicked = self.set_combat_stance(max_play_stance['name'], max_play_stance['value'], ['auto_play', 'tracking_match_rate'])
						if is_clicked:
							return self.status
			else:
				self.logger.debug('[지역 체크] 필드')
			# e = time.time()
			# print('[DEBUG] Elapsed Time AREA Detect:', 
				# current_area, '['+str(int(current_area_rate*100))+']', round(e - s, 3))
			# print('[DEBUG] Area:', round(e-s, 2))


		if (	self.scene_name == 'tera_jiha_arena_main_scene' or 
				self.scene_name == 'tera_kaia_junjang_main_scene'
				):

			# print('[DEBUG] JihaArena')
			return self.status

		if self.status == self.get_work_status('몬스터 도감'):
			# 하드 코딩
			if self.game_object.get_scene('tera_monster_dogam_scene').get_checkpoint('dogam_chase') == 0:
				elapsed_time_chase = 0
			else:
				elapsed_time_chase = time.time() - self.game_object.get_scene('tera_monster_dogam_scene').get_checkpoint('dogam_chase')
			# print('DEBUG == ', elapsed_time_chase, int(self.get_game_config(lybconstant.LYB_DO_STRING_DOGAM_INTERVAL)), max_play_stance)

			if elapsed_time_chase > int(self.get_game_config(lybconstant.LYB_DO_STRING_DOGAM_INTERVAL)):
				if max_play_stance['value'] > 0.9:
					if max_play_stance['name'] == 'manual_play':
						if dogam_stance_index != 0:
							time.sleep(1)
							self.lyb_mouse_click('tera_main_scene_sudong', custom_threshold=0)
					elif max_play_stance['name'] == 'half_auto_play':
						if dogam_stance_index != 1:
							time.sleep(1)
							self.lyb_mouse_click('tera_main_scene_banjadong', custom_threshold=0)
					elif max_play_stance['name'] == 'auto_play':
						if dogam_stance_index != 2:
							time.sleep(1)
							self.lyb_mouse_click('tera_main_scene_jadong', custom_threshold=0)
					elif max_play_stance['name'] == 'tracking_match_rate':
						if dogam_stance_index != 3:
							time.sleep(1)
							self.lyb_mouse_click('tera_main_scene_tracking_icon_0', custom_threshold=0)
					else:
						pass
					time.sleep(1)
			else:
				self.loggingElapsedTime('[시간 체크] 태세 전환까지 남은 시간',
					elapsed_time_chase, int(self.get_game_config(lybconstant.LYB_DO_STRING_DOGAM_INTERVAL)))

		# print('DEBUG XX: ', self.status)
		if (	self.status == self.get_work_status('영웅 변경') or
				self.status == self.get_work_status('영웅 변경 - 솔') or
				self.status == self.get_work_status('영웅 변경 - 올렌더') or
				self.status == self.get_work_status('영웅 변경 - 레인') or
				self.status == self.get_work_status('영웅 변경 - 라브랭') or
				self.status == self.get_work_status('영웅 변경 - 리벨리아') or
				self.status == self.get_work_status('영웅 변경 - 리나') or
				self.status == self.get_work_status('영웅 변경 - 카야')
				):
			is_clicked = self.set_combat_stance(max_play_stance['name'], max_play_stance['value'], ['manual_play'])
			if is_clicked:
				hero_change_count = self.get_option('hero_change_count')
				if hero_change_count == None:
					hero_change_count = 0

				# print('hero_change_count', hero_change_count)
				if hero_change_count < 1:
					self.set_option('hero_change_count', hero_change_count + 1)
					return self.status
				else:
					self.set_option('hero_change_count', 0)

			# else:
			# 	self.set_option('end_flag', True)

		# print('[DEBUG] status:', self.status, 'work:', self.current_work)
		if self.status == 0:
			# print('schedule_list length:', len(self.schedule_list))
			# if len(self.schedule_list) == 0:
			# 	self.schedule_list.append('메인 퀘스트')

			self.status += 1

		elif self.status >= 1 and self.status < 1000:
			# s_list_iter = 0
			# s_list_number = len(self.schedule_list)

			if self.current_work != None:
				if self.current_work in self.move_status:
					self.status = self.move_status[self.current_work]
					self.move_status.pop(self.current_work)

			# if self.status > s_list_number:
			# 	self.status = s_list_number

			while True:
				# self.current_work = self.schedule_list[self.status - 1]
				# print('[DEBUG] callstack TEST XX S: current_work:', self.current_work, self.status)
				self.current_work = self.get_current_work()
				# print('[DEBUG] callstack TEST XX E: current_work:', self.current_work, self.status)
				if self.current_work == '게임 시작':
					pass
				elif self.current_work == '로그인':
					pass
				else:
					break
				self.status += 1
				# s_list_iter += 1
				# if s_list_iter > s_list_number:
				# 	break

			if len(self.callstack) == 0 and len(self.current_work) < 1:

				if self.get_option('schedule_done_enter') != True:
					self.set_option('schedule_done_enter', True)
					self.set_checkpoint('schedule_done')
				
				schedule_done_wait = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_REST))
				# print('LYB_DO_STRING_PERIOD_REST: ', schedule_done_wait)
				elapsed_time = time.time() - self.get_checkpoint('schedule_done')
				if elapsed_time < schedule_done_wait:
					self.loggingElapsedTime('[스케쥴링 ] 지정된 스케쥴 완료 후 대기 중', int(elapsed_time), schedule_done_wait)
					return self.status
				else:
					self.set_option('schedule_done_enter', False)

				is_multi_account = self.get_window_config('multi_account')
				if is_multi_account == True:
					#TODO: 접속 종료
					if self.get_option('hero_change_do') != True:
						self.logger.critical('다음 계정 작업을 위해 로그오프합니다')
						self.game_object.get_scene('tera_main_menu_scene').status = self.get_work_status('로그인')
						self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
						self.status = 0
					else:
						self.logger.warn('[영웅 변경] 이 완료되야 로그오프를 할 수 있습니다.')
						self.status = 1
				else:
					
					is_restart = self.get_game_config(lybconstant.LYB_DO_BOOLEAN_RESTART_GAME)
					if is_restart:
						self.logger.critical('[스케쥴링 ] 지정된 스케줄을 완료해서 게임을 종료합니다')
						self.game_object.terminate_application()
						self.status = 1000000
					else:
						if self.get_option('loop_start') == None:
							self.logger.critical('[스케쥴링 ] 지정된 스케줄을 완료해서 처음으로 돌아갑니다')							
							self.game_object.addStatistic(lybconstant.LYB_STATISTIC_0)
							# 반복
							self.status = 1
						else:
							self.logger.ciritical('[스케쥴링 ] 지정된 스케줄을 완료해서 [반복 시작]으로 돌아갑니다')
							self.status = self.get_option('loop_start')
					return self.status
			else:
				# 복잡하다. callstack 다시 구현해보자.
				# print('[DEBUG} callstack - scene status:', self.status, 'current_work:', self.current_work)
				schedule_number = self.status
				if len(self.callstack) > 0:
					schedule_number = self.status + 1

				self.set_work_status()

				if len(self.callstack) > 0:
					iterator_key = self.game_object.build_iterator_key(len(self.callstack)-1, self.callstack[-1])
					schedule_number = self.get_option(iterator_key)
				else:
					schedule_number = self.last_status[self.current_work] 
				
				log_callstack = ''

				if len(self.current_work) > 0:
					if len(self.callstack) > 0:

						prev_call = None	
						custom_config_dic = self.game_object.configure.window_config['custom_config_dic']
						stack_index = 0					
						for each_call in self.callstack:
							if prev_call != None:
								schedule_list = custom_config_dic[prev_call]['schedule_list']
							else:
								schedule_list = self.schedule_list
							log_callstack += ' ' + str(self.callstack_status[stack_index]) +'. '
							log_callstack += '[' + each_call + ']'
							prev_call = each_call
							stack_index += 1

						log_callstack += ' '
					else:
						log_callstack = ' '

					self.logger.critical('[스케쥴링 ]' + log_callstack + str(schedule_number) + '. ' + self.current_work)

					if self.game_object.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work') == True:
						default_text = '['+log_callstack + str(schedule_number) + '. ' + self.current_work+' ] '
						send_text = self.game_object.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work')
						if len(send_text) < 1:
							send_text = '작업 시작'

						self.game_object.telegram_send(default_text + send_text)

					# 몬스터 도감 작업 다음에 메인퀘스트면 시작이 안된다.
					if (	self.current_work == '메인 퀘스트' or
							self.current_work == '지역 퀘스트'
							):
						if tracking_match_rate > 0.7:
							self.lyb_mouse_click('tera_main_scene_tracking_icon_0', custom_threshold=0)
				return self.status
			self.status += 1
		elif self.status == self.get_work_status('메인 퀘스트') or self.status == self.get_work_status('메인 퀘스트') + 1:
			
			self.game_object.current_matched_scene['name'] = ''

			elapsed_time = self.get_elapsed_time()
			self.loggingElapsedTime('메인 퀘스트 경과 시간: ', 
				int(elapsed_time), 
				int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST)) * 60,
				period=30)

			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST)) * 60


			# print('hero_death:', self.get_option('hero_death'))

			if self.get_option('hero_death') == True:
				self.set_option('hero_death', False)
				self.set_option(self.current_work +'_end_flag', True)

			# 설정으로 빼자. 180
			if ( 	(elapsed_time > duration_limit) or
					self.get_option(self.current_work + '_end_flag') == True
				 ):
				
				self.logger.debug('경과 시간: ' + str(int(elapsed_time)) +':'+str(duration_limit))
				self.tolerance_weight_factor = 1
				self.threshold_weight_factor = 1
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1

				return self.status

			# skill_red = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_skill_red')
			# self.loggingToGUI('RED 매칭률: '+str(int(skill_red*100))+'%')
			# if skill_red > 0.9:
			# 	out_field = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_out_field')
			# 	self.loggingToGUI('FIELD OUT 매칭률: '+str(int(out_field*100))+'%')

			if self.status == self.get_work_status('메인 퀘스트'):
				self.status = self.get_work_status('메인 퀘스트') + 1
			else:
				self.status = self.get_work_status('메인 퀘스트')

		elif (	self.status == self.get_work_status('요일 던전') or
				self.status == self.get_work_status('독립군 장비 보급') or
				self.status == self.get_work_status('무한의 탑') or
				self.status == self.get_work_status('블가메시의 훈련') or
				self.status == self.get_work_status('황금 거인 강탈') or
				self.status == self.get_work_status('독립군 보급 기지') or
				self.status == self.get_work_status('후카족 마을 수복전') or
				self.status == self.get_work_status('밤피르의 저택') or
				self.status == self.get_work_status('달의 호수 쟁탈전') or
				self.status == self.get_work_status('황금의 미궁') or
				self.status == self.get_work_status('왕자의 궁전') or
				self.status == self.get_work_status('불의 제단') or
				self.status == self.get_work_status('벤튤라') or
				self.status == self.get_work_status('데미안') or
				self.status == self.get_work_status('그림자 기수') or
				self.status == self.get_work_status('굴') or
				self.status == self.get_work_status('티라누스') or
				self.status == self.get_work_status('라우라바') or
				self.status == self.get_work_status('고대 던전 입구') or
				self.status == self.get_work_status('고대 던전 1구역') or
				self.status == self.get_work_status('고대 던전 2구역') or
				self.status == self.get_work_status('카이아의 던전')

				):
			# (temp_name, match_rate) = self.get_current_area()
			# print('[DEBUG] DungeonArea:', temp_name, match_rate)
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if self.get_checkpoint(self.current_work + '_check_start_each') == 0:
				elapsed_time_each = 0
			else:
				elapsed_time_each = time.time() - self.get_checkpoint(self.current_work + '_check_start_each')
				
			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DUNGEON)) * 60
			# duration_limit_each = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH)) * 60

			# self.loggingElapsedTime(self.current_work +' 개별 경과 시간', elapsed_time_each, duration_limit_each)
			# self.loggingElapsedTime(self.current_work +' 전체 경과 시간', elapsed_time, duration_limit)

			# print(str(time.strftime('%H:%M:%S', time.gmtime(int(time.time())))), self.current_work, self.get_option(self.current_work + '_end_flag'))

			if ( 	self.get_option(self.current_work + '_end_flag') == True
				):
				# area_name = self.current_work.replace(' ','',10)
				# (temp_name, match_rate) = self.get_current_area()

				# if area_name != temp_name.replace('tera_area_', '', 1).replace('_loc', '', 1):
				self.logger.debug('DungeonEndFlag: ' + str(self.current_work) + 
					'F:' + str(self.get_option(self.current_work + '_dungeon_end')) +
					'Each:' + str(self.get_checkpoint(self.current_work + '_check_start_each')))
				defense_checkpoint = self.get_option('defense_checkpoint')
				if defense_checkpoint == None:
					self.set_option('defense_checkpoint', time.time())
				else:
					if time.time() - defense_checkpoint > 300:
						self.set_option(self.current_work + '_dungeon_end', True)

				if self.get_option(self.current_work + '_dungeon_end') != False:
					# print('[DEBUG] DungeonArea:', area_name, 'CurrentArea:', temp_name)
					self.set_option(self.current_work + '_end_flag', False)
					self.set_option(self.current_work + '_end', False)
					self.set_option(self.current_work + '_dungeon_done', False)
					self.set_option('defense_checkpoint', None)
					self.checkpoint[self.current_work + '_check_start_each'] = 0
					self.status = self.last_status[self.current_work] + 1

				return self.status

			# terminate_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_LIMIT_DUNGEON)) * 60
			# print('terminate_limit',terminate_limit)

			# if elapsed_time_each > duration_limit_each:
			# 	self.loggingToGUI('던전 개별 제한 시간을 초과했기 때문에 프로그램을 종료합니다.')
			# 	self.loggingToGUI('제한 시간: '+ str(duration_limit) +
			# 		' 경과 시간: '+str(int(elapsed_time)))
			# 	self.game_object.terminate_application()
			# 	return 1000000

			# if elapsed_time > duration_limit:
			# 	self.loggingToGUI('던전 스케쥴 제한 시간을 초과했기 때문에 프로그램을 종료합니다.')
			# 	self.loggingToGUI('제한 시간: '+ str(duration_limit) +
			# 		' 경과 시간: '+str(int(elapsed_time)))
			# 	self.game_object.terminate_application()
			# 	return 1000000

			# print(self.current_work + '_dungeon_done', self.get_option(self.current_work + '_dungeon_done'))

			if self.get_option(self.current_work + '_dungeon_done') != True:

				if elapsed_time > duration_limit:
					self.logger.info(self.current_work + ' 완료')
					self.set_option(self.current_work + '_end_flag', True)
				else:
					self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
					self.set_option(self.current_work + '_dungeon_end', False)
					self.game_object.get_scene('tera_main_menu_scene').status = self.status
			else:
				if self.get_option(self.current_work + '_dungeon_end') != True:
					self.game_object.interval = float(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON))
					# self.loggingElapsedTime('현재 ' + self.current_work + ' 진행 중입니다. 경과 시간:', elapsed_time, duration_limit, period=10)
					# self.use_skill()
					# self.use_skill2()
				else:
					self.logger.info(self.current_work + ' 완료')
					self.set_option(self.current_work + '_end_flag', True)


		elif (	self.status == self.get_work_status('소모품 상자 열기') or
				self.status == self.get_work_status('자동 장착') or
				self.status == self.get_work_status('일괄 판매') or
				self.status == self.get_work_status('가슴 레벨업') or
				self.status == self.get_work_status('무기 레벨업') or
				self.status == self.get_work_status('신발 레벨업') or
				self.status == self.get_work_status('장갑 레벨업') or
				self.status == self.get_work_status('목걸이 레벨업') or
				self.status == self.get_work_status('반지 레벨업') or
				self.status == self.get_work_status('팔찌 레벨업') or
				self.status == self.get_work_status('귀걸이 레벨업') or
				self.status == self.get_work_status('장비 세트')or
				self.status == self.get_work_status('경험치 부스터 사용')or
				self.status == self.get_work_status('골드 부스터 사용')
				):

			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			self.logger.debug(str(self.current_work) + ', ' + str(elapsed_time) + ', ' + str(self.get_option(self.current_work + '_end_flag')))
			if ( 	elapsed_time > self.period_bot(10)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				# if self.get_option('full_inventory') == True:
				# 	self.status = self.last_status['full_inventory']
				# 	self.current_work = self.get_option('full_inventory_last_current_work')
				# 	self.set_option('full_inventory', False)
				# else:
				self.status = self.last_status[self.current_work] + 1

				return self.status

			# rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_inventory')
			# self.loggingToGUI('가방 아이콘 매칭률: '+str(int(rate_match*100))+'%')
			rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_inventory_full')
			if rate_match > 0.7:
				self.logger.debug('가방 아이콘 가득 참 매칭률: '+str(int(rate_match*100))+'%')

			
			is_clicked = self.lyb_mouse_click('tera_main_scene_inventory')
			if is_clicked == False:
				is_clicked = self.lyb_mouse_click('tera_main_scene_inventory_full')
			self.game_object.get_scene('tera_inventory_scene').status = self.get_work_status(self.current_work)

		elif (	self.status == self.get_work_status('무기 레벨업 - 대장간') or
				self.status == self.get_work_status('방어구 레벨업 - 대장간') or
				self.status == self.get_work_status('장신구 레벨업 - 대장간')
				):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(30):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if elapsed_time < self.period_bot(5):
				rate_match = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_inventory_full')
				if rate_match > 0.7:
					self.logger.debug('가방 아이콘 가득 참 매칭률: '+str(int(rate_match*100))+'%')

				
				is_clicked = self.lyb_mouse_click('tera_main_scene_inventory')
				if is_clicked == False:
					is_clicked = self.lyb_mouse_click('tera_main_scene_inventory_full')

				self.game_object.get_scene('tera_inventory_scene').status = self.status
			else:
				self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
				self.game_object.get_scene('tera_main_menu_scene').status = self.status


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
				
		elif self.status == self.get_work_status('[정예]'):

			self.status = self.last_status[self.current_work] + 1
			self.set_option('elite_mode', True)

		elif self.status == self.get_work_status('[일반]'):

			self.status = self.last_status[self.current_work] + 1
			self.set_option('elite_mode', False)

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

		elif (	self.status == self.get_work_status('임무 보상') or
				self.status == self.get_work_status('업적 보상') or
				self.status == self.get_work_status('영웅 변경') or
				self.status == self.get_work_status('영웅 변경 - 솔') or
				self.status == self.get_work_status('영웅 변경 - 올렌더') or
				self.status == self.get_work_status('영웅 변경 - 레인') or
				self.status == self.get_work_status('영웅 변경 - 라브랭') or
				self.status == self.get_work_status('영웅 변경 - 리벨리아') or
				self.status == self.get_work_status('영웅 변경 - 리나') or
				self.status == self.get_work_status('영웅 변경 - 카야') or
				self.status == self.get_work_status('지하 결투장')
				# self.status == self.get_work_status('카이아의 전장')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(60)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
			self.game_object.get_scene('tera_main_menu_scene').status = self.status


		elif (	self.status == self.get_work_status('경험치 부스터 구매') or
				self.status == self.get_work_status('골드 부스터 구매')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time >  self.period_bot(10)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			# print('[DEBUG] shop exp 1:', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1))
			# print('[DEBUG] shop exp 2:', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2))
			# print('[DEBUG] shop exp 5:', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5))
			# print('[DEBUG] shop gold 1:', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1))
			# print('[DEBUG] shop gold 2:', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2))
			# print('[DEBUG] shop gold 5:', self.get_game_config(lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5))
			self.lyb_mouse_click('tera_main_scene_shop', custom_threshold=0)
			self.game_object.get_scene('tera_summon_scene').status = self.status

		elif (	self.status == self.get_work_status('무료 소환') 
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time >  self.period_bot(10)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_shop', custom_threshold=0)
			self.game_object.get_scene('tera_summon_scene').status = self.status

		elif (	self.status == self.get_work_status('이벤트 보상')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(5) or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_event', custom_threshold=0)

		elif (	self.status == self.get_work_status('보상 회수')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
			self.game_object.get_scene('tera_main_menu_scene').status = self.status

		elif (	self.status == self.get_work_status('우편함')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_mail', custom_threshold=0)
		elif self.status == self.get_work_status('[작업 예약]'):

			self.logger.debug('[작업 예약]')
			self.game_object.wait_for_start_reserved_work = False
			self.status = self.last_status[self.current_work] + 1

		elif self.status == self.get_work_status('채널 변경'):

			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if (	elapsed_time > self.period_bot(300) or
					self.get_option(self.current_work + '_end_flag') == True
					):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_change_channel', custom_threshold=0)

		elif (	self.status == self.get_work_status('몬스터 추적') or
				self.status == self.get_work_status('몬스터 추적') + 1
				):
			elapsed_time = self.get_elapsed_time()
			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE)) * 60

			if ( 	(elapsed_time > duration_limit) or
					self.get_option(self.current_work + '_end_flag') == True
				 ):
				
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('chase_monster_commit', False)
				self.status = self.last_status[self.current_work] + 1

				return self.status

			if self.get_option('chase_monster_commit') == True:
				self.loggingElapsedTime('몬스터 추적 작업 경과 시간', int(elapsed_time), duration_limit)
				if self.status == self.get_work_status('몬스터 추적'):
					self.status = self.get_work_status('몬스터 추적') + 1
				else:
					self.status = self.get_work_status('몬스터 추적')
			else:
				if self.is_open_map() == True:
					self.lyb_mouse_click('tera_main_scene_show_map', custom_threshold=0)
				else:
					self.lyb_mouse_click('tera_main_scene_plus', custom_threshold=0)

				self.game_object.get_scene('tera_world_map_local_scene').status = self.get_work_status('몬스터 추적')

		elif (	self.status == self.get_work_status('보스 퀘스트') or
				self.status == self.get_work_status('보스 퀘스트') + 1
				):
			elapsed_time = self.get_elapsed_time()
			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST)) * 60
			duration_boss_kill = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS)) *60
			self.loggingElapsedTime('보스 퀘스트 경과 시간: ', int(elapsed_time), duration_limit)
			last_boss_kill_time = int(time.time() - self.get_checkpoint('boss_kill_success'))
			self.logger.debug('최근 보스 킬 경과 시간: ' + str(last_boss_kill_time) + '/' + str(duration_boss_kill) + '초')

			if ( 	elapsed_time > duration_limit or
					last_boss_kill_time < duration_boss_kill or
					self.get_option(self.current_work + '_end_flag') == True
				 ):
				
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1

				return self.status

			if self.status == self.get_work_status('보스 퀘스트'):
				self.status = self.get_work_status('보스 퀘스트') + 1
			else:
				self.status = self.get_work_status('보스 퀘스트')

		elif self.status == self.get_work_status('지역 이동'):

			elapsed_time = self.get_elapsed_time()
			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA))
			# print('[DEBUG]::::::', self.get_option(self.current_work + '_end_flag'), self.current_work)

			if ( 	(elapsed_time > duration_limit) or
					self.get_option(self.current_work + '_end_flag') == True
				 ):
				
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('move_local', False)
				self.status = self.last_status[self.current_work] + 1

				return self.status

			if self.get_option('move_local') == True:
				self.loggingElapsedTime('지역 이동('+self.get_game_config(lybconstant.LYB_DO_STRING_SUB_AREA)+') 작업 경과 시간:', 
					int(elapsed_time),	duration_limit, period=5)


				if self.game_object.get_scene('tera_world_map_local_scene').get_option('current_area') != None:
					landing_area_name = self.get_game_config(lybconstant.LYB_DO_STRING_SUB_AREA).replace(' ', '', 10)
					current_area_name = self.game_object.get_scene('tera_world_map_local_scene').get_option('current_area').replace('tera_area_', '', 1).replace('_loc', '', 1)
					current_area_rate = self.game_object.get_scene('tera_world_map_local_scene').get_option('current_area_rate')

					if landing_area_name in current_area_name:
						self.logger.debug('지역 도착('+landing_area_name+')')
						self.set_option(self.current_work + '_end_flag', True)
						return self.status
				
				# (current_area, current_area_rate) = self.get_current_area()

				# landing_area_name = self.get_game_config(lybconstant.LYB_DO_STRING_SUB_AREA).replace(' ', '', 10)
				# current_area_name = current_area.replace('tera_area_', '', 1).replace('_loc', '', 1)

				if self.is_open_map() == True:
					self.lyb_mouse_click('tera_main_scene_show_map', custom_threshold=0)
					self.game_object.get_scene('tera_world_map_local_scene').status = 777
				else:
					self.lyb_mouse_click('tera_main_scene_plus', custom_threshold=0)

			else:
				if self.is_open_map() == True:
					self.logger.info('[' + 
						self.get_game_config(lybconstant.LYB_DO_STRING_SUB_AREA) + '] 이동합니다.')
					self.lyb_mouse_click('tera_main_scene_show_map', custom_threshold=0)
					self.game_object.get_scene('tera_world_map_local_scene').status = self.status
					self.game_object.get_scene('tera_world_map_scene').status = self.status
				else:
					self.lyb_mouse_click('tera_main_scene_plus', custom_threshold=0)

		elif self.status == self.get_work_status('지역 퀘스트'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(600):
				self.set_option(self.current_work + '_end_flag', True)
			
			if int(elapsed_time) % 10 < 2:
				self.game_object.current_matched_scene['name'] = ''

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				self.set_option('jiyuk_quest_found', False)
				self.set_option('jiyuk_quest_accept', False)
				self.set_option('jiyuk_quest_drag_count', 0)
				return self.status

			if self.get_option('jiyuk_quest_accept') != True:
				loc_x, loc_y = self.loc_jiyuk_quest()
				self.game_object.get_scene('tera_uregesipan_scene').status = self.status
				if self.get_option('jiyuk_quest_found') != True:
					jiyuk_quest_drag_count = self.get_option('jiyuk_quest_drag_count')
					if jiyuk_quest_drag_count == None:
						jiyuk_quest_drag_count = 0

					if jiyuk_quest_drag_count > 1:
						self.lyb_mouse_drag('tera_main_scene_quest_drag_top', 'tera_main_scene_quest_drag_bottom')
						self.set_option(self.current_work + '_end_flag', True)
						self.logger.warn('[인식 실패] [지역] 퀘스트가 리스트에 있다면 [수동] 태세에서 시작해주세요')
						return self.status

					if loc_x == -1:
						self.set_option('jiyuk_quest_drag_count', jiyuk_quest_drag_count + 1)
						self.lyb_mouse_drag('tera_main_scene_quest_drag_bottom', 'tera_main_scene_quest_drag_top')
						self.game_object.interval = self.period_bot(2)
					else:
						self.logger.debug('[클릭 성공] [지역] 퀘스트 ' + str((loc_x, loc_y)))
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.set_option('jiyuk_quest_found', True)
						self.game_object.interval = self.period_bot(2)
				else:
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
					self.game_object.interval = self.period_bot(2)


		elif self.status == self.get_work_status('랜덤 퀘스트'):
			
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			loc_x, loc_y = self.loc_random_quest()
			if loc_x != -1:
				self.logger.debug('[클릭 성공] [랜덤] 퀘스트 ' + str((loc_x, loc_y)))
				self.set_tutorial(True)
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.logger.warn('랜덤 퀘스트를 찾지 못했습니다.')
				self.set_option(self.current_work + '_end_flag', True)
		
		elif (	self.status == self.get_work_status('우정 포인트') or
				self.status == self.get_work_status('친구 관리')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_friend', custom_threshold=0)
			self.game_object.get_scene('tera_friend_scene').status = self.status

		elif (	self.status == self.get_work_status('영웅 특성') or
				self.status == self.get_work_status('영웅 스킬')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_hero_icon', custom_threshold=0)
			self.game_object.get_scene('tera_manage_hero_scene').status = self.status
		elif (	self.status == self.get_work_status('친밀도') or
				self.status == self.get_work_status('글로리아로 이동') or
				self.status == self.get_work_status('아이샤로 이동') or
				self.status == self.get_work_status('오르단으로 이동') or
				self.status == self.get_work_status('블가메시로 이동')or
				self.status == self.get_work_status('야몽으로 이동')
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')
			if ( 	elapsed_time > self.period_bot(1800)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			check_time = int(elapsed_time) % 30
			if ( self.game_object.get_scene('tera_hero_information_scene').get_option('running') != True or
				check_time >= 0 and check_time <= 5 ): 
				self.lyb_mouse_click('tera_main_scene_level', custom_threshold=0)
				self.game_object.get_scene('tera_hero_information_scene').status = self.status

		elif self.status == self.get_work_status('몬스터 도감'):
			elapsed_time = self.get_elapsed_time()
			last_check_time = self.get_checkpoint('last_dogam_check_time')

			duration_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM)) * 60
			check_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK))

			if last_check_time != 0:
				self.loggingElapsedTime('[시간 체크] 몬스터 도감 진행 중', elapsed_time, duration_limit)
				self.loggingElapsedTime('[시간 체크] 몬스터 도감 다음 체크 시간', time.time() - last_check_time, check_time)

			if ( 	elapsed_time > duration_limit or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				self.checkpoint['last_dogam_check_time'] = 0
				self.game_object.get_scene('tera_monster_dogam_scene').status = 0
				self.set_option('dogam_opened', False) 
				return self.status

			if (	time.time() - last_check_time > check_time or
					self.get_option('dogam_opened') != True 
					):
				self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
				self.set_checkpoint('last_dogam_check_time')
				self.game_object.get_scene('tera_main_menu_scene').status = self.status

		elif (	self.status == self.get_work_status('길드 출석') or
				self.status == self.get_work_status('길드 보상') or
				self.status == self.get_work_status('길드 업적') or
				self.status == self.get_work_status('길드 기부') or
				self.status == self.get_work_status('길드 마을') or
				self.status == self.get_work_status('길드 상점 - 경험치') or
				self.status == self.get_work_status('길드 상점 - 대량의 경험치') or
				self.status == self.get_work_status('길드 스킬') 
				):
			if self.get_checkpoint(self.current_work + '_check_start') == 0:
				elapsed_time = 0
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_check_start')

			if ( 	elapsed_time > self.period_bot(5)  or
					self.get_option(self.current_work + '_end_flag') == True
				):
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
			self.game_object.get_scene('tera_main_menu_scene').status = self.status

		elif self.status == self.get_work_status('나가기'):

			self.lyb_mouse_click('tera_main_scene_out_field', custom_threshold=0)
			self.status = self.last_status[self.current_work] + 1

		elif self.status == self.get_work_status('알림'):

			self.logger.debug('알림 전송:' + str(self.get_game_config(lybconstant.LYB_DO_STRING_NOTIFY_MESSAGE)))
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

		elif (	self.status == self.get_work_status('설정 - 파티 초대 거절')
				):
			elapsed_time = self.get_elapsed_time()

			if elapsed_time > self.period_bot(10):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('tera_main_scene_menu', custom_threshold=0)
			self.game_object.get_scene('tera_main_menu_scene').status = self.status

		elif self.status == self.get_work_status('파티원에게 이동'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			party_member_index = int(self.get_game_config(lybconstant.LYB_DO_STRING_PARTY_LOC)) - 1
			self.logger.debug(str(party_member_index) + '번 파티원에게 이동')

			self.lyb_mouse_click('tera_main_scene_party_' + str(party_member_index), custom_threshold=0)
			self.game_object.get_scene('tera_party_member_scene').status = self.status
		else:
			self.status = self.last_status[self.current_work] + 1

		return self.status





























































































































































	def is_new_event_bosang(self):
		cfg_check_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period'))
		if cfg_check_period != 0:
			elapsed_time = time.time() - self.get_checkpoint('last_check_event')
			if elapsed_time > cfg_check_period:
				self.set_checkpoint('last_check_event')
				pb_name = 'main_scene_event_new'
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_top_level=(255, 140, 60),
								custom_below_level=(200, 15, 10),
								custom_flag=1,
								custom_rect=(10, 80, 150, 110)
								)
				self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(int(match_rate*100)) + '%')
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y + 10)
					return True

		return False

	def tera_create_charater_scene(self):
		# self.loggingToGUI('자동으로 캐릭터를 생성할 순 없습니다. [' + str(self.window_title) + '] 작업을 종료합니다.')

		return 0

	def nox_init_screen_scene(self):
		
		self.schedule_list = self.get_game_config('schedule_list')
		if not '게임 시작' in self.schedule_list:
			return 0


		loc_x = -1
		loc_y = -1


		if self.game_object.player_type == 'nox':
			for each_icon in lybgameTera.LYBTera.nox_tera_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				self.logger.debug('NoxTeraIcon: ' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.logger.debug('녹스 테라 아이콘 클릭해서 게임 시작. 아이콘 위치: '+str((loc_x, loc_y)))
					break
		elif self.game_object.player_type == 'momo':
			for each_icon in lybgameTera.LYBTera.momo_tera_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
								)
				self.logger.debug('MomoTeraIcon: ' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.logger.debug('모모 테라 아이콘 클릭해서 게임 시작. 아이콘 위치: '+str((loc_x, loc_y)))
					break

		# if loc_x == -1:
		# 	self.loggingToGUI('테라 아이콘 발견 못함')

		return 0

	def logon_screen_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		
		if not '로그인' in self.schedule_list:
			return 0

		if time.time() - self.get_checkpoint('wait_finding_account') > 30:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('wait_finding_account')
			if self.get_window_config('multi_account'):
				self.logger.debug('구글 계정 변경 시도')
				
			self.status += 1
		elif self.status == 1:
			if time.time() - self.get_checkpoint('wait_finding_account') > 100:
				self.logger.warn('구글 계정 감지 실패')
				return -1

			if self.get_window_config('multi_account'):
				self.logger.debug('google multi account On')
				rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'account_change_icon', custom_tolerance=50)
				self.logger.debug('change icon: ' + str(int(rate*100)) +'%')
				is_there = self.lyb_mouse_click('account_change_icon', custom_tolerance=50, custom_threshold=0)
				self.logger.debug('account change is clicked: ' + str(is_there))
				if is_there:
					self.status = 2
					self.set_option('load_complete_flag', False)
			else:	
				self.status = 3
		elif self.status == 2:
			self.logger.debug('wait for loading account select')
			if self.get_option('load_complete_flag'):
				self.set_option('load_complete_flag', False)
				self.status = 3
			else:
				self.status = 1
		elif self.status == 3:
			self.lyb_mouse_click_location(320, 330)
			self.logger.debug('게임 로고 화면 터치')
			self.status +=1
		elif self.status == 4:
			self.status -= 1

		return self.status

	def connect_account_scene(self):
		if self.status == 0:
			self.set_checkpoint('interval_login')
			self.status += 1
		elif self.status == 1:

			self.logger.debug('select_complete_flag: ' + str(self.get_option('select_complete_flag')))
			if (self.get_option('select_complete_flag') == True or 
				time.time() - self.get_checkpoint('interval_login') > 100):
				self.lyb_mouse_click('connect_account_close_icon')
				self.game_object.get_scene('logon_screen_scene').set_option('load_complete_flag', True)
				self.set_option('select_complete_flag', False)
				self.status = 0
			else:
				# 회색
				# print('DEBUG 00')
				is_logff_status = self.lyb_mouse_click('google_login_letter_0', custom_threshold=0.9)
				if not is_logff_status:
					# print('DEBUG 11')
					# 파란색
					self.lyb_mouse_click('google_login_icon', custom_threshold=0)
				else:
					# print('DEBUG 12')
					self.set_option('select_complete_flag', False)

		return self.status

	def google_play_account_select_scene(self):
		(top_loc_x, top_loc_y) = lybgame.LYBGame.locationOnWindow(
			self.window_image, 
			self.game_object.resource_manager.pixel_box_dic['google_play_letter']
			)
		self.logger.debug('구글 계정 기준점: ' + str((top_loc_x, top_loc_y)))
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
				self.logger.debug('구글 계정 5개 이상 감지됨')
			else:
				self.logger.debug('구글 계정 '+str(self.google_account_number)+'개 감지됨')

		self.logger.debug('google account DEBUG:' + str(self.status) + ', ' + str(self.google_account_number))
		if self.status >= self.google_account_number:
			self.status = 0		
			self.logger.debug(str(self.google_account_number)+' 개의 계정 작업 완료')	
			return -1
		else:
			self.logger.debug(str(self.status + 1)+' 번째 구글 계정 로그인 시도')
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

				self.logger.debug(str(from_x, from_y, to_x, to_y))
				for i in range(self.status - 4):
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
					self.logger.warn(str(self.status + 1)+' 번째 구글 계정 감지 실패')
					self.logger.debug('총 '+str(self.status)+' 개의 계정 작업 완료')
					return -1

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












	# def get_current_area(self):
	# 	area_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_AREA_THRESHOLD))
	# 	max_match = { 'name' : '', 'rate' : 0 }

	# 	if (	self.get_option('max_matched_area_name') != None and
	# 			self.get_option('max_matched_area_rate') != None
	# 			):

	# 		area_match = self.game_object.rateMatchedResource(
	# 							self.window_pixels,
	# 							self.get_option('max_matched_area_name'),
	# 							custom_below_level=area_threshold
	# 						)
	# 		if area_match > 0.9 and abs(area_match - self.get_option('max_matched_area_rate')) < 0.1:
	# 			return (self.get_option('max_matched_area_name'), self.get_option('max_matched_area_rate'))

	# 	for resource_name, resource in self.game_object.resource_manager.resource_dic.items():
	# 		if '_area_loc' in resource_name:
	# 			area_match = self.game_object.rateMatchedResource(
	# 								self.window_pixels,
	# 								resource_name,
	# 								custom_below_level=area_threshold
	# 							)
	# 			print('[', resource_name, ']:', round(area_match,3), ' ::: ', area_threshold)
	# 			if area_match > max_match['rate']:
	# 				max_match['name'] = resource_name
	# 				max_match['rate'] = area_match

	# 	self.set_option('max_matched_area_name', max_match['name'])
	# 	self.set_option('max_matched_area_rate', max_match['rate'])

	# 	return (max_match['name'], max_match['rate'])

	def get_current_area2(self):
		for resource_name, resource in self.game_object.resource_manager.resource_dic.items():
			if (	'tera_area2_' in resource_name and
					resource.resource_type == 'location'
					): 
				match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
				if match_rate > 0.9:
					return resource_name, match_rate

		return ('', 0)

	def get_current_area(self, custom_rect=(510, 30, 638, 60)):
		area_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_AREA_THRESHOLD)) * 0.01
		if area_threshold > 0.8:
			area_threshold = 0.8

		# print('S -- tera_boss_use_dealer_skill::::')

		if (	self.get_option('max_matched_area_name') != None and
				self.get_option('max_matched_area_rate') != None
				):

			(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										self.get_option('max_matched_area_name'),
										custom_below_level=(100, 100, 100),
										custom_top_level=(255,255,255),
										custom_threshold=area_threshold,
										custom_flag=1,
										custom_rect=custom_rect
										)

			# print('match_rate:', match_rate, abs(match_rate - self.get_option('max_matched_area_rate')))
			if loc_x != -1:
				if match_rate > area_threshold and abs(match_rate - self.get_option('max_matched_area_rate')) < 0.1:
					self.set_option('max_matched_area_rate', match_rate)
					return (self.get_option('max_matched_area_name'), self.get_option('max_matched_area_rate'))

		max_match_rate = 0
		match_area = ''

		for resource_name, resource in self.game_object.resource_manager.resource_dic.items():
			if (	'tera_area_' in resource_name and
					resource.resource_type == 'location'
					): 
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										resource_name,
										custom_below_level=(150, 150, 150),
										custom_top_level=(255,255,255),
										custom_threshold=area_threshold,
										custom_flag=1,
										custom_rect=(500,30,638,60)
										)

				if loc_x != -1:
					if max_match_rate < match_rate:
						max_match_rate = match_rate
						match_area = resource_name

		if match_area != '':
			self.set_option('max_matched_area_name', match_area)
			self.set_option('max_matched_area_rate', max_match_rate)

			self.logger.debug('[지역 체크] '+ 
				match_area.replace('tera_area_', '', 1).replace('_loc', '', 1) +
				' '+str(int(max_match_rate*100))+'%')

		return (match_area, max_match_rate)

	def get_tutorial(self):
		return self.game_object.get_tutorial()

	def set_tutorial(self, flag):
		self.game_object.set_tutorial(flag)

	def is_main_quest(self):
		if self.status == self.get_work_status('메인 퀘스트') or self.status == self.get_work_status('메인 퀘스트') + 1:
			return True
		else:
			return False

	def is_boss_quest(self):
		if self.status == self.get_work_status('보스 퀘스트') or self.status == self.get_work_status('보스 퀘스트') + 1:
			return True
		else:
			return False

	def is_full_inventory(self):
		full_icon = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_inventory_full', custom_tolerance=80)
		# self.loggingToGUI('가방 가득참 매칭률: '+str(int(full_icon*100))+'%')

		if full_icon > 0.8:
			return True
		else:
			return False

	def is_open_map(self):
		show_map = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_show_map', custom_tolerance=80)
		# self.loggingToGUI('지도 보기 매칭률: '+str(int(show_map*100))+'%')

		if show_map > 0.9:
			return True

		show_npc = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tera_main_scene_show_npc', custom_tolerance=80)
		# self.loggingToGUI('NPC 보기 매칭률: '+str(int(show_npc*100))+'%')

		if show_npc > 0.9:
			self.lyb_mouse_click('tera_main_scene_map_tab', custom_threshold=0)
			return True
		else:
			return False










	def loc_quest(self):
		# self.loc_boss_quest()
		# self.loc_random_quest()

		loc_x, loc_y = self.loc_main_quest()
		if loc_x != -1:
			return (loc_x, loc_y)

		loc_x, loc_y = self.loc_sub_quest()
		if loc_x != -1:
			return (loc_x, loc_y)

		loc_x, loc_y = self.loc_complete_quest()
		if loc_x != -1:
			return (loc_x, loc_y)

		loc_x, loc_y = self.loc_challenge_quest()
		if loc_x != -1:
			return (loc_x - 50, loc_y)

		loc_x, loc_y = self.loc_dungeon_quest()
		if loc_x != -1:
			return (loc_x - 50, loc_y)

		loc_x, loc_y = self.loc_tobul_quest()
		if loc_x != -1:
			return (loc_x - 50, loc_y)

		loc_x, loc_y = self.loc_level_quest()

		return (loc_x, loc_y)

	def loc_dungeon(self):

		loc_x, loc_y = self.loc_challenge_quest()
		if loc_x != -1:
			return (loc_x - 50, loc_y)

		loc_x, loc_y = self.loc_dungeon_quest()
		if loc_x != -1:
			return (loc_x - 50, loc_y)

		loc_x, loc_y = self.loc_complete_quest()
		if loc_x != -1:
			return (loc_x, loc_y)

		loc_x, loc_y = self.loc_tobul_quest()
		if loc_x != -1:
			return (loc_x - 50, loc_y)		

		return (loc_x, loc_y)

	def loc_main_quest(self):
		# Yellow '메인'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_main',
					color='yellow'
					)

	def loc_boss_quest(self):
		# Yellow '메인'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_boss',
					color='yellow'
					)


	def loc_sub_quest(self):
		# White '서브'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_sub'
					)

	def loc_complete_quest(self):
		# Yellow '완료'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_complete', 
					color='yellow'
					)	

	def loc_challenge_quest(self):
		# Green '도전'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_challenge', 
					color='green'
					)

	def loc_dungeon_quest(self):
		# White '지역'
		return self.loc_main_scene_quest(
					'tera_main_scene_dungeon'
					)

	def loc_talent_quest(self):
		# White '특성'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_talent'
					)

	def loc_skill_quest(self):
		# White '스킬'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_skill'
					)

	def loc_bosang_quest(self):
		# White '보상'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_bosang'
					)

	def loc_equip_quest(self):
		# White '장비'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_equip'
					)

	def loc_buhal_quest(self):
		# White '보상'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_buhal'
					)

	def loc_jiyuk_quest(self):
		# White '지역'
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_jiyuk'
					)

	def loc_tobul_quest(self):
		return self.loc_main_scene_quest(
					'tera_main_scene_tobul',
					color='red'
					)

	def loc_level_quest(self):
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_level',
					color='orange'
					)

	def loc_random_quest(self):
		return self.loc_main_scene_quest(
					'tera_main_scene_quest_random',
					color='green'
					)

	def loc_main_scene_quest(self, pixel_box_name, color='white'):
		threshold_main_quest_loc = int(self.get_game_config(lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD)) * 0.01

		if color == 'green':
			custom_below_level=(40, 110, 40)
			custom_top_level=(90, 190, 90)
		elif color == 'yellow':
			custom_below_level=(130, 120, 20)
			custom_top_level=(255, 200, 100)
		elif color == 'red':
			custom_below_level=(130, 50, 60)
			custom_top_level=(190, 90, 120)
		elif color == 'orange':
			custom_below_level=(140, 70, 0)
			custom_top_level=(255, 130, 40)
		else:
			custom_below_level=(100, 100, 100)
			custom_top_level=(255, 255, 255)

		s_time = time.time()
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pixel_box_name],
								custom_below_level=custom_below_level,
								custom_top_level=custom_top_level,
								custom_threshold=threshold_main_quest_loc,
								custom_flag=1,
								custom_rect=(600, 55, 640, 180)
								)
		e_time = time.time()
		# print('[DEBUG]', pixel_box_name, (loc_x, loc_y), '[', int(match_rate*100), ']', e_time - s_time)
		# print('[DEBUG] Elapsed Time QUEST:', e_time - s_time)

		return (loc_x, loc_y)	



	def update_skill_time(self):

		# print('[DEBUG] HP2', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2))
		# print('[DEBUG] HP3', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3))
		# for i in range(4):
		# 	print('[DEBUG] PARTY2 MEMBER'+str(i), self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + str(i)))
		
		s = time.time()
		hero_hp_percent = self.hero_hp()
		if hero_hp_percent != None:
			self.game_object.get_scene('tera_main_scene').set_option('hero_current_hp', hero_hp_percent)
		else:
			self.game_object.get_scene('tera_main_scene').set_option('hero_current_hp', '')

		target_hp_percent = self.target_hp()
		if target_hp_percent != None:
			self.game_object.get_scene('tera_main_scene').set_option('target_current_hp', target_hp_percent)
		else:
			self.game_object.get_scene('tera_main_scene').set_option('target_current_hp', '')

		party_member_hp_list = self.party_member_hp()

		is_clicked_skill = self.use_skill2()

		if is_clicked_skill == True:
			return 
		# print('[DEBUG] - CHECK', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP))

		# hero_hp_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP))

				
		e = time.time()
		# print('[DEBUG] Elapsed Time SKILL:', round(e - s, 4))

		global_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL))
		cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL))
		cooltime_1 = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1))
		cooltime_2 = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2))

		if hero_hp_percent != None:
			if hero_hp_percent < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP)):
				if (	time.time() - self.get_checkpoint('hero_skill_0') > self.period_bot(cooltime) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[궁극 사용] 발동 사유 - 영웅 HP: ' + str(hero_hp_percent) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_0', custom_threshold=0)
					self.set_checkpoint('hero_skill_0')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return

			if hero_hp_percent < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2)):
				if (	time.time() - self.get_checkpoint('hero_skill_1') >  self.period_bot(cooltime_1) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[도발/평정 사용] 발동 사유 - 영웅 HP: ' + str(hero_hp_percent) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_1', custom_threshold=0)
					self.set_checkpoint('hero_skill_1')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return
				
			if hero_hp_percent < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3)):
				if (	time.time() - self.get_checkpoint('hero_skill_2') >  self.period_bot(cooltime_2) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[회피 사용] 발동 사유 - 영웅 HP: ' + str(hero_hp_percent) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_2', custom_threshold=0)
					self.set_checkpoint('hero_skill_2')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return
		
		if target_hp_percent != None:
			if target_hp_percent < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP)):
				if (	time.time() - self.get_checkpoint('hero_skill_0') > self.period_bot(cooltime) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[궁극 사용] 발동 사유 - 대상 HP: ' + str(target_hp_percent) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_0', custom_threshold=0)
					self.set_checkpoint('hero_skill_0')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return

			if target_hp_percent < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2)):
				if (	time.time() - self.get_checkpoint('hero_skill_1') >  self.period_bot(cooltime_1) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[도발/평정 사용] 발동 사유 - 대상 HP: ' + str(target_hp_percent) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_1', custom_threshold=0)
					self.set_checkpoint('hero_skill_1')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return
				
			if target_hp_percent < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3)):
				if (	time.time() - self.get_checkpoint('hero_skill_2') >  self.period_bot(cooltime_2) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[회피 사용] 발동 사유 - 대상 HP: ' + str(target_hp_percent) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_2', custom_threshold=0)
					self.set_checkpoint('hero_skill_2')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return

		# print(party_member_hp_list)
		for i in range(4):
			if party_member_hp_list[i] == None:
				continue

			# print('[DEBUG] - CHECK -', i, self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + str(i)))

			if party_member_hp_list[i] < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + str(i))):
				if (	time.time() - self.get_checkpoint('party_hp_skill_0') >  self.period_bot(cooltime) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[궁극 사용] 발동 사유 - 파티원'+str(i+1)+' HP: ' + str(party_member_hp_list[i]) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_0', custom_threshold=0)
					self.set_checkpoint('party_hp_skill_0')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return
				
			if party_member_hp_list[i] < int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + str(i))):
				if (	time.time() - self.get_checkpoint('party_hp_skill_1') >  self.period_bot(cooltime_2) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[도발/평정 사용] 발동 사유 - 파티원'+str(i+1)+' HP: ' + str(party_member_hp_list[i]) +'%')
					self.lyb_mouse_click('tera_main_scene_hero_skill_1', custom_threshold=0)
					self.set_checkpoint('party_hp_skill_1')
					self.set_checkpoint('global_cooltime')
					is_clicked_skill = True

			if is_clicked_skill == True:
				return

		# 일반 스킬 사용
		for normal_skill_index in range(4):
			ns_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(normal_skill_index)))
			if ns_cooltime == 60:
				continue

			ns_name = 'tera_normal_skill_' + str(normal_skill_index)

			if self.get_checkpoint(ns_name) == 0:
				self.set_checkpoint(ns_name)
				ns_elapsed_time = 0
			else:
				ns_elapsed_time = time.time() - self.get_checkpoint(ns_name)

			if ns_elapsed_time > ns_cooltime:
				self.set_checkpoint(ns_name)
				self.lyb_mouse_click(ns_name, custom_threshold=0)
				self.logger.info('[일반 스킬 ' + str(normal_skill_index + 1) + ' 사용] - 다음 쿨타임:' + str(ns_cooltime) + '초')
				return

			# print('[DEBUG] CheckingNormalSkill:', normal_skill_index, self.get_game_config(lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(normal_skill_index)))


	def hero_hp(self):
		hero_hp_percent = self.hp_status(
			'tera_main_scene_hp_start', 
			'tera_main_scene_hp_middle', 
			'tera_main_scene_hp_end', 
			ignore_rgb=(255, 0, 0)
			)
		# print('[DEBUG] HERO HP        ', hero_hp_percent)

		return hero_hp_percent

	def target_hp(self):
		target_hp_percent = self.hp_status(
			'tera_main_scene_target_hp_start', 
			'tera_main_scene_target_hp_middle', 
			'tera_main_scene_target_hp_end'
			)
		# print('[DEBUG] TARGET HP      ', target_hp_percent)

		return target_hp_percent

	def party_member_hp(self):

		party_member_hp_list = []

		for i in range(4):
			party_member_hp_list.append(
				self.hp_status(
				'tera_main_scene_party_member_'+str(i)+'_hp_start',
				'tera_main_scene_party_member_'+str(i)+'_hp_middle',
				'tera_main_scene_party_member_'+str(i)+'_hp_end', 
				ignore_rgb=(255, 0, 0) 
				)
			)
			# print('[DEBUG] PARTY MEMBER['+str(i)+']', party_member_hp_list[i])

		return party_member_hp_list

	def hp_status(self, hp_s, hp_m, hp_e, ignore_rgb=-1, adjust=(15, 15, 15), adjust_s=(0,0), adjust_e=(0,0)):

		(s_loc_x, s_loc_y) = self.get_location(hp_s)
		s_loc_x += adjust_s[0]
		s_loc_y += adjust_s[1]

		(e_loc_x, e_loc_y) = self.get_location(hp_e)
		e_loc_x += adjust_e[0]
		e_loc_y += adjust_e[1]

		hp_pb = self.get_center_pixel_info(hp_m)
		hp_rgb = hp_pb[1]

		total_length = e_loc_x - s_loc_x
		j = 0

		hp_percent = None
		while True:
			(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x - j, e_loc_y)

			# print((e_loc_x -j, e_loc_y), hp_rgb, (r, g, b))

			if abs(hp_rgb[0] - r) < adjust[0] and abs(hp_rgb[1] - g) < adjust[1] and abs(hp_rgb[2] - b) < adjust[2]:
				# print('[DEBUG] HP:', int(((total_length - j) / total_length) * 100))
				hp_percent = int(((total_length - j) / total_length) * 100)
				break
			if ignore_rgb != -1:
				if abs(ignore_rgb[0] - r) < adjust[0] and abs(ignore_rgb[1] - g) < adjust[1] and abs(ignore_rgb[2] - b) < adjust[2]:
					break

			j += 1
			if j > total_length:
				break


		return hp_percent

	def quest_list(self):
		quests = [
			'tera_main_scene_quest_0',	# yellow
			'tera_main_scene_quest_1',	# blue
			'tera_main_scene_quest_2',	# yellow
			'tera_main_scene_quest_3'	# gray
		]



		





		(loc_x, loc_y) = self.get_location(quests[0])		
		pb = self.get_center_pixel_info(quests[0])

		last_rgb = (0, 0, 0)
		q_list = []

		j = 0
		while True:
			(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, loc_x, loc_y + j)

			# print(last_rgb, (r, g, b))

			if abs(last_rgb[0] - r) > 10 or abs(last_rgb[1] - g) > 10 or abs(last_rgb[2] - b) > 10:

				# print('DEBUG1:', (loc_x, loc_y + j), last_rgb, (r,g,b), self.get_center_pixel_info(quests[1]))
				for each_quest in quests:
					is_matchded = self.game_object.isMatchedCenterPixelBox(
						self.window_pixels, 
						each_quest,
						loc_x,
						loc_y + j
						)

					if is_matchded:
						# print('DEBUG2:', (loc_x, loc_y + j))
						(adj_x, adj_y) = self.game_object.get_player_adjust()
						q_list.append((each_quest, (loc_x + adj_x, loc_y + j + adj_y)))
						j += 24
				last_rgb = (r, g, b)

			j += 1
			if j > 100:
				break

		# print('-------------------------S')
		for each_quest in q_list:
			print(each_quest)
		# print('-------------------------E')

		return q_list

	def location_main_quest(self):
		current_quest_list = self.quest_list()

		for each_quest in current_quest_list:
			if each_quest[0] == 'tera_main_scene_quest_2' or each_quest[0] == 'tera_main_scene_quest_0':
				return each_quest[1]

		return (-1, -1)

	def location_etc_quest(self):
		current_quest_list = self.quest_list()

		for each_quest in current_quest_list:
			if each_quest[0] == 'tera_main_scene_quest_1':
				return each_quest[1]

		return (-1, -1)


	def get_work_status(self, work_name):
		return self.game_object.get_work_status(work_name)

	def set_combat_stance(self, current_stance, stance_rate, stance_list):
		# print('combat_stance:', current_stance, stance_rate, stance_list)
		if stance_rate < 0.8:
			return False

		for each_stance in stance_list:
			if current_stance in each_stance:
				return False

		time.sleep(1)
		if current_stance == 'manual_play':
			self.lyb_mouse_click('tera_main_scene_sudong', custom_threshold=0)
		elif current_stance == 'half_auto_play':
			self.lyb_mouse_click('tera_main_scene_banjadong', custom_threshold=0)
		elif current_stance == 'auto_play':
			self.lyb_mouse_click('tera_main_scene_jadong', custom_threshold=0)
		elif current_stance == 'tracking_match_rate':
			self.lyb_mouse_click('tera_main_scene_tracking_icon_0', custom_threshold=0)
		elif current_stance == 'maul_play':
			self.lyb_mouse_click('tera_main_scene_maul', custom_threshold=0)
			time.sleep(1)
			return False
		else:
			return False

		time.sleep(1)
		return True

	def use_skill(self):
		skill_0_use_rate = int(self.get_game_config(lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE))
		skill_1_use_rate = int(self.get_game_config(lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1))
		skill_2_use_rate = int(self.get_game_config(lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2))
		
		use_rate = 0
		for i in range(3):
			rand = random.random()

			if i == 0:
				use_rate = skill_0_use_rate * 0.01
			elif i == 1:
				use_rate = skill_1_use_rate * 0.01
			elif i == 2:
				use_rate = skill_2_use_rate * 0.01

			if rand < use_rate:
				self.lyb_mouse_click('tera_main_scene_hero_skill_' + str(i), custom_threshold=0)

		# print('[SKILL1]', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP))
		# print('[SKILL2]', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_1_HP))
		# print('[SKILL3]', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_2_HP))
		# print('[SKILL4]', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_3_HP))
		# print('[SKILL5]', self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_4_HP))

	def use_skill2(self):

		if (	self.get_game_config(lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL) == False and
				self.get_game_config(lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE) == False
				):
			return

		s_time = time.time()
		# print('S -- tera_boss_use_dealer_skill::::')
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic['tera_boss_use_dealer_skill'],
								custom_below_level=(100, 0, 0),
								custom_top_level=(255,100,10),
								custom_threshold=int(self.get_game_config(lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING)) * 0.01,
								custom_flag=1,
								custom_rect=(320,120,380,140)
								)
		e_time = time.time()
		# print('E -- tera_boss_use_dealer_skill::::', (loc_x, loc_y), match_rate, e_time - s_time)
		# self.logger.warn('E -- tera_boss_use_dealer_skill::::' + str((loc_x, loc_y)) +':'+str(int(match_rate*100)) +':'+ str(e_time - s_time))
		# print('[DEBUG] Elapsed Time BOSS:', '[', int(match_rate*100), ']', round(e_time - s_time, 5))
		global_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL))
		cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL))
		cooltime_1 = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1))
		cooltime_2 = int(self.get_game_config(lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2))
		after_boss = float(self.get_game_config(lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2))

		is_clicked_skill = False
		if loc_x != -1:			
			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL) == True:
				if (	time.time() - self.get_checkpoint('used_skill_0') >  self.period_bot(cooltime) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					self.logger.info('[보스 경고] 보스에게 궁극기 시전(경고 인식률: '+str(int(match_rate*100))+'%)')
					self.lyb_mouse_click('tera_main_scene_hero_skill_0', custom_threshold=0)
					is_clicked_skill = True
					self.set_checkpoint('used_skill_0')
					self.set_checkpoint('global_cooltime')

			if is_clicked_skill == True:
				return True

			# print('[DEBUG] Evade Test:', time.time() - self.get_checkpoint('used_skill_2'), time.time() - self.get_checkpoint('global_cooltime'))

			if self.get_game_config(lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE) == True:
				if (	time.time() - self.get_checkpoint('used_skill_2') >  self.period_bot(cooltime_2) and
						time.time() - self.get_checkpoint('global_cooltime') > self.period_bot(global_cooltime)
						):
					
					# print('[DEBUG] After BOSS:', after_boss)
					if self.get_option('after_boss') == None:
						self.set_option('after_boss', time.time())

					if time.time() - self.get_option('after_boss') < after_boss:
						is_clicked_skill = True
					else:
						self.logger.info('[보스 경고] 회피 시전(경고 인식률: '+str(int(match_rate*100))+'%)')
						self.lyb_mouse_click('tera_main_scene_hero_skill_2', custom_threshold=0)
						is_clicked_skill = True
						self.set_checkpoint('used_skill_2')
						self.set_checkpoint('global_cooltime')
						self.set_option('after_boss', None)

		# 보스 경고 메세지가 끝났으나 회피를 하려는 경우
		if is_clicked_skill == False:
			if self.get_option('after_boss') != None:
				self.logger.info('[보스 경고] 회피 시전(경고 인식률: '+str(int(match_rate*100))+'%)')
				self.lyb_mouse_click('tera_main_scene_hero_skill_2', custom_threshold=0)
				is_clicked_skill = True
				self.set_checkpoint('used_skill_2')
				self.set_checkpoint('global_cooltime')
				self.set_option('after_boss', None)

		return is_clicked_skill

	def find_item_loc(self, start_x, start_y, end_x, end_y, pixel_rgb, adjust=(30, 30, 30)):

		dx = start_x
		dy = start_y

		while True:
			if dx > end_x:
				break

			(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, dx, dy)
			if abs(pixel_rgb[0] - r) < adjust[0] and abs(pixel_rgb[1] - g) < adjust[1] and abs(pixel_rgb[2] - b) < adjust[2]:
				# print((dx, dy), pixel_rgb, (r, g, b))

				is_found = True
				for i in range(10):
					if self.game_object.get_pixel_info(self.window_pixels, dx+i, dy) != (r, g, b):
						is_found = False

				if is_found == True:
					return (dx, dy)

			dy += 1

			if dy > end_y:
				dx += 1
				dy = start_y

		return (-1, -1)
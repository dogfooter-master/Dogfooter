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
import likeyoubot_talion as lybgametalion
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBTalionScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBTalionScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'init_screen_scene':
			rc = self.init_screen_scene()
		elif self.scene_name == 'main_scene':
			rc = self.main_scene()
		elif self.scene_name == 'tutorial_scene':
			rc = self.tutorial_scene()
		elif self.scene_name == 'quest_complete_scene':
			rc = self.quest_complete_scene()
		elif self.scene_name == 'quest_surak_scene':
			rc = self.quest_surak_scene()
		elif self.scene_name == 'jeoljeon_mode_scene':
			rc = self.jeoljeon_mode_scene()
		elif self.scene_name == 'login_scene':
			rc = self.login_scene()
		elif self.scene_name == 'character_scene':
			rc = self.character_scene()
		elif self.scene_name == 'upjeok_scene':
			rc = self.upjeok_scene()
		elif self.scene_name == 'dungeon_scene':
			rc = self.dungeon_scene()
		elif self.scene_name == 'story_dungeon_scene':
			rc = self.dungeon_common_scene()
		elif self.scene_name == 'siryeon_dungeon_scene':
			rc = self.dungeon_common_scene()
		elif self.scene_name == 'gob_dungeon_scene':
			rc = self.dungeon_common_scene()
		elif self.scene_name == 'golem_dungeon_scene':
			rc = self.dungeon_common_scene()
		elif self.scene_name == 'dojeontap_dungeon_scene':
			rc = self.dungeon_common_scene()
		elif self.scene_name == 'jeongye_dungeon_scene':
			rc = self.dungeon_common_scene()
		elif self.scene_name == 'dungeon_main_scene':
			rc = self.dungeon_main_scene()
		elif self.scene_name == 'dojeon_clear_scene':
			rc = self.dungeon_clear_scene()
		elif self.scene_name == 'dungeon_clear_scene':
			rc = self.dungeon_clear_scene()
		elif self.scene_name == 'biheng_scene':
			rc = self.biheng_scene()
		elif self.scene_name == 'dungeon_death_scene':
			rc = self.death_scene()
		elif self.scene_name == 'death_scene':
			rc = self.death_scene()
		elif self.scene_name == 'mail_scene':
			rc = self.mail_scene()
		elif self.scene_name == 'jungke_sangjeom_scene':
			rc = self.jungke_sangjeom_scene()
		elif self.scene_name == 'japhwa_sangjeom_scene':
			rc = self.japhwa_sangjeom_scene()
		elif self.scene_name == 'gume_confirm_scene':
			rc = self.gume_confirm_scene()
		elif self.scene_name == 'gabang_scene':
			rc = self.gabang_scene()
		elif self.scene_name == 'gabang_select_item_scene':
			rc = self.gabang_select_item_scene()
		elif self.scene_name == 'death_match_scene':
			rc = self.death_match_scene()
		elif self.scene_name == 'team_pvp_scene':
			rc = self.team_pvp_scene()
		elif self.scene_name == 'jeomryeongjeon_scene':
			rc = self.jeomryeongjeon_scene()
		elif self.scene_name == 'jeomryeongjeon_select_scene':
			rc = self.jeomryeongjeon_select_scene()
		elif self.scene_name == 'pvp_scene':
			rc = self.pvp_scene()
		elif self.scene_name == 'kiki_support_scene':
			rc = self.kiki_support_scene()
		elif self.scene_name == 'youmul_scene':
			rc = self.youmul_scene()
		elif self.scene_name == 'youmul_register_scene':
			rc = self.youmul_register_scene()
		elif self.scene_name == 'nalge_scene':
			rc = self.nalge_scene()
		elif self.scene_name == 'jeomryeongjeon_combat_scene':
			rc = self.jeomryeongjeon_combat_scene()



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
	

	def jeomryeongjeon_combat_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 1000:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def nalge_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 20:
			self.status += 1
			pb_name = 'nalge_scene_ether_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				return self.status
			self.status = 99999
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def youmul_register_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.game_object.get_scene('youmul_scene').set_option('register', True)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('youmul_register_scene_register', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def youmul_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.game_object.get_scene('youmul_register_scene').status = 0
			self.set_option('register', False)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.status += 1
			pb_name = 'youmul_scene_open'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.9,
							custom_flag=1,
							custom_rect=(20, 190, 250, 380)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:				
				self.status = 5
		elif self.status >= 5 and self.status < 10:
			if self.status > 5 and self.get_option('register') == False:
				self.status = 99999
				return self.status
			else:
				self.status += 1

			pb_name = 'youmul_scene_register'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.9,
							custom_flag=1,
							custom_rect=(20, 190, 250, 380)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click('youmul_scene_list_00', custom_threshold=0)
			else:
				self.status = 99999
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def kiki_support_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.status += 1

			pb_name = 'kiki_support_scene_complete'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_top_level=(255, 80, 80),
							custom_below_level=(180, 20, 20),
							custom_rect=(70, 90, 500, 330)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				return self.status

			cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select')
			cfg_index = lybgametalion.LYBTalion.kiki_support_list.index(cfg_select)

			pb_name = 'kiki_support_scene_ure_' + str(cfg_index)
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				return self.status
			self.status = 99999
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def jeomryeongjeon_select_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('jeomryeongjeon_select_scene_0', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def pvp_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 300:
			if self.checkSpecialSkill() == True:
				return self.status
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def jeomryeongjeon_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.lyb_mouse_click('jeomryeongjeon_scene_enter', custom_threshold=0)
			self.game_object.get_scene('jeomryeongjeon_combat_scene').status = 0
			self.game_object.get_scene('main_scene').set_checkpoint('dungeon_enter_click')
			self.game_object.get_scene('pvp_scene').status = 0
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def team_pvp_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.lyb_mouse_click('team_pvp_scene_enter', custom_threshold=0)
			self.game_object.get_scene('main_scene').set_checkpoint('dungeon_enter_click')
			self.game_object.get_scene('pvp_scene').status = 0

		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def death_match_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			pb_name = 'death_match_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				self.status = 99999
				return self.status

			self.lyb_mouse_click('death_match_scene_enter', custom_threshold=0)
			self.game_object.get_scene('main_scene').set_checkpoint('dungeon_enter_click')
			self.game_object.get_scene('pvp_scene').status = 0
			self.status += 1

		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def gabang_select_item_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def gabang_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.status += 1
			pb_name = 'gabang_scene_bunhe'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click('gabang_scene_bunhe')	
				self.status = 5
			else:
				self.lyb_mouse_click('gabang_scene_tab_0', custom_threshold=0)
		elif self.status >= 5 and self.status < 10:
			self.status += 1
			pb_name = 'gabang_scene_select_rank'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.game_object.get_scene('gabang_select_item_scene').status = 0
				self.lyb_mouse_click('gabang_scene_select_rank')
				self.status = 10
		elif self.status == 10:
			self.lyb_mouse_click('gabang_scene_select_bunhe', custom_threshold=0)
			self.status += 1
		elif self.status == 100:
			self.status += 1
		elif self.status == 101:
			pb_name = 'gabang_scene_potion_enable'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.3,
							custom_top_level=(255, 150, 150),
							custom_below_level=(145, 0, 0),
							custom_flag=1,
							custom_rect=(90, 110, 130, 160)
							)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if loc_x == -1:

				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 물약 없음 감지')
				png_name = self.game_object.save_image('character_death')
				self.game_object.telegram_send('', image=png_name)
				

				self.game_object.get_scene('jungke_sangjeom_scene').status = 100
				self.game_object.get_scene('main_scene').set_option('menu_click', True)
				self.game_object.get_scene('main_scene').set_option('menu_status', 10)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def gume_confirm_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 100:
			self.lyb_mouse_click('gume_confirm_scene_ok', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def japhwa_sangjeom_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 100:
			self.lyb_mouse_click('japhwa_sangjeom_scene_tab_0', custom_threshold=0)
			self.status += 1
		elif self.status == 101:
			self.lyb_mouse_click('japhwa_sangjeom_scene_tab_00', custom_threshold=0)
			self.status += 1
		elif self.status == 102:
			self.game_object.get_scene('gume_confirm_scene').status = 100
			self.lyb_mouse_click('japhwa_sangjeom_scene_hp_potion', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def jungke_sangjeom_scene(self):

		self.game_object.current_matched_scene['name'] = ''

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 100 and self.status < 105:
			self.game_object.get_scene('japhwa_sangjeom_scene').status = 100
			self.lyb_mouse_click('jungke_sangjeom_scene_japhwa', custom_threshold=0)
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
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def mail_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 9:
			self.status += 1
			for i in range(2):
				pb_name = 'mail_scene_new_' + str(i)
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(10, 50, 200, 100)
								)
				if loc_x != -1:		
					self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
					self.set_option('last_status', self.status)
					self.status = 10
					return self.status

			self.status = 99999
		elif self.status == 10:
			self.lyb_mouse_click('mail_scene_modu', custom_threshold=0)
			self.status += 1
		elif self.status >= 11 and self.status < 20:
			self.status += 1

			pb_name = 'mail_scene_receive'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(410, 80, 510, 340)
							)
			if loc_x != -1:		
				self.lyb_mouse_click_location(loc_x, loc_y)
				return self.status

			self.status = self.get_option('last_status')
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def death_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.game_object.get_scene('main_scene').set_option('dungeon_fail', False)
			self.status += 1
		elif self.status == 1:
			self.game_object.get_scene('main_scene').set_option('dungeon_fail', True)
			self.logger.warn('캐릭터 사망 감지')
			current_work = self.game_object.get_scene('main_scene').current_work
			if current_work == '메인 퀘스트':
				quest_index = self.game_object.get_scene('main_scene').get_option('quest_index')
				if quest_index == None:
					quest_index = 0
				self.game_object.get_scene('main_scene').set_option('quest_index', quest_index + 1)
				self.logger.info('퀘스트 종료: ' + str(quest_index))

			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

			if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 캐릭터 사망 감지')
				png_name = self.game_object.save_image('character_death')
				self.game_object.telegram_send('', image=png_name)
				
			self.status = 0

		return self.status

	def biheng_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			current_work = self.game_object.get_scene('main_scene').current_work
			self.logger.info('현재 작업: ' + str(current_work))
			if current_work == '메인 퀘스트':
				pb_name = 'biheng_scene_free'
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(340, 180, 570, 330)
								)
				if loc_x != -1:		
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status = 10
					return self.status
			self.status += 1
		elif self.status == 10:
			self.lyb_mouse_click('biheng_scene_move', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def dungeon_clear_scene(self):

		pb_name = 'dungeon_clear_scene_rank_f'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate > 0.9:
			self.game_object.get_scene('main_scene').set_option('dungeon_fail', True)
			self.status = 99999

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 10:
			count = self.game_object.get_scene('dungeon_clear_scene').get_option('count')
			if count == None:
				count = 0

			limit_count = self.game_object.get_scene('dungeon_clear_scene').get_option('limit_count')
			if limit_count == None:
				limit_count = 0

			count += 1
			self.game_object.get_scene('dungeon_clear_scene').set_option('count', count)

			self.logger.info('던전 클리어 횟수: ' + str(count) + '/' + str(limit_count))

			if limit_count != 0 and count >= limit_count:
				self.status = 99999
			else:
				# pb_name = 'dojeon_clear_scene_next'
				# match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				# self.logger.debug(pb_name + ' ' + str(match_rate))
				# if match_rate > 0.9:
				# 	self.lyb_mouse_click(pb_name, custom_threshold=0)
				# 	return self.status

				pb_name = self.scene_name + '_again'
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.debug(pb_name + ' ' + str(match_rate))
				if match_rate > 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def dungeon_main_scene(self):

		if self.pre_process_common() == True:
			return self.status

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 1200:
			self.status += 1

			self.game_object.get_scene('dungeon_clear_scene').status = 0

			if self.isAutoOn(limit_count=2) == False:
				self.lyb_mouse_click('auto_on', custom_threshold=0)
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def dungeon_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('스토리 던전'):
			self.lyb_mouse_click('dungeon_scene_story_dungeon', custom_threshold=0)
			self.game_object.get_scene('story_dungeon_scene').status = 0
		elif self.status == self.get_work_status('고브의 금고'):
			self.lyb_mouse_click('dungeon_scene_gob_dungeon', custom_threshold=0)
			self.game_object.get_scene('gob_dungeon_scene').status = 0
		elif self.status == self.get_work_status('시련의 동굴'):
			self.lyb_mouse_click('dungeon_scene_siryeon_dungeon', custom_threshold=0)
			self.game_object.get_scene('siryeon_dungeon_scene').status = 0
		elif self.status == self.get_work_status('골렘 연구소'):
			self.lyb_mouse_click('dungeon_scene_golem_dungeon', custom_threshold=0)
			self.game_object.get_scene('golem_dungeon_scene').status = 0
		elif self.status == self.get_work_status('도전의 탑'):
			self.lyb_mouse_click('dungeon_scene_dojeontap_dungeon', custom_threshold=0)
			self.game_object.get_scene('dojeontap_dungeon_scene').status = 0
		elif self.status == self.get_work_status('정예 던전'):
			self.lyb_mouse_click('dungeon_scene_jeongye_dungeon', custom_threshold=0)
			self.game_object.get_scene('jeongye_dungeon_scene').status = 0
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def dungeon_common_scene(self):

		if self.game_object.get_scene('main_scene').get_option('dungeon_fail') == True:
			self.game_object.get_scene('main_scene').set_option('dungeon_fail', False)
			self.status = 99999

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)			
			self.set_option('last_status', 99999)
			self.status += 1
		elif self.status == 1:
			if self.scene_name == 'story_dungeon_scene':
				self.status = 10
			elif self.scene_name == 'gob_dungeon_scene':
				self.status = 20
			elif self.scene_name == 'siryeon_dungeon_scene':
				self.status = 30
			elif self.scene_name == 'golem_dungeon_scene':
				self.status = 40
			elif self.scene_name == 'dojeontap_dungeon_scene':
				self.status = 50
			elif self.scene_name == 'jeongye_dungeon_scene':
				self.status = 60
			else:
				self.status = 900

		elif self.status == 10:
			pb_name = 'story_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				if self.game_object.get_scene('main_scene').get_option('from_quest') == True:
					if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
						quest_index = self.game_object.get_scene('main_scene').get_option('quest_index')
						if quest_index == None:
							quest_index = 0
						self.game_object.get_scene('main_scene').set_option('quest_index', quest_index + 1)
				self.status = 99999
				return self.status


			if self.game_object.get_scene('main_scene').get_option('from_quest') == True:
				self.status = 900
				self.game_object.get_scene('dungeon_clear_scene').set_option('count', 1)
				self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 1)
			else:				
				dungeon_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count'))
				self.game_object.get_scene('dungeon_clear_scene').set_option('count', 0)
				self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', dungeon_count)
				dungeon_selected = self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select')
				self.logger.warn('스토리 던전: [' + str(dungeon_selected) + ']')
				if dungeon_selected == lybgametalion.LYBTalion.story_dungeon_list[0]:
					self.status += 1
				else:
					self.status += 1
					# 회색 안보이게 하려고
					self.lyb_mouse_click('story_dungeon_scene_difficulty_0', custom_threshold=0)
					self.set_option('resource_name', 'story_dungeon_scene_' + dungeon_selected + '_loc')
					self.set_option('last_status', self.status)
					self.set_option('drag_start', 'story_dungeon_scene_drag_left')
					self.set_option('drag_end', 'story_dungeon_scene_drag_right')
					self.set_option('end_count', 0)
					self.status = 100
		elif self.status == 11:

			pb_name = 'story_dungeon_scene_boss_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.95:
				self.logger.info('횟수 부족')
				self.status = 99999
				return self.status

			# 스토리 던전
			cfg_difficulty = self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty')
			cfg_difficulty_index = lybgametalion.LYBTalion.story_dungeon_difficulty_list.index(cfg_difficulty)
			self.set_option('difficulty', cfg_difficulty_index)
			self.status += 1
		elif self.status == 12:
			difficulty = self.get_option('difficulty')
			if difficulty < 0:
				self.status = 99999
			else:
				pb_name = 'story_dungeon_scene_difficulty_' + str(difficulty)
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('last_status', self.status)
				self.set_option('difficulty', difficulty - 1)
				if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol') == True:
					self.status += 1
				else:
					self.status = 900
		elif self.status >= 13 and self.status < 15:
			self.status += 1
			pb_name = 'story_dungeon_scene_tobeol'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				return self.status
			self.status = 900

		elif self.status == 20:

			pb_name = 'gob_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				if self.game_object.get_scene('main_scene').get_option('from_quest') == True:
					if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
						quest_index = self.game_object.get_scene('main_scene').get_option('quest_index')
						if quest_index == None:
							quest_index = 0
						self.game_object.get_scene('main_scene').set_option('quest_index', quest_index + 1)
				self.status = 99999
				return self.status

			if self.game_object.get_scene('main_scene').get_option('from_quest') == True:
				self.status = 900
				self.game_object.get_scene('dungeon_clear_scene').set_option('count', 1)
				self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 1)
			else:				
				self.game_object.get_scene('dungeon_clear_scene').set_option('count', 0)
				self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 0)
				cfg_difficulty = self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty')
				cfg_difficulty_index = lybgametalion.LYBTalion.dungeon_difficulty_list.index(cfg_difficulty)
				self.set_option('difficulty', cfg_difficulty_index)
				self.status += 1
		elif self.status == 21:

			difficulty = self.get_option('difficulty')
			if difficulty < 0:
				self.status = 99999
			else:
				pb_name = 'gob_dungeon_scene_difficulty_' + str(difficulty)
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('last_status', self.status)
				self.set_option('difficulty', difficulty - 1)
				self.status = 900

		elif self.status == 30:

			pb_name = 'siryeon_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				if self.game_object.get_scene('main_scene').get_option('from_quest') == True:
					if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
						quest_index = self.game_object.get_scene('main_scene').get_option('quest_index')
						if quest_index == None:
							quest_index = 0
						self.game_object.get_scene('main_scene').set_option('quest_index', quest_index + 1)
				self.status = 99999
				return self.status

			if self.game_object.get_scene('main_scene').get_option('from_quest') == True:
				self.status = 900
				self.game_object.get_scene('dungeon_clear_scene').set_option('count', 1)
				self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 1)
			else:				
				self.game_object.get_scene('dungeon_clear_scene').set_option('count', 0)
				self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 0)
				cfg_difficulty = self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty')
				cfg_difficulty_index = lybgametalion.LYBTalion.dungeon_difficulty_list.index(cfg_difficulty)
				self.set_option('difficulty', cfg_difficulty_index)
				self.status += 1
		elif self.status == 31:

			difficulty = self.get_option('difficulty')
			if difficulty < 0:
				self.status = 99999
			else:
				pb_name = 'siryeon_dungeon_scene_difficulty_' + str(difficulty)
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('last_status', self.status)
				self.set_option('difficulty', difficulty - 1)
				self.status = 900


		elif self.status == 40:

			pb_name = 'golem_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				self.status = 99999
				return self.status

			self.game_object.get_scene('dungeon_clear_scene').set_option('count', 0)
			self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 0)
			cfg_difficulty = self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty')
			cfg_difficulty_index = lybgametalion.LYBTalion.dungeon_difficulty_list.index(cfg_difficulty)
			self.set_option('difficulty', cfg_difficulty_index)
			self.status += 1
		elif self.status == 41:

			difficulty = self.get_option('difficulty')
			if difficulty < 0:
				self.status = 99999
			else:
				pb_name = 'golem_dungeon_scene_difficulty_' + str(difficulty)
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('last_status', self.status)
				self.set_option('difficulty', difficulty - 1)
				self.status = 900

		elif self.status == 50:

			pb_name = 'dojeon_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				self.status = 99999
				return self.status

			self.game_object.get_scene('dungeon_clear_scene').set_option('count', 0)
			self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 0)

			self.status = 900

		elif self.status == 60:

			pb_name = 'dojeon_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.98:
				self.logger.info('티켓 부족')
				self.status = 99999
				return self.status

			self.game_object.get_scene('dungeon_clear_scene').set_option('count', 0)
			self.game_object.get_scene('dungeon_clear_scene').set_option('limit_count', 0)

			if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon') == True:
				self.set_option(self.scene_name + 'enter', 'jeongye_dungeon_scene_enter_solo')
			else:
				self.set_option(self.scene_name + 'enter', None)

			self.status = 900

		elif self.status == 100:
			resource_name = self.get_option('resource_name')
			for i in range(3):
				s_x = 80 + (i*160) - 100
				e_x = 80 + (i*160) + 100

				if s_x < 5:
					s_x = 5
				if e_x > 510:
					e_x = 510
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
						self.window_image,
						resource_name,
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(s_x, 180, e_x, 220)
						)
				self.logger.debug(resource_name + ' ' + str((s_x, 180, e_x, 220)) + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status = self.get_option('last_status')
					return self.status

			self.lyb_mouse_drag(self.get_option('drag_start'), self.get_option('drag_end'), stop_delay=1)
			self.status += 1
		elif self.status == 101:
			is_end = True
			for i in range(4):
				pb_name = 'story_dungeon_scene_check_' + str(i)
				(loc_x, loc_y) = self.get_location(pb_name)
				last_pixel = self.get_option('last_pixel_' + pb_name)
				if last_pixel == None:		
					is_end = False
				else:		
					self.logger.debug(str((loc_x, loc_y)) + ' ' + str(last_pixel) + ' ' + str(self.game_object.window_pixels[loc_x, loc_y]))
					if last_pixel != self.game_object.window_pixels[loc_x, loc_y]:
						is_end = False

				self.set_option('last_pixel_' + pb_name, self.game_object.window_pixels[loc_x, loc_y])
			if is_end == True:
				end_count = self.get_option('end_count')
				if end_count == 1:
					self.status = 99999
					return self.status

				self.set_option('end_count', end_count + 1)
				drag_start = self.get_option('drag_start')
				self.set_option('drag_start', self.get_option('drag_end'))
				self.set_option('drag_end', drag_start)
			self.status -= 1
		elif self.status >= 900 and self.status < 910:				
			self.status += 1
			pb_name = self.scene_name + '_enter_new'
			if self.get_option(self.scene_name + 'enter') != None:
				pb_name = self.get_option(self.scene_name + 'enter')

			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(220, 330, 520, 380)
							)
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:		
				self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
				self.game_object.get_scene('dungeon_main_scene').status = 0
				self.game_object.get_scene('main_scene').set_checkpoint('dungeon_enter_click')
				return self.status

			self.status = self.get_option('last_status')
		elif self.status == 910:			
			if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
				quest_index = self.game_object.get_scene('main_scene').get_option('quest_index')
				if quest_index == None:
					quest_index = 0
				self.game_object.get_scene('main_scene').set_option('quest_index', quest_index + 1)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def upjeok_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 9:
			self.status += 1
			pb_name_list = [
				'upjeok_scene_new_0',
				'upjeok_scene_new_1',
			]
			for pb_name in pb_name_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(10, 50, 400, 100)
								)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x - 10, loc_y + 5)
					self.set_option('last_status', self.status)
					self.status = 10
					return self.status

			self.status = 99999
		elif self.status >= 10 and self.status < 20:
			self.status += 1
			pb_name = 'upjeok_scene_bosang'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(420, 90, 500, 150)
							)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				return self.status

			self.status = self.get_option('last_status')
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def character_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
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

	def jeoljeon_mode_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_drag('jeoljeon_mode_scene_drag_bot', 'jeoljeon_mode_scene_drag_top', stop_delay=1)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def quest_surak_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def quest_complete_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def tutorial_scene(self):

		if self.status == 0:
			self.logger.info('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
		# 	pb_name_list = [
		# 		'main_scene_menu',
		# 		'menu_tamheom',
		# 		'menu_tamheom_dungeon',
		# 		'menu_tamheom_rvr',
		# 		'menu_tamheom_fieldboss',
		# 		'menu_tamheom_raid',
		# 		'menu_community',
		# 		'menu_community_party',
		# 		'menu_community_friend',
		# 		'menu_community_guild',
		# 		'menu_community_yeonmeng',
		# 	]

			# tutorial_scene_click_loc
			for i in range(10):
				pb_name = 'tutorial_scene_click_' + str(i)
				if pb_name in self.game_object.resource_manager.pixel_box_dic:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
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
			for each_icon in lybgametalion.LYBTalion.talion_icon_list:
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
			for each_icon in lybgametalion.LYBTalion.talion_icon_list:
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

			cfg_duration_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration'))
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(cfg_duration_time):
				self.set_option(self.current_work + '_end_flag', True)	

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_inner_status', None)
				self.set_option('quest_index', None)
				self.status = self.last_status[self.current_work] + 1
				return self.status	

			quest_pb_name_list = [
				[ 'main_scene_quest_sub', '[보조]'],
				[ 'main_scene_quest_day', '[일일]'],
				[ 'main_scene_quest_repeat', '[반복]'],
				[ 'main_scene_quest_main', '[메인]' ],
			]

			inner_status = self.get_option(self.current_work + '_inner_status')
			if inner_status == None:
				inner_status = 0

			self.set_option(self.current_work + '_inner_status', inner_status + 1)
			self.logger.debug('inner_status ' + str(inner_status))

			quest_index = self.get_option('quest_index')
			if quest_index == None:
				quest_index = 0
				self.set_option('quest_index', 0)

			if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub') == False and quest_index == 0:
				quest_index += 1

			if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day') == False and quest_index == 1:
				quest_index += 1

			if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat') == False and quest_index == 2:
				quest_index += 1

			if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main') == False and quest_index == 3:
				quest_index += 1

			if quest_index >= len(quest_pb_name_list):
				self.logger.info('[메인 퀘스트] 작업을 종료합니다')
				self.set_option(self.current_work + '_end_flag', True)	
				return self.status

			quest_pb_name = quest_pb_name_list[quest_index][0]
			quest_prefix = quest_pb_name_list[quest_index][1]

			if self.isAutoQuest(limit_count=5) == False:
				(loc_x, loc_y), match_rate = self.locationOnQuestArea(quest_pb_name)
				if loc_x != -1:
					if time.time() - self.get_checkpoint('quest_click') < self.period_bot(10):
						quest_enable_check = self.get_option('quest_enable_check')
						if quest_enable_check == None:
							quest_enable_check = 0
						if quest_enable_check >= 3:
							# 퀘스트를 클릭했지만 무언가 때문에 수행이 되지 않는 경우
							self.logger.info('퀘스트 클릭 무반응: ' + str(quest_prefix))
							self.set_option('quest_enable_check', 0)
							self.set_option('quest_index', quest_index + 1)
							return self.status
						self.set_option('quest_enable_check', quest_enable_check + 1)
					else:
						self.set_option('quest_enable_check', 0)
					self.logger.debug('click quest: ' + str(quest_pb_name))
					self.logger.info(quest_prefix + ' 퀘스트 클릭')
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.set_option('quest_drag_count', 1)
					self.set_checkpoint('quest_click')
					self.set_option('from_quest', True)
					return self.status	
				else:
					quest_drag_count = self.get_option('quest_drag_count')
					if quest_drag_count == None:
						quest_drag_count = 1

					self.logger.debug('quest_drag_count ' + str(quest_drag_count))
					self.logger.info(quest_prefix + ' 퀘스트 탐색 중입니다..')

					if quest_drag_count % 6 == 0:
						self.logger.info('퀘스트 탐색 실패: ' + quest_prefix)
						self.set_option('quest_index', quest_index + 1)
						quest_drag_count = 0
					elif inner_status % 4 == 0:
						self.lyb_mouse_drag('main_scene_quest_drag_bot', 'main_scene_quest_drag_top')
					elif inner_status % 2 == 0:
						self.lyb_mouse_drag('main_scene_quest_drag_top', 'main_scene_quest_drag_bot')

					self.set_option('quest_drag_count', quest_drag_count + 1)

		elif (	self.status == self.get_work_status('스토리 던전') or
				self.status == self.get_work_status('고브의 금고') or
				self.status == self.get_work_status('시련의 동굴') or
				self.status == self.get_work_status('골렘 연구소') or
				self.status == self.get_work_status('도전의 탑') or
				self.status == self.get_work_status('정예 던전')
				):

			elapsed_time = time.time() - self.get_checkpoint('dungeon_clicked')
			if elapsed_time < self.period_bot(60):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.checkpoint['dungeon_clicked'] = 0
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('dungeon_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
			self.set_option('menu_click', True)
			self.set_option('menu_status', self.status)
			self.set_checkpoint('dungeon_clicked')

		elif (	self.status == self.get_work_status('키키 지원단') or
				self.status == self.get_work_status('날개')
				):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('kiki_support_scene').status = 0
			self.game_object.get_scene('nalge_scene').status = 0
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
			self.set_option('menu_click', True)
			self.set_option('menu_status', self.status)

		elif self.status == self.get_work_status('유물'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('youmul_scene').status = 0
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
			self.set_option('menu_click', True)
			self.set_option('menu_status', self.status)

		elif self.status == self.get_work_status('분해'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('gabang_scene').status = 0
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
			self.set_option('menu_click', True)
			self.set_option('menu_status', self.status)

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

		# 던전 취소
		resource_name = 'main_scene_match_dashboard_loc'
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
		self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
		if match_rate > 0.9:
			self.lyb_mouse_click('main_scene_match_dashboard_cancel', custom_threshold=0)		
			return True

		pb_name = 'main_scene_dungeon_matching'
		(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(440, 80, 560, 130)
						)
		self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			elapsed_time = time.time() - self.get_checkpoint('dungeon_enter_click')
			self.loggingElapsedTime('매칭 대기', elapsed_time, 120, period=1)
			if elapsed_time > 120:
				self.lyb_mouse_click_location(loc_x, loc_y)
			
			if self.current_work != '메인 퀘스트':
				return True

		if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match') == True:
			pb_name = 'main_scene_realtime_pvp'
			elapsed_time = time.time() - self.get_checkpoint(pb_name + '_clicked')
			if elapsed_time > self.period_bot(60):					
				self.set_checkpoint(pb_name + '_clicked')
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(440, 80, 560, 130)
								)
				self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
				if loc_x != -1:
					self.game_object.get_scene('death_match_scene').status = 0
					self.lyb_mouse_click_location(loc_x, loc_y)
					return True

		if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp') == True:
			pb_name = 'main_scene_team_pvp'
			elapsed_time = time.time() - self.get_checkpoint(pb_name + '_clicked')
			if elapsed_time > self.period_bot(60):					
				self.set_checkpoint(pb_name + '_clicked')
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(440, 80, 560, 130)
								)
				self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
				if loc_x != -1:
					self.game_object.get_scene('team_pvp_scene').status = 0
					self.lyb_mouse_click_location(loc_x, loc_y)
					return True
				
		if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon') == True:
			pb_name = 'main_scene_jeomryeongjeon'
			elapsed_time = time.time() - self.get_checkpoint(pb_name + '_clicked')
			if elapsed_time > self.period_bot(60):					
				self.set_checkpoint(pb_name + '_clicked')
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(440, 80, 560, 130)
								)
				self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
				if loc_x != -1:
					self.game_object.get_scene('jeomryeongjeon_scene').status = 0
					self.lyb_mouse_click_location(loc_x, loc_y)
					return True

		quest_pb_name_list = [
			'main_scene_quest_upjeok',
		]

		for pb_name in quest_pb_name_list:
			(loc_x, loc_y), match_rate = self.locationOnQuestArea(pb_name)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				return True

		pb_name = 'main_scene_invite_accept'
		(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_top_level=(30, 255, 255),
						custom_below_level=(0, 100, 100),
						custom_rect=(610, 130, 635, 170)
						)
		if loc_x != -1:
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.lyb_mouse_click_location(loc_x, loc_y)
			return True


		if self.get_game_config(lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on') == True:
			if self.isAutoOn(limit_count=2) == False:
				self.lyb_mouse_click('auto_on', custom_threshold=0)

		if self.pre_process_common() == True:
			return True

	def pre_process_common(self):

		if self.checkSpecialSkill() == True:
			return True

		if self.openQuickslot() == True:
			return True

		if self.emptyPotion() == True:
			return True

		if self.checkBunhe() == True:
			return True

	def checkBunhe(self):
		cfg_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period'))
		checkpoint_time = self.get_checkpoint('bunhe_period')
		if checkpoint_time == 0:
			self.set_checkpoint('bunhe_period')
			return False

		elapsed_time = time.time() - checkpoint_time
		if elapsed_time > cfg_period:	
			self.loggingElapsedTime("자동 [분해] 작업 실행", elapsed_time, cfg_period, period=1)		
			self.game_object.get_scene('gabang_scene').status = 0
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
			self.set_option('menu_click', True)
			self.set_option('menu_status', self.get_work_status("분해"))			
			self.set_checkpoint('bunhe_period')

	def checkSpecialSkill(self):
		resource_name = 'main_scene_special_skill_loc'
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
				self.window_image,
				resource_name,
				custom_threshold=0.8,
				custom_top_level=(255, 255, 255),
				custom_below_level=(120, 120, 120),
				custom_flag=1,
				custom_rect=(460, 220, 540, 250)
				)
		if loc_x != -1:
			self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			for i in range(4):
				pb_name = 'main_scene_ss_' + str(3 - i)
				self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True


	def emptyPotion(self):
		if self.isStatusByResource (
			'[물약 없음]', 
			'main_scene_potion_enable_loc', 
			0.35, 
			(200, 180, 180), (110, 100, 90), 
			(90, 220, 125, 270),
			limit_count=5,
			average=True,
			) == False:
			self.game_object.get_scene('gabang_scene').status = 100
			self.lyb_mouse_click('main_scene_potion', custom_threshold=0)
			return True
		return False

	def openQuickslot(self):
		if self.isStatusByResource (
			'[퀵슬롯 닫힘]', 
			'main_scene_open_loc', 
			0.7, 
			(140, 140, 140), (70, 70, 70),
			(125, 230, 155, 260),
			limit_count=3,
			) == False:
			self.lyb_mouse_click('main_scene_close', custom_threshold=0)
			return True
		return False

	def locationOnQuestArea(self, pb_name, custom_top_level=-1, custom_below_level=-1):
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic[pb_name],
					custom_threshold=0.85,
					custom_flag=1,
					custom_top_level=custom_top_level,
					custom_below_level=custom_below_level,
					custom_rect=(600, 125, 635, 300)
						)
		self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))

		return (loc_x, loc_y), match_rate

	def isAutoQuest(self, limit_count=-1):
		return self.isStatusByResource (
			'[퀘스트 자동 진행 중]', 
			'main_scene_auto_quest_loc', 
			0.5, 
			(255, 255, 255), (150, 150, 150), 
			(250, 220, 400, 320),
			limit_count=limit_count
			)

	def isAutoOn(self, limit_count=-1):
		return self.isStatusByResource (
			'[자동전투]', 
			'auto_on_loc', 
			0.7, 
			(255, 255, 255), (150, 150, 150), 
			(150, 335, 180, 375),
			limit_count=limit_count
			)

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
		if work_name in lybgametalion.LYBTalion.work_list:
			return (lybgametalion.LYBTalion.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
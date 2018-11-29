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
import likeyoubot_blackdesert as lybgamebd
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBBlackDesertScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBBlackDesertScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'init_screen_scene':
			rc = self.init_screen_scene()
		elif self.scene_name == 'google_play_account_select_scene':
			rc = self.google_play_account_select_scene()
		elif self.scene_name == 'main_scene':

			s = time.time()

			rc = self.main_scene()

			e = time.time()
			# self.logger.warn('@ ElapsedTime >> main_scene <<: ' + str(round(e - s, 5)))

		elif self.scene_name == 'repair_service_scene':
			rc = self.repair_service_scene()
		elif self.scene_name == 'login_scene':
			rc = self.login_scene()
		elif self.scene_name == 'signin_scene':
			rc = self.signin_scene()
		elif self.scene_name == 'character_scene':
			rc = self.character_scene()
		elif self.scene_name == 'jeoljeon_mode_death_scene':
			rc = self.jeoljeon_mode_death_scene()
		elif self.scene_name == 'jeoljeon_mode_scene':
			rc = self.jeoljeon_mode_scene()
		elif self.scene_name == 'tutorial_lv1_scene':
			rc = self.tutorial_lv1_scene()
		elif self.scene_name == 'tutorial_lv1_0_scene':
			rc = self.tutorial_lv1_0_scene()
		elif self.scene_name == 'urewanryo_scene':
			rc = self.urewanryo_scene()
		elif self.scene_name == 'tutorial_scene':
			rc = self.tutorial_scene()
		elif self.scene_name == 'death_scene':
			rc = self.death_scene()
		elif self.scene_name == 'character_field_death_scene':
			rc = self.character_field_death_scene()
		elif self.scene_name == 'killed_by_player_scene':
			rc = self.killed_by_player_scene()
		elif self.scene_name == 'character_death_scene':
			rc = self.character_death_scene()
		elif self.scene_name == 'character_death_2_scene':
			rc = self.character_death_2_scene()
		elif self.scene_name == 'gabang_scene':
			rc = self.gabang_scene()
		elif self.scene_name == 'gisul_scene':
			rc = self.gisul_scene()
		elif self.scene_name == 'geomungiun_scene':
			rc = self.geomungiun_scene()
		elif self.scene_name == 'pearl_sangjeom_scene':
			rc = self.pearl_sangjeom_scene()
		elif self.scene_name == 'confirm_scene':
			rc = self.confirm_scene()
		elif self.scene_name == 'jamjeryeok_jeonsu_scene':
			rc = self.jamjeryeok_jeonsu_scene()
		elif self.scene_name == 'nejeongbo_scene':
			rc = self.nejeongbo_scene()
		elif self.scene_name == 'potion_shop_scene':
			rc = self.potion_shop_scene()
		elif self.scene_name == 'select_ure_scene':
			rc = self.select_ure_scene()
		elif self.scene_name == 'mulpum_gume_scene':
			rc = self.mulpum_gume_scene()
		elif self.scene_name == 'npc_scene':
			rc = self.npc_scene()
		elif self.scene_name == 'mulpum_deyeo_scene':
			rc = self.mulpum_deyeo_scene()
		elif self.scene_name == 'tutorial_gisul_scene':
			rc = self.tutorial_gisul_scene()
		elif self.scene_name == 'gwangwonseok_jangchak_scene':
			rc = self.gwangwonseok_jangchak_scene()
		elif self.scene_name == 'jeongye_immu_scene':
			rc = self.jeongye_immu_scene()
		elif self.scene_name == 'youngji_jujeom_scene':
			rc = self.youngji_jujeom_scene()
		elif self.scene_name == 'select_youngjimin_scene':
			rc = self.select_youngjimin_scene()
		elif self.scene_name == 'immu_success_scene':
			rc = self.immu_success_scene()
		elif self.scene_name == 'tobeol_gesipan_scene':
			rc = self.tobeol_gesipan_scene()
		elif self.scene_name == 'sakatu_shop_scene':
			rc = self.sakatu_shop_scene()
		elif self.scene_name == 'banryoe_dongmul_scene':
			rc = self.banryoe_dongmul_scene()
		elif self.scene_name == 'menu_scene':
			rc = self.menu_scene()
		elif self.scene_name == 'banryoe_dongmul_no_saryo_scene':
			rc = self.banryoe_dongmul_no_saryo_scene()
		elif self.scene_name == 'config_scene':
			rc = self.config_scene()
		elif self.scene_name == 'guild_scene':
			rc = self.guild_scene()
		elif self.scene_name == 'tutorial_potion_up_scene':
			rc = self.tutorial_potion_up_scene()
		elif self.scene_name == 'hukjeongryoung_ure_scene':
			rc = self.hukjeongryoung_ure_scene()
		elif self.scene_name == 'hukjeongryoung_soksakim_scene':
			rc = self.hukjeongryoung_soksakim_scene()
		elif self.scene_name == 'sujeong_hapseong_scene':
			rc = self.sujeong_hapseong_scene()
		elif self.scene_name == 'gwangwonseok_hapseong_scene':
			rc = self.gwangwonseok_hapseong_scene()
		elif self.scene_name == 'mail_scene':
			rc = self.mail_scene()
		elif self.scene_name == 'notify_confirm_scene':
			rc = self.notify_confirm_scene()
		elif self.scene_name == 'jongja_shop_scene':
			rc = self.jongja_shop_scene()
		elif self.scene_name == 'mulpum_suryang_scene':
			rc = self.mulpum_suryang_scene()
		elif self.scene_name == 'youngji_scene':
			rc = self.youngji_scene()
		elif self.scene_name == 'tobeol_ready_scene':
			rc = self.tobeol_ready_scene()
		elif self.scene_name == 'tobeol_fail_scene':
			rc = self.tobeol_fail_scene()
		elif self.scene_name == 'tobeol_success_scene':
			rc = self.tobeol_success_scene()
		elif self.scene_name == 'tobeol_success2_scene':
			rc = self.tobeol_success2_scene()			
		elif self.scene_name == 'tobeol_success3_scene':
			rc = self.tobeol_success_scene()		
		elif self.scene_name == 'tobeol_success4_scene':
			rc = self.tobeol_success_scene()	
		elif self.scene_name == 'tobeol_repeat_success_scene':
			rc = self.tobeol_repeat_success_scene()
		elif self.scene_name == 'tobeol_special_success_scene':
			rc = self.tobeol_special_success_scene()
		elif self.scene_name == 'tukbat_scene':
			rc = self.tukbat_scene()
		elif self.scene_name == 'chejip_scene':
			rc = self.chejip_scene()
		elif self.scene_name == 'world_chejip_scene':
			rc = self.world_chejip_scene()
		elif self.scene_name == 'gwaje_scene':
			rc = self.gwaje_scene()
		elif self.scene_name == 'youngjimin_select_scene':
			rc = self.youngjimin_select_scene()
		elif self.scene_name == 'sujeong_hapseong_select_scene':
			rc = self.sujeong_hapseong_select_scene()
		elif self.scene_name == 'gwangwonseok_hapseong_select_scene':
			rc = self.gwangwonseok_hapseong_select_scene()
		elif self.scene_name == 'sujeong_hapseong_progress_scene':
			rc = self.sujeong_hapseong_progress_scene()
		elif self.scene_name == 'daejeon_scene':
			rc = self.daejeon_scene()
		elif self.scene_name == 'tugijang_scene':
			rc = self.tugijang_scene()
		elif self.scene_name == 'tugijang_loading_scene':
			rc = self.tugijang_loading_scene()
		elif self.scene_name == 'tugijang_main_scene':
			rc = self.tugijang_main_scene()
		elif self.scene_name == 'jamjeryeok_dolpa_scene':
			rc = self.jamjeryeok_dolpa_scene()
		elif self.scene_name == 'guild_ure_surak_scene':
			rc = self.guild_ure_surak_scene()
		elif self.scene_name == 'jamjeryeok_dolpa_confirm_scene':
			rc = self.jamjeryeok_dolpa_confirm_scene()
		elif self.scene_name == 'chuksa_scene':
			rc = self.chuksa_scene()
		elif self.scene_name == 'tukbat_jakmul_simgi_scene':
			rc = self.tukbat_jakmul_simgi_scene()
		elif self.scene_name == 'migung_scene':
			rc = self.migung_scene()
		elif self.scene_name == 'migung_matching_scene':
			rc = self.migung_matching_scene()
		elif self.scene_name == 'migung_gecheok_scene':
			rc = self.migung_gecheok_scene()
		elif self.scene_name == 'migung_ready_scene':
			rc = self.migung_ready_scene()
		elif self.scene_name == 'migung_success_scene':
			rc = self.migung_success_scene()
		elif self.scene_name == 'migung_member_success_scene':
			rc = self.migung_member_success_scene()
		elif self.scene_name == 'world_boss_success_scene':
			rc = self.world_boss_success_scene()
		elif self.scene_name == 'world_boss_success_2_scene':
			rc = self.world_boss_success_2_scene()
		elif self.scene_name == 'world_boss_success_3_scene':
			rc = self.world_boss_success_3_scene()
		elif self.scene_name == 'chingu_scene':
			rc = self.chingu_scene()
		elif self.scene_name == 'waiting_for_server_scene':
			rc = self.waiting_for_server_scene()
		elif self.scene_name == 'gachuk_shop_scene':
			rc = self.gachuk_shop_scene()
		elif self.scene_name == 'guild_tobeol_success_scene':
			rc = self.guild_tobeol_success_scene()
		elif self.scene_name == 'login_waiting_scene':
			rc = self.login_waiting_scene()
		elif self.scene_name == 'google_play_store3_scene':
			rc = self.google_play_store_scene()
		elif self.scene_name == 'google_play_store2_scene':
			rc = self.google_play_store_scene()	
		elif self.scene_name == 'google_play_store_scene':
			rc = self.google_play_store_scene()	
		elif self.scene_name == 'mal_gwanri_scene':
			rc = self.mal_gwanri_scene()	
		elif self.scene_name == 'mal_gwanri_move_scene':
			rc = self.mal_gwanri_move_scene()
		elif self.scene_name == 'mal_gwanri_move_suryang_scene':
			rc = self.mal_gwanri_move_suryang_scene()	
		elif self.scene_name == 'sujeong_jangchak_scene':
			rc = self.sujeong_jangchak_scene()
		elif self.scene_name == 'gyobon_shop_scene':
			rc = self.gyobon_shop_scene()
		elif self.scene_name == 'migung_select_scene':
			rc = self.migung_select_scene()	
		elif self.scene_name == 'dogam_scene':
			rc = self.dogam_scene()		
		elif self.scene_name == 'dogam_bogi_scene':
			rc = self.dogam_bogi_scene()
		elif self.scene_name == 'dogam_bogi_dungrok_scene':
			rc = self.dogam_bogi_dungrok_scene()	
		elif self.scene_name == 'iyagi_scene':
			rc = self.iyagi_scene()		
		elif self.scene_name == 'tobeol_gesipan_exchange_scene':
			rc = self.tobeol_gesipan_exchange_scene()	
		elif self.scene_name == 'tobeol_gesipan_exchange_special_scene':
			rc = self.tobeol_gesipan_exchange_special_scene()
		elif self.scene_name == 'jeongjeso_ggeonegi_scene':
			rc = self.jeongjeso_ggeonegi_scene()
		elif self.scene_name == 'jihwiso_scene':
			rc = self.jihwiso_scene()

		else:
			rc = self.else_scene()

		return rc



	def else_scene(self):

		if self.status == 0:
			self.logger.debug('unknown scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def jihwiso_scene(self):
		
		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.status += 1
			resource_name = 'jiwongum_suryeong_loc'
			(loc_x, loc_y), match_rate	= self.game_object.locationResourceOnWindowPart(
										self.window_image,
										resource_name,
										custom_threshold=0.9,
										custom_flag=1,
										custom_rect=(410, 310, 550, 370)									
										)
			self.logger.warn('영지지원금 탐색: ' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)) + '%')
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.logger.info('지원금 수령')
				return self.status
			else:
				self.status = 5
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)		
			self.status = 0

		return self.status

	def jeongjeso_ggeonegi_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.lyb_mouse_click('jeongjeso_ggeonegi_scene_modu', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def tobeol_special_success_scene(self):

		if self.status == 0:
			self.game_object.addStatistic('토벌 클리어 횟수')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 토벌 클리어 감지')
				png_name = self.game_object.save_image('tobeol')
				self.game_object.telegram_send('', image=png_name)	
			self.status = 0

		return self.status


	def tobeol_gesipan_exchange_special_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			# self.lyb_mouse_click('tobeol_gesipan_exchange_special_scene_enter', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status


	def tobeol_gesipan_exchange_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('tobeol_gesipan_exchange_scene_max', custom_threshold=0)
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('tobeol_gesipan_exchange_scene_confirm', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
				
			self.status = 0

		return self.status

	def iyagi_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.set_option('drag_count', 0)
			self.status += 1
		elif self.status == 1:
			self.status += 1
		elif self.status == 2:
			pb_name = 'iyagi_scene_gisul_gebang'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.status = 3
				return self.status

			pb_name = 'iyagi_scene_list'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.status = 4
				return self.status
		elif self.status == 3:
			for i in range(2):
				pb_name = 'iyagi_scene_gisul_list_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
					self.status = 1
					return self.status
			self.lyb_mouse_click('iyagi_scene_gisul_list_2', custom_threshold=0)
			self.status = 1
		elif self.status == 4:
			pb_name = 'iyagi_scene_surak'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(530, 70, 620, 380))
			self.logger.warn(pb_name + ' '+ str((loc_x, loc_y)) + ':' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 99999
			else:
				self.status += 1
		elif self.status == 5:
			drag_count = self.get_option('drag_count')
			if drag_count > 1:
				self.status = 99999
			else:
				self.lyb_mouse_drag('iyagi_scene_drag_bot', 'iyagi_scene_drag_top')
				self.set_option('drag_count', drag_count + 1)
				self.status = 1
		else:
			self.game_object.get_scene('main_scene').set_option('iyagi_start', True)
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def dogam_bogi_dungrok_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('dogam_bogi_dungrok_scene_ok')
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def dogam_bogi_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.set_option('found', False)
			self.status += 1
		elif self.status == 1:	

			pb_name = 'dogam_bogi_scene_bosang'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.95:
				self.lyb_mouse_click(pb_name)
				return self.status

			self.game_object.get_scene('dogam_bogi_dungrok_scene').status = 0
			pb_name = 'dogam_bogi_scene_new'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(410, 120, 620, 320))
			self.logger.warn(pb_name + ' '+ str((loc_x, loc_y)) + ':' + str(match_rate))
			if loc_x != -1:
				self.set_option('found', True)
				self.lyb_mouse_click_location(loc_x, loc_y)				
			else:
				self.status += 1
		elif self.status == 2:
			if self.get_option('found') == True:
				self.status = 99999
			else:
				self.logger.warn('갯수 부족인데도 느낌표 뜨는 버그 감지')
				self.game_object.get_scene('dogam_scene').status = 99999
				self.status += 1
		# elif self.status == 3:
		# 	self.lyb_mouse_click('dogam_bogi_scene_list_0', custom_threshold=0)
		# 	self.status += 1
		# elif self.status == 4:
		# 	self.lyb_mouse_click('dogam_bogi_scene_list_1', custom_threshold=0)
		# 	self.status += 1
		# elif self.status == 5:
		# 	for i in range(2, 8):
		# 		pb_name = 'dogam_bogi_scene_list_' + str(i)
		# 		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 									self.window_image,
		# 									self.game_object.resource_manager.pixel_box_dic[pb_name],
		# 									custom_threshold=0.7,
		# 									custom_flag=1,
		# 									custom_rect=(410, 120, 620, 320))
		# 		self.logger.warn(pb_name + ' '+ str((loc_x, loc_y)) + ':' + str(match_rate))
		# 		if loc_x == -1:
		# 			self.lyb_mouse_click_location(loc_x, loc_y)
		# 			return self.status

		# 	self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def dogam_scene(self):

		self.game_object.current_matched_scene['name'] = ''	
		elapsed_time = time.time() - self.get_checkpoint('start')
		if elapsed_time > 120 and elapsed_time < 150:
			self.logger.warn('도감 진행 시간 초과로 작업 종료')
			self.status = 99999

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			for i in range(4):
				pb_name = 'dogam_scene_tab_new_' + str(i)
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[pb_name],
											custom_threshold=0.7,
											custom_flag=1,
											custom_top_level=(210, 45, 75),
											custom_below_level=(130, 0, 15),
											custom_rect=(80, 60, 130, 380))
				self.logger.debug(pb_name + ' '+ str((loc_x, loc_y)) + ':' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x - 10, loc_y + 20)
					self.set_option('last_status', self.status)
					self.status = 2
					return self.status
			self.status = 99999
		elif self.status == 2:
			self.set_option('drag_count', 0)
			self.lyb_mouse_drag('dogam_scene_drag_top', 'dogam_scene_drag_bottom')
			self.status += 1
		elif self.status >= 3 and self.status < 10:			
			for i in range(5):
				pb_name = 'dogam_scene_new_' + str(i)
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[pb_name],
											custom_threshold=0.7,
											custom_flag=1,
											custom_top_level=(210, 45, 75),
											custom_below_level=(130, 0, 15),
											custom_rect=(140, 70, 440, 360))
				self.logger.debug(pb_name + ' '+ str((loc_x, loc_y)) + ':' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.set_option('sub_last_status', self.status)
					self.status = 11
					return self.status

			if self.status > 3 and self.status % 3 == 0:
				drag_count = self.get_option('drag_count')
				self.set_option('drag_count', drag_count + 1)
				self.lyb_mouse_drag('dogam_scene_drag_bottom', 'dogam_scene_drag_top')
			self.status += 1
		elif self.status == 10:
			self.status = self.get_option('last_status')
		elif self.status == 11:
			self.set_option('list_drag_count', 0)
			self.lyb_mouse_drag('dogam_scene_list_drag_top', 'dogam_scene_list_drag_bottom')
			self.status += 1
		elif self.status >= 12 and self.status < 17:
			pb_name_list = [
				'dogam_scene_list_new',
				'dogam_scene_list_new_0'
			]
			for pb_name in pb_name_list:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[pb_name],
											custom_threshold=0.7,
											custom_flag=1,
											# custom_top_level=(210, 45, 75),
											# custom_below_level=(130, 0, 15),
											custom_rect=(550, 140, 620, 340))
				self.logger.debug(pb_name + ' '+ str((loc_x, loc_y)) + ':' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y + 5)
					self.game_object.get_scene('dogam_bogi_scene').status = 0
					return self.status

			if self.status > 12 and self.status % 3 == 0:
				list_drag_count = self.get_option('list_drag_count')
				self.set_option('list_drag_count', list_drag_count + 1)
				self.lyb_mouse_drag('dogam_scene_list_drag_bottom', 'dogam_scene_list_drag_top')
			self.status += 1
		elif self.status == 17:
			self.status = self.get_option('sub_last_status')
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def migung_select_scene(self):

		if self.status == 0:
			self.logger.debug('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('미궁 개척'):
			self.lyb_mouse_click('migung_select_scene_enter_0', custom_threshold=0)
			self.game_object.get_scene('migung_gecheok_scene').status = 0
			self.status = 99990
		elif self.status == self.get_work_status('미궁 목록'):
			self.lyb_mouse_click('migung_select_scene_enter_1', custom_threshold=0)
			self.game_object.get_scene('migung_scene').status = 0
			self.status = 99990
		elif self.status == 99990:
			self.status += 1
		elif self.status == 99991:
			self.status += 1
		elif self.status == 99992:
			self.status += 1
		elif self.status == 99993:
			current_work = self.game_object.get_scene('main_scene').current_work
			self.game_object.get_scene('main_scene').set_option(current_work + '_end_flag', True)
			self.status = 99999
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def gyobon_shop_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('potion_shop_scene_jeonripum_jeongri')
			self.game_object.interval = self.period_bot(1)
			self.set_option('drag_count', 0)
			self.set_option('iterator', 0)
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('gyobon_shop_scene_modu')
			self.status += 1
		# 	i = self.get_option('iterator')
		# 	resource_pb_name = 'gyobon_shop_scene_s'
		# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 								self.window_image,
		# 								self.game_object.resource_manager.pixel_box_dic[resource_pb_name],
		# 								custom_threshold=0.7,
		# 								custom_flag=1,
		# 								custom_rect=(60, 110 + (65*i), 90, 185 + (65*i)))
		# 	self.logger.warn('교본 탐색 :' + str((loc_x, loc_y)) + ':' + str(match_rate))
		# 	if loc_x != -1:
		# 		self.lyb_mouse_click_location(loc_x, loc_y)
		# 	else:
		# 		self.status += 1

		# 	self.set_option('iterator', i + 1)
		# elif self.status == self.get_work_status('교본상점') + 2:
		# 	drag_count = self.get_option('drag_count')
		# 	if drag_count == None:
		# 		drag_count = 0

		# 	if drag_count > 0:
		# 		self.status = 99999
		# 	else:
		# 		self.set_option('iterator', 0)
		# 		self.set_option('drag_count', drag_count + 1)
		# 		self.lyb_mouse_drag('gyobon_shop_scene_drag_bottom', 'gyobon_shop_scene_drag_top')
		# 		self.game_object.interval = self.period_bot(2)
		# 		self.status -= 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def sujeong_jangchak_scene(self):

		if self.status == 0:
			if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
				self.lyb_mouse_click('main_quest_lv20_sujeong_sequence_0', custom_threshold=0)
				time.sleep(2)
				self.lyb_mouse_click('main_quest_lv20_sujeong_sequence_1', custom_threshold=0)
				time.sleep(2)
				self.lyb_mouse_click('main_quest_lv20_sujeong_sequence_2', custom_threshold=0)
			self.status += 1
		else:
			self.status = 0
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

		return self.status

	def mal_gwanri_move_suryang_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('mal_gwanri_move_suryang_scene_max', custom_threshold=0)
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('mal_gwanri_move_suryang_scene_confirm', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

		return self.status

	def mal_gwanri_move_scene(self):

		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'mal_gwanri_move_scene')
		if match_rate < 0.9:
			self.status = 0
			return self.status

		if self.status == 0:
			pb_name = 'mal_gwanri_move_scene_pet'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.95:
				self.lyb_mouse_click('mal_gwanri_move_scene_0', custom_threshold=0)
			else:
				self.lyb_mouse_click('mal_gwanri_move_scene_move', custom_threshold=0)
				self.game_object.get_scene('mal_gwanri_move_suryang_scene').status = 0
				item_count = self.game_object.get_scene('mal_gwanri_scene').get_option('item_count')
				if item_count == None:
					item_count = 0
				self.game_object.get_scene('mal_gwanri_scene').set_option('item_count', item_count + 1)
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def mal_gwanri_scene(self):
		
		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('말 가방에 넣기'):
			self.lyb_mouse_click('mal_gwanri_scene_potion_tab', custom_threshold=0)
			self.set_option('drag_count', 0)
			self.status += 1
		elif self.status == self.get_work_status('말 가방에 넣기') + 1:
			drag_count = self.get_option('drag_count')
			if drag_count > 10:
				self.status += 1
			else:
				pb_name = 'mal_gwanri_scene_empty_slot'
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if match_rate > 0.95:
					self.status += 1
				else:
					self.lyb_mouse_drag('mal_gwanri_scene_drag_bottom', 'mal_gwanri_scene_drag_top')
					self.set_option('drag_count', drag_count + 1)
		elif self.status == self.get_work_status('말 가방에 넣기') + 2:
			self.lyb_mouse_drag('mal_gwanri_scene_drag_bottom', 'mal_gwanri_scene_drag_top')
			self.status += 1
		elif self.status == self.get_work_status('말 가방에 넣기') + 3:
			self.lyb_mouse_click('mal_gwanri_scene_open_bag')
			self.status += 1
		elif self.status == self.get_work_status('말 가방에 넣기') + 4:
			self.lyb_mouse_click('mal_gwanri_scene_select_move', custom_threshold=0)
			self.set_option('item_count', 0)
			self.set_option('item_row', 0)
			self.status = 10
		elif self.status >= 10 and self.status < 15:
			item_count = self.get_option('item_count')
			item_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'))
			if item_count >= item_limit:
				self.status = 15
			else:
				item_row = self.get_option('item_row')
				slot_index = 14 - self.status
				pb_name = 'mal_gwanri_scene_slot_' + str(slot_index)
				(loc_x, loc_y) = self.get_location(pb_name)
				self.lyb_mouse_click_location2(loc_x, loc_y - item_row*40)
				self.game_object.interval = self.period_bot(1)
				self.game_object.get_scene('mal_gwanri_move_scene').status = 0
				self.status += 1
		elif self.status == 15:
			item_count = self.get_option('item_count')
			item_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'))
			if item_count < item_limit:
				item_row = self.get_option('item_row')
				self.set_option('item_row', item_row + 1)
				self.status = 10
			else:
				self.status += 1
		elif self.status == self.get_work_status('말 가방 모두 꺼내기'):
			self.lyb_mouse_click('mal_gwanri_scene_open_bag')
			self.status += 1
		elif self.status == self.get_work_status('말 가방 모두 꺼내기') + 1:
			self.lyb_mouse_click('mal_gwanri_scene_modu')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

		return self.status

	def google_play_store_scene(self):

		elapsed_time = time.time() - self.get_checkpoint('start')
		if elapsed_time > 120 and elapsed_time < 180:
			self.set_checkpoint('start')
			self.game_object.terminate_application()
			self.status = 0
			return self.status

		if self.status == 0:
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			pb_name = self.scene_name + '_open'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name)
			else:
				self.status += 1
		elif self.status == 2:
			pb_name = self.scene_name + '_update'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name)
			else:
				self.status = 1
		else:
			self.status = 0

		return self.status

	def login_waiting_scene(self):

		return self.login_scene()

	def gachuk_shop_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('potion_shop_scene_jeonripum_jeongri')
			self.status += 1
		elif self.status == self.get_work_status('가축상점'):
			self.lyb_mouse_click('potion_shop_scene_jeonripum_jeongri')
			self.set_option('pet_number', 0)
			self.game_object.interval = self.period_bot(1)
			self.status += 1
		elif self.status == self.get_work_status('가축상점') + 1:
			pet_number = self.get_option('pet_number')
			pet_number_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number'))
			self.logger.info('pet_number:' + str(pet_number) + ' pet_limit:' + str(pet_number_limit))
			if pet_number >= pet_number_limit:
				self.status += 1
			else:
				potion_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'))
				muge_gage_percent = int(self.bar_percent('muge_gage_s', 'muge_gage_m', 'muge_gage_e', adjust=(20, 20, 20), reverse=True))
				self.logger.warn('가방 무게: ' + str(muge_gage_percent) + '/' + str(potion_limit) + '%')
				if muge_gage_percent < potion_limit:
					pixel_box_name = 'pet_shop_list_0'
					self.lyb_mouse_click(pixel_box_name, custom_threshold=0)
					self.game_object.get_scene('mulpum_suryang_scene').set_option('set', int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set')))
				else:
					self.status += 1
				self.set_option('pet_number', pet_number + 1)
			self.game_object.interval = self.period_bot(1)
		elif self.status >= (1000 * 1000) and self.status < (1000 * 1000 * 1000):
			self.status = self.get_work_status('가축상점')
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def waiting_for_server_scene(self):

		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'waiting_for_server_scene')
		if match_rate < 0.9:
			self.status = 0
			return self.status

		last_check_time = self.get_checkpoint('last_check_time')
		elapsed_time = time.time() - last_check_time

		if elapsed_time > 120:
			self.set_checkpoint('last_check_time')
			self.status = 0

		if self.status >= 0 and self.status < 30:
			self.logger.info('서버의 응답을 기다리고 있습니다. - 재시작 카운트: ' + str(self.status) + '/30')
			self.status += 1
		else:
			self.game_object.terminate_application()
			self.status = 0

		return self.status

	def chingu_scene(self):

		if self.status == 0:
			self.lyb_mouse_click('chingu_scene_mokrok', custom_threshold=0)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('chingu_scene_modu_insa')
			self.game_object.interval = self.period_bot(3)
			self.status += 1
		elif self.status == 10:
			limit_page = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'insahagi_page'))
			drag_page = self.get_option('drag_page')
			if drag_page == None:
				drag_page = 0

			if drag_page >= limit_page:
				self.status = 99999
			else:
				self.logger.info('인사하기 페이지: ' + str(drag_page + 1) + '/' + str(limit_page))
				resource_pb_name = 'chingu_scene_insahagi'
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[resource_pb_name],
											custom_threshold=0.6,
											custom_below_level=(60, 70, 110),
											custom_top_level=(255, 255, 255),
											custom_flag=1,
											custom_rect=(500, 100, 550, 340))
				self.logger.warn('인사하기: ' + str((loc_x, loc_y)) + ':' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
				else:
					self.lyb_mouse_drag('chingu_scene_drag_bottom', 'chingu_scene_drag_top')
					self.set_option('drag_page', drag_page + 1)
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')	
			self.status = 0

		return self.status


	def guild_tobeol_success_scene(self):

		if self.status == 0:
			# if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol') == True:
			# 	self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 토벌 클리어 감지')
			# 	png_name = self.game_object.save_image('tobeol')
			# 	self.game_object.telegram_send('', image=png_name)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')	
			self.status = 0

		return self.status

	def tobeol_success2_scene(self):

		pb_name = 'tobeol_success2_scene_end'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		if match_rate > 0.9:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
		else:
			self.game_object.addStatistic('토벌 클리어 횟수')
			self.lyb_mouse_click(pb_name, custom_threshold=0)

		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol') == True:
			self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 토벌 클리어 감지')
			png_name = self.game_object.save_image('tobeol')
			self.game_object.telegram_send('', image=png_name)

		return self.status

	def tobeol_repeat_success_scene(self):
		if self.status == 0:
			self.game_object.addStatistic('토벌 클리어 횟수')	
			self.status += 1
		else:
			pb_name = self.scene_name + '_baro_sijak'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
			else:
				self.lyb_mouse_click(self.scene_name + '_close_icon')

			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 토벌 클리어 감지')
				png_name = self.game_object.save_image('tobeol')
				self.game_object.telegram_send('', image=png_name)
				
			self.status = 0

		return self.status

	def tobeol_success_scene(self):

		if self.status == 0:
			self.game_object.addStatistic('토벌 클리어 횟수')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 토벌 클리어 감지')
				png_name = self.game_object.save_image('tobeol')
				self.game_object.telegram_send('', image=png_name)	
			self.status = 0

		return self.status

	def world_boss_success_3_scene(self):

		return self.world_boss_success_scene()

	def world_boss_success_2_scene(self):

		return self.world_boss_success_scene()

	def world_boss_success_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 월드 보스 클리어 감지')
				png_name = self.game_object.save_image('world_boss')
				self.game_object.telegram_send('', image=png_name)
			self.game_object.get_scene('main_scene').set_option('월드 보스' + '_end_flag', True)
			self.game_object.interval = self.period_bot(3)
			self.status = 0

		return self.status


	def migung_member_success_scene(self):

		if self.status == 0:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 미궁 클리어 감지')
				png_name = self.game_object.save_image('migung')
				self.game_object.telegram_send('', image=png_name)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')	
			self.status = 0

		return self.status

	def migung_success_scene(self):

		if self.status == 0:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 미궁 클리어 이벤트 감지')
				png_name = self.game_object.save_image('migung')
				self.game_object.telegram_send('', image=png_name)
			self.status += 1
		elif self.status == 1:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat') == True:
				self.lyb_mouse_click('migung_success_scene_repeat')
			self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')	
			self.status = 0

		return self.status

	def migung_ready_scene(self):


		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.set_option('invite_count', 0)
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend'))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild'))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open'))
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend') == True:
				self.lyb_mouse_click('migung_ready_scene_friend', custom_threshold=0)
				self.status += 1
			else:
				self.status = 10
		elif self.status >= 2 and self.status < 10:
			pb_name = 'migung_ready_scene_invite_full'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.status = 20
			else:
				invite_count = self.get_option('invite_count')
				invite_count_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'))
				if invite_count >= invite_count_limit:
					self.status = 10
				else:
					resource_pb_name = 'migung_ready_scene_invite'
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
												self.window_image,
												self.game_object.resource_manager.pixel_box_dic[resource_pb_name],
												custom_threshold=0.8,
												custom_flag=1,
												custom_rect=(180, 100, 250, 360))
					self.logger.warn('요청 예약: ' + str(match_rate))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.set_option('invite_count', invite_count + 1)
						self.game_object.interval = self.period_bot(2)
					else:
						self.lyb_mouse_drag('migung_ready_scene_drag_bottom', 'migung_ready_scene_drag_top')
						self.status += 1
		elif self.status == 10:
			self.set_option('invite_count', 0)
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild') == True:
				self.lyb_mouse_click('migung_ready_scene_guild', custom_threshold=0)
				self.status += 1
			else:
				self.status = 20
		elif self.status >= 11 and self.status < 20:
			pb_name = 'migung_ready_scene_invite_full'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.status = 20
			else:
				invite_count = self.get_option('invite_count')
				invite_count_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'))
				if invite_count >= invite_count_limit:
					self.status = 20
				else:
					resource_pb_name = 'migung_ready_scene_invite'
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
												self.window_image,
												self.game_object.resource_manager.pixel_box_dic[resource_pb_name],
												custom_threshold=0.8,
												custom_flag=1,
												custom_rect=(180, 100, 250, 360))
					self.logger.warn('초대 예약: ' + str(match_rate))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.set_option('invite_count', invite_count + 1)
						self.game_object.interval = self.period_bot(2)
					else:
						self.lyb_mouse_drag('migung_ready_scene_drag_bottom', 'migung_ready_scene_drag_top')
						self.status += 1

		elif self.status == 20:
			pb_name = 'migung_ready_scene_open'
			user_open = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open')
			is_open = False
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.8:
				is_open = True

			if user_open == False and is_open == True:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
			elif user_open == True and is_open == False:
				self.lyb_mouse_click(pb_name, custom_threshold=0)

			self.status += 1
		elif self.status == 21:
			self.lyb_mouse_click('migung_ready_scene_start', custom_threshold=0)
			self.status += 1
		elif self.status == 22:
			self.status += 1
		elif self.status == 23:
			self.status += 1
		elif self.status == 24:
			self.logger.warn('화면 전환이 되지 않았습니다. [미궁 개척] 작업을 종료합니다.')
			self.game_object.get_scene('main_scene').set_option('미궁 개척' + '_end_flag', True)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def migung_gecheok_scene(self):

		if self.status == 0:			
			match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'migung_gecheok_scene')
			if match_rate > 0.9:
				self.status += 1
		elif self.status == 1:			
			self.game_object.get_scene('main_scene').set_option('미궁 개척' + '_clicked', True)	
			self.status += 1
		elif self.status == 2:
			self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'))
			user_rank = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'))
			current_rank = 1
			for i in range(1, 9):
				pb_name = 'migung_scene_gecheok_rank_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(str(pb_name) + ':' + str(match_rate))
				if match_rate > 0.98:
					current_rank = i
					break
			diff = abs(user_rank - current_rank)
			if user_rank > current_rank:
				self.lyb_mouse_click('migung_scene_gecheok_rank_plus')
			elif user_rank < current_rank:
				self.lyb_mouse_click('migung_scene_gecheok_rank_minus')
			else:
				# pass
				self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('migung_scene_select')
			self.game_object.get_scene('migung_ready_scene').status = 0
			self.game_object.interval = self.period_bot(3)
			self.set_checkpoint('clicked_select')
			self.status += 1
		elif self.status == 4:
			elapsed_time = time.time() - self.get_checkpoint('clicked_select')
			if elapsed_time > 10:
				self.status = self.get_work_status('미궁 개척')
			else:
				self.logger.warn('화면 전환이 되지 않았습니다. [미궁 개척] 작업을 종료합니다.')
				self.game_object.get_scene('main_scene').set_option('미궁 개척' + '_end_flag', True)
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def migung_matching_scene(self):

		elapsedTime = time.time() - self.get_checkpoint('start')
		if elapsedTime > 60:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			elapsedTime = time.time() - self.get_checkpoint('matching_limit')
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit'))
			if elapsedTime > limit_time:
				self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def migung_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.game_object.get_scene('main_scene').set_option('미궁 목록' + '_clicked', True)	
			pb_name = 'migung_scene_zero'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			# self.logger.debug(match_rate)
			if match_rate > 0.97:
				self.game_object.get_scene('main_scene').set_option('미궁 목록' + '_end_flag', True)
				self.status = 99999
			else:
				self.status += 1
		elif self.status == 2:
			self.logger.debug(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'))
			user_rank = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'))
			current_rank = 1
			for i in range(1, 9):
				pb_name = 'migung_scene_rank_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				# resource_pb_name = 'migung_scene_rank_' + str(i)
				# (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				# 							self.window_image,
				# 							self.game_object.resource_manager.pixel_box_dic[resource_pb_name],
				# 							custom_threshold=0.9,
				# 							custom_flag=1,
				# 							custom_rect=(420, 140, 520, 220))
				if match_rate > 0.98:
					current_rank = i
					break
			diff = abs(user_rank - current_rank)
			if user_rank > current_rank:
				self.lyb_mouse_click('migung_scene_rank_plus')
			elif user_rank < current_rank:
				self.lyb_mouse_click('migung_scene_rank_minus')
			else:
				# pass
				self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('migung_scene_join')
			self.game_object.get_scene('migung_matching_scene').status = 0
			self.game_object.get_scene('migung_matching_scene').set_checkpoint('matching_limit')
			self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status


	def tukbat_jakmul_simgi_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('tukbat_jakmul_simgi_scene_jongja', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def jamjeryeok_dolpa_confirm_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			pb_name = 'jamjeryeok_dolpa_confirm_scene_skip'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
			self.logger.warn(match_rate)
			if match_rate < 0.95:
				self.lyb_mouse_click(pb_name, custom_threshold=0)

			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def guild_ure_surak_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('guild_ure_surak_scene_ok')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def jamjeryeok_dolpa_scene(self):


		# select_mode_click_count = self.get_option('select_mode_click_count')
		# if select_mode_click_count == None:
		# 	select_mode_click_count = 0

		# pb_name = 'jamjeryeok_dolpa_scene_select_mode'
		# match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
		# self.logger.warn('선택모드? ' + str(match_rate))
		# if match_rate < 0.85 and select_mode_click_count < 2:
		# 	self.lyb_mouse_click(pb_name, custom_threshold=0)

		# 	self.set_option('select_mode_click_count', select_mode_click_count + 1)
		# 	return self.status

		# if select_mode_click_count > 1:
		# 	self.status = 99999 
		
		# self.set_option('select_mode_click_count', 0)

		rank_order = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order')
		rank_order_index = lybgamebd.LYBBlackDesert.jamjeryeok_dolpa_rank_order_list.index(rank_order)
		rank = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank')
		rank_index = lybgamebd.LYBBlackDesert.jamjeryeok_dolpa_rank_list.index(rank)

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			for i in range(6):
				option_name = 'full_percent_' + str(i)
				self.set_option(option_name, False)

			self.set_option('item_iterator', 0)
			self.status += 1
		elif self.status == 2:
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank'))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order'))

			item_iterator = self.get_option('item_iterator')
			if item_iterator > 5:
				self.status = 100
			else:
				self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_' + str(item_iterator), custom_threshold=0)
				if rank_order_index == 0:
					self.set_option('item_rank_iterator', 0)
				else:
					self.set_option('item_rank_iterator', rank_index)
				self.game_object.interval = self.period_bot(2)
				self.status += 1
		elif self.status == 3:
			pb_name = 'jamjeryeok_dolpa_scene_100_percent'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn('100%? ' + str(match_rate))
			if match_rate > 0.9:
				self.status += 2
			else:
				item_rank_iterator = self.get_option('item_rank_iterator')
				if item_rank_iterator > rank_index or item_rank_iterator < 0:
					self.status += 1
				else:
					pb_name = 'jamjeryeok_dolpa_scene_rank_' + str(item_rank_iterator)
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
					self.logger.warn('0? ' + str(match_rate))
					if match_rate > 0.9:
						self.status += 1
					else:
						self.lyb_mouse_click(pb_name, custom_threshold=0, delay=3)
						if rank_order_index == 0:
							self.set_option('item_rank_iterator', item_rank_iterator + 1)
						else:
							self.set_option('item_rank_iterator', item_rank_iterator - 1)
			self.game_object.interval = self.period_bot(2)
		elif self.status == 4:
			item_iterator = self.get_option('item_iterator')
			self.set_option('item_iterator', item_iterator + 1)
			self.status -= 2
		elif self.status == 5:
			item_iterator = self.get_option('item_iterator')
			option_name = 'full_percent_' + str(item_iterator)
			self.set_option(option_name, True)
			self.set_option('item_iterator', item_iterator + 1)
			self.status -= 3
		elif self.status == 100:
			is_full_percent_all = True
			for i in range(2):
				option_name = 'full_percent_' + str(i)
				if self.get_option(option_name) == False:
					is_full_percent_all = False
					break

			if is_full_percent_all == True:
				self.status += 1
			else:
				self.status = 200
		elif self.status == 101:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_0', custom_threshold=0)
			self.status += 1
		elif self.status == 102:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_try', custom_threshold=0)
			self.status += 1
		elif self.status == 103:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_1', custom_threshold=0)
			self.status += 1
		elif self.status == 104:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_try', custom_threshold=0)
			self.status = 200
		elif self.status == 200:
			is_full_percent_all = True
			for i in range(2, 6):
				option_name = 'full_percent_' + str(i)
				if self.get_option(option_name) == False:
					is_full_percent_all = False
					break

			if is_full_percent_all == True:
				self.status += 1
			else:
				self.status = 99999
		elif self.status == 201:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_2', custom_threshold=0)
			self.status += 1
		elif self.status == 202:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_try', custom_threshold=0)
			self.status += 1
		elif self.status == 203:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_3', custom_threshold=0)
			self.status += 1
		elif self.status == 204:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_try', custom_threshold=0)
			self.status += 1
		elif self.status == 205:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_4', custom_threshold=0)
			self.status += 1
		elif self.status == 206:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_try', custom_threshold=0)
			self.status += 1
		elif self.status == 207:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_item_5', custom_threshold=0)
			self.status += 1
		elif self.status == 208:
			self.lyb_mouse_click('jamjeryeok_dolpa_scene_try', custom_threshold=0)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def tugijang_main_scene(self):

		if self.status == 0:
			tugijang_count = self.game_object.get_scene('tugijang_scene').get_option('tugijang_count')
			if tugijang_count == None:
				tugijang_count = 0

			self.game_object.get_scene('tugijang_scene').set_option('tugijang_count', tugijang_count + 1)

			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			elapsedTime = time.time() - self.get_checkpoint('start')
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'))
			self.loggingElapsedTime('투기장 진행 시간', int(elapsedTime), limit_time, period=30)
			if elapsedTime > limit_time:
				self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def tugijang_loading_scene(self):

		if self.status == 0:
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			elapsedTime = time.time() - self.get_checkpoint('start')
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match'))
			self.loggingElapsedTime('매칭 중..', int(elapsedTime), limit_time, period=5)
			if elapsedTime > limit_time:
				self.status += 1
		else:
			self.logger.warn('매칭 취소')
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def tugijang_scene(self):

		if self.status == 0:
			self.status += 1
			self.set_option('tugijang_count', 0)
		elif self.status == 1:
			self.lyb_mouse_click('tugijang_scene_receive', custom_threshold=0)
			self.status += 1
		elif self.status == 2:
			tugijang_count = self.get_option('tugijang_count')
			limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'))
			if tugijang_count < limit_count:
				self.logger.warn('투기장 횟수: ' + str(tugijang_count + 1) + ' / ' + str(limit_count))
				self.lyb_mouse_click('tugijang_scene_start')
				self.game_object.get_scene('tugijang_loading_scene').status = 0
				self.game_object.get_scene('tugijang_main_scene').status = 0
			else:
				self.logger.warn('투기장 종료: ' + str(tugijang_count) + ' / ' + str(limit_count))
				self.game_object.get_scene('daejeon_scene').status = 99999
				self.game_object.get_scene('main_scene').set_option('투기장' + '_end_flag', True)
				self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def daejeon_scene(self):

		if self.status == 0:
			self.status = 10
		elif self.status == 10:			
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'))
			is_clicked = self.lyb_mouse_click('daejeon_scene_start', custom_threshold=0)
			if is_clicked == False:
				self.status = 99999
		elif self.status == self.get_work_status('투기장'):
			self.status = 10
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status


	def sujeong_hapseong_progress_scene(self):

		return self.status

	def youngjimin_select_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('youngjimin_select_scene_all')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def gwaje_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			is_clicked = self.lyb_mouse_click('gwaje_scene_ilil_gwaje', custom_threshold=0)
			self.status += 1
		elif self.status >= 2 and self.status < 4:
			is_clicked = self.lyb_mouse_click('gwaje_scene_receive_all')
			if is_clicked == False:
				self.status = 4
			else:
				self.game_object.interval = self.period_bot(2)
				self.status += 1
		elif self.status == 4:
			is_clicked = self.lyb_mouse_click('gwaje_scene_receive_5')
			if is_clicked == True:
				self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == 5:
			is_clicked = self.lyb_mouse_click('gwaje_scene_receive_10')
			if is_clicked == True:
				self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == 6:
			is_clicked = self.lyb_mouse_click('gwaje_scene_receive_15')
			if is_clicked == True:
				self.game_object.interval = self.period_bot(2)
			self.status = 99999
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def world_chejip_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status >= 1 and self.status < 9:
			chejip_resource_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(self.status - 1))
			chejip_resource_index = lybgamebd.LYBBlackDesert.chejip_list.index(chejip_resource_name)
			chejip_place_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(self.status - 1))
			chejip_place_index = lybgamebd.LYBBlackDesert.chejip_place_list.index(chejip_place_name)

			if chejip_resource_index == len(lybgamebd.LYBBlackDesert.chejip_list) - 1:
				self.logger.warn('채집 ' + str(self.status) + '번 설정 없음')
				self.status += 1
			else:
				resource_pb_name = 'chejip_resource_' + str(chejip_resource_index)
				place_pb_name = 'world_chejip_place_' + str(int(chejip_resource_index / 4)) + str(chejip_place_index)

				self.set_option('resource_pb_name', resource_pb_name)
				self.set_option('place_pb_name', place_pb_name)
				self.set_option('resource_name', chejip_resource_name)

				self.logger.warn(resource_pb_name + ':' + place_pb_name)

				self.logger.warn('채집 ' + str(self.status) + '번 ' + chejip_resource_name + ' ' + str(chejip_resource_index))
				
				if chejip_resource_index <= 5:
					self.status += 110
				else:
					self.status += 210
		elif self.status >= 11 and self.status < 19:

			resource_pb_name = self.get_option('resource_pb_name')
			resource_name = self.get_option('resource_name')

			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[resource_pb_name],
										custom_flag=1,
										custom_rect=(5, 90, 55, 385))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.game_object.interval = self.period_bot(2)
				self.status += 10
			else:
				self.logger.warn(resource_name + ' 탐색 실패')
				self.status += 1
				self.status -= 10

			# for i in range(4):
			# 	# self.logger.debug(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)))
			# 	# self.logger.debug(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i)))
			# 	chejip_resource_index = lybgamebd.LYBBlackDesert.chejip_list.index(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)))
			# 	chejip_place_index = lybgamebd.LYBBlackDesert.chejip_place_list.index(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i)))
			# 	self.logger.warn(str(chejip_resource_index) + ':' + str(chejip_place_index))
		elif self.status >= 21 and self.status < 29:
			place_pb_name = self.get_option('place_pb_name')
			self.lyb_mouse_click(place_pb_name, custom_threshold=0)
			self.game_object.get_scene('youngjimin_select_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
			self.status -= 20
		elif self.status >= 111 and self.status < 119:
			self.lyb_mouse_drag('world_chejip_scene_drag_top', 'world_chejip_scene_drag_bottom')
			self.game_object.interval = self.period_bot(2)
			self.status -= 100
		elif self.status >= 211 and self.status < 219:
			self.lyb_mouse_drag('world_chejip_scene_drag_bottom', 'world_chejip_scene_drag_top')
			self.game_object.interval = self.period_bot(2)
			self.status -= 200
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)	
			self.status = 0

		return self.status


	def chejip_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('chejip_scene_world_chejip')
			self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)	
			self.status = 0

		return self.status


	def chuksa_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('chuksa_scene_all', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def tukbat_scene(self):

		if self.status == 0:
			self.set_option('tukbat_count', 0)
			self.status += 1
		elif self.status == 1:
			tukbat_count = self.get_option('tukbat_count')
			self.set_option('tukbat_count', tukbat_count + 1)

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tukbat_scene_modu_suhwak')
			self.logger.warn('모두 수확 감지: ' + str(int(match_rate*100)) + '%')
			if match_rate > 0.9:
				self.lyb_mouse_click('tukbat_scene_modu_suhwak')
				self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('tukbat_scene_right', custom_threshold=0)
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == 3:
			tukbat_count = self.get_option('tukbat_count')

			# 텃밭 갯수
			tukbat_user_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'))
			if tukbat_count > tukbat_user_count - 1:
				self.set_option('tukbat_count', 0)
				self.status += 1
			else:
				self.status -= 2
		elif self.status == 4:
			tukbat_count = self.get_option('tukbat_count')

			# 텃밭 갯수
			tukbat_user_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'))
			if tukbat_count > tukbat_user_count - 1:
				self.status = 99999 
			else:
				self.lyb_mouse_click('tukbat_scene_jakmul_simgi')
				self.game_object.get_scene('tukbat_jakmul_simgi_scene').status = 0
				self.set_option('tukbat_count', tukbat_count + 1)
				self.status += 1
		elif self.status == 5:
			self.lyb_mouse_click('tukbat_scene_right', custom_threshold=0)
			self.game_object.interval = self.period_bot(2)
			self.status -= 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def tobeol_fail_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			tobeol_index = self.game_object.get_scene('tobeol_gesipan_scene').get_option('tobeol_index')
			tobeol_drag_index = self.game_object.get_scene('tobeol_gesipan_scene').get_option('tobeol_drag_index')

			if tobeol_index != None and tobeol_drag_index != None:			
				fail_count = self.game_object.get_scene('tobeol_gesipan_scene').get_option('tobeol_fail_' + str(tobeol_drag_index) + '_' + str(tobeol_index))
				if fail_count == None:
					fail_count = 0

				self.game_object.get_scene('tobeol_gesipan_scene').set_option('tobeol_fail_' + str(tobeol_drag_index) + '_' + str(tobeol_index), fail_count + 1)
				if self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update') == True:
					i = tobeol_drag_index*5 + tobeol_index
					self.set_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i), fail_count + 1)

			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tobeol_ready_scene(self):

		# for i in range(0, 10):
		# 	pb_name = 'tobeol_number_' + str(i)
		# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 				self.window_image,
		# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
		# 				custom_top_level=(255, 255, 255),
		# 				custom_below_level=(100, 100, 100),
		# 				custom_threshold=0.7,
		# 				custom_flag=1,
		# 				custom_rect=(425, 150, 455, 170)
		# 				)
		# 	self.logger.warn(str(i) + ' -- ' + str((loc_x, loc_y)) + ':' + str(match_rate))



		# return self.status

		elapsedTime = time.time() - self.get_checkpoint('start')
		if elapsedTime > 60:
			self.status = 0
			
		if self.status == 0:
			self.set_checkpoint('start')
			# self.game_object.getImageLocation(self.window_image, (420, 150, 460, 170)).save('test_ocr.png')
			self.status += 1
		elif self.status == 1:
			tobeol_index = self.game_object.get_scene('tobeol_gesipan_scene').get_option('tobeol_index')
			tobeol_drag_index = self.game_object.get_scene('tobeol_gesipan_scene').get_option('tobeol_drag_index')

			tobeol_degrade_number = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number'))
			if tobeol_degrade_number > 0:
				self.logger.warn('[토벌 단계 조정] ' + str(tobeol_drag_index) + '드래깅, ' + str(tobeol_index) +'번째 => ' + str(tobeol_degrade_number) + '단계 낮춤')
				for i in range(int(tobeol_degrade_number)):
					self.lyb_mouse_click('tobeol_ready_scene_degrade', custom_threshold=0)
					time.sleep(0.5)
			else:
				if tobeol_index != None and tobeol_drag_index != None:
					fail_count = self.game_object.get_scene('tobeol_gesipan_scene').get_option('tobeol_fail_' + str(tobeol_drag_index) + '_' + str(tobeol_index))
					if fail_count != None and fail_count > 0:
						self.logger.warn('[토벌 단계 조정] ' + str(tobeol_drag_index) + '드래깅, ' + str(tobeol_index) +'번째 => ' + str(fail_count) + '단계 하락')
						for i in range(int(fail_count)):
							self.lyb_mouse_click('tobeol_ready_scene_degrade', custom_threshold=0)
							time.sleep(0.5)

			self.status += 1
		elif self.status == 2:
			pb_name = 'tobeol_ready_scene_start_special'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' +str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.status = 0
				return self.status

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tobeol_ready_scene_start_0')
			self.logger.warn('tobeol_ready_scene_start_0: ' +str(match_rate))
			if match_rate > 0.95:
				self.status = 99999
			else:
				self.lyb_mouse_click('tobeol_ready_scene_start_0', custom_threshold=0)
				self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def youngji_scene(self):

		if self.status == 0:
			self.status = self.get_work_status('영지')		
		elif self.status == self.get_work_status('영지'):
			self.lyb_mouse_click('youngji_hq')
			self.game_object.get_scene('jeongjeso_ggeonegi_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('영지') + 1:
			pb_name = 'youngji_scene_info_off'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.7,
										custom_flag=1,
										custom_top_level=(180,180,180),
										custom_below_level=(140,140,140),
										custom_rect=(510, 340, 550, 380))
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status += 1
		elif self.status == self.get_work_status('영지') + 2:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money') == True:
				self.logger.info('영지 지원금')
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
											self.window_image,
											'youngji_money_loc',
											custom_threshold=0.7,
											custom_flag=1,
											custom_rect=(230, 230, 420, 310))
				self.logger.warn('영지지원금 탐색: ' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)) + '%')
				if loc_x != -1:
					self.game_object.get_scene('jihwiso_scene').status = 0
					self.lyb_mouse_click_location(loc_x, loc_y)
			self.set_option('last_status', self.status + 1)
			self.status = self.get_work_status('영지') + 100	
		elif self.status == self.get_work_status('영지') + 3:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone') == True:
				self.logger.info('블랙스톤')
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
											self.window_image,
											'youngji_jeongjeso_loc',
											custom_threshold=0.7,
											custom_flag=1,
											custom_rect=(160, 90, 550, 340))
				self.logger.warn('정제소 탐색: ' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)) + '%')
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.status += 2
		elif self.status == self.get_work_status('영지') + 4:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['youngji_ggoenegi'],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(200, 200, 450, 340))
			self.logger.warn('꺼내기 탐색: ' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)) + '%')
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.logger.warn('정제소 꺼내기를 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
			self.status += 1
		elif self.status == self.get_work_status('영지') + 5:
			self.lyb_mouse_click('youngji_hq')
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('영지') + 6:

			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat') == True:
				self.logger.info('텃밭')
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
											self.window_image,
											'youngji_tukbat_loc',
											custom_threshold=0.7,
											custom_flag=1,
											custom_rect=(160, 90, 550, 340))
				self.logger.warn('텃밭 탐색: ' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)) + '%')
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.status += 2
		elif self.status == self.get_work_status('영지') + 7:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['youngji_jakmulgwanri'],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(200, 200, 450, 340))
			if loc_x != -1:
				self.game_object.get_scene('tukbat_scene').status = 0
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.logger.warn('작물 관리를 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
			self.status += 1
		elif self.status == self.get_work_status('영지') + 8:
			self.lyb_mouse_click('youngji_hq')
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('영지') + 9:

			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa') == True:
				self.logger.info('축사')
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
											self.window_image,
											'youngji_chuksa_loc',
											custom_threshold=0.7,
											custom_flag=1,
											custom_rect=(160, 90, 550, 340))
				self.logger.warn('축사 탐색: ' + str((loc_x, loc_y)) + ' : ' + str(int(match_rate*100)) + '%')
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.status += 2
		elif self.status == self.get_work_status('영지') + 10:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['youngji_chuksa_gwanri'],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(200, 200, 450, 340))
			if loc_x != -1:
				self.game_object.get_scene('chuksa_scene').status = 0
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.logger.warn('축사 관리를 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
			self.status += 1
		elif self.status == self.get_work_status('영지') + 11:
			self.lyb_mouse_click('youngji_hq')
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('영지') + 12:

			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip') == True:
				self.logger.info('채집')
			# for i in range(4):
			# 	self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)))
				self.lyb_mouse_click('youngji_scene_youngjimin', custom_threshold=0)
				self.status += 1
			else:
				self.status += 2
		elif self.status == self.get_work_status('영지') + 13:
			# for i in range(4):
			# 	self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)))
			self.lyb_mouse_click('youngji_scene_chejip', custom_threshold=0)
			self.game_object.get_scene('chejip_scene').status = 0
			self.status += 1		
		elif self.status == self.get_work_status('영지') + 100:
			self.lyb_mouse_click('youngji_hq')
			self.status = self.get_option('last_status')
		elif self.status == self.get_work_status('토벌 게시판'):
			self.game_object.get_scene('main_scene').set_option('토벌 게시판' + '_clicked', True)	
			self.lyb_mouse_click('youngji_hq')
			self.game_object.get_scene('tobeol_gesipan_scene').status = self.status
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'youngji_scene_info')
			if match_rate < 0.8:
				self.lyb_mouse_click('youngji_scene_info', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 2:
			(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										'youngji_toboel_gesipan_loc',
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(160, 90, 550, 340))
			self.logger.warn('토벌 게시판: ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.logger.warn('토벌 게시판을 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
				self.status = 99999
		elif self.status == self.get_work_status('토벌 게시판') + 3:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['youngji_immu_ipjang'],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(200, 200, 450, 340))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 0
			else:
				self.logger.warn('토벌 게시판 임무 입장을 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
				self.status = 99999		
		elif self.status == self.get_work_status('미궁 목록'):
			self.game_object.get_scene('main_scene').set_option('미궁 목록' + '_clicked', True)	
			self.lyb_mouse_click('youngji_hq')
			self.game_object.get_scene('migung_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('미궁 목록') + 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'youngji_scene_info')
			if match_rate < 0.8:
				self.lyb_mouse_click('youngji_scene_info', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('미궁 목록') + 2:
			(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										'youngji_migung_loc',
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(160, 90, 550, 340))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.logger.warn('탐험의 문을 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
				self.status = 99999
		elif self.status == self.get_work_status('미궁 목록') + 3:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['youngji_migung_mokrok'],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(200, 200, 450, 340))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 0
			else:
				self.logger.warn('탐험의 문을 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
				self.status = 99999		
		elif self.status == self.get_work_status('미궁 개척'):
			self.game_object.get_scene('main_scene').set_option('미궁 개척' + '_clicked', True)	
			self.lyb_mouse_click('youngji_hq')
			self.game_object.get_scene('migung_gecheok_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('미궁 개척') + 1:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'youngji_scene_info')
			if match_rate < 0.8:
				self.lyb_mouse_click('youngji_scene_info', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('미궁 개척') + 2:
			(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										'youngji_migung_loc',
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(160, 90, 550, 340))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.logger.warn('미궁을 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
				self.status = 99999
		elif self.status == self.get_work_status('미궁 개척') + 3:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['youngji_migung_gecheok'],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(200, 200, 450, 340))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status = 0
			else:
				self.logger.warn('미궁개척을 찾지 못했습니다. 지휘소 근처에 위치 시키세요.')
				self.status = 99999
		elif self.status == 99998:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0				
		else:
			self.status = 99998

		return self.status

	def mulpum_suryang_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			potion_set = self.get_option('set')
			# potion_set = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set'))
			if potion_set != 10 and potion_set != 50 and potion_set != 100:
				potion_set = 10

			self.lyb_mouse_click('mulpum_suryang_scene_plus_' + str(potion_set))
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def notify_confirm_scene(self):

		if self.check_migung_invite() == True:
			self.logger.info('미궁 초대 인식')
			return True
		else:
			self.lyb_mouse_click('notify_confirm_scene_ok')

		return self.status

	def mail_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('mail_scene_tab_1', custom_threshold=0)
			self.status += 1
		elif self.status == 2:			
			self.lyb_mouse_click('mail_scene_refresh', custom_threshold=0)
			self.status += 1
		elif self.status >= 3 and self.status < 10:
			self.status += 1

			pb_name = 'mail_scene_mulpum'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pb_name],
				custom_threshold=0.9,
				custom_flag=1,
				custom_rect=(530, 130, 630, 340)
				)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				return self.status			

			self.status = 10
		elif self.status == 10:
			self.lyb_mouse_click('mail_scene_tab_0', custom_threshold=0)
			self.status += 1
		elif self.status == 11:
			self.lyb_mouse_click('mail_scene_refresh', custom_threshold=0)
			self.status += 1
		elif self.status == 12:
			self.lyb_mouse_click('mail_scene_receive_all', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

		
	def gwangwonseok_hapseong_select_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong')
			rank_index = lybgamebd.LYBBlackDesert.sujeong_rank_list.index(rank_name)
			self.logger.warn(rank_name)
			self.lyb_mouse_click('sujeong_hapseong_select_scene_rank_' + str(rank_index), custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def gwangwonseok_hapseong_scene(self):

		if self.status == 0:
			self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto'))
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto') == False:
				self.set_option('limit_hapseong_count', 0)
				self.status = 100
			else:
				self.status += 1
		elif self.status == 1:
			is_clicked = self.lyb_mouse_click('sujeong_hapseong_scene_auto_hapseong')
			self.game_object.get_scene('gwangwonseok_hapseong_select_scene').status = 0
			self.status = 99999
		elif self.status == 100:
			is_clicked = self.lyb_mouse_click('sujeong_hapseong_scene_auto_select', custom_threshold=0)
			self.status += 1
		elif self.status == 101:
			limit_hapseong_count = self.get_option('limit_hapseong_count')
			if limit_hapseong_count > 100:
				self.status += 1
			else:
				(e_loc_x, e_loc_y) = self.get_location('gwangwonseok_hapseong_scene_rank_0')
				(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x, e_loc_y)
				rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong')
				rank_index = lybgamebd.LYBBlackDesert.sujeong_rank_list.index(rank_name)
				is_there = False
				for i in range(rank_index + 1):
					pb = self.get_center_pixel_info('gwangwonseok_hapseong_scene_rank_' + str(i))
					pb_rgb = pb[1]
					if abs(pb_rgb[0] - r) < 20 and abs(pb_rgb[1] - g) < 20 and abs(pb_rgb[2] - b) < 20:
						self.lyb_mouse_click('gwangwonsoek_hapseong_scene_hapseong')
						self.game_object.interval = self.period_bot(3)
						self.status += 1
						is_there = True
						break
				
				if is_there == False:
					self.status = 99999
				self.set_option('limit_hapseong_count', limit_hapseong_count + 1)

		elif self.status == 102:
			self.status = 100
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def sujeong_hapseong_select_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong')
			rank_index = lybgamebd.LYBBlackDesert.sujeong_rank_list.index(rank_name)
			self.lyb_mouse_click('sujeong_hapseong_select_scene_rank_' + str(rank_index), custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def sujeong_hapseong_scene(self):

		if self.status == 0:
			self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto'))
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto') == False:
				self.set_option('limit_hapseong_count', 0)
				self.status = 100
			else:
				self.status += 1
		elif self.status == 1:
			is_clicked = self.lyb_mouse_click('sujeong_hapseong_scene_auto_hapseong')
			self.game_object.get_scene('sujeong_hapseong_select_scene').status = 0
			self.status = 99999
		elif self.status == 100:
			is_clicked = self.lyb_mouse_click('sujeong_hapseong_scene_auto_select', custom_threshold=0)
			self.status += 1
		elif self.status == 101:
			limit_hapseong_count = self.get_option('limit_hapseong_count')
			if limit_hapseong_count > 100:
				self.status += 1
			else:
				(e_loc_x, e_loc_y) = self.get_location('sujeong_hapseong_scene_rank_0')
				(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x, e_loc_y)
				rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong')
				rank_index = lybgamebd.LYBBlackDesert.sujeong_rank_list.index(rank_name)
				is_there = False
				for i in range(rank_index + 1):
					pb = self.get_center_pixel_info('sujeong_hapseong_scene_rank_' + str(i))
					pb_rgb = pb[1]
					self.logger.warn(str(pb_rgb) + ' ' + str((r, g, b)))
					if abs(pb_rgb[0] - r) < 20 and abs(pb_rgb[1] - g) < 20 and abs(pb_rgb[2] - b) < 20:
						self.lyb_mouse_click('sujeong_hapseong_scene_hapseong')
						self.game_object.interval = self.period_bot(3)
						self.status += 1
						is_there = True
						break
				
				if is_there == False:
					self.status = 99999
				self.set_option('limit_hapseong_count', limit_hapseong_count + 1)
		elif self.status == 102:
			self.status = 100
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def hukjeongryoung_soksakim_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == self.get_work_status('흑정령 - 흑정령 의뢰'):
			self.lyb_mouse_click('hukjeongryoung_soksakim_scene_ure', custom_threshold=0)
			self.status = 0
		elif self.status == self.get_work_status('흑정령 - 검은 기운'):
			self.lyb_mouse_click('hukjeongryoung_soksakim_scene_black', custom_threshold=0)
			self.status = 0
		elif self.status == self.get_work_status('흑정령 - 수정 합성'):
			self.lyb_mouse_click('hukjeongryoung_soksakim_scene_sujung_hapseong', custom_threshold=0)
			self.status = 0
		elif self.status == self.get_work_status('흑정령 - 광원석 합성'):
			self.lyb_mouse_click('hukjeongryoung_soksakim_scene_gwangwonseok_hapseong', custom_threshold=0)
			self.status = 0
		elif self.status == self.get_work_status('흑정령 - 잠재력 돌파'):
			self.lyb_mouse_click('hukjeongryoung_soksakim_scene_jamjeryoek_dolpa', custom_threshold=0)
			self.game_object.get_scene('jamjeryeok_dolpa_scene').status = 0
			self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def hukjeongryoung_ure_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic['hukjeongryoung_ure_scene_accept'],
				custom_threshold=0.9,
				custom_flag=1,
				custom_rect=(510, 100, 630, 330)
				)
			self.logger.warn('의뢰: ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def tutorial_potion_up_scene(self):

		self.lyb_mouse_drag('tutorial_potion_up_drag_bottom', 'tutorial_potion_up_drag_top', delay=2)

		return self.status

	def guild_scene(self):

		if self.status == 0:
			self.set_option('ure_surak_index', 0)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('guild_scene_chukseok')
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('guild_scene_ure', custom_threshold=0)
			self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('guild_scene_modu_jeap', custom_threshold=0)
			self.status += 4
		# elif self.status >= 4 and self.status < 7:
		# 	self.lyb_mouse_drag('guild_scene_ure_drag_bottom', 'guild_scene_ure_drag_top')
		# 	self.status += 1
		elif self.status == 7:
			ure_surak_index = self.get_option('ure_surak_index')
			if ure_surak_index > 1:
				self.status += 1
			else:
				(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
					self.window_image,
					'guild_scene_ure_surak_loc',
					custom_threshold=0.7,
					custom_flag=1,
					custom_rect=(570, 200 + (80*ure_surak_index), 600, 280 + (80*ure_surak_index))
					)
				self.logger.warn('길드 의뢰: ' + str(match_rate))
				if loc_x != -1:
					self.game_object.get_scene('guild_ure_surak_scene').status = 0
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status = 99999
				else:
					self.set_option('ure_surak_index', ure_surak_index + 1)
		elif self.status == 8:
			self.lyb_mouse_drag('guild_scene_ure_drag_bottom', 'guild_scene_ure_drag_top')
			self.status += 1
		elif self.status == 9:
			(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
				self.window_image,
				'guild_scene_ure_surak_loc',
				custom_threshold=0.7,
				custom_flag=1,
				custom_rect=(570, 160, 600, 300),
				)
			self.logger.warn('길드 의뢰: ' + str(match_rate))
			if loc_x != -1:
				self.game_object.get_scene('guild_ure_surak_scene').status = 0
				self.lyb_mouse_click_location(loc_x, loc_y)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def config_scene(self):

		if self.status == self.get_work_status('캐릭터 변경'):
			self.lyb_mouse_click('config_scene_account', custom_threshold=0)
			self.status += 1
		elif self.status == self.get_work_status('캐릭터 변경') + 1:
			self.lyb_mouse_click('config_scene_character_byoenkyoung', custom_threshold=0)
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')

		return self.status

	def banryoe_dongmul_no_saryo_scene(self):

		self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

		return self.status

	def menu_scene(self):
		if self.status == 0:
			self.status += 1
		elif self.status == 10:
			self.lyb_mouse_click('menu_scene_jeoljeon_mode', custom_threshold=0)
			self.game_object.get_scene('jeoljeon_mode_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('반려동물 - 먹이주기'):
			self.lyb_mouse_click('menu_scene_banryoe_dongmul', custom_threshold=0)
			self.game_object.get_scene('banryoe_dongmul_scene').status = self.status
			self.status = 0
		elif self.status == self.get_work_status('우편함'):
			# self.set_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean', False)
			self.lyb_mouse_click('menu_scene_mail', custom_threshold=0)
			self.game_object.get_scene('mail_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('이야기'):
			self.lyb_mouse_click('menu_scene_iyagi', custom_threshold=0)
			self.game_object.get_scene('iyagi_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('도감'):
			self.lyb_mouse_click('menu_scene_dogam', custom_threshold=0)
			self.game_object.get_scene('dogam_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('캐릭터 변경'):
			self.lyb_mouse_click('menu_scene_config', custom_threshold=0)
			self.game_object.get_scene('config_scene').status = self.status
			self.status = 0
		elif self.status == self.get_work_status('길드'):
			self.lyb_mouse_click('menu_scene_guild', custom_threshold=0)
			self.game_object.get_scene('guild_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('미궁 개척'):
			self.lyb_mouse_click('menu_scene_migung', custom_threshold=0)			
			self.game_object.get_scene('migung_select_scene').status = self.status
			self.status = 0
		elif self.status == self.get_work_status('미궁 목록'):
			self.lyb_mouse_click('menu_scene_migung', custom_threshold=0)			
			self.game_object.get_scene('migung_select_scene').status = self.status
			self.status = 0
		elif self.status == self.get_work_status('토벌 게시판'):
			self.lyb_mouse_click('menu_scene_tobeol', custom_threshold=0)			
			self.game_object.get_scene('tobeol_gesipan_scene').status = self.status
			self.status = 0
		elif self.status == self.get_work_status('인사하기'):
			self.lyb_mouse_click('menu_scene_chingu', custom_threshold=0)
			self.game_object.get_scene('chingu_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('과제'):
			self.lyb_mouse_click('menu_scene_gwaje', custom_threshold=0)
			self.game_object.get_scene('guild_scene').status = 0
			self.status = 0
		elif self.status == self.get_work_status('투기장'):
			self.lyb_mouse_click('menu_scene_daejeon', custom_threshold=0)
			self.game_object.get_scene('daejeon_scene').status = self.status
			self.status = 0
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def banryoe_dongmul_scene(self):

		if self.status == 0:
			self.status = self.get_work_status('반려동물 - 먹이주기') 
		elif self.status == self.get_work_status('반려동물 - 먹이주기'):
			self.status += 1
		elif self.status == self.get_work_status('반려동물 - 먹이주기') + 1:
			pb_name = 'banryoe_dongmul_scene_manbok'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pb_name],
				custom_below_level=(230, 230, 230),
				custom_top_level=(255, 255, 255),
				custom_flag=1,
				custom_rect=(230, 270, 260, 320)
				)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if loc_x == -1:
				self.lyb_mouse_click('banryoe_dongmul_scene_manbok', custom_threshold=0)
			self.set_option('pet_iterator', 0)
			self.status += 1
		elif self.status == self.get_work_status('반려동물 - 먹이주기') + 2:
			self.set_option('saryo_index', 0)
			self.status += 1
		elif self.status == self.get_work_status('반려동물 - 먹이주기') + 3:
			pet_iterator = self.get_option('pet_iterator')
			if pet_iterator > 2:
				self.lyb_mouse_drag('banryoe_dongmul_scene_drag_bottom', 'banryoe_dongmul_scene_drag_top')
				self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('반려동물 - 먹이주기') + 4:
			pet_iterator = self.get_option('pet_iterator')
			if pet_iterator >= int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PET + 'number')):
				self.status = 99999
			else:
				# loc_x, loc_y = self.get_location('banryoe_dongmul_scene_pet_top')
				# self.logger.debug((loc_x, loc_y + 60*pet_iterator))
				# self.lyb_mouse_click_location2(loc_x, loc_y + 60*pet_iterator)
				if pet_iterator > 1:
					loc_y_offset = 2
					loc_y_adjust = 30
				else:
					loc_y_offset = pet_iterator
					loc_y_adjust = 0
				self.set_option('pet_iterator', pet_iterator + 1)

				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic['banryoe_dongmul_scene_active_pet'],
					custom_flag=1,
					custom_rect=(590, 120 + loc_y_offset*60, 630, 170 + loc_y_offset*60 + loc_y_adjust)
					)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.set_option('found_saryo', False)
					self.status += 1
				else:
					self.status -= 1

		elif self.status == self.get_work_status('반려동물 - 먹이주기') + 5:
			saryo_index = self.get_option('saryo_index')
			pb_name = 'banryoe_dongmul_scene_saryo_empty_' + str(saryo_index)
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn("사료 "+str(saryo_index)+" :" + str(match_rate))
			if match_rate < 0.95:
				self.lyb_mouse_click('banryoe_dongmul_scene_saryo_' + str(saryo_index))
				self.set_option('found_saryo', True)
				saryo_index = 2

			saryo_index += 1
			if saryo_index > 2: 
				if self.get_option('found_saryo') == True:
					self.status = self.get_work_status('반려동물 - 먹이주기') + 2
				else:
					if self.game_object.get_scene('main_scene').current_work != None:
						current_work = self.game_object.get_scene('main_scene').current_work
						self.logger.warn('반려동물 사료가 없습니다. 사료 구매 시퀀스를 실행합니다.')
						self.game_object.get_scene('main_scene').status = (1000 * 1000) + self.get_work_status(current_work)
						self.game_object.get_scene('main_scene').set_option('saryo_sequence_status', 0)
						self.game_object.interval = self.period_bot(2)
					self.status = 99999
			else:
				self.set_option('saryo_index', saryo_index)

			# 첫번째 반려 동물
			# manbok_gage = int(self.bar_percent('banryoe_dongmul_scene_manbok_gage_start', 'banryoe_dongmul_scene_manbok_gage_middle', 'banryoe_dongmul_scene_manbok_gage_end', adjust=(20, 20, 20)))
			# if manbok_gage > 95:
			# 	self.status += 1
			# else:
			# 	self.set_option('manbok_gage', manbok_gage)
			# 	self.lyb
			# self.logger.debug(manbok_gage)
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def sakatu_shop_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status
		
	def tobeol_gesipan_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.status = self.get_work_status('토벌 게시판')
		elif self.status == self.get_work_status('토벌 게시판'):			
			self.game_object.get_scene('main_scene').set_option('토벌 게시판' + '_clicked', True)	
			self.set_option('tobeol_index', 0)
			self.set_option('tobeol_drag_index', 0)
			self.set_option('tobeol_drag_count', 0)
			self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 1:
			is_clicked = self.lyb_mouse_click('tobeol_gesipan_scene_exchange_all')
			self.game_object.get_scene('tobeol_gesipan_exchange_scene').status = 0
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom') == True:
				self.status += 101
			else:
				self.status += 1
			# is_clicked = self.lyb_mouse_click('tobeol_gesipan_scene_exchange')
			# if is_clicked == True:
			# 	self.game_object.interval = self.period_bot(3)
			# else:
			# 	self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 2:
			for i in range(3):
				self.lyb_mouse_drag('tobeol_gesipan_scene_drag_left', 'tobeol_gesipan_scene_drag_right')
				time.sleep(1)
			self.set_option('tobeol_drag_count', 0)
			self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 3:	
			tobeol_index = self.get_option('tobeol_index')
			tobeol_drag_index = self.get_option('tobeol_drag_index')
			tobeol_drag_count = self.get_option('tobeol_drag_count')

			self.logger.debug('[DEBUG - TOBEOL - 00] tobeol_index: ' + str(tobeol_index))
			if tobeol_index > 4:
				tobeol_drag_index += 1
				tobeol_index = 0
				self.set_option('tobeol_drag_index', tobeol_drag_index)
				self.set_option('tobeol_index', 0)

			# 4 번 이상 드래그하면 종료
			self.logger.debug('[DEBUG - TOBEOL - 01] tobeol_drag_index: ' + str(tobeol_drag_index))
			if tobeol_drag_index > 4:
				self.status = 99999

			if tobeol_drag_index > tobeol_drag_count:
				self.set_option('tobeol_drag_count', tobeol_drag_count + 1)
				self.lyb_mouse_drag('tobeol_gesipan_scene_drag_right', 'tobeol_gesipan_scene_drag_left')
			else:
				pb_name_list = [ 'tobeol_gesipan_fist', 'tobeol_gesipan_special']
				for pb_name in pb_name_list:
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.7,
										custom_flag=1,
										custom_rect=(120*tobeol_index, 280, 120*(tobeol_index + 1), 330)
										)
					self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) +':'+ str(match_rate))						
					if loc_x != -1:
						break

				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status += 1
				else:	
					self.logger.debug('[DEBUG - TOBEOL - 2] tobeol_index: ' + str(tobeol_index))
					self.set_option('tobeol_index', tobeol_index + 1)
		elif self.status == self.get_work_status('토벌 게시판') + 4:
			pb_name = 'tobeol_gesipan_scene_bosang'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.9,
								custom_flag=1,
								custom_rect=(300, 210, 380, 280)
								)
			
			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) +':'+ str(match_rate))	
			if loc_x == -1:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				return self.status

			tobeol_index = self.get_option('tobeol_index')
			tobeol_drag_index = self.get_option('tobeol_drag_index')

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tobeol_gesipan_scene_ready_0')
			self.logger.warn('tobeol_gesipan_scene_ready_0: ' + str(int(match_rate * 100)))
			if match_rate > 0.95:
				self.set_option('tobeol_index', tobeol_index + 1)
				self.status -= 1
			else:
				self.lyb_mouse_click('tobeol_gesipan_scene_ready_0', custom_threshold=0)
				self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 5:
			self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 6:
			self.status = self.get_work_status('토벌 게시판') + 2
		elif self.status == self.get_work_status('토벌 게시판') + 102:
			# for each_boss in lybgamebd.LYBBlackDesert.tobeol_boss_list:
			# 	i = lybgamebd.LYBBlackDesert.tobeol_boss_list.index(each_boss)
			# 	self.logger.warn(each_boss + ':' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i))) + ':' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(i))))

			for i in range(len(lybgamebd.LYBBlackDesert.tobeol_boss_list)):
				tobeol_degrade_number = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i)))
				tobeol_drag_index = int(i / 5)
				tobeol_index = int(i % 5)
				self.set_option('tobeol_fail_' + str(tobeol_drag_index) + '_' + str(tobeol_index), tobeol_degrade_number)

			tobeol_index = self.get_option('tobeol_index')
			tobeol_drag_index = self.get_option('tobeol_drag_index')
			current_index = tobeol_index + tobeol_drag_index*5
			tobeol_boss_count = len(lybgamebd.LYBBlackDesert.tobeol_boss_list)

			if current_index >= tobeol_boss_count:
				self.status = 99999
			elif current_index >= tobeol_boss_count - 5:
				for i in range(3):
					self.lyb_mouse_drag('tobeol_gesipan_scene_drag_right', 'tobeol_gesipan_scene_drag_left')
					time.sleep(1)
				self.status += 101
			else:
				for i in range(3):
					self.lyb_mouse_drag('tobeol_gesipan_scene_drag_left', 'tobeol_gesipan_scene_drag_right')
					time.sleep(1)
				self.set_option('tobeol_drag_count', 0)
				self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 103:
			tobeol_index = self.get_option('tobeol_index')
			tobeol_drag_index = self.get_option('tobeol_drag_index')
			tobeol_drag_count = self.get_option('tobeol_drag_count')
			tobeol_boss_count = len(lybgamebd.LYBBlackDesert.tobeol_boss_list)

			self.logger.debug('[TOBEOLEACH 1] tobeol_index: ' + str(tobeol_index))
			if tobeol_index > 4:
				tobeol_drag_index += 1
				tobeol_index = 0
				self.set_option('tobeol_drag_index', tobeol_drag_index)
				self.set_option('tobeol_index', 0)

			# 4 번 이상 드래그하면 종료
			self.logger.debug('[TOBEOLEACH 2] tobeol_drag_index: ' + str(tobeol_drag_index))
			if tobeol_drag_index > 4:
				self.status = 99999

			if tobeol_drag_index > tobeol_drag_count:
				self.set_option('tobeol_drag_count', tobeol_drag_count + 1)
				self.lyb_mouse_drag('tobeol_gesipan_scene_drag_right', 'tobeol_gesipan_scene_drag_left')
			else:

				current_index = tobeol_index + tobeol_drag_index*5
				if current_index >= tobeol_boss_count - 5:
					self.lyb_mouse_drag('tobeol_gesipan_scene_drag_right', 'tobeol_gesipan_scene_drag_left')
					self.status += 100
				else:
					is_process = self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(current_index))
					if is_process == True:
						tobeol_degrade_number = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(current_index)))
						self.logger.warn('토벌 보스 : ' + str(lybgamebd.LYBBlackDesert.tobeol_boss_list[current_index]) + ' - ' + str(tobeol_degrade_number) + ' 단계 하락')

						pb_name_list = [ 'tobeol_gesipan_fist', 'tobeol_gesipan_special']
						for pb_name in pb_name_list:
							(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
												self.window_image,
												self.game_object.resource_manager.pixel_box_dic[pb_name],
												custom_threshold=0.7,
												custom_flag=1,
												custom_rect=(120*tobeol_index, 280, 120*(tobeol_index + 1), 330)
												)
							self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) +':'+ str(match_rate))						
							if loc_x != -1:
								break

						if loc_x != -1:
							self.lyb_mouse_click_location(loc_x, loc_y)
							self.status += 1
						else:	
							self.logger.debug('[TOBEOLEACH 4] tobeol_index: ' + str(tobeol_index))
							self.set_option('tobeol_index', tobeol_index + 1)
					else:
						self.logger.debug('[TOBEOLEACH 5] tobeol_index: ' + str(tobeol_index))
						self.set_option('tobeol_index', tobeol_index + 1)
						self.game_object.interval = self.period_bot(0.1)
		elif self.status == self.get_work_status('토벌 게시판') + 104:

			pb_name = 'tobeol_gesipan_scene_bosang'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				pb_name = 'tobeol_gesipan_scene_clock'
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if match_rate < 0.9:
					self.lyb_mouse_click('tobeol_gesipan_scene_bosang', custom_threshold=0)
					return self.status
				
			tobeol_index = self.get_option('tobeol_index')
			tobeol_drag_index = self.get_option('tobeol_drag_index')

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'tobeol_gesipan_scene_ready_0')
			self.logger.warn('tobeol_gesipan_scene_ready_0: ' + str(int(match_rate * 100)))
			if match_rate > 0.95:
				self.set_option('tobeol_index', tobeol_index + 1)
				self.status -= 1
			else:
				self.lyb_mouse_click('tobeol_gesipan_scene_ready_0', custom_threshold=0)
				self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 105:
			self.status += 1
		elif self.status == self.get_work_status('토벌 게시판') + 106:
			self.status = self.get_work_status('토벌 게시판') + 102
		elif self.status == self.get_work_status('토벌 게시판') +  203:
			tobeol_index = self.get_option('tobeol_index')
			tobeol_drag_index = self.get_option('tobeol_drag_index')
			current_index = tobeol_index + tobeol_drag_index*5
			tobeol_boss_count = len(lybgamebd.LYBBlackDesert.tobeol_boss_list)
			location_index = (current_index - tobeol_boss_count + 5) 

			if current_index >= tobeol_boss_count:
				self.status = 99999
			else:
				is_process = self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(current_index))
				if is_process == True:
					tobeol_degrade_number = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(current_index)))
					self.logger.warn('토벌 보스 : ' + str(lybgamebd.LYBBlackDesert.tobeol_boss_list[current_index]) + ' - ' + str(tobeol_degrade_number) + ' 단계 하락')
					custom_x = 47 + 120*(location_index + 1)
					if custom_x > 640:
						custom_x = 639

					pb_name_list = [ 'tobeol_gesipan_fist', 'tobeol_gesipan_special']
					for pb_name in pb_name_list:
						(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
											self.window_image,
											self.game_object.resource_manager.pixel_box_dic[pb_name],
											custom_threshold=0.7,
											custom_flag=1,
											custom_rect=(47 + 120*location_index, 280, custom_x, 330)
											)
						self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) +':'+ str(match_rate))						
						if loc_x != -1:
							break

					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.status -= 99
					else:	
						self.logger.debug('[TOBEOLEACH 4] tobeol_index: ' + str(tobeol_index))
						self.set_option('tobeol_index', tobeol_index + 1)
				else:
					self.set_option('tobeol_index', tobeol_index + 1)
					self.game_object.interval = self.period_bot(0.1)
		else:
			self.game_object.get_scene('main_scene').set_option('토벌 게시판' + '_end_flag', True)
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def immu_success_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def select_youngjimin_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('select_youngjimin_scene_select')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status


	def youngji_jujeom_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def jeongye_immu_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('jeongye_immu_scene_start', custom_threshold=0)
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def gwangwonseok_jangchak_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status


	def tutorial_gisul_scene(self):

		self.lyb_mouse_drag('skill_drag_center', 'skill_drag_right')
		# time.sleep(1)
		# self.lyb_mouse_drag('skill_drag_right', 'skill_drag_left')

		return self.status

	def mulpum_deyeo_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def npc_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def mulpum_gume_scene(self):
		self.lyb_mouse_click('mulpum_gume_scene_buy')

		return self.status

	def select_ure_scene(self):

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[self.scene_name + '_close_icon'],
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(310, 250, 420, 350)
							)
		if loc_x != -1:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence') == True:
				random_factor = float(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'))
				random_second = random.random() * random_factor
				self.logger.info('퀘스트 완료 클릭 - 무작위 지연 시간: ' + str(round(random_second,2)) + '초, 좌표: ' + str((loc_x, loc_y)))
				time.sleep(random_second)

			self.lyb_mouse_click_location(loc_x, loc_y)
			self.game_object.interval = self.period_bot(1)

		return self.status
		

	def jongja_shop_scene(self):
		self.game_object.current_matched_scene['name'] = ''
		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('potion_shop_scene_jeonripum_jeongri')
			self.status += 1
		elif self.status == 2:
			if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
				self.lyb_mouse_click('jongja_shop_scene_jongja_list_0', custom_threshold=0)
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status
				
	def potion_shop_scene(self):
		self.game_object.current_matched_scene['name'] = ''

		# for i in range(len(lybgamebd.LYBBlackDesert.sell_pummok_list)):
		# 	self.logger.warn(str(lybgamebd.LYBBlackDesert.sell_pummok_list[i]) + ':' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i))))

		# for i in range(len(lybgamebd.LYBBlackDesert.item_rank_list)):
		# 	self.logger.warn(str(lybgamebd.LYBBlackDesert.item_rank_list[i]) + ':' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i))))

		# self.logger.warn(str('잠재력 돌파:') + str(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek')))
		# return self.status

		if self.status == 0:
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('potion_shop_scene_jeonripum_jeongri')
			self.set_option('potion_number', 0)
			self.status += 1
		elif self.status == 2:
			is_buy_potion = self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean')

			if is_buy_potion == True:
				potion_number = self.get_option('potion_number')
				potion_number_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number'))
				self.logger.info('potion_number:' + str(potion_number) + ' potion_limit:' + str(potion_number_limit))
				if potion_number >= potion_number_limit:
					self.status += 1
				else:
					potion_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'))
					muge_gage_percent = int(self.bar_percent('muge_gage_s', 'muge_gage_m', 'muge_gage_e', adjust=(20, 20, 20), reverse=True))
					self.logger.warn('가방 무게: ' + str(muge_gage_percent) + '/' + str(potion_limit) + '%')
					if muge_gage_percent < potion_limit:
						potion_thing = self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing')
						potion_list_index = lybgamebd.LYBBlackDesert.potion_list.index(potion_thing)
						pixel_box_name = 'potion_list_' + str(potion_list_index)

						(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pixel_box_name],
							custom_flag=1,
							custom_rect=(20, 100, 70, 300)
							)
						if loc_x != -1:
							self.lyb_mouse_click_location(loc_x, loc_y)
							self.game_object.get_scene('mulpum_suryang_scene').set_option('set', int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set')))
					else:
						self.status += 1
					self.set_option('potion_number', potion_number + 1)
			else:
				self.status += 1
		elif self.status == 3:
			is_sell = self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean')
			if is_sell == True:
				self.lyb_mouse_click('potion_shop_scene_sell')
				self.set_option('sell_pummok_count', 0)
				self.status += 1
			else:
				self.status = 99999
		elif self.status == 4:
			sell_pummok_count = self.get_option('sell_pummok_count')
			if sell_pummok_count > 5:
				self.status += 1
			else:
				is_clicked = False
				search_delay = 0.5
				for i in range(len(lybgamebd.LYBBlackDesert.sell_pummok_list)):
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'sell_pummok_' + str(i))
					# self.logger.warn(str(lybgamebd.LYBBlackDesert.sell_pummok_list[i]) + ':' + str(match_rate))
					# match_rate 가 1.0 이면 체크 해제된 상태
					if (match_rate > 0.8 and self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i)) == True):
						self.lyb_mouse_click('sell_pummok_' + str(i), custom_threshold=0)
						is_clicked = True
						time.sleep(search_delay)
					elif (match_rate < 0.8 and self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i)) == False):
						self.lyb_mouse_click('sell_pummok_' + str(i), custom_threshold=0)
						is_clicked = True
						time.sleep(search_delay)

				for i in range(len(lybgamebd.LYBBlackDesert.item_rank_list)):
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'sell_item_rank_' + str(i))
					# self.logger.warn(str(lybgamebd.LYBBlackDesert.item_rank_list[i]) + ':' + str(match_rate))
					# match_rate 가 1.0 이면 체크 해제된 상태
					if (match_rate > 0.8 and self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i)) == True):
						self.lyb_mouse_click('sell_item_rank_' + str(i), custom_threshold=0)
						is_clicked = True
						time.sleep(search_delay)
					elif (match_rate < 0.8 and self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i)) == False):
						self.lyb_mouse_click('sell_item_rank_' + str(i), custom_threshold=0)
						is_clicked = True
						time.sleep(search_delay)

				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'sell_jamjeryoek')
				# self.logger.warn(str(match_rate) + ':' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek')))

				if (match_rate > 0.8 and self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek') == True):
					self.lyb_mouse_click('sell_jamjeryoek', custom_threshold=0)
					is_clicked = True
					time.sleep(search_delay)
				elif (match_rate < 0.8 and self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek') == False):
					self.lyb_mouse_click('sell_jamjeryoek', custom_threshold=0)
					is_clicked = True
					time.sleep(search_delay)
				

				if is_clicked == False:
					self.status += 1
				else:
					self.set_option('sell_pummok_count', sell_pummok_count + 1)
		elif self.status == 5:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'sell_select_all')
			if match_rate > 0.8:
				self.lyb_mouse_click('sell_select_all', custom_threshold=0)
			self.status += 1
		elif self.status == 6:
			self.lyb_mouse_click('potion_shop_scene_panme')
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
			self.status = 0

		return self.status

	def nejeongbo_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status
		
	def jamjeryeok_jeonsu_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def confirm_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def pearl_sangjeom_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def geomungiun_scene(self):

		if self.status == 0:
			self.set_option('tab_iterator', 0)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('geomungiun_scene_mugi', custom_threshold=0)
			self.status = 100
		elif self.status == 2:
			(s_loc_x, s_loc_y) = self.get_location('geomungiun_scene_item_rank_anchor_1')
			(e_loc_x, e_loc_y) = self.get_location('geomungiun_scene_item_rank_anchor_2')
			(a_loc_x, a_loc_y) = self.get_location('geomungiun_scene_item_rank_anchor_3')

			self.logger.warn(str((s_loc_x, s_loc_y)) + '--' + str((a_loc_x, a_loc_y)))
			adjust_x = a_loc_x - s_loc_x
			if self.get_option('tab_iterator') == 0:
				item_rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun')
			else:
				item_rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2')

			
			item_rank_index = lybgamebd.LYBBlackDesert.geomun_rank_list.index(item_rank_name)
			self.logger.warn(item_rank_name + ' ' + str(self.get_center_pixel_info('geomungiun_scene_item_rank_' + str(item_rank_index))[1]))

			for i in range(5):
				(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, s_loc_x + (i*adjust_x) - 15, s_loc_y)
				(r2, g2, b2) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x + (i*adjust_x) - 15, e_loc_y)
				is_found = False
				is_found2 = False
				for j in range(item_rank_index + 1):
					pb = self.get_center_pixel_info('geomungiun_scene_item_rank_' + str(j))
					pb_rgb = pb[1]
					
					if abs(pb_rgb[0] - r) < 40 and abs(pb_rgb[1] - g) < 40 and abs(pb_rgb[2] - b) < 45:
						is_found = True

					if abs(pb_rgb[0] - r2) < 40 and abs(pb_rgb[1] - g2) < 40 and abs(pb_rgb[2] - b2) < 45:
						is_found2 = True
					self.logger.warn(lybgamebd.LYBBlackDesert.geomun_rank_list[j] + ' ' + str(pb_rgb) + ' ' + str((r, g, b)) + ':' + str(is_found) + ' ' + str((r2, g2, b2)) + ':' + str(is_found2))

				pb = self.get_center_pixel_info('geomungiun_scene_item_rank_empty')
				pb_rgb = pb[1]
				if abs(pb_rgb[0] - r) < 40 and abs(pb_rgb[1] - g) < 40 and abs(pb_rgb[2] - b) < 45:
					is_found = True

				if abs(pb_rgb[0] - r2) < 40 and abs(pb_rgb[1] - g2) < 40 and abs(pb_rgb[2] - b2) < 45:
					is_found2 = True

				self.logger.warn(str((r, g, b)) + ':' + str((r2, g2, b2)) + ':' + str(is_found) + ':' + str(is_found2))
				if is_found == False or is_found2 == False:
					# 뭔가 이상한게 발견됨
					self.logger.warn('NO')
					self.status = 10
					break

			if is_found == True and is_found2 == True:
				self.logger.warn('OK')
				self.lyb_mouse_click('geomungiun_scene_auto_select', custom_threshold=0)
				self.game_object.interval = self.period_bot(3)
				self.status += 1
		elif self.status == 3:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'geomungiun_scene_giun_hupsu')
			if match_rate > 0.9:
				self.lyb_mouse_click('geomungiun_scene_giun_hupsu')
				self.status += 1
			else:
				self.status = 10
		elif self.status == 4:
			self.status += 1
		elif self.status == 5:
			self.status = 2
		elif self.status == 10:
			tab_iterator = self.get_option('tab_iterator')
			if tab_iterator == 0:
				self.lyb_mouse_click('geomungiun_scene_banji', custom_threshold=0)
				self.set_option('tab_iterator', 1)
				self.status = 2
			else:
				self.status += 1
		elif self.status >= 100 and self.status < 110:
			self.status += 1
			pb_name = 'geomungiun_scene_filter_open'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate < 0.9:
				self.logger.warn(pb_name + ' ' + str(match_rate))
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				return self.status

			if self.get_option('tab_iterator') == 0:
				item_rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun')
				self.logger.warn("무기/방어구 흑정령 - 검은 기운: " + str(item_rank_name) + ' ' + str(lybgamebd.LYBBlackDesert.geomun_rank_list.index(item_rank_name)))
			else:
				item_rank_name = self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2')
				self.logger.warn("반지 흑정령 - 검은 기운: " + str(item_rank_name) + ' ' + str(lybgamebd.LYBBlackDesert.geomun_rank_list.index(item_rank_name)))
						
			item_rank_index = lybgamebd.LYBBlackDesert.geomun_rank_list.index(item_rank_name)

			is_clicked = False
			for i in range(len(lybgamebd.LYBBlackDesert.geomun_rank_list)):
				pb_name = 'geomungiun_scene_filter_item_rank_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.debug(pb_name + ' ' + str(match_rate))
				if match_rate < 0.9 and i <= item_rank_index:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
					self.game_object.interval = self.period_bot(2)
					is_clicked = True
				elif match_rate > 0.9 and i > item_rank_index:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
					is_clicked = True
			if is_clicked == True:
				return self.status

			self.status = 110
		elif self.status == 110:
			self.lyb_mouse_click('geomungiun_scene_auto_select', custom_threshold=0)
			self.status += 1
		elif self.status >= 111 and self.status < 113:
			self.status += 1
		elif self.status == 113:
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'geomungiun_scene_giun_hupsu')
			if match_rate > 0.9:
				self.lyb_mouse_click('geomungiun_scene_giun_hupsu')
				self.status += 1
			else:
				self.status = 115
		elif self.status == 114:
			self.status = 100
		elif self.status == 115:
			tab_iterator = self.get_option('tab_iterator')
			if tab_iterator == 0:
				self.lyb_mouse_click('geomungiun_scene_banji', custom_threshold=0)
				self.set_option('tab_iterator', 1)
				self.status = 100
			else:
				self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def gisul_scene(self):

		if self.status == 0:
			self.set_option('gisul_scene_drag_count', 0)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('gisul_scene_beugi')
			self.status += 1
			# gisul_scene_drag_count = self.get_option('gisul_scene_drag_count')

			# if gisul_scene_drag_count > 6:
			# 	self.status = 99999
			# else:
			# 	(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
			# 						self.window_image,
			# 						self.game_object.resource_manager.pixel_box_dic['gisul_up'],
			# 						custom_flag=1,
			# 						custom_threshold=0.6,
			# 						custom_rect=(530, 90, 560, 360)
			# 						)
			# 	self.logger.warn(str((loc_x, loc_y)) +':'+str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.status = 2
			# 	else:
			# 		(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
			# 							self.window_image,
			# 							self.game_object.resource_manager.pixel_box_dic['gisul_skill_up'],
			# 							custom_flag=1,
			# 							custom_threshold=0.6,
			# 							custom_rect=(530, 90, 560, 360)
			# 							)
			# 		self.logger.warn(str((loc_x, loc_y)) +':'+str(match_rate))
			# 		if loc_x != -1:
			# 			self.lyb_mouse_click_location(loc_x, loc_y)
			# 			self.set_option('gisul_skill_up_limit', 0)
			# 			self.status = 3
			# 		else:
			# 			self.lyb_mouse_drag('gisul_scene_drag_bottom', 'gisul_scene_drag_top')
			# 			self.set_option('gisul_scene_drag_count', gisul_scene_drag_count + 1)

		elif self.status == 2:
			pb_name = 'gisul_scene_beugi_process'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				self.game_object.interval = self.period_bot(3)
				self.set_option('gisul_limit_count', 0)
				self.status = 100
				# self.lyb_mouse_click('gisul_scene_all', custom_threshold=0)
			# self.status = 0
		# elif self.status == 3:
		# 	gisul_skill_up_limit = self.get_option('gisul_skill_up_limit')
		# 	if gisul_skill_up_limit > 2:
		# 		self.status = 0 
		# 	else:
		# 		(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
		# 							self.window_image,
		# 							self.game_object.resource_manager.pixel_box_dic['gisul_skill_up'],
		# 							custom_flag=1,
		# 							custom_threshold=0.6,
		# 							custom_rect=(350, 100, 510, 280)
		# 							)
		# 		# self.logger.warn(str((loc_x, loc_y)) +':'+str(match_rate))
		# 		if loc_x != -1:
		# 			self.lyb_mouse_click_location(loc_x, loc_y)
		# 			self.set_option('gisul_skill_up_limit', gisul_skill_up_limit + 1)
		# 		else:
		# 			self.status = 0
		elif self.status == 100:
			gisul_limit_count = self.get_option('gisul_limit_count')
			if gisul_limit_count == None:
				gisul_limit_count = 0

			if gisul_limit_count > 5:
				self.status = 99999
			else:
				self.set_option('gisul_scene_drag_count', 0)
				self.set_option('gisul_limit_count', gisul_limit_count + 1)
				self.status += 1
		elif self.status == 101:
			gisul_scene_drag_count = self.get_option('gisul_scene_drag_count')

			if gisul_scene_drag_count > 6:
				self.status = 99999
			else:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
									self.window_image,
									self.game_object.resource_manager.pixel_box_dic['gisul_up'],
									custom_flag=1,
									custom_threshold=0.6,
									custom_rect=(530, 90, 560, 360)
									)
				self.logger.warn(str((loc_x, loc_y)) +':'+str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.status = 102
				else:
					(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic['gisul_skill_up'],
										custom_flag=1,
										custom_threshold=0.6,
										custom_rect=(530, 90, 560, 360)
										)
					self.logger.warn(str((loc_x, loc_y)) +':'+str(match_rate))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.set_option('gisul_skill_up_limit', 0)
						self.status = 103
					else:
						self.lyb_mouse_drag('gisul_scene_drag_bottom', 'gisul_scene_drag_top')
						self.set_option('gisul_scene_drag_count', gisul_scene_drag_count + 1)

		elif self.status == 102:
			self.lyb_mouse_click('gisul_scene_all', custom_threshold=0)
			self.status = 100
		elif self.status == 103:
			gisul_skill_up_limit = self.get_option('gisul_skill_up_limit')
			if gisul_skill_up_limit > 2:
				self.status = 100 
			else:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
									self.window_image,
									self.game_object.resource_manager.pixel_box_dic['gisul_skill_up'],
									custom_flag=1,
									custom_threshold=0.6,
									custom_rect=(350, 100, 510, 280)
									)
				# self.logger.warn(str((loc_x, loc_y)) +':'+str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.set_option('gisul_skill_up_limit', gisul_skill_up_limit + 1)
				else:
					self.status = 100

		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def gabang_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def death_scene(self):

		self.logger.warn('캐릭터가 사망했습니다. 되돌아가기 클릭.')
		self.lyb_mouse_click('death_scene_back')

		return self.status


	def character_death_2_scene(self):
		if self.get_checkpoint('start') == 0:
			elapsed_time = 0
		else:
			elapsed_time = time.time() - self.get_checkpoint('start')

		if elapsed_time > 300:
			self.lyb_mouse_click('death_scene_back_button', custom_threshold=0)
			# self.lyb_mouse_click('death_scene_buhal_button', custom_threshold=0)
			self.status = 0
			return self.status

		if self.status == 0:
			self.set_checkpoint('start')
			self.status += 1
		elif self.status == 1:
			self.logger.info('캐릭터 사망. 돌아가기 클릭하지 않습니다.' + str(int(elapsed_time)) + '/300초')

		return self.status

		# return self.character_death_scene()

	def character_field_death_scene(self):
		return self.character_death_scene()

	def killed_by_player_scene(self):
		return self.character_death_scene()

	def character_death_scene(self):

		is_clicked = self.lyb_mouse_click(self.scene_name + '_close_icon')

		self.game_object.addStatistic('캐릭터 사망 횟수')

		if is_clicked == True:
			self.logger.warn('캐릭터가 사망했습니다. 마을에서 부활 클릭.')

		if self.game_object.get_scene('main_scene').current_work != None:
			work_name = self.game_object.get_scene('main_scene').current_work
			self.logger.warn('캐릭터가 사망해서 작업['+ work_name +']을 종료합니다.')
			self.game_object.get_scene('main_scene').set_option(work_name + '_end_flag', True)

		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death') == True:
			self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 캐릭터 사망 감지')
			png_name = self.game_object.save_image('character_death')
			self.game_object.telegram_send('', image=png_name)

		return self.status

	def tutorial_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def urewanryo_scene(self):

		(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic['urewanryo_scene_select'],
							custom_flag=1,
							custom_rect=(370, 180, 400, 260)
							)
		if loc_x != -1:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence') == True:
				random_factor = float(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'))
				random_second = random.random() * random_factor
				self.logger.info('퀘스트 완료 클릭 - 무작위 지연 시간: ' + str(round(random_second,2)) + '초, 좌표: ' + str((loc_x, loc_y)))
				time.sleep(random_second)

			self.lyb_mouse_click_location(loc_x, loc_y)
			time.sleep(1)
			self.lyb_mouse_click('urewanryo_scene_touch', custom_threshold=0)

		else:
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence') == True:
				random_factor = float(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'))
				random_second = random.random() * random_factor
				self.logger.info('퀘스트 완료 클릭 - 무작위 지연 시간: ' + str(round(random_second,2)) + '초, 터치')
				time.sleep(random_second)

			self.lyb_mouse_click('urewanryo_scene_touch', custom_threshold=0)
			self.game_object.addStatistic('의뢰 완료 횟수')
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo') == True:
				self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 의뢰완료 이벤트 감지')
				png_name = self.game_object.save_image('urewanryo')
				self.game_object.telegram_send('', image=png_name)


		return self.status


	def tutorial_lv1_0_scene(self):

		self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

		return self.status

	def tutorial_lv1_scene(self):

		if self.status == 0:
			self.status += 1
		elif self.status == 1: 
			self.lyb_mouse_drag('pad_drag_center', 'pad_drag_9', stop_delay=2)
			self.status += 1
		elif self.status == 2: 
			self.lyb_mouse_drag('pad_drag_center', 'pad_drag_6', stop_delay=2)
			self.status += 1
		elif self.status == 3: 
			self.lyb_mouse_drag('pad_drag_center', 'pad_drag_3', stop_delay=5)
			self.status += 1
		else:
			self.status = 0

		return self.status


	def jeoljeon_mode_death_scene(self):

		if self.status == 0:
			self.lyb_mouse_drag('jeoljeon_mode_scene_drag_bottom', 'jeoljeon_mode_scene_drag_top')
			self.status += 1
		else:
			self.status = 0

		return self.status

	def jeoljeon_mode_scene(self):

		# self.game_object.count_for_freeze = 0

		if self.status == 0:
			self.set_option('jeoljeon_mode_warning', False)
			self.status += 1
		elif self.status == 1:
			self.set_option('warning_index', 0)

			if ( self.game_object.get_scene('main_scene').current_work == '자동 사냥' and
				 self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode') == True ):
				current_work = self.game_object.get_scene('main_scene').current_work
				elapsed_time = time.time() - self.game_object.get_scene('main_scene').get_checkpoint(current_work + '_check_start')
				limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'period'))

				if elapsed_time > limit_time:
					self.status += 1
				else:
					self.status = 10
			else:
				self.status += 1
		elif self.status == 2:
			self.lyb_mouse_drag('jeoljeon_mode_scene_drag_bottom', 'jeoljeon_mode_scene_drag_top')
			self.status += 1
		elif self.status == 10:
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning'))
			
			warning_index = self.get_option('warning_index')
			if warning_index == 0:
				pb_name = 'jeoljeon_mode_scene_gabang_warning'
			elif warning_index == 1:
				pb_name = 'jeoljeon_mode_scene_potion_warning'
			else:
				pb_name = 'jeoljeon_mode_scene_quest_warning'
				limit_time = 0

			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pb_name],
				custom_threshold=0.8,
				custom_flag=1,
				custom_rect=(500, 330, 620, 370)
				)
			if loc_x != -1:
				if self.get_option('jeoljeon_mode_warning') == False:
					self.set_checkpoint('jeoljeon_mode_warning_start')
					self.set_option('jeoljeon_mode_warning', True)
				else:
					elapsed_time = int(time.time() - self.get_checkpoint('jeoljeon_mode_warning_start'))
					if elapsed_time > limit_time:
						self.status = 2
						return self.status
					else:
						self.loggingElapsedTime('절전모드경고', elapsed_time, limit_time, period=10)
			
			if warning_index > 1:
				self.status = 1
			else:
				self.set_option('warning_index', warning_index + 1)
		else:
			self.status = 0

		return self.status

	def character_scene(self):

		if self.status == 0:
			self.lyb_mouse_drag('character_scene_drag_top', 'character_scene_drag_bottom')
			self.status += 1
		elif self.status == 1:
			index = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change')) - 1
			if index < 6:
				self.lyb_mouse_click('character_scene_character_' + str(index), custom_threshold=0)
				self.status = 0
			else:
				self.status += 1
		elif self.status == 2:
			self.lyb_mouse_drag('character_scene_drag_bottom', 'character_scene_drag_top')
			self.status += 1
		elif self.status == 3:
			self.lyb_mouse_click('character_scene_character_5', custom_threshold=0)
			self.status = 0
		else:
			self.status = 0

		return self.status

	def signin_scene(self):

		if self.status == 0:
			self.status += 1
		else:
			# 구글 계정
			self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status

	def repair_service_scene(self):

		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'repair_service_scene')
		if match_rate < 0.8:
			return self.status

		self.logger.info('임시 점검 화면: ' + str(self.status) + '/30')
		
		if self.status == 0:
			self.set_checkpoint('start')
			self.status += 1
		elif self.status >= 1 and self.status < 30:
			self.status += 1
		else:
			self.game_object.terminate_application()
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
			self.game_object.interval = self.period_bot(5)
			self.status += 1
		elif self.status == 2:
			self.status += 1
		elif self.status >= 2 and self.status < 30:
			self.logger.info('로그인 화면 랙 인식: ' + str(self.status) + '/30')
			self.status += 1
		elif self.status == 30:
			self.game_object.terminate_application()
			self.status += 1
		else:
			# self.lyb_mouse_click(self.scene_name + '_close_icon')
			self.status = 0

		return self.status



















































	# +----------------------------+
	# |                            |
	# |           M A I N          |
	# |                            |
	# +----------------------------+



	def main_scene(self):

		if self.game_object.current_schedule_work != self.current_work:
			self.game_object.current_schedule_work = self.current_work

		self.game_object.main_scene = self

		if self.is_moving() == True:
			return self.status

		s = time.time()
		is_clicked = self.event_process_main_scene()
		e = time.time()
		# self.logger.warn('@ ElapsedTime event_process_main_scene: ' + str(round(e - s, 5)))

		if is_clicked == True:
			return self.status

		s = time.time()
		is_clicked = self.pre_process_main_scene()
		e = time.time()
		# self.logger.warn('@ ElapsedTime pre_process_main_scene: ' + str(round(e - s, 5)))
		if is_clicked == True:
			return self.status


		self.schedule_list = self.get_game_config('schedule_list')
		if len(self.schedule_list) == 1:
			self.logger.warn('스케쥴 작업이 없어서 종료합니다.')
			return -1

		if self.status == 0:
			# self.logger.debug('schedule_list length: ' + str(len(self.schedule_list)))
			self.status += 1
		elif self.status >= 1 and self.status < 1000:

			self.set_schedule_status()

		elif self.status == self.get_work_status('메인 퀘스트'):

			elapsed_time = self.get_elapsed_time()
			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('check_quest', None)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			check_quest = self.get_option('check_quest')
			if check_quest != True:
				self.lyb_mouse_drag('main_scene_quest_drag_top', 'main_scene_quest_drag_bottom')
				time.sleep(2)
				self.set_option('check_quest', True)
				loc_x, loc_y = self.get_location('quest_location_0')
				self.lyb_mouse_click_location2(loc_x, loc_y)
				time.sleep(2)
				self.lyb_mouse_click_location2(loc_x - 20, loc_y)
				time.sleep(2)
				self.set_checkpoint('main_quest_clicked')
				return self.status

			is_clicked = self.main_scene_close_map()
			if is_clicked == True:
				return self.status

			s = time.time()
			is_clicked = self.process_main_quest()
			e = time.time()

			if is_clicked == True:
				# self.logger.debug('clicked main quest image -- ')
				self.set_checkpoint('last_clicked_main_quest')
				self.game_object.interval = self.period_bot(2)
				return self.status

			# 낚시 퀘스트

			threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest')) * 0.01
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic['fishing_lod'],
					custom_threshold=threshold_main_quest,
					custom_flag=1,
					custom_rect=(550, 300, 600, 360)
					)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				time.sleep(30)
				self.lyb_mouse_click_location(loc_x, loc_y)
				time.sleep(1)
				self.lyb_mouse_click_location(loc_x, loc_y)
				return self.status

			# self.logger.debug('ElpasedTime process_main_quest : ' + str(round(e - s, 5)))
		elif self.status == self.get_work_status('자동 사냥'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('jeoljeon_mode_flag', False)	
				self.set_option('check_quest', None)
				self.set_option('exclude', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			check_quest = self.get_option('check_quest')
			if check_quest != True:
				self.lyb_mouse_drag('main_scene_quest_drag_top', 'main_scene_quest_drag_bottom')
				time.sleep(2)
				self.set_option('fast_move_click', False)
				self.set_option('check_quest', True)
				self.set_option('jeoljeon_mode_flag', False)	
				quest_index = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'))
				if quest_index > 0 and quest_index < 5:
					loc_x, loc_y = self.get_location('quest_location_0')
					self.lyb_mouse_click_location2(loc_x, loc_y + 28 * (quest_index - 1))
					time.sleep(1)
					self.lyb_mouse_click_location2(loc_x - 20, loc_y + 28 * (quest_index - 1))
					return self.status
				elif quest_index >= 5 and quest_index < 8:
					if self.click_to_maul() == True:
						self.set_option('fast_move_click', True)
					else:
						self.logger.warn('마을로 가는 아이콘을 못찾겠습니다.')

			elapsed_time = self.get_elapsed_time()
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'period'))
			pet_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period'))
			period_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'))
			is_search_complete = self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete')

			if elapsed_time > limit_time:
				self.set_option(self.current_work + '_end_flag', True)
			elif elapsed_time < period_main_quest:

				self.loggingElapsedTime(self.current_work + ' 준비 중...', int(elapsed_time), period_main_quest)				
				return self.status
			elif self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode') == True:
				if self.is_sudong() == False and self.get_option('jeoljeon_mode_flag') != True:
					# menu_scene_jeoljeon_mode
					self.game_object.get_scene('menu_scene').status = 10
					self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
					self.set_option('jeoljeon_mode_flag', True)	
					return self.status
			elif pet_period != 0 and elapsed_time > pet_period and elapsed_time % pet_period < 5:
				self.logger.info('자동 사냥 중 반려 동물 체크')
				self.lyb_mouse_click('main_scene_menu')
				self.game_object.get_scene('menu_scene').status = self.get_work_status('반려동물 - 먹이주기')
			elif is_search_complete and elapsed_time % period_main_quest < 5:
				self.logger.info('퀘스트 완료 탐색(↓)')
				self.lyb_mouse_drag('main_scene_quest_drag_bottom', 'main_scene_quest_drag_top')
				return self.status
			elif is_search_complete and elapsed_time % period_main_quest < 10:
				self.logger.info('퀘스트 완료 탐색(↑)')
				self.lyb_mouse_drag('main_scene_quest_drag_top', 'main_scene_quest_drag_bottom')
				return self.status
			else:
				self.loggingElapsedTime(self.current_work, int(elapsed_time), limit_time, period=60)



			# 타겟 고정 풀기
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target') == True:
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'target_fix', custom_tolerance=50)
				if match_rate > 0.7:
					self.logger.info('타겟 고정을 해제합니다.')
					self.lyb_mouse_click('target_fix', custom_threshold=0)
					return True




			failover_lag = self.get_checkpoint(self.current_work + '_failover_lag')
			if failover_lag == 0:
				failover_lag = time.time()
				self.set_checkpoint(self.current_work + '_failover_lag')

			failover_lag_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag'))
			if failover_lag_threshold != 0:
				elapsed_time = time.time() - failover_lag
				self.loggingElapsedTime('자동 사냥 랙 방지', int(elapsed_time), failover_lag_threshold, period=30)
				if elapsed_time > failover_lag_threshold:
					random_direction = int(random.random() * 8)
					self.logger.warn('자동 사냥 랙 방지 움직임: ' + str(lybgamebd.LYBBlackDesert.character_move_list[random_direction]))
					self.set_checkpoint(self.current_work + '_failover_lag')
					self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(random_direction), stop_delay=1)
					return True
			else:
				self.set_checkpoint(self.current_work + '_failover_lag')


			# if self.is_sudong() == True:
			# 	self.lyb_mouse_click('sudong', custom_threshold=0)

			# self.game_object.interval = self.period_bot(0.01)

		elif self.status == self.get_work_status('마우스 클릭'):
			loc_x = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'))
			loc_y = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'))

			self.lyb_mouse_click_location(loc_x, loc_y)
			self.status = self.last_status[self.current_work] + 1

		elif self.status == self.get_work_status('기술 성장'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_gisul', custom_threshold=0)

		elif (	self.status == self.get_work_status('흑정령 - 흑정령 의뢰') or
				self.status == self.get_work_status('흑정령 - 검은 기운') or
				self.status == self.get_work_status('흑정령 - 수정 합성') or
				self.status == self.get_work_status('흑정령 - 광원석 합성') or
				self.status == self.get_work_status('흑정령 - 잠재력 돌파')
				):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('hukjeongryoung_soksakim_scene').status = self.status
			self.lyb_mouse_click('main_scene_hukjeongryoung', custom_threshold=0)

		elif self.status == self.get_work_status('반려동물 - 먹이주기'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('menu_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

		elif (	self.status == self.get_work_status('우편함') or
				self.status == self.get_work_status('도감')
				):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('menu_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

		elif self.status == self.get_work_status('이야기'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(600):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option('iyagi_start', False)
				self.set_option('inner_status', None)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.get_option('iyagi_start') != True:
				self.game_object.get_scene('menu_scene').status = self.status
				self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
				self.game_object.interval = self.period_bot(2)
			else:
				inner_status = self.get_option('inner_status')
				if inner_status == None:
					inner_status = 0

				if inner_status >= 0 and inner_status < 30:
					pb_name = 'main_scene_quest_iyagi'
					(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
									self.window_image,
									self.game_object.resource_manager.pixel_box_dic[pb_name],
									custom_threshold=0.7,
									custom_flag=1,
									custom_rect=(480, 90, 630, 210)
									)
					self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)					
						self.set_option('inner_status', inner_status + 1)
				else:							
					if inner_status > 200:
						self.set_option('inner_status', 0)
					else:
						self.set_option('inner_status', inner_status + 1)

					self.loggingElapsedTime(self.current_work, elapsed_time, 600)

		elif self.status == self.get_work_status('캐릭터 변경'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('menu_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

		elif (	self.status == self.get_work_status('교감') or
				self.status == self.get_work_status('말 가방에 넣기') or
				self.status == self.get_work_status('말 가방 모두 꺼내기') ):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(60):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_status', None)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			inner_status = self.get_option(self.current_work + '_status')
			if inner_status == None or inner_status == 0:
				is_clicked = self.main_scene_close_map()
				inner_status = 1
			elif inner_status == 1:
				self.lyb_mouse_click('main_scene_horse_top', custom_threshold=0)
				self.game_object.interval = self.period_bot(3)
				inner_status += 1
			elif inner_status == 2:
				if self.status == self.get_work_status('교감'):
					pb_name = 'horse_gyogam'
				elif self.status == self.get_work_status('말 가방에 넣기'):
					pb_name = 'horse_bag'
				elif self.status == self.get_work_status('말 가방 모두 꺼내기'):
					pb_name = 'horse_bag'

				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.85,
								custom_flag=1,
								custom_rect=(180, 70, 460, 300)
								)
				self.logger.warn(match_rate)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.game_object.get_scene('mal_gwanri_scene').status = self.status
					self.game_object.interval = self.period_bot(3)
					inner_status += 1
				else:
					inner_status -= 1
			else:
				self.lyb_mouse_click('sudong', custom_threshold=0)
				self.set_option(self.current_work + '_end_flag', True)
			
			self.set_option(self.current_work + '_status', inner_status)


		elif self.status == self.get_work_status('캐릭터 이동'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			direction_index = lybgamebd.LYBBlackDesert.character_move_list.index(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'character_move'))
			# self.logger.warn(str(direction_index) + ':' + str(lybgamebd.LYBBlackDesert.character_move_list[direction_index]))
			# self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'))
			move_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'))

			self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(direction_index), stop_delay=move_time)
			self.set_option(self.current_work + '_end_flag', True)

		elif (	self.status == self.get_work_status('길드') or
				self.status == self.get_work_status('인사하기')):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('menu_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

		elif self.status == self.get_work_status('과제'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('menu_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

		elif self.status == self.get_work_status('가축상점'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option('exclude', False)	
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_status', 0)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.is_field() == True:
				self.logger.warn('캐릭터가 필드에 있습니다. 작업을 종료합니다([마을로 이동] 작업을 먼저 실행하세요).')
				self.set_option(self.current_work + '_end_flag', True)
			else:
				self.main_scene_goto_shop(self.current_work)

		elif self.status == self.get_work_status('교본상점'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option('exclude', False)	
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_status', 0)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.is_field() == True:
				self.logger.warn('캐릭터가 필드에 있습니다. 작업을 종료합니다([마을로 이동] 작업을 먼저 실행하세요).')
				self.set_option(self.current_work + '_end_flag', True)
			else:
				self.main_scene_goto_shop(self.current_work)

		elif self.status == self.get_work_status('이벤트 보상 수령'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				pb_name = 'main_scene_bosang'
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
												self.window_image,
												self.game_object.resource_manager.pixel_box_dic[pb_name],
												custom_threshold=0.7,
												custom_flag=1,
												custom_rect=(150, 30, 250, 130)
												)
				self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)

				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_clicked')
			if elapsed_time > 30:
				if self.click_event_bosang() == True:
					self.set_option('event_status', 0)
					self.set_option('event_tab_iterator', 0)
					self.set_checkpoint(self.current_work + '_clicked')

		elif self.status == self.get_work_status('마을로 이동'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.is_field() == False:
				self.logger.warn('캐릭터가 마을에 있습니다. 작업을 종료합니다.')
				self.set_option(self.current_work + '_end_flag', True)
			else:
				elapsed_time = time.time() - self.get_checkpoint(self.current_work + '_clicked')
				if elapsed_time > 30:
					if self.click_to_maul() == True:
						self.set_checkpoint(self.current_work + '_clicked')

		elif self.status == self.get_work_status('월드 보스'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(1200):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_clicked', False)
				self.set_option('exclude', False)	
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.get_option(self.current_work + '_clicked') != True:
				self.set_option('exclude', True)

				(loc_x, loc_y), match_rate, pb_name = self.find_world_boss()
				self.logger.warn(str(pb_name) + ' ' + str(match_rate))
				if match_rate > 0.7:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.set_option(self.current_work + '_clicked', False)
					self.set_checkpoint(self.current_work + '_check_start')
				else:
					self.logger.warn('월드 보스 아이콘 감지 실패 - 작업을 종료합니다')
					self.set_option(self.current_work + '_end_flag', True)
			else:

				# 항상 보스 입구를 찾아본다.

				custom_rect = (180, 90, 480, 260)
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
												self.window_image,
												self.game_object.resource_manager.pixel_box_dic['main_scene_enter_world_boss'],
												custom_threshold=0.7,
												custom_flag=1,
												custom_rect=custom_rect
												)
				self.logger.warn('월드 보스 입구: ' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					return self.status

				elapsedTime = self.get_elapsed_time()
				limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss'))
				if elapsedTime < limit_time:
					self.loggingElapsedTime('월드 보스 이동', elapsedTime, limit_time)
					self.set_option(self.current_work + '_status', 0)
					self.set_option(self.current_work + '_direction_index', 0)
					self.set_option(self.current_work + '_boss_check', 0)
				else:
					inner_status = self.get_option(self.current_work + '_status')
					if inner_status == None:
						inner_status = 0
					direction_index = self.get_option(self.current_work + '_direction_index')
					if direction_index == None:
						direction_index = 0

					if inner_status == 0:
						(loc_x, loc_y), match_rate, pb_name = self.find_world_boss()
						self.logger.warn(str(pb_name) + ' ' + str(match_rate))
						if match_rate < 0.7:
							boss_check = self.get_option(self.current_work + '_boss_check')
							if boss_check == None:
								boss_check = 0

							if boss_check > 1:
								self.set_option(self.current_work + '_status', 99)
							else:
								self.set_option(self.current_work + '_boss_check', boss_check + 1)
						else:
							self.set_option(self.current_work + '_boss_check', 0)
							if direction_index > 7:
								self.logger.warn('월드 보스 입구 탐색 실패 - 재탐색 시도')
								self.set_option(self.current_work + '_direction_index', None)
							else:
								self.logger.warn('월드 보스 입구 탐색... ' + str(lybgamebd.LYBBlackDesert.character_move_list[direction_index]))
								self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(direction_index), stop_delay=1)
								self.set_option(self.current_work + '_status', inner_status + 1)
								self.set_option(self.current_work + '_direction_index', direction_index + 1)
					elif inner_status == 1:

						# custom_rect = (180, 90, 480, 260)
						# (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						# 								self.window_image,
						# 								self.game_object.resource_manager.pixel_box_dic['main_scene_enter_world_boss'],
						# 								custom_threshold=0.7,
						# 								custom_flag=1,
						# 								custom_rect=custom_rect
						# 								)
						# self.logger.warn(match_rate)
						# if loc_x != -1:
						# 	self.lyb_mouse_click_location(loc_x, loc_y)
						# 	self.set_option(self.current_work + '_status', inner_status + 1)
						# else:
						#	self.set_option(self.current_work + '_status', inner_status + 2)
						self.set_option(self.current_work + '_status', inner_status + 1)
					elif inner_status == 2:

						# custom_rect = (180, 90, 480, 260)
						# (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						# 								self.window_image,
						# 								self.game_object.resource_manager.pixel_box_dic['main_scene_enter_world_boss'],
						# 								custom_threshold=0.7,
						# 								custom_flag=1,
						# 								custom_rect=custom_rect
						# 								)
						# self.logger.warn(match_rate)
						# if loc_x != -1:
						# 	self.lyb_mouse_click_location(loc_x, loc_y)
						# else:
						# 	self.set_option(self.current_work + '_status', 99)
						self.set_option(self.current_work + '_status', inner_status + 1)
					elif inner_status == 3:
						(loc_x, loc_y), match_rate, pb_name = self.find_world_boss()
						self.logger.warn(str(pb_name) + ' ' + str(match_rate))
						if loc_x != -1:
							self.lyb_mouse_click_location(loc_x, loc_y)
						self.set_option(self.current_work + '_status', inner_status + 1)
					elif inner_status == 4:
						self.game_object.interval = self.period_bot(10)
						self.set_option(self.current_work + '_status', 0)
					elif inner_status >= 99:
						self.main_scene_check_sudong(custom_count=3)
						self.set_option(self.current_work + '_status', inner_status + 1)
						self.logger.info('월드 보스 진행 중... ' + str(inner_status))
						if inner_status > 200:
							self.set_option('exclude', False)							

		elif self.status == self.get_work_status('투기장'):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('menu_scene').status = self.status
			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

		elif self.status == self.get_work_status('영지'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(10):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.game_object.get_scene('youngji_scene').status = self.status
			self.game_object.current_matched_scene['name'] = ''
			self.lyb_mouse_click('main_scene_youngji', custom_threshold=0)


		elif self.status == self.get_work_status('영지로 이동'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(10):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_scene_migung_loc', custom_below_level=200,custom_top_level=255)
			# self.logger.warn('미궁: ' + str(match_rate))
			if match_rate < 0.7:
				is_clicked = self.lyb_mouse_click('main_scene_youngji')
				if is_clicked == False:
					self.set_option(self.current_work + '_end_flag', True)

			self.game_object.current_matched_scene['name'] = ''

		elif self.status == self.get_work_status('영지 나가기'):
			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(10):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			is_clicked = self.main_scene_out()
			if is_clicked == False:
				self.set_option(self.current_work + '_end_flag', True)

		elif self.status == self.get_work_status('토벌 게시판'):
			# elapsed_time = self.get_elapsed_time()
			# if elapsed_time > self.period_bot(5):
			# 	self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.lyb_mouse_click('main_scene_out', custom_threshold=0)
				self.game_object.get_scene('tobeol_gesipan_scene').status = 99999
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_clicked', False)	
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.get_option(self.current_work + '_clicked') == True:

				tobeol_lag = self.get_checkpoint('tobeol_lag')
				if tobeol_lag == 0:
					tobeol_lag = time.time()
					self.set_checkpoint('tobeol_lag')

				migung_lag_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'))
				if migung_lag_threshold != 0:
					elapsed_time = time.time() - tobeol_lag
					if elapsed_time > migung_lag_threshold:
						random_direction = int(random.random() * 8)
						self.logger.warn('토벌 랙 방지 움직임: ' + str(lybgamebd.LYBBlackDesert.character_move_list[random_direction]))
						self.set_checkpoint('tobeol_lag')
						self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(random_direction), stop_delay=1)
						return self.status
				else:
					self.set_checkpoint('tobeol_lag')

				is_clicked = self.process_main_quest_sub(
					'tobeol_quest_troll',
					custom_below_level=(150, 150, 150),
					custom_top_level=(255, 255, 255),
					custom_r_rect=(200, 30, 400, 130),
					threshold_main_quest=0.7,
					no_delay=True)
				if is_clicked == True:
					return self.status

			else:
				self.logger.warn('[토벌 게시판]작업은 물약 상점 앞에서 시작하세요')
				# is_clicked = self.lyb_mouse_click('main_scene_youngji')
				# if is_clicked == False:
				# 	self.set_option(self.current_work + '_end_flag', True)

				self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
				self.game_object.get_scene('menu_scene').status = self.status

				self.game_object.get_scene('youngji_scene').status = self.status
				self.game_object.current_matched_scene['name'] = ''

		elif (	self.status == self.get_work_status('미궁 목록') or
				self.status == self.get_work_status('미궁 개척') ):

			self.logger.critical('[' + self.current_work + '] 작업은 더 이상 지원하지 않습니다.')

			self.set_option(self.current_work + '_end_flag', True)

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > 3600:
				self.set_option(self.current_work + '_end_flag', True)
			
			if self.get_option(self.current_work + '_end_flag') == True:
				self.main_scene_out()
				if self.status == self.get_work_status('미궁 목록'):
					self.game_object.get_scene('migung_scene').status = 99999
				elif self.status == self.get_work_status('미궁 개척'):
					self.game_object.get_scene('migung_gecheok_scene').status = 99999
				self.set_option(self.current_work + '_end_flag', False)
				self.set_option(self.current_work + '_clicked', False)	
				self.status = self.last_status[self.current_work] + 1
				return self.status

			if self.get_option(self.current_work + '_clicked') == True:
				match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_scene_migung_loc', custom_below_level=200,custom_top_level=255)
				# self.logger.warn('미궁: ' + str(match_rate))
				if match_rate < 0.5:
					migung_check_count = self.get_option(self.current_work + '_migung_check_count')
					migung_check_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit'))
					if migung_check_count == None:
						migung_check_count = 0
					self.logger.warn('미궁 체크: ' + str(migung_check_count) + '/' + str(migung_check_limit))
					if migung_check_count >= migung_check_limit:
						self.set_option(self.current_work + '_clicked', False)
						self.set_option(self.current_work + '_migung_check_count', 0)
					else:
						self.set_option(self.current_work + '_migung_check_count', migung_check_count + 1)
				else:
					self.set_option(self.current_work + '_migung_check_count', 0)
			else:
				self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
				self.game_object.get_scene('menu_scene').status = self.status
				# is_clicked = self.lyb_mouse_click('main_scene_youngji')
				# if is_clicked == False:
				# 	self.set_option(self.current_work + '_end_flag', True)

				self.game_object.get_scene('youngji_scene').status = self.status
				self.game_object.current_matched_scene['name'] = ''


		elif self.status == self.get_work_status('낚시'):
			match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_scene_migung_loc', custom_below_level=200,custom_top_level=255)
			if match_rate > 0.7:
				is_clicked = self.main_scene_check_sudong()
				return self.status

			elapsed_time = self.get_elapsed_time()
			limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit'))
			if elapsed_time > limit_time:
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status
			threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box')) * 0.01

			fish_status = self.get_option('fish_status')
			if fish_status == None:
				fish_status = 0

			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic['fishing_lod'],
					custom_threshold=threshold_main_quest,
					custom_flag=1,
					custom_rect=(550, 300, 600, 360)
					)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.set_option('fish_status', 0)
				self.game_object.interval = self.period_bot(3)
				return self.status

			is_clicked = self.process_main_quest_sub(
				pixel_box_name='fishing_lure',
				custom_below_level=(210, 210, 210),
				custom_top_level=(255, 255, 255),
				custom_r_rect=(550, 300, 600, 360),
				threshold_main_quest=threshold_main_quest,
				no_delay=True)
			if is_clicked == True:
				self.set_option('fish_status', 1)
				self.game_object.interval = self.period_bot(2)
				return self.status

			if fish_status == 1:
				(s_loc_x, s_loc_y) = self.get_location('fish_green_top')
				(e_loc_x, e_loc_y) = self.get_location('fish_green_bottom')

				pb = self.get_center_pixel_info('fish_green_top')
				pb_rgb = pb[1]

				total_length = e_loc_y - s_loc_y
				j = 0
				is_inside = False
				while True:
					(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, s_loc_x, s_loc_y + j)

					if abs(pb_rgb[0] - r) > 50 or abs(pb_rgb[1] - g) > 50 or abs(pb_rgb[2] - b) > 50:
						is_inside = True
						break
						
					j += 1
					if j > total_length:
						break

				if is_inside == True:
					self.lyb_mouse_click('fishing_lure', custom_threshold=0)
					self.game_object.interval = self.period_bot(0.01)
				else:
					self.game_object.interval = self.period_bot(0.01)

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

		elif self.current_work != None and self.status == (1000 * 1000) + self.get_work_status(self.current_work):

			if self.get_option(self.current_work + '_end_flag') == True:
				self.status = self.get_work_status(self.current_work)
				return self.status

			# 사료 구매 시퀀스
			saryo_sequence_status = self.get_option('saryo_sequence_status')
			if saryo_sequence_status == None:
				saryo_sequence_status = 0

			self.logger.warn('사료 구매 시퀀스 실행 중 ' + str(saryo_sequence_status))

			if saryo_sequence_status >= 0 and saryo_sequence_status < 100:
				if self.is_field() == True:
					self.set_option('go_to_home_flag', True)
					if self.click_to_maul() == True:
						self.set_option('saryo_sequence_status', 100)
						self.checkpoint[self.current_work + '_check_start'] = time.time()
						self.game_object.interval = self.period_bot(5)
					else:
						self.set_option('saryo_sequence_status', saryo_sequence_status + 1)
				else:
					self.set_option('saryo_sequence_status', 100)
					self.checkpoint[self.current_work + '_check_start'] = time.time()

					# else:
					# 	self.status = self.status - (1000 * 1000)
			elif saryo_sequence_status == 100:
				self.main_scene_goto_shop('가축상점')
		else:
			self.status = self.last_status[self.current_work] + 1


		s = time.time()
		is_clicked = self.post_process_main_scene()
		e = time.time()
		# self.logger.warn('@ ElapsedTime post_process_main_scene: ' + str(round(e - s, 5)))
		if is_clicked == True:
			return self.status


		return self.status





















































	def init_screen_scene(self):
		
		self.schedule_list = self.get_game_config('schedule_list')
		if not '게임 시작' in self.schedule_list:
			return 0


		loc_x = -1
		loc_y = -1


		if self.game_object.player_type == 'nox':
			for each_icon in lybgamebd.LYBBlackDesert.nox_bd_icon_list:
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
			for each_icon in lybgamebd.LYBBlackDesert.momo_bd_icon_list:
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(30, 40, 610, 300)
								)
				# self.logger.debug(match_rate)
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					break

		# if loc_x == -1:
		# 	self.loggingToGUI('테라 아이콘 발견 못함')

		return 0

	def logo_screen_scene(self):

		self.schedule_list = self.get_game_config('schedule_list')
		if not '로그인' in self.schedule_list:
			return 0

		if time.time() - self.get_checkpoint('wait_finding_account') > 30:
			self.status = 0

		if self.status == 0:
			self.set_checkpoint('wait_finding_account')
			if self.get_window_config('multi_account'):
				self.logger.info('구글 계정 변경 시도')
				
			self.status += 1
		elif self.status == 1:
			if time.time() - self.get_checkpoint('wait_finding_account') > 100:
				self.logger.warn('구글 계정 감지 실패')
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
		self.logger.info('구글 계정 기준점: ' + str((top_loc_x, top_loc_y)))
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
				self.logger.info('구글 계정 5개 이상 감지됨')
			else:
				self.logger.info('구글 계정 '+str(self.google_account_number)+'개 감지됨')

		if self.status >= self.google_account_number:
			self.status = 0		
			self.logger.info(str(self.google_account_number)+' 개의 계정 작업 완료')	
			return self.status
		else:
			self.logger.info(str(self.status + 1)+' 번째 구글 계정 로그인 시도')
			# self.game_object.get_scene('connect_account_scene').set_option('select_complete_flag', True)
		
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
					self.logger.warn(str(self.status + 1)+' 번째 구글 계정 감지 실패')
					self.logger.info('총 '+str(self.status)+' 개의 계정 작업 완료')
					self.status = 0

				else:
					click_loc_x = top_loc_x + 10
					click_loc_y = top_loc_y + self.google_account_height*4 + self.google_account_height*0.8
					self.lyb_mouse_click_location(click_loc_x, click_loc_y)
					#self.lyb_mouse_move_location(click_loc_x, click_loc_y)
					self.status += 1

		return self.status









	def is_potion(self):
		pixel_box_name = 'potion_icon'
		sudong_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pixel_box_name, custom_tolerance=100)
		if sudong_rate > 0.7:
			return True

		return False

	def is_sudong(self):
		pixel_box_name = 'sudong'
		sudong_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pixel_box_name, custom_tolerance=100)

		if sudong_rate > 0.95:
			# self.logger.debug('수동 아이콘: ' + str(sudong_rate))
			return True

		return False

	def is_moving(self):
		if self.is_field() == True:
			moving_threshold = self.get_option('main_scene_moving_threshold')
			if moving_threshold == None:
				moving_threshold = 0

			moving_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit'))
			if moving_limit != 0:
				if moving_threshold < moving_limit:
					pb_name = "main_scene_moving"
					match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_top_level=255, custom_below_level=180)
					if match_rate > 0.9:
						self.logger.info("이동 중..." + str(moving_threshold) + '/' + str(moving_limit))
						self.set_option('main_scene_moving_threshold', moving_threshold + 1)
						return True
					else:
						self.set_option('main_scene_moving_threshold', 0)				
				elif moving_threshold >= moving_limit and moving_threshold < moving_limit + 20:
					self.set_option('main_scene_moving_threshold', moving_threshold + 1)
				else:
					self.set_option('main_scene_moving_threshold', 0)

			return False

	def exclude_work_main_scene(self):
		# 선처리 통과

		if self.current_work == None or len(self.current_work) < 1:
			return True
		elif self.current_work == '게임 시작':
			return True
		elif self.current_work == '로그인':
			return True
		elif self.current_work == '[작업 대기]':
			return True
		elif self.current_work == '캐릭터 이동':
			return True
		elif self.current_work == '마을로 이동':
			return True
		elif self.current_work == '낚시':
			return True

		if self.get_option('exclude') == True:
			self.logger.debug('Excluded!!')
			return True

		return False

	def pre_process_main_scene(self):

		# 순서가 중요하다.
		if self.exclude_work_main_scene() == True:
			return False

		#. 전투의 흔적
		threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box')) * 0.01
		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box') == True and self.is_field():
			s = time.time()
			box_range_index = lybgamebd.LYBBlackDesert.box_range_list.index(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range'))
			# self.logger.debug('box range: ' + str(box_range_index))

			if box_range_index == 0:
				custom_rect = (230, 160, 400, 320)
			elif box_range_index == 1:
				custom_rect = (180, 120, 450, 265)
			else:
				custom_rect = (180, 50, 600, 350)

			combat_box_iterator = self.get_option('combat_box_iterator')
			if combat_box_iterator == None:
				combat_box_iterator = 0

			if combat_box_iterator == 0:
				#. 박스 루팅 1
				is_clicked = self.process_main_quest_sub(
					'main_quest_looting',
					custom_below_level=(150, 150, 150),
					custom_top_level=(255, 255, 255),
					custom_r_rect=custom_rect,
					threshold_main_quest=threshold_main_quest,
					no_delay=True)
			else:
				#. 박스 루팅 2
				is_clicked = self.process_main_quest_sub(
					'main_quest_looting2',
					custom_below_level=(150, 150, 150),
					custom_top_level=(255, 255, 255),
					custom_r_rect=custom_rect,
					threshold_main_quest=threshold_main_quest,
					no_delay=True)


			e = time.time()
			# self.logger.debug('+ElapsedTime 박스 루팅: ' + str(round(e - s, 5)))

			if is_clicked == True:
				return True

			combat_box_iterator += 1
			if combat_box_iterator > 1:
				combat_box_iterator = 0
			self.set_option('combat_box_iterator', combat_box_iterator)

		#. 채집, 채광, 벌목
		custom_rect = (230, 120, 420, 300)
		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang') == True and self.is_field():
			is_clicked = self.process_main_quest_sub(
				'main_quest_chegwang',
				custom_below_level=(150, 150, 150),
				custom_top_level=(255, 255, 255),
				custom_r_rect=custom_rect,
				threshold_main_quest=threshold_main_quest,
				no_delay=True)
			if is_clicked == True:
				return True

		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip') == True and self.is_field():
			is_clicked = self.process_main_quest_sub(
				'main_quest_chejip',
				custom_below_level=(150, 150, 150),
				custom_top_level=(255, 255, 255),
				custom_r_rect=custom_rect,
				threshold_main_quest=threshold_main_quest,
				no_delay=True)
			if is_clicked == True:
				return True

		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok') == True and self.is_field():
			is_clicked = self.process_main_quest_sub(
				'main_quest_beolmok',
				custom_below_level=(150, 150, 150),
				custom_top_level=(255, 255, 255),
				custom_r_rect=custom_rect,
				threshold_main_quest=threshold_main_quest,
				no_delay=True)
			if is_clicked == True:
				return True

		threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest')) * 0.01
		#. 완료 1
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_complete',
			# custom_below_level=(210, 210, 210),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=(490, 100, 520, 210),
			custom_r_rect=(600, 100, 640, 210),
			threshold_main_quest=threshold_main_quest,
			no_delay=True,
			pair_click=True)
		if is_clicked == True:
			self.do_complete_sequence()
			return True

		#. 완료 2
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_complete2',
			# custom_below_level=(210, 210, 210),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=(490, 100, 520, 210),
			custom_r_rect=(600, 100, 640, 210),
			threshold_main_quest=threshold_main_quest,
			no_delay=True,
			pair_click=True)
		if is_clicked == True:
			self.do_complete_sequence()
			return True


		#. 완료 3
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_complete3',
			# custom_below_level=(210, 210, 210),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=(490, 100, 520, 210),
			custom_r_rect=(600, 100, 640, 210),
			threshold_main_quest=threshold_main_quest*1.1,
			no_delay=True,
			pair_click=True)
		if is_clicked == True:
			self.do_complete_sequence()
			return True

		#. 완료 3
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_complete4',
			# custom_below_level=(210, 210, 210),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=(490, 100, 520, 210),
			custom_r_rect=(600, 100, 640, 210),
			threshold_main_quest=threshold_main_quest*1.2,
			no_delay=True,
			pair_click=True)
		if is_clicked == True:
			self.do_complete_sequence()
			return True

		#. 장비 TOUCH
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_touch',
			# custom_below_level=(210, 210, 210),
			# custom_top_level=(255, 255, 255),
			custom_r_rect=(180, 210, 230, 280),
			threshold_main_quest=threshold_main_quest,
			no_delay=True)
		if is_clicked == True:
			return True


		# 길드 토벌 확인
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'main_scene_guild_tobeol', custom_tolerance=100)
		# self.logger.warn('길드 토벌:' + str(match_rate))
		if match_rate > 0.9:
			guild_tobeol_check_count = self.get_option('guild_tobeol_check_count')
			if guild_tobeol_check_count == None:
				guild_tobeol_check_count = 0

			self.logger.warn('길드 토벌 인식됨: ' + str(guild_tobeol_check_count) +'/3')
			if guild_tobeol_check_count >= 3:
				self.set_option('guild_tobeol_check_count', 0)
				self.lyb_mouse_click('main_scene_guild_tobeol', custom_threshold=0)
				return True
			else:
				self.set_option('guild_tobeol_check_count', guild_tobeol_check_count + 1)
		else:
			self.set_option('guild_tobeol_check_count', 0)

		is_clicked = self.process_main_quest_sub(
			'go_to_home',
			threshold_main_quest=threshold_main_quest,
			custom_r_rect=(250, 200, 280, 230))
		if is_clicked == True:
			return True

		#. 물약 구매
		is_clicked = self.process_main_quest_sub(
			'potion',
			threshold_main_quest=threshold_main_quest*1.2,
			custom_r_rect=(480, 220, 630, 370),
			period_main_quest=int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop')))
		if is_clicked == True:
			# self.logger.debug('물약')
			if self.current_work != None:
				self.logger.warn('물약 상점을 이용하기 위해 현재 작업[' +str(self.current_work)+']을 종료합니다.')
				self.set_option(self.current_work + '_end_flag', True)

			return True

		#. 씨앗상점
		is_clicked = self.process_main_quest_sub(
			'jongja',
			threshold_main_quest=threshold_main_quest*1.2,
			custom_r_rect=(480, 220, 630, 370))
		if is_clicked == True:
			self.logger.debug('씨앗상점')
			return True

		is_clicked = self.process_main_quest_sub(
			'urechiso',
			threshold_main_quest=threshold_main_quest,
			custom_r_rect=(290, 200, 310, 235))
		if is_clicked == True:
			time.sleep(0.1)
			self.lyb_mouse_click('urechiso_button')
			return True

		#. 가방 풀
		if self.is_field() == True:
			self.set_option('field_check_count', 0)
			is_clicked = self.process_main_quest_sub(
				'gabang_warning',
				threshold_main_quest=threshold_main_quest,
				custom_r_rect=(240, 320, 400, 340),
				custom_below_level=(170, 40, 0), 
				custom_top_level=(250, 160, 80),
				period_main_quest=int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full')),
				pass_first=True)
			if is_clicked == True:
				self.set_option('gabang_warning_go_to_maul', True)
				return True
		else:
			field_check_count = self.get_option('field_check_count')
			if field_check_count == None:
				field_check_count = 0

			if field_check_count > 2:
				is_clicked = self.process_main_quest_sub(
					'gabang_warning',
					threshold_main_quest=threshold_main_quest,
					custom_r_rect=(240, 320, 400, 340),
					custom_below_level=(170, 40, 0),
					custom_top_level=(250, 160, 80),
					period_main_quest=2)
				if is_clicked == True:
					self.set_option('gabang_warning_go_to_maul', True)
					self.logger.info('무게추 클릭')
					return True
				self.set_option('field_check_count', 0)
			else:
				self.set_option('field_check_count', field_check_count + 1)


		#. 수동일 경우 자동으로 태세 전환
		is_clicked = self.main_scene_check_sudong()
		if is_clicked == True:
			return True

		if self.is_migung() == True:
			migung_lag = self.get_checkpoint('migung_lag')
			if migung_lag == 0:
				migung_lag = time.time()
				self.set_checkpoint('migung_lag')

			migung_lag_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'))

			if migung_lag_threshold != 0:
				elapsed_time = time.time() - migung_lag
				self.loggingElapsedTime('미궁 랙 방지', int(elapsed_time), migung_lag_threshold, period=30)
				if elapsed_time > migung_lag_threshold:
					random_direction = int(random.random() * 4) * 2
					self.logger.warn('미궁 랙 방지 움직임: ' + str(lybgamebd.LYBBlackDesert.character_move_list[random_direction]))
					self.set_checkpoint('migung_lag')
					self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(random_direction), stop_delay=1)
					return True
			else:
				self.set_checkpoint('migung_lag')
		else:
			self.set_checkpoint('migung_lag')


		#. 임무
		if self.is_sudong() == False:
			return False

		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_immu',
			# custom_below_level=(120, 90, 80),
			# custom_top_level=(180, 140, 110),
			custom_l_rect=(450, 90, 485, 140),
			custom_r_rect=(600, 90, 640, 140),
			threshold_main_quest=threshold_main_quest,
			period_main_quest=10)
		if is_clicked == True:
			return True

		# 여기가 마지막이다. 임무 위로 추가해라.

		return False

	def event_process_main_scene(self):

		# 메뉴
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'menu_scene_config')
		if match_rate > 0.9:
			self.game_object.current_matched_scene['name'] = ''
			return True

		if self.check_migung_invite() == True:
			return True

		# 입장 가능한 미궁 목록
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'migung_list_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('migung_list_close_icon', custom_threshold=0)
			return True

		# 영지로 이동?
		# match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'youngji_move_loc')
		# # self.logger.warn('영지로 이동: ' + str(match_rate))
		# if match_rate > 0.9:
		# 	self.lyb_mouse_click('youngji_move_confirm', custom_threshold=0)
		# 	if self.current_work != None and '영지' in self.current_work:
		# 		self.set_option(self.current_work+'_end_flag', True)
		# 	return True
		resource_name = 'youngji_move_loc'
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										resource_name,
										custom_threshold=0.8,
										custom_flag=1,
										custom_rect=(160, 100, 480, 320))
		if loc_x != -1:
			pb_name = 'youngji_move_confirm'
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(160, 100, 480, 320))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				if self.current_work != None and '영지' in self.current_work:
					self.set_option(self.current_work+'_end_flag', True)
				return True


		# 영지를 나가시겠습니까?
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'youngji_nagagi_loc')
		# self.logger.warn('영지를 나가기: ' + str(match_rate))
		if match_rate > 0.9:
			self.lyb_mouse_click('youngji_nagagi_confirm', custom_threshold=0)
			if self.current_work != None and '영지' in self.current_work:
				self.set_option(self.current_work+'_end_flag', True)
			return True

		# 영지를 나가시겠습니까? 2
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'youngji_nagagi2_loc')
		# self.logger.warn('영지를 나가기: ' + str(match_rate))
		if match_rate > 0.9:
			self.lyb_mouse_click('youngji_nagagi2_confirm', custom_threshold=0)
			if self.current_work != None and '영지' in self.current_work:
				self.set_option(self.current_work+'_end_flag', True)
			return True

		# 길드 토벌
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'guild_tobeol_confirm_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('guild_tobeol_confirm_button')
			return True

		# 보상 확인
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'bosang_confirm_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('bosang_confirm_button')
			return True

		# 보상 확인2 - 1줄짜리
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'bosang_confirm2_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('bosang_confirm2_button')
			return True

		# 보상 확인3 - 2줄짜리
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'bosang_confirm3_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('bosang_confirm3_button')
			return True

		# 보상 확인4 - 2줄짜리
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'bosang_confirm4_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('bosang_confirm4_button')
			return True

		# 보상 확인5 - 3줄 이상
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'bosang_confirm5_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('bosang_confirm5_button')
			return True

		# 검은 마력석 - 알림
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'black_notice_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('black_notice_confirm_button')
			return True

		# 미궁 생성
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'migung_create_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('migung_create_button')
			return True

		# 임무를 시작 하시겠습니까?
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'immu_start_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('immu_start_button')
			return True

		# 임무를 나가겠습니까?
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'immu_finish_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('immu_finish_button')
			return True
		
		# 이야기 보기
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'new_skill_story_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('new_skill_story_button')
			return True

		# 영지민 목록
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'youngjimin_list_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('youngjimin_list_complete')
			time.sleep(1)
			self.lyb_mouse_click('youngjimin_list_close')
			self.game_object.current_matched_scene['name'] = ''
			self.game_object.interval = self.period_bot(5)
			return True

		# 전리품 목록
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'jeonripum_mokrok_confirm_loc')
		if match_rate > 0.9:
			self.lyb_mouse_click('jeonripum_mokrok_confirm_button')
			return True

		# 출정
		# match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'chuljeong_loc')
		# if match_rate > 0.9:
		# 	self.set_option('월드 보스' + '_clicked', True)
		# 	self.logger.warn('출정')
		# 	self.lyb_mouse_click('chuljeong_button')
		# 	return True

		# 순서 중요
		# 출현 지역으로 이동하시겠습니까?
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'chulhyeon_move_loc')
		if match_rate > 0.9:
			self.logger.warn('출현 지역으로 이동하시겠습니까?')
			self.lyb_mouse_click('chulhyeon_move_confirm')
			return True

		# 출정
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'chuljeong_2_loc')
		if match_rate > 0.9:
			self.set_option('월드 보스' + '_clicked', True)
			self.logger.warn('출정')
			self.lyb_mouse_click('chuljeong_2_button')
			return True

		# 우두머리 현황판
		resource_name = 'chuljeong_loc'
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										resource_name,
										custom_threshold=0.8,
										custom_top_level=(140, 140, 140),
										custom_below_level=(70, 70, 70),
										source_custom_top_level=(255, 255, 255),
										source_custom_below_level=(130, 130, 130),
										custom_flag=1,
										custom_rect=(150, 320, 300, 360))
		if loc_x != -1:
			self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.logger.warn('월드 보스 출정 비활성 감지됨: 작업 종료')
			self.lyb_mouse_click('world_boss_dashboard_close', custom_threshold=0)
			self.game_object.get_scene('main_scene').set_option('월드 보스' + '_end_flag', True)
			return True

		# 우두머리 현황판
		resource_name = 'chuljeong_loc'
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										resource_name,
										custom_threshold=0.8,
										custom_top_level=(255, 255, 255),
										custom_below_level=(130, 130, 130),
										custom_flag=1,
										custom_rect=(150, 320, 300, 360))
		if loc_x != -1:
			self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			iterator = self.get_option(resource_name + '_iteration')
			if iterator == None:
				iterator = 0
			if iterator == 0:
				self.lyb_mouse_click_location(loc_x, loc_y)
			else:
				self.lyb_mouse_click('world_boss_dashboard_close', custom_threshold=0)

			self.set_option(resource_name + '_iteration', (iterator + 1) % 2)
			self.set_option('월드 보스' + '_clicked', True)
			self.logger.warn('출정')
			return True

		# 무법자
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'mubeopja_popup_loc')
		if match_rate > 0.9:
			self.logger.warn('무법자 모드 설정 비활성화 후 닫기')
			self.lyb_mouse_click('mubeopja_inactive', custom_threshold=0)
			time.sleep(1)
			self.lyb_mouse_click('mubeopja_popup_close_icon')
			return True

		# 이벤트 & 보상 수령
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'event_and_reward_loc')
		if match_rate > 0.9:
			self.logger.info("이벤트 보상 수령: " + str(match_rate))
			event_status = self.get_option('event_status')
			if event_status == None:
				event_status = 0

			elapsed_time = time.time() - self.get_checkpoint('er_last')
			if elapsed_time > 60:
				event_status = 0
				self.set_option('drag_count', 0)
				self.set_checkpoint('er_last')
			elif elapsed_time > 30:
				self.lyb_mouse_click('event_and_reward_close_icon')
				self.set_option('event_status', None)
				return True

			self.logger.debug('event_status: ' + str(event_status))
			if event_status == 0:
				for i in range(3):
					pb_name = 'event_and_reward_scene_new_' + str(i)
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(590, 90, 630, 370)
								)
					self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
					if loc_x != -1:
						self.lyb_mouse_click_location(loc_x, loc_y)
						self.set_option('er_row', 0)
						self.set_option('er_col', 0)
						self.set_option('event_status', 10)
						return True
					else:
						self.set_option('event_status', 20)
			elif event_status == 10:
				pb_name_list = [
					'event_and_reward_scene_chulseok',
					'event_and_reward_scene_chulseok_2',
					'event_and_reward_scene_chulseok_3',
					'event_and_reward_scene_chulseok_4',
					'event_and_reward_scene_mulpum',
					'event_and_reward_scene_mulpum_2',
					'event_and_reward_scene_bosang'
				]
				er_row = self.get_option('er_row')
				er_col = self.get_option('er_col')
				for row in range(er_row, 5):
					for col in range(er_col, 5):
						for pb_name in pb_name_list:
							(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
										self.window_image,
										self.game_object.resource_manager.pixel_box_dic[pb_name],
										custom_threshold=0.8,
										custom_flag=1,
										custom_rect=(50 + (col*80) - 45, 100 + (row*50) - 30, 150 + (col*80) + 40, 150 + (row*50) + 25)
										)
							self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
							if loc_x != -1:
								self.lyb_mouse_click_location(loc_x, loc_y)
								self.period_bot(3)
								self.set_option('er_row', er_row)
								self.set_option('er_col', er_col + 1)
								self.set_option('event_status', event_status + 1)
								return True

				self.set_option('event_status', 0)
			elif event_status >= 11 and event_status < 13:
				self.set_option('event_status', event_status + 1)
			elif event_status == 13:
				self.set_option('event_status', 10)
			elif event_status == 20:
				drag_count = self.get_option('drag_count')
				if drag_count > 1:
					self.lyb_mouse_click('event_and_reward_close_icon')
					self.set_option('event_status', None)
					return True
				self.set_option('drag_count', drag_count + 1)
				self.lyb_mouse_drag('event_and_reward_scene_drag_bot', 'event_and_reward_scene_drag_top', stop_delay=1)
				self.set_option('event_status', 0)

			return True

		# 미궁 초대
		# (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 			self.window_image,
		# 			self.game_object.resource_manager.pixel_box_dic['migung_invite'],
		# 			custom_flag=1,
		# 			custom_rect=(320, 160, 440, 200)
		# 			)
		# # self.logger.debug(match_rate)
		# if loc_x != -1:
		# 	if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean') == True:
		# 		migung_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'))
		# 		is_there = False
		# 		for i in range(migung_level - 1):
		# 			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 				self.window_image,
		# 				self.game_object.resource_manager.pixel_box_dic['migung_invite_level_' + str(i)],
		# 				custom_flag=1,
		# 				custom_rect=(350, 150, 440, 200)
		# 				)	
		# 			self.logger.debug(str(i) + ':' + str(match_rate))
		# 			if loc_x != -1:
		# 				is_there = True
		# 				break
		# 		self.logger.debug(is_there)
		# 		if is_there != True:
		# 			# 확인			
		# 			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 				self.window_image,
		# 				self.game_object.resource_manager.pixel_box_dic['migung_invite_ok'],
		# 				custom_flag=1,
		# 				custom_rect=(320, 220, 400, 300)
		# 				)
		# 			if loc_x != -1:
		# 				self.lyb_mouse_click_location(loc_x, loc_y)
		# 		else:
		# 			# 취소
		# 			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 				self.window_image,
		# 				self.game_object.resource_manager.pixel_box_dic['migung_invite_cancel'],
		# 				custom_flag=1,
		# 				custom_rect=(250, 220, 310, 300)
		# 				)
		# 			if loc_x != -1:
		# 				self.lyb_mouse_click_location(loc_x, loc_y)
		# 			return True
		# 	else:
		# 		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
		# 			self.window_image,
		# 			self.game_object.resource_manager.pixel_box_dic['migung_invite_cancel'],
		# 			custom_flag=1,
		# 			custom_rect=(250, 220, 310, 300)
		# 			)
		# 		if loc_x != -1:
		# 			self.lyb_mouse_click_location(loc_x, loc_y)
		# 		return True

				
		# 무게 정보
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'muge_jeongbo_loc')
		if match_rate > 0.9:
			if self.get_option('gabang_warning_go_to_maul') == True:
				self.set_option('gabang_warning_go_to_maul', False)

				muge_percentage = self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage')
				muge_percentage_index = lybgamebd.LYBBlackDesert.muge_percentage_list.index(muge_percentage)

				if muge_percentage_index > 0:
					for i in range(muge_percentage_index):
						pb_name = 'muge_number_' + str(lybgamebd.LYBBlackDesert.muge_percentage_list[i])
						match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
						if match_rate > 0.9:
							self.logger.warn("무게 " + str(lybgamebd.LYBBlackDesert.muge_percentage_list[i]) + " < " + str(muge_percentage) + " : 패스")
							self.lyb_mouse_click('muge_jeongbo_close_icon', custom_threshold=0)
							return True

				self.lyb_mouse_click('muge_jeongbo_to_maul', custom_threshold=0)
				if self.current_work != None:
					self.logger.warn('무게 경고로 상점 이동하기 위해 현재 작업[' +str(self.current_work)+']을 종료합니다.')					
					self.set_option(self.current_work + '_end_flag', True)
			else:
				self.lyb_mouse_click('muge_jeongbo_close_icon', custom_threshold=0)

			return True

		# 가까운 마을로 이동하시겠습니까?
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'go_to_maul_loc')
		if match_rate > 0.9:
			if self.get_option('potion_empty') == True:
				self.lyb_mouse_click('go_to_maul')
				self.set_option('potion_empty', False)
			elif self.get_option('go_to_home_flag') == True:
				self.lyb_mouse_click('go_to_maul')
				self.set_option('go_to_home_flag', False)
			elif self.current_work != None and self.current_work == '마을로 이동':
				is_clicked = self.lyb_mouse_click('go_to_maul')	
				if is_clicked == False:
					self.lyb_mouse_click('go_to_maul_close_icon', custom_threshold=0)					
			elif self.current_work != None and self.current_work == '자동 사냥' and self.get_option('fast_move_click') == True:
				quest_index = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'))
				pb_name = 'fast_move_location_' + str(quest_index - 5)				
				is_clicked = self.lyb_mouse_click(pb_name)				
				if is_clicked == False:
					self.logger.warn('빠른 이동 클릭 실패: ' + str(quest_index-4) + ' 번째 위치')
					self.lyb_mouse_click('go_to_maul_close_icon', custom_threshold=0)
				else:
					self.logger.warn('빠른 이동 클릭 성공: ' + str(quest_index-4) + ' 번째 위치')
			else:
				self.lyb_mouse_click('go_to_maul_close_icon', custom_threshold=0)
					
			return True


		# 생명력 회복제 구매를 위하여 가까운 마을로 이동하시겠습니까?
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'go_to_maul_potion_loc')
		if match_rate > 0.9:
			if self.get_option('potion_empty') == True:
				self.lyb_mouse_click('go_to_maul_potion')
				self.set_option('potion_empty', False)				
			else:
				self.lyb_mouse_click('go_to_maul_potion_close_icon', custom_threshold=0)
					
			return True

		if self.is_potion() == False:

			potion_empty_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit'))
			if potion_empty_limit > 0:
				# 물약 쿨 돌 때 이미지가 있으므로 진짜 물약이 없는 지를 체크한다.
				potion_empty_count = self.get_option('potion_empty_count')
				if potion_empty_count == None:
					potion_empty_count = 0

				if potion_empty_count == potion_empty_limit + 1:
					self.lyb_mouse_click('potion_icon', custom_threshold=0)
					self.set_option('potion_empty_count', potion_empty_count + 1)
					self.set_option('potion_empty', True)
					return True
				elif potion_empty_count > potion_empty_limit + 1 and potion_empty_count < potion_empty_limit + 5:	
					self.lyb_mouse_click('potion_icon', custom_threshold=0)	
					self.set_option('potion_empty_count', potion_empty_count + 1)
				elif potion_empty_count >= potion_empty_limit + 5:
					self.set_option('potion_empty_count', 0)
				else:
					if potion_empty_count > 5:
						self.logger.info('물약 없음 체크: ' + str(potion_empty_count) + '/' + str(potion_empty_limit))
					self.set_option('potion_empty_count', potion_empty_count + 1)
		else:
			self.set_option('potion_empty_count', 0)

		# 접속 유지 보상
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_scene_jeopsok_bosang_loc')
		if match_rate > 0.9:
			is_clicked = self.lyb_mouse_click('main_scene_jeopsok_bosang_receive')
			if is_clicked == False:
				self.lyb_mouse_click('main_scene_jeopsok_bosang_close_icon', custom_threshold=0)

			return True




			# tab_iterator = self.get_option('event_tab_iterator')
			# if tab_iterator == None:
			# 	tab_iterator = 0
			# elif tab_iterator > 4:
			# 	event_status = 7
			# 	self.set_option('event_tab_iterator', 0)

			# if event_status == 0:
			# 	self.lyb_mouse_click('event_and_reward_scene_tab_' + str(tab_iterator), custom_threshold=0)
			# 	self.set_option('event_status', event_status + 1)
			# elif event_status == 1:
			# 	pb_name = 'event_and_reward_scene_chulseok'
			# 	# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
			# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# 				self.window_image,
			# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
			# 				custom_below_level=(130, 130, 130),
			# 				custom_top_level=(255, 255, 255),
			# 				custom_threshold=0.6,
			# 				custom_flag=1,
			# 				custom_rect=(10, 200, 330, 240)
			# 				)
			# 	self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.set_option('event_status', 0)
			# 		self.set_option('event_tab_iterator', tab_iterator + 1)
			# 		self.game_object.interval = self.period_bot(3)
			# 	else:
			# 		self.set_option('event_status', event_status + 1)

			# elif event_status == 2:
			# 	pb_name = 'event_and_reward_scene_chulseok'
			# 	# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
			# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# 				self.window_image,
			# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
			# 				custom_below_level=(130, 130, 130),
			# 				custom_top_level=(255, 255, 255),
			# 				custom_threshold=0.6,
			# 				custom_flag=1,
			# 				custom_rect=(10, 290, 330, 330)
			# 				)
			# 	self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.set_option('event_status', 0)
			# 		self.set_option('event_tab_iterator', tab_iterator + 1)
			# 		self.game_object.interval = self.period_bot(3)
			# 	else:
			# 		self.set_option('event_status', event_status + 1)

			# elif event_status == 3:
			# 	pb_name = 'event_and_reward_scene_chulseok'
			# 	# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
			# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# 				self.window_image,
			# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
			# 				custom_below_level=(150, 150, 150),
			# 				custom_top_level=(255, 255, 255),
			# 				custom_threshold=0.6,
			# 				custom_flag=1,
			# 				custom_rect=(10, 250, 500, 300)
			# 				)
			# 	self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.set_option('event_status', 0)
			# 		self.set_option('event_tab_iterator', tab_iterator + 1)
			# 		self.game_object.interval = self.period_bot(3)
			# 	else:
			# 		self.set_option('event_status', event_status + 1)

			# elif event_status == 4:
			# 	pb_name = 'event_and_reward_scene_chulseok_3'
			# 	# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
			# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# 				self.window_image,
			# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
			# 				custom_threshold=0.7,
			# 				custom_flag=1,
			# 				custom_rect=(210, 310, 310, 340)
			# 				)
			# 	self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.set_option('event_status', 0)
			# 		self.set_option('event_tab_iterator', tab_iterator + 1)
			# 		self.game_object.interval = self.period_bot(3)
			# 	else:
			# 		self.set_option('event_status', event_status + 1)

			# elif event_status == 5:
			# 	pb_name = 'event_and_reward_scene_mulpum'
			# 	# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
			# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# 				self.window_image,
			# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
			# 				custom_below_level=(150, 150, 150),
			# 				custom_top_level=(255, 255, 255),
			# 				custom_threshold=0.6,
			# 				custom_flag=1,
			# 				custom_rect=(40, 200, 300, 340)
			# 				)
			# 	self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.set_option('event_status', 0)
			# 		self.set_option('event_tab_iterator', tab_iterator + 1)
			# 		self.game_object.interval = self.period_bot(3)
			# 	else:
			# 		self.set_option('event_status', event_status + 1)

			# elif event_status == 6:
			# 	pb_name = 'event_and_reward_scene_chulseok_2'
			# 	# self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
			# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# 				self.window_image,
			# 				self.game_object.resource_manager.pixel_box_dic[pb_name],
			# 				custom_below_level=(130, 130, 130),
			# 				custom_top_level=(255, 255, 255),
			# 				custom_threshold=0.7,
			# 				custom_flag=1,
			# 				custom_rect=(10, 250, 330, 290)
			# 				)
			# 	self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	if loc_x != -1:
			# 		self.lyb_mouse_click_location(loc_x, loc_y)
			# 		self.game_object.interval = self.period_bot(3)
			# 	self.set_option('event_status', 0)
			# 	self.set_option('event_tab_iterator', tab_iterator + 1)
			# # elif event_status == 3:
			# # 	(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
			# # 									self.window_image,
			# # 									'meil_immu_dalseong_loc',
			# # 									custom_flag=1,
			# # 									custom_rect=(500, 110, 620, 360))
			# # 	self.logger.warn('매일 임무 달성: ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# # 	if loc_x != -1:
			# # 		self.lyb_mouse_click_location(loc_x, loc_y)
			# # 		self.set_option('event_status', event_status + 1)
			# # 	else:
			# # 		self.set_option('event_status', 99999)
			# # elif event_status == 4:
			# # 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
			# # 				self.window_image,
			# # 				self.game_object.resource_manager.pixel_box_dic['meil_immu_dalseong_bosang'],
			# # 				custom_below_level=(130, 130, 130),
			# # 				custom_top_level=(255, 255, 255),
			# # 				custom_threshold=0.6,
			# # 				custom_flag=1,
			# # 				custom_rect=(10, 320, 500, 360)
			# # 				)
			# # 	self.logger.warn('보상 받기: ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# # 	if loc_x != -1:
			# # 		self.lyb_mouse_click_location(loc_x, loc_y)
			# # 		self.game_object.interval = self.period_bot(3)
			# # 	else:
			# # 		self.set_option('event_status', 99999)
			# else:
			# 	self.lyb_mouse_click('event_and_reward_close_icon')
			# 	self.set_option('event_status', 0)
			# 	self.set_option('event_tab_iterator', 0)

			# return True

		return False

	def post_process_main_scene(self):
		# 선처리 통과
		if self.exclude_work_main_scene() == True:
			return False

		threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box')) * 0.01

		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean') == True:

			for i in range(len(lybgamebd.LYBBlackDesert.ddolmani_skill_list)):
				#. 흑정령 스킬 열기

				if int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i))) == 0:
					continue

				# ddolmani_skill_status = self.get_option('ddolmani_skill_status_' + str(i))
				# if ddolmani_skill_status == None or ddolmani_skill_status > 1:
				# 	ddolmani_skill_status = 0

				elapsed_time = int(time.time() - self.get_checkpoint(lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)))
				if elapsed_time > int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i))):

						# 닫혀 있으면 열기
						match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'ddolmani_skill')
						if match_rate > 0.98:
							self.lyb_mouse_click('ddolmani_skill')
							return True

						match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'ddolmani_skill2')
						if match_rate < 0.98:
							self.lyb_mouse_click('ddolmani_skill2')
							return True

						self.set_checkpoint(lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i))
						# 스킬이 잘 안눌려진다.
						self.lyb_mouse_click('ddolmani_skill2_' + str(i), custom_threshold=0)
						time.sleep(0.1)
						self.lyb_mouse_click('ddolmani_skill2_' + str(i), custom_threshold=0)

						return True

		# ddolmani_skill2_delay = self.get_option('ddolmani_skill2_delay')
		# if ddolmani_skill2_delay == None:
		# 	ddolmani_skill2_delay = 0

		# if ddolmani_skill2_delay < 3:
		# 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, 'ddolmani_skill2')
		# 	if match_rate > 0.9:
		# 		self.set_option('ddolmani_skill2_delay', ddolmani_skill2_delay + 1)
		# 		self.lyb_mouse_click('ddolmani_skill2', custom_threshold=0)
		# 		return True
		# 	else:
		# 		self.set_option('ddolmani_skill2_delay', 0)
		# else:
		# 	if ddolmani_skill2_delay > 30:
		# 		self.set_option('ddolmani_skill2_delay', 0)
		# 	else:
		# 		self.set_option('ddolmani_skill2_delay', ddolmani_skill2_delay + 1)

		return False

	def process_main_quest(self):
		#. 완료
		custom_l_rect=(490, 90, 520, 130)
		custom_r_rect=(600, 90, 640, 130)

		threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest')) * 0.01
		period_main_quest_afk = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk'))
		period_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'))
		period_wait_attack = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack'))

		last_clicked_main_quest = self.get_checkpoint('main_quest_clicked')
		self.logger.debug('AFK TimeCheck:' + str(int(time.time() - last_clicked_main_quest)) + '/' + str(period_main_quest_afk) + ' sec')
		if last_clicked_main_quest != 0 and time.time() - last_clicked_main_quest > period_main_quest_afk:
			self.logger.debug('AFK Clicked')
			self.lyb_mouse_click('quest_location_0', custom_threshold=0)
			time.sleep(1)
			self.lyb_mouse_click('quest_location_0', custom_threshold=0)
			self.set_checkpoint('main_quest_clicked')

			return True

		#. 펫
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_pet',
			custom_below_level=(210, 210, 210),
			custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return

		#. 대화
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_conversation',
			custom_below_level=(150, 150, 150),
			custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 임무 시작 대화
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_immu_start',
			# custom_below_level=(150, 150, 150),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 손
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_hand3',
			custom_below_level=(150, 150, 150),
			custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 호미
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_homi2',
			custom_below_level=(150, 150, 150),
			custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 도끼
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_dokki2',
			custom_below_level=(150, 150, 150),
			custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 미로
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_miro',
			# custom_below_level=(150, 150, 150),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 물고기
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_fish',
			# custom_below_level=(150, 150, 150),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest*1.1,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 느낌표
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_warning',
			# custom_below_level=(150, 150, 150),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			no_delay=True,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 처치
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_monster',
			custom_below_level=(150, 150, 150),
			custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest,
			period_main_quest=period_main_quest,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 써클
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_r_circle',
			# custom_below_level=(150, 150, 150),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest*1.1,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		#. 기술
		is_clicked = self.process_main_quest_sub(
			pixel_box_name='main_quest_r_gisul',
			# custom_below_level=(150, 150, 150),
			# custom_top_level=(255, 255, 255),
			custom_l_rect=custom_l_rect,
			custom_r_rect=custom_r_rect,
			threshold_main_quest=threshold_main_quest*1.1,
			wait_attack=True,
			pair_click=True)
		if is_clicked == True:
			return True

		# 물약 먹는 메인 퀘스트를 감지해보자.
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_quest_lv1_potion_loc', custom_tolerance=100)
		self.logger.debug('물약 먹는 메인 퀘스트: ' + str(match_rate))
		if match_rate > 0.98:
			self.lyb_mouse_click('potion_icon', custom_threshold=0)
			return True

		# 기술 교본 배우는 메인퀘스트를 감지해보자.
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_quest_lv5_skill_loc', custom_tolerance=100)
		self.logger.debug('기술 교본 배우는 메인 퀘스트: ' + str(match_rate))
		if match_rate > 0.98:
			self.lyb_mouse_click('main_scene_gisul', custom_threshold=0)
			self.game_object.get_scene('gisul_scene').status = 100
			return True

		# 벨리아 마을로
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_quest_lv19_move_loc', custom_tolerance=100)
		self.logger.debug('벨리아 마을로 메인 퀘스트: ' + str(match_rate))
		if match_rate > 0.98:
			# 작동			
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic['main_quest_lv19_move_enter'],
				custom_flag=1,
				custom_rect=(250, 100, 400, 250)
				)
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				time.sleep(2)
				self.lyb_mouse_click('main_quest_lv19_move_sequence_0', custom_threshold=0)
				time.sleep(2)
				self.lyb_mouse_click('main_quest_lv19_move_sequence_1', custom_threshold=0)
				time.sleep(2)
				self.lyb_mouse_click('main_quest_lv19_move_sequence_2', custom_threshold=0)

				return True

		# 지붕 위의 수상한 자
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_quest_lv22_jibung_loc', custom_tolerance=100)
		self.logger.debug('지붕 위의 수상한 자: ' + str(match_rate))
		if match_rate > 0.98:
			self.checkpoint['main_quest_clicked'] = 0
			self.game_object.telegram_send('[지붕 위의 수상한 자] 퀘스트에서 막혔습니다. 확인해주세요!')

			main_quest_lv22_jibung_status = self.get_option('main_quest_lv22_jibung_status')
			if main_quest_lv22_jibung_status == None:
				main_quest_lv22_jibung_status = 0

			if main_quest_lv22_jibung_status == 0:
				self.lyb_mouse_click('main_scene_youngji', custom_threshold=0)
			elif main_quest_lv22_jibung_status >= 1 and main_quest_lv22_jibung_status < 9:
				time.sleep(20)
				move_direction = int(main_quest_lv22_jibung_status - 1)
				self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(move_direction), stop_delay=1)
				time.sleep(2)
				self.lyb_mouse_click('skill_0', custom_threshold=0)
				time.sleep(1)
				self.lyb_mouse_click('skill_0', custom_threshold=0)
			else:
				main_quest_lv22_jibung_status = 0

			self.set_option('main_quest_lv22_jibung_status', main_quest_lv22_jibung_status + 1)

			return True

		if self.is_field() and self.get_checkpoint('main_quest_clicked') != 0:

			elapsed_time = time.time() - self.get_checkpoint('main_quest_clicked')

			if elapsed_time > period_wait_attack:
				if self.is_sudong() == True:
					skill_iteration = self.get_option('skill_iteration')
					if skill_iteration == None or skill_iteration == 4:
						skill_iteration = 0
					else:
						skill_iteration += 1
					self.set_option('skill_iteration', skill_iteration)

					self.lyb_mouse_click('skill_' + str(skill_iteration), custom_threshold=0, delay=3)
					return True

		# 상호 작용 처리

		s = time.time()

		for search_count in range(2):
			if search_count == 0:
				response_custom_rect = (220, 50, 430, 130)
			else:
				response_custom_rect = (150, 130, 480, 315)

			#. 놓기
			is_clicked = self.process_main_quest_response(
				'main_quest_hand',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 돕기
			is_clicked = self.process_main_quest_response(
				'main_quest_hand2',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 자물쇠
			is_clicked = self.process_main_quest_response(
				'main_quest_lock',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 돋보기
			is_clicked = self.process_main_quest_response(
				'main_quest_dotbogi',
				threshold_main_quest=threshold_main_quest*0.8,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 돋보기
			is_clicked = self.process_main_quest_response(
				'main_quest_dotbogi2',
				threshold_main_quest=threshold_main_quest*0.8,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 곡괭이
			is_clicked = self.process_main_quest_response(
				'main_quest_gokgengi',
				threshold_main_quest=threshold_main_quest*0.8,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 하늘색 깃발
			is_clicked = self.process_main_quest_response(
				'main_quest_blue_flag',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 호미
			is_clicked = self.process_main_quest_response(
				'main_quest_homi',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 씨뿌리기
			is_clicked = self.process_main_quest_response(
				'main_quest_hand4',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 도끼
			is_clicked = self.process_main_quest_response(
				'main_quest_dokki',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 톱니
			is_clicked = self.process_main_quest_response(
				'main_quest_topni2',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 물
			is_clicked = self.process_main_quest_response(
				'main_quest_water',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 제작
			is_clicked = self.process_main_quest_response(
				'main_quest_enter',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True


			#. 부수기
			is_clicked = self.process_main_quest_response(
				'main_quest_busugi',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 입장
			is_clicked = self.process_main_quest_response(
				'main_quest_topni',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True

			#. 도끼
			is_clicked = self.process_main_quest_response(
				'main_quest_hand5',
				threshold_main_quest=threshold_main_quest,
				custom_rect=response_custom_rect)
			if is_clicked == True:
				return True
		e = time.time()
		self.logger.warn('탐색에 걸린 시간 1: ' + str(round(e - s, 5)))

		return False

	# def terms_of_use_scene(self):
	# 	#print(self.game_object.rateMatchedPixelBox(self.window_pixels, 'terms_of_use_bottom_0'))
	# 	self.lyb_mouse_click('terms_of_use_bottom_0')

	# 	#print(self.game_object.rateMatchedPixelBox(self.window_pixels, 'terms_of_use_bottom_1'))
	# 	self.lyb_mouse_click('terms_of_use_bottom_1')
	# 	return 0

	# def loc_plus(self):

	# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
	# 					self.window_image,
	# 					self.game_object.resource_manager.pixel_box_dic['item_plus'],
	# 					custom_below_level=(220, 200, 100),
	# 					custom_top_level=(255,255,180),
	# 					custom_threshold=0.7,
	# 					custom_flag=1,
	# 					custom_rect=(360,130,620,260)
	# 					)

	# 	print('[DEBUG] ItemPLus:', (loc_x, loc_y), match_rate)
	# 	if loc_x != -1:
	# 		return loc_x, loc_y

	# 	return -1, -1

	# def loc_gate(self):

	# 	custom_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE)) * 0.01

	# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
	# 					self.window_image,
	# 					self.game_object.resource_manager.pixel_box_dic['item_gate'],
	# 					custom_threshold=custom_threshold,
	# 					custom_flag=1,
	# 					custom_rect=(200,180,240,320)
	# 					)

	# 	print('[DEBUG] ItemGate:', (loc_x, loc_y), match_rate)
	# 	if loc_x != -1:
	# 		return loc_x, loc_y

	# 	return -1, -1

	# def loc_jadong(self):

	# 	custom_threshold = int(self.get_game_config(lybconstant.LYB_DO_STRING_YH_THRESHOLD_STANCE)) * 0.01
	# 	(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
	# 					self.window_image,
	# 					self.game_object.resource_manager.pixel_box_dic['combat_stance_jadong'],
	# 					custom_threshold=custom_threshold,
	# 					custom_below_level=(80, 80, 80),
	# 					custom_top_level=(255, 255, 190),
	# 					custom_flag=1,
	# 					custom_rect=(5,80,40,110)
	# 					)

	# 	print('[DEBUG] Jadong Stance:', (loc_x, loc_y), match_rate)
	# 	if loc_x != -1:
	# 		return loc_x, loc_y

	# 	return -1, -1


	def process_main_quest_response(self,
		pixel_box_name,
		threshold_main_quest=0.5,
		custom_rect=-1):

		if time.time() - self.get_checkpoint(pixel_box_name + '_clicked') < 30:
			return False

		rc = False
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pixel_box_name],
				custom_threshold=threshold_main_quest,
				custom_flag=1,
				custom_rect=custom_rect
				)
		# if 'main_quest_lock' in pixel_box_name:
		# 	self.logger.warn(pixel_box_name + ':' + str((loc_x, loc_y)) + ' ::: ' + str(match_rate))
			# self.game_object.getImagePixelBox(pixel_box_name).save(pixel_box_name + '.png')

		if loc_x != -1:

			view_count = self.get_option(pixel_box_name + '_view_count')
			if view_count == None:
				view_count = 0

			view_loc = self.get_option(pixel_box_name + '_view_loc')
			if view_loc == None:
				view_loc = (-1, -1)

			if (loc_x, loc_y) == view_loc:
				view_count += 1
			else:
				view_loc = (loc_x, loc_y)
				view_count = 0

			if view_count >= 0:
				self.logger.info('+ ' + str(pixel_box_name) + ' - ' + str((loc_x, loc_y)) + ':' + str(match_rate))
				self.set_checkpoint(pixel_box_name + '_clicked')
				self.lyb_mouse_click_location(loc_x, loc_y)
				view_count = 0
				view_loc = (-1, -1)
				rc = True

			self.set_option(pixel_box_name + '_view_count', view_count)
			self.set_option(pixel_box_name + '_view_loc', view_loc)

		return rc
			

	def process_main_quest_sub(self, 
		pixel_box_name, 
		custom_below_level=-1, 
		custom_top_level=-1,
		custom_l_rect=-1, 
		custom_r_rect=-1, 
		threshold_main_quest=0.5, 
		period_main_quest=30,
		wait_attack=False,
		no_delay=False,
		pass_first=False,
		pair_click=False):
		if custom_l_rect != -1:
			
			#. 좌측
			elapsed_time = time.time() - self.get_checkpoint(pixel_box_name)
			if no_delay == True or elapsed_time > period_main_quest:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pixel_box_name],
								custom_below_level=custom_below_level,
								custom_top_level=custom_top_level,
								custom_threshold=threshold_main_quest,
								custom_flag=1,
								custom_rect=custom_l_rect
								)
				# if 'gabang_warning' in pixel_box_name:
				# 	self.logger.warn('< ' + str(pixel_box_name) + ' - ' + str((loc_x, loc_y)) + ':' + str(match_rate))

				if loc_x != -1:
					self.logger.info('< ' + str(pixel_box_name) + ' - ' + str((loc_x, loc_y)) + ':' + str(match_rate))
					
					if no_delay == False:
						self.set_checkpoint(pixel_box_name)

					if pass_first == True:
						if self.get_option(pixel_box_name + 'pass_first') != True:
							self.set_option(pixel_box_name + 'pass_first', True)
							return False
						else:
							self.set_option(pixel_box_name + 'pass_first', False)

					if wait_attack == True:
						self.set_checkpoint('main_quest_clicked')
					else:
						self.set_checkpoint('main_quest_clicked', custom_time_key=0)

					self.lyb_mouse_click_location(loc_x + 30, loc_y)
					return True


		if custom_r_rect == -1:
			return False

		#. 우측 
		elapsed_time = time.time() - self.get_checkpoint(pixel_box_name + '_right')
		if no_delay == True or elapsed_time > period_main_quest:
			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pixel_box_name],
							custom_below_level=custom_below_level,
							custom_top_level=custom_top_level,
							custom_threshold=threshold_main_quest,
							custom_flag=1,
							custom_rect=custom_r_rect
							)

			# if 'complete' in pixel_box_name:
			# 	self.logger.warn('> ' + str(pixel_box_name) + ' - ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			# 	self.game_object.getImagePixelBox(pixel_box_name).save(pixel_box_name + '.png')

			if loc_x != -1:
				self.logger.info('> ' + str(pixel_box_name) + ' - ' + str((loc_x, loc_y)) + ':' + str(match_rate))

				if no_delay == False:
					self.set_checkpoint(pixel_box_name + '_right')

				if pass_first == True:
						if self.get_option(pixel_box_name + '_right_pass_first') != True:
							self.set_option(pixel_box_name + '_right_pass_first', True)
							return False
						else:
							self.set_option(pixel_box_name + '_right_pass_first', False)

				if custom_l_rect != -1:
					self.set_checkpoint(pixel_box_name, custom_time_key=0)

				if wait_attack == True:
					self.set_checkpoint('main_quest_clicked')
				else:
					self.set_checkpoint('main_quest_clicked', custom_time_key=0)
				self.lyb_mouse_click_location(loc_x, loc_y)
				if pair_click == True:
					time.sleep(1)
					self.lyb_mouse_click_location(loc_x - 20, loc_y)
				return True

		return False



	def is_field(self):

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic['mubeopja_mode'],
				custom_below_level=(222, 222, 222),
				custom_top_level=(255, 255, 255),
				custom_flag=1,
				custom_rect=(150, 30, 250, 130)
				)
		# self.logger.warn('필드: ' + str(match_rate))
		if loc_x != -1:
			return True

		return False

	def is_dungeon(self):

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic['out'],
				custom_below_level=(222, 222, 222),
				custom_top_level=(255, 255, 255),
				custom_flag=1,
				custom_rect=(460, 30, 500, 70)
				)
		if loc_x != -1:
			# self.logger.debug('던전')
			return True

		return False



	def bar_percent(self, hp_s, hp_m, hp_e, ignore_rgb=-1, adjust=(15, 15, 15), adjust_s=(0,0), adjust_e=(0,0), reverse=False):

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

			# self.logger.debug(str((e_loc_x -j, e_loc_y)) + ':' + str(hp_rgb) + ':' + str((r, g, b)))

			if abs(hp_rgb[0] - r) < adjust[0] and abs(hp_rgb[1] - g) < adjust[1] and abs(hp_rgb[2] - b) < adjust[2]:
				# self.logger.debug(int(((total_length - j) / total_length) * 100))
				if reverse == False:
					hp_percent = int(((total_length - j) / total_length) * 100)
					break
			else:
				if reverse == True:
					hp_percent = int(((total_length - j) / total_length) * 100)
					break

			if ignore_rgb != -1:
				if abs(ignore_rgb[0] - r) < adjust[0] and abs(ignore_rgb[1] - g) < adjust[1] and abs(ignore_rgb[2] - b) < adjust[2]:
					break

			j += 1
			if j > total_length:
				break


		return hp_percent

	def is_matched_color(self, pixel_box_name, rgb):
		(s_loc_x, s_loc_y) = self.get_location(pixel_box_name)
		(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, s_loc_x, s_loc_y)
		self.logger.info((r, g, b))
		if abs(r - rgb[0]) < 50 and abs(g - rgb[1]) < 50 and abs(b - rgb[2]) < 50:
			return True

		return False



	def get_work_status(self, work_name):
		if work_name in lybgamebd.LYBBlackDesert.work_list:
			return (lybgamebd.LYBBlackDesert.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999

	def check_migung_invite(self):
		(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
										self.window_image,
										'migung_invite_loc',
										custom_threshold=0.8,
										custom_flag=1,
										custom_rect=(240, 150, 400, 230))
		if loc_x != -1:
			self.logger.warn('미궁 초대 인식됨: ' + str((loc_x, loc_y)) + ':' + str(match_rate))
			if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean') == True:
				migung_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'))
				migung_level2 = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2'))
				migung_level_op = self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op')
				migung_level_op_index = lybgamebd.LYBBlackDesert.migung_rank_op_list.index(migung_level_op)

				is_there = False

				if migung_level_op_index == 1:
					for i in range(migung_level - 1):
						resource_name = 'migung_invite_level_' + str(i) + '_loc'
						(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
														self.window_image,
														resource_name,
														custom_threshold=0.9,
														custom_flag=1,
														custom_rect=(320, 170, 360, 210))
						self.logger.warn(str(i + 1) + ' 단계 <= '+ str(migung_level) + ' 단계 이상:' + str(match_rate))
						if loc_x != -1:
							is_there = True
							break

					if is_there == False:
						is_there = True
						for i in range(migung_level2):
							resource_name = 'migung_invite_level_' + str(i) + '_loc'
							(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
															self.window_image,
															resource_name,
															custom_threshold=0.9,
															custom_flag=1,
															custom_rect=(320, 170, 360, 210))
							self.logger.warn(str(i + 1) + ' <= 단계'+ str(migung_level2) + ' 단계 이하:' + str(match_rate))
							if loc_x != -1:
								is_there = False
								break
				else:
					resource_name = 'migung_invite_level_' + str(migung_level - 1) + '_loc'
					(loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
													self.window_image,
													resource_name,
													custom_threshold=0.9,
													custom_flag=1,
													custom_rect=(320, 170, 360, 210))

					self.logger.warn(str(migung_level) + ' 단계 Only: ' + str(match_rate))
					if loc_x == -1:
						is_there = True

				self.logger.debug(is_there)

				if is_there != True:
					# 확인			
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['migung_invite_ok'],
						custom_flag=1,
						custom_rect=(320, 220, 400, 300)
						)
					if loc_x != -1:
						self.game_object.addStatistic('미궁 초대 수락 횟수')
						self.logger.warn('미궁 초대 수락')
						self.lyb_mouse_click_location(loc_x, loc_y)
				else:
					# 취소
					(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic['migung_invite_cancel'],
						custom_flag=1,
						custom_rect=(250, 220, 310, 300)
						)
					if loc_x != -1:
						self.logger.warn('미궁 초대 거절')
						self.lyb_mouse_click_location(loc_x, loc_y)
					return True
			else:
				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
					self.window_image,
					self.game_object.resource_manager.pixel_box_dic['migung_invite_cancel'],
					custom_flag=1,
					custom_rect=(250, 220, 310, 300)
					)
				if loc_x != -1:
					self.logger.warn('미궁 초대 거절(사유:설정)')
					self.lyb_mouse_click_location(loc_x, loc_y)
					return True

		return False

	def main_scene_close_map(self):
		pb_name = 'main_scene_map_open'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
		# self.logger.warn('MapOpener: ' + str(match_rate))
		if match_rate > 0.8:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True
		return False

	def main_scene_open_map(self):
		pb_name = 'main_scene_map_open'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
		# self.logger.warn('MapOpener: ' + str(match_rate))
		if match_rate < 0.8:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True
		return False

	def main_scene_unfold_map(self):
		pb_name = 'main_scene_map_fold'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		# self.logger.warn('Map Unfold: ' + str(match_rate))
		if match_rate > 0.8:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True
		return False

	def main_scene_fold_map(self):
		pb_name = 'main_scene_map_unfold'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		# self.logger.warn('Map fold: ' + str(match_rate))
		if match_rate > 0.8:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True
		return False

	def main_scene_out(self):
		main_scene_migung_check_count = self.get_option('main_scene_migung_check_count')
		if main_scene_migung_check_count == None:
			main_scene_migung_check_count = 0

		if main_scene_migung_check_count > 1:
			is_clicked = self.lyb_mouse_click('main_scene_out')
			main_scene_migung_check_count = self.set_option('main_scene_migung_check_count', 0)
			return is_clicked
		else:
			match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'main_scene_migung_loc', custom_below_level=200,custom_top_level=255)
			# self.logger.warn('미궁: ' + str(match_rate))
			if match_rate < 0.7:
				main_scene_migung_check_count = self.set_option('main_scene_migung_check_count', main_scene_migung_check_count + 1)
			else:
				main_scene_migung_check_count = self.set_option('main_scene_migung_check_count', 0)

		return False

	def main_scene_check_sudong(self, custom_count=-1):

		period_wait_jadong = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong'))
		if custom_count == -1:
			sudong_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit'))
		else:
			sudong_limit = custom_count
		if (	self.current_work == '자동 사냥' or
				self.current_work == '이야기' or
				self.current_work == '미궁 목록' or
				self.current_work == '미궁 개척' or
				self.current_work == '월드 보스' or
				self.current_work == '낚시' or
				self.current_work == '토벌 게시판' or
				self.current_work == '메인 퀘스트'):
			elapsed_time = time.time() - self.get_checkpoint('last_clicked_main_quest')
			# 메인퀘스트가 아니면 항상 참일 것이다.
			if elapsed_time > period_wait_jadong:
				if self.is_sudong() == True:
					sudong_check_count = self.get_option('sudong_check_count')
					if sudong_check_count == None:
						sudong_check_count = 0

					if sudong_check_count > 1:
						self.logger.info('수동태세감지: ' + str(sudong_check_count) + '/' + str(sudong_limit))

					if sudong_check_count >= sudong_limit:
						self.set_option('sudong_check_count', 0)
						self.lyb_mouse_click('sudong', custom_threshold=0)
						return True
					else:
						self.set_option('sudong_check_count', sudong_check_count + 1)
				else:
					self.set_option('sudong_check_count', 0)

	def is_migung(self):
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, 
														'main_scene_migung_loc', 
														custom_below_level=200,
														custom_top_level=255)
		if match_rate > 0.7:
			return True

		return False


	def do_complete_sequence(self):

		if self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence') == True:

			loc_x = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'))
			loc_y = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'))

			random_factor = float(self.get_game_config(lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'))

			random_second = random.random() * random_factor
			self.logger.info('퀘스트 완료 클릭 시퀀스 1 - 무작위 지연 시간: ' + str(round(random_second,2)) + '초, 좌표: ' + str((loc_x, loc_y)))
			time.sleep(random_second)
			self.lyb_mouse_click_location(loc_x, loc_y)

			random_second = random.random() * random_factor + 1.0
			self.logger.info('퀘스트 완료 클릭 시퀀스 2 - 무작위 지연 시간: ' + str(round(random_second,2)) + '초, 좌표: ' + str((loc_x, loc_y)))
			time.sleep(random_second)
			self.lyb_mouse_click_location(loc_x, loc_y)

	def click_to_maul(self):

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic['to_home'],
				custom_threshold=0.85,
				custom_below_level=(222, 222, 222),
				custom_top_level=(255, 255, 255),
				custom_flag=1,
				custom_rect=(150, 30, 250, 130)
				)
		self.logger.warn('마을로 이동: ' + str(match_rate))
		if loc_x != -1:
			self.lyb_mouse_click_location(loc_x, loc_y)
			return True

		return False

	def click_event_bosang(self):

		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic['event_bosang'],
				custom_threshold=0.7,
				custom_below_level=(222, 222, 222),
				custom_top_level=(255, 255, 255),
				custom_flag=1,
				custom_rect=(150, 30, 250, 130)
				)
		self.logger.warn('이벤트 보상: ' + str(match_rate))
		if loc_x != -1:
			self.lyb_mouse_click_location(loc_x, loc_y)
			return True

		return False

	def find_world_boss(self):

		pb_name = 'main_scene_world_boss'
		(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
				self.window_image,
				self.game_object.resource_manager.pixel_box_dic[pb_name],
				custom_threshold=0.7,
				custom_below_level=(222, 222, 222),
				custom_top_level=(255, 255, 255),
				custom_flag=1,
				custom_rect=(150, 30, 250, 130)
				)
		self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			return (loc_x, loc_y), match_rate, pb_name

		return (-1, -1), 0, ''

	def main_scene_goto_shop(self, shop_name):
		is_clicked = self.main_scene_open_map()
		if is_clicked == True:
			self.set_option(self.current_work + '_status', 0)
			return self.status

		is_clicked = self.main_scene_fold_map()
		if is_clicked == True:
			self.set_option(self.current_work + '_status', 0)
			return self.status

		elapsedTime = self.get_elapsed_time()
		limit_time = 60
		if elapsedTime > limit_time:
			self.set_option(self.current_work + '_end_flag', True)								
			self.set_option('exclude', False)
		else:
			inner_status = self.get_option(self.current_work + '_status')
			if inner_status == None:
				inner_status = 0

			if inner_status == 0:								
				self.set_option('exclude', True)
				self.lyb_mouse_click('main_scene_map_list', custom_threshold=0)
				self.set_option(self.current_work + '_status', inner_status + 1)
			elif inner_status >= 1 and inner_status < 3:
				self.lyb_mouse_drag('main_scene_map_drag_top', 'main_scene_map_drag_bottom')
				self.set_option(self.current_work + '_status', inner_status + 1)
			elif inner_status == 3:
				pb_name = 'main_scene_map_npc_' + str(lybgamebd.LYBBlackDesert.npc_list.index(shop_name))

				(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
						self.window_image,
						self.game_object.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.7,
						custom_below_level=(222, 222, 222),
						custom_top_level=(255, 255, 255),
						custom_flag=1,
						custom_rect=(5, 50, 35, 130)
						)
				self.logger.warn(shop_name + ' : ' + str((loc_x, loc_y)) + ':' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.set_option(self.current_work + '_status', inner_status + 1)
				else:
					self.lyb_mouse_drag('main_scene_map_drag_bottom', 'main_scene_map_drag_top')
			elif inner_status >= 4 and inner_status < 20:
				self.logger.warn(str(shop_name) + ' 찾아가는 중...  ' + str(inner_status) + '/20')
				self.set_option(self.current_work + '_status', inner_status + 1)
			elif inner_status == 20:
				threshold_main_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest')) * 0.01
				pb_name = 'main_scene_npc_icon_' + str(lybgamebd.LYBBlackDesert.npc_list.index(shop_name))

				is_clicked = self.process_main_quest_sub(
					pb_name,
					threshold_main_quest=threshold_main_quest * 1.1,
					custom_r_rect=(480, 220, 630, 370))
				if is_clicked == True:
					if shop_name == '가축상점':
						self.game_object.get_scene('gachuk_shop_scene').status = self.status
					elif shop_name == '교본상점':
						self.game_object.get_scene('gyobon_shop_scene').status = 0

					self.set_option(self.current_work + '_end_flag', True)
					self.set_option('exclude', True)	


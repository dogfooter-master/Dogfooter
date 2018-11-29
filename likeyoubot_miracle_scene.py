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
import likeyoubot_miracle as lybgamemiracle
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time

class LYBMiracleScene(likeyoubot_scene.LYBScene):
	def __init__(self, scene_name):
		likeyoubot_scene.LYBScene.__init__(self, scene_name)

	def process(self, window_image, window_pixels):

		super(LYBMiracleScene, self).process(window_image, window_pixels)

		rc = 0
		if self.scene_name == 'init_screen_scene':
			rc = self.init_screen_scene()
		elif self.scene_name == 'login_scene':
			rc = self.login_scene()
		elif self.scene_name == 'main_scene':
			rc = self.main_scene()			
		elif self.scene_name == 'dungeon_scene':
			rc = self.dungeon_scene()	
		elif self.scene_name == 'yoil_dungeon_scene':
			rc = self.yoil_dungeon_scene()	
		elif self.scene_name == 'immu_scene':
			rc = self.immu_scene()	
		elif self.scene_name == 'mail_scene':
			rc = self.mail_scene()	
		elif self.scene_name == 'muhantap_scene':
			rc = self.muhantap_scene()	
		elif self.scene_name == 'ready_scene':
			rc = self.ready_scene()
		elif self.scene_name == 'victory_scene':
			rc = self.victory_scene()
		elif self.scene_name == 'dejeon_scene':
			rc = self.dejeon_scene()
		elif self.scene_name == 'combat_scene':
			rc = self.combat_scene()
		elif self.scene_name == 'arena_scene':
			rc = self.arena_scene()	
		elif self.scene_name == 'arena_combat_scene':
			rc = self.arena_combat_scene()	
		elif self.scene_name == 'arena_defeat_scene':
			rc = self.arena_defeat_scene()			
		elif self.scene_name == 'moheom_scene':
			rc = self.moheom_scene()			
		elif self.scene_name == 'arena_limit_scene':
			rc = self.arena_limit_scene()	
		elif self.scene_name == 'jeryeon_scene':
			rc = self.jeryeon_scene()	
		elif self.scene_name == 'jeryeon_item_select_scene':
			rc = self.jeryeon_item_select_scene()	
		elif self.scene_name == 'ganghwa_fail_scene':
			rc = self.ganghwa_fail_scene()	
		elif self.scene_name == 'ganghwa_success_scene':
			rc = self.ganghwa_success_scene()	
		elif self.scene_name == 'ganghwa_scene':
			rc = self.ganghwa_scene()
		elif self.scene_name == 'menu_scene':
			rc = self.menu_scene()	
		elif self.scene_name == 'boonhe_item_select_scene':
			rc = self.boonhe_item_select_scene()	
		elif self.scene_name == 'gabang_scene':
			rc = self.gabang_scene()
		elif self.scene_name == 'chingu_scene':
			rc = self.chingu_scene()
		elif self.scene_name == 'petroom_scene':
			rc = self.petroom_scene()
		elif self.scene_name == 'goldroom_scene':
			rc = self.goldroom_scene()
		elif self.scene_name == 'sangjeom_scene':
			rc = self.sangjeom_scene()
		elif self.scene_name == 'jeryeon_use_gem_scene':
			rc = self.jeryeon_use_gem_scene()
		elif self.scene_name == 'google_play_store_scene':
			rc = self.google_play_store_scene()



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

	def jeryeon_use_gem_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:

			use_gem = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem')
			if use_gem == False:
				self.lyb_mouse_click('jeryeon_use_gem_scene_cancel')
			else:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status


	def sangjeom_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.set_option('find_limit', 0)
			self.status += 1
		elif self.status == 1:			
			pb_name = 'sangjeom_scene_sohwan'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(580, 60, 630, 380)
							)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.set_option('find_limit', 0)
				self.status += 1
			else:
				find_limit = self.get_option('find_limit')
				if find_limit == None:
					find_limit = 0

				if find_limit > 4:
					self.status = 99999
				else:
					self.set_option('last_status', 1)
					if find_limit < 2:
						self.status = 10
					else:
						self.status = 20
					self.set_option('find_limit', find_limit + 1)
		elif self.status == 2:
			self.status += 1
		elif self.status == 3:		
			pb_name = 'sangjeom_scene_free'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.8,
							custom_flag=1,
							custom_rect=(170, 330, 550, 360)
							)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.status += 1
			else:
				find_limit = self.get_option('find_limit')
				if find_limit == None:
					find_limit = 0

				if find_limit > 4:
					self.status = 99999
				else:
					self.set_option('last_status', 3)
					if find_limit < 2:
						self.status = 30
					else:
						self.status = 40
					self.set_option('find_limit', find_limit + 1)
		elif self.status == 4:
			self.status += 1
		elif self.status == 5:
			self.status = 3
		elif self.status == 10:
			self.lyb_mouse_drag('sangjeom_scene_drag_top', 'sangjeom_scene_drag_bottom')
			self.status += 1
		elif self.status == 11:
			self.status = self.get_option('last_status')
		elif self.status == 20:
			self.lyb_mouse_drag('sangjeom_scene_drag_bottom', 'sangjeom_scene_drag_top')
			self.status += 1
		elif self.status == 21:
			self.status = self.get_option('last_status')
		elif self.status == 30:
			self.lyb_mouse_drag('sangjeom_scene_drag_right', 'sangjeom_scene_drag_left')
			self.status += 1
		elif self.status == 31:
			self.status = self.get_option('last_status')
		elif self.status == 40:
			self.lyb_mouse_drag('sangjeom_scene_drag_left', 'sangjeom_scene_drag_right')
			self.status += 1
		elif self.status == 41:
			self.status = self.get_option('last_status')
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def chingu_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('chingu_scene_modu')
			self.status += 1
		elif self.status >= 2 and self.status < 5:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def boonhe_item_select_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:			
			for each_item in lybgamemiracle.LYBMiracle.item_group_list:
				i = lybgamemiracle.LYBMiracle.item_group_list.index(each_item)
				cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + str(i))

				# self.logger.warn(each_item + ' ' + str(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + str(i))))

				pb_name = 'bunhe_item_select_scene_item_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if cfg_select == True and match_rate > 0.9:
					self.lyb_mouse_click(pb_name)
				elif cfg_select == False and match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)

				# self.logger.warn(pb_name + ' ' + str(match_rate))

			for each in lybgamemiracle.LYBMiracle.rank_list:
				i = lybgamemiracle.LYBMiracle.rank_list.index(each)
				cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + str(i))

				# self.logger.warn(each + ' ' + str(cfg_select))
				
				pb_name = 'bunhe_item_select_scene_rank_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if cfg_select == True and match_rate > 0.9:
					self.lyb_mouse_click(pb_name)
				elif cfg_select == False and match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)

				# self.logger.warn(pb_name + ' ' + str(match_rate))


			for each in lybgamemiracle.LYBMiracle.etc_list:
				i = lybgamemiracle.LYBMiracle.etc_list.index(each)
				cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + str(i))

				# self.logger.warn(each + ' ' + str(cfg_select))
				
				pb_name = 'bunhe_item_select_scene_etc_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if cfg_select == True and match_rate > 0.9:
					self.lyb_mouse_click(pb_name)
				elif cfg_select == False and match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
				# self.logger.warn(pb_name + ' ' + str(match_rate))
			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('boonhe_item_select_scene_select')
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')				
			self.status = 0

		return self.status


	def gabang_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:	
			self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count'))	
			if self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count') == '분해':	
				pb_name = 'gabang_scene_boonhe'
			else:
				pb_name = 'gabang_scene_sell'

			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				self.status += 1
			else:
				self.lyb_mouse_click(pb_name)
		elif self.status == 2:
			self.lyb_mouse_click('gabang_scene_select_boonhe', custom_threshold=0)
			self.game_object.get_scene('boonhe_item_select_scene').status = 0
			self.status += 1
		elif self.status == 3:
			self.status += 1
		elif self.status == 4:
		# 	pb_name = 'gabang_scene_sort_close'
		# 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		# 	self.logger.warn(pb_name + ' ' + str(match_rate))
		# 	if match_rate > 0.9:
		# 		self.lyb_mouse_click('gabang_scene_sort', custom_threshold=0)
		# 	self.status += 1
		# elif self.status == 3:
		# 	self.status += 1
		# elif self.status == 4:			
		# 	pb_name = 'gabang_scene_sort_rank_desc'
		# 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		# 	self.logger.warn(pb_name + ' ' + str(match_rate))
		# 	if match_rate < 0.9:
		# 		self.lyb_mouse_click(pb_name, custom_threshold=0)
		# 	self.status += 1
		# elif self.status == 5:
		# 	self.lyb_mouse_click('gabang_scene_sort', custom_threshold=0)
		# 	self.status += 1
		# elif self.status == 6:
		# 	is_there = False
		# 	rank_limit = lybgamemiracle.LYBMiracle.rank_list.index(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank')) + 1
		# 	for i in range(rank_limit):
		# 		self.logger.debug(str(i) + '                      ')
		# 		pb_name = 'gabang_scene_item_rank_' + str(i)
		# 		rgb = self.get_center_pixel_info(pb_name)
		# 		(a_loc_x, a_loc_y) = self.get_location(pb_name)
		# 		(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, a_loc_x, a_loc_y)
		# 		self.logger.debug(pb_name + ' ' + str((a_loc_x, a_loc_y)) + ' ' + str(rgb) + ' ' + str((r, g, b)))
				

		# 		pb_name_h = 'gabang_scene_item_rank_h'
		# 		(h_loc_x, h_loc_y) = self.get_location(pb_name_h)

		# 		pb_name_v = 'gabang_scene_item_rank_v'
		# 		(v_loc_x, v_loc_y) = self.get_location(pb_name_v)

		# 		cell_w = h_loc_x - a_loc_x
		# 		cell_h = v_loc_y - a_loc_y
		# 		self.logger.debug(str(cell_w) + ', ' + str(cell_h) + ' ' + str(rgb[1]) + ' ' + str(self.normalize_rgb(rgb[1])) + ' ' + str(self.contrast_rgb(rgb[1])))

		# 		for y in range(5):
		# 			for x in range(7):
		# 				e_loc_x = a_loc_x + (x * cell_w)
		# 				e_loc_y = a_loc_y + (y * cell_h)

		# 				(r, g, b) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x, e_loc_y)
		# 				self.logger.debug('(' + str(x) + ', ' + str(y) + '):' + ' ' + 
		# 					str((e_loc_x, e_loc_y)) + ' ' + 
		# 					str((r, g, b)) + ' ' +
		# 					str(self.is_same_rgb(rgb[1], (r, g, b))) + ' ' +
		# 					str(self.normalize_rgb((r, g, b))) + ' ' +
		# 					str(self.contrast_rgb((r, g, b)))
		# 					)
		# 				if self.is_same_rgb(rgb[1], (r, g, b)) == True:
		# 					self.lyb_mouse_click_location2(e_loc_x, e_loc_y)
		# 					is_there = True
		# 				# self.logger.warn('(' + str(x) + ', ' + str(y) + '):' + ' ' + str((e_loc_x, e_loc_y)) + ' ' + str((r, g, b)) + ' ' + str(self.normalize_rgb((r, g, b))))
		# 	if is_there == True:
		# 		self.status += 1
		# 	else:
		# 		self.status = 99999
			self.status += 1
		elif self.status == 5:
			self.status += 1
		elif self.status == 6:
			pb_name = 'gabang_scene_bunhe_0'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.status = 99999
			else:
				self.lyb_mouse_click('gabang_scene_boonhe', custom_threshold=0)
				self.status = 2
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def menu_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('분해'):
			self.lyb_mouse_click('menu_scene_gabang', custom_threshold=0)
			self.game_object.get_scene('gabang_scene').status = 0
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def ganghwa_fail_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.game_object.get_scene('ganghwa_scene').set_option('done', True)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def ganghwa_success_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.game_object.get_scene('ganghwa_scene').set_option('done', True)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def ganghwa_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('ganghwa_scene_ganghwa')
			self.set_option('done', False)
			self.status += 1
		elif self.status >= 2 and self.status < 20:
			if self.get_option('done') == True:
				self.status = 0
			else:
				self.status += 1
		elif self.status == 20:
			self.status = 0
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def combat_scene(self):

		if self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_CONFIG + 'auto') == True:
			self.auto_on()
			self.gosok_on()

		if self.status == self.get_work_status('반복 모험'):
			self.game_object.get_scene('victory_scene').status = self.status
		else:
			self.game_object.get_scene('victory_scene').status = 0


		return self.status

	def jeryeon_item_select_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			for each_item in lybgamemiracle.LYBMiracle.item_list:
				i = lybgamemiracle.LYBMiracle.item_list.index(each_item)
				cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + str(i))

				# self.logger.warn(each_item + ' ' + str(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + str(i))))

				pb_name = 'jeryeon_item_select_scene_item_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if cfg_select == True and match_rate > 0.9:
					self.lyb_mouse_click(pb_name)
				elif cfg_select == False and match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)

				# self.logger.warn(pb_name + ' ' + str(match_rate))

			for each in lybgamemiracle.LYBMiracle.rank_list:
				i = lybgamemiracle.LYBMiracle.rank_list.index(each)
				cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + str(i))

				# self.logger.warn(each + ' ' + str(cfg_select))
				
				pb_name = 'jeryeon_item_select_scene_rank_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if cfg_select == True and match_rate > 0.9:
					self.lyb_mouse_click(pb_name)
				elif cfg_select == False and match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)

				# self.logger.warn(pb_name + ' ' + str(match_rate))


			for each in lybgamemiracle.LYBMiracle.etc_list:
				i = lybgamemiracle.LYBMiracle.etc_list.index(each)
				cfg_select = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + str(i))

				# self.logger.warn(each + ' ' + str(cfg_select))
				
				pb_name = 'jeryeon_item_select_scene_etc_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				if cfg_select == True and match_rate > 0.9:
					self.lyb_mouse_click(pb_name)
				elif cfg_select == False and match_rate < 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)

				# self.logger.warn(pb_name + ' ' + str(match_rate))

			self.status += 1
		elif self.status == 2:
			self.lyb_mouse_click('jeryeon_item_select_scene_select')
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def jeryeon_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.set_option('enter_count', 0)
			self.status += 1
		elif self.status == 1:
			cfg_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level')) - 1
			self.lyb_mouse_click('jeryeon_scene_level_' + str(cfg_level), custom_threshold=0)
			self.status += 1
		elif self.status == 2:
			is_clicked = self.lyb_mouse_click('jeryeon_scene_item_select')
			if is_clicked == True:
				self.status += 1
			self.game_object.interval = self.period_bot(2)
		elif self.status == 3:
			is_clicked = self.lyb_mouse_click('jeryeon_scene_auto')
			if is_clicked == True:
				self.game_object.get_scene('jeryeon_item_select_scene').status = 0
				self.status += 1
			else:
				self.status = 99999
			self.game_object.interval = self.period_bot(2)
		elif self.status >= 4 and self.status < 6:
			self.status += 1
		elif self.status == 6:
			self.lyb_mouse_click('jeryeon_scene_item_select_close_icon')
			self.status += 1
		elif self.status == 7:
			cfg_taret_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target'))
			for i in range(cfg_taret_count):
				pb_name = 'jeryeon_scene_target_' + str(i)
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if match_rate > 0.9:
					self.status = 99999
					return self.status
			self.status += 1
		elif self.status == 8:
			enter_count = self.get_option('enter_count')
			if enter_count > 10:
				self.status = 99999
			else:
				use_gem = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem')
				pb_name = 'jeryeon_scene_enter_limit'
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if use_gem == True or match_rate < 0.95:
					self.set_option('enter_count', enter_count + 1)
					self.lyb_mouse_click('jeryeon_scene_enter', custom_threshold=0)
					self.status += 1
				else:
					self.status = 99999
		elif self.status >= 9 and self.status < 14:
			self.status += 1
		elif self.status == 14:
			self.status = 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def arena_limit_scene(self):

		self.game_object.get_scene('arena_scene').status = 99999

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def arena_defeat_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def arena_combat_scene(self):

		self.game_object.get_scene('arena_scene').status = 0

		loc_name = 'arena_result_event'
		match_rate = self.game_object.rateMatchedResource(self.window_pixels, loc_name)
		self.logger.debug(loc_name + ' ' + str(match_rate))
		if match_rate > 0.8:
			self.lyb_mouse_click(loc_name + '_button', custom_threshold=0)
			return self.status

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def moheom_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			cfg_moheom_level = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level')
			moheom_level = lybgamemiracle.LYBMiracle.moheom_level_list.index(cfg_moheom_level)

			pb_name = 'moheom_scene_level_' + str(moheom_level)
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			# match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			# self.logger.warn(pb_name + ' ' + str(match_rate))
			# if match_rate < 0.9:
			# 	self.lyb_mouse_click(pb_name, custom_threshold=0)
			# 	time.sleep(1)
			# 	self.lyb_mouse_click('moheom_scene_level_select_' + str(moheom_level), custom_threshold=0)

			self.status += 1
		elif self.status == 2:
			i = 0
			current_area_index = len(lybgamemiracle.LYBMiracle.moheom_area_list) - 1 
			for each_area in lybgamemiracle.LYBMiracle.moheom_area_list:				
				loc_name = 'moheom_scene_area_' + str(i) + '_loc'
				match_rate = self.game_object.rateMatchedResource(self.window_pixels, loc_name)
				self.logger.warn(loc_name + ' ' + str(match_rate))
				if match_rate > 0.9:
					current_area_index = i
					break
				i += 1
			self.set_option('current_area_index', current_area_index)
			self.status += 1
		elif self.status == 3:
			current_area_index = self.get_option('current_area_index')
			cfg_moheom_area = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area')
			moheom_area_index = lybgamemiracle.LYBMiracle.moheom_area_list.index(cfg_moheom_area)

			if current_area_index == moheom_area_index:
				self.status += 1
			elif current_area_index > moheom_area_index:
				self.lyb_mouse_click('moheom_scene_left', custom_threshold=0)
				self.set_option('current_area_index', current_area_index - 1)
			else:
				self.lyb_mouse_click('moheom_scene_right', custom_threshold=0)
				self.set_option('current_area_index', current_area_index + 1)

			self.game_object.interval = self.period_bot(2)
		elif self.status == 4:
			current_area_index = self.get_option('current_area_index')
			cfg_area_number = int(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number')) - 1			
			self.lyb_mouse_click('moheom_scene_location_' + str(current_area_index) + str(cfg_area_number), custom_threshold=0)
			self.game_object.get_scene('ready_scene').status = self.get_work_status('반복 모험')
			self.status += 1
		elif self.status >= 5 and self.status < 10:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def arena_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			pb_name = 'arena_scene_enter'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.status += 1
			else:
				self.status = 99999
		elif self.status >= 2 and self.status < 10:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status


	def dejeon_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('결투장'):
			self.game_object.get_scene('arena_scene').status = 0
			self.lyb_mouse_click('dejeon_scene_arena', custom_threshold=0)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def victory_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			self.status += 1
		elif self.status == 2:
			self.status += 1
		elif self.status == 3:
			pb_name = 'victory_scene_next'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)				
				self.game_object.get_scene('ready_scene').status = 0
				self.game_object.get_scene('ready_scene').set_option('try_count', 0)
			else:
				pb_name = 'victory_scene_retry'
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if match_rate > 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)	
				else:
					self.status += 1
		elif self.status >= 4 and self.status < 7:
			self.status += 1	
		elif ( self.status >= self.get_work_status('반복 모험') and 
		 		self.status < self.get_work_status('반복 모험') + 30 ):
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.game_object.get_scene('jeryeon_scene').status = 0
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def ready_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.set_option('try_count', 0)
			self.status += 1
		elif self.status == 1:
			try_count = self.get_option('try_count')
			if try_count == None:
				try_count = 0

			if try_count > 2:
				self.status = 99999
			else:
				pb_name = 'ready_scene_enter'
				match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if match_rate > 0.9:
					self.lyb_mouse_click(pb_name, custom_threshold=0)
					self.game_object.interval = self.period_bot(3)
				else:
					self.status += 1
			self.set_option('try_count', try_count + 1)
		elif self.status == self.get_work_status('반복 모험'):
			self.lyb_mouse_click('ready_scene_banbok')			
			self.game_object.get_scene('combat_scene').status = self.status
			self.status += 1
		elif self.status == self.get_work_status('반복 모험') + 1:
			self.status += 1
		elif self.status == self.get_work_status('반복 모험') + 2:
			self.status += 1
		elif self.status == self.get_work_status('반복 모험') + 3:
			self.status += 1
		elif self.status == self.get_work_status('반복 모험') + 4:
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def muhantap_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			try_count = self.game_object.get_scene('ready_scene').get_option('try_count')
			if try_count != None and try_count > 2:
				try_count = self.game_object.get_scene('ready_scene').set_option('try_count', 0)
				self.status = 99999
			else:
				pb_name = 'muhantap_scene_ready'
				(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
								self.window_image,
								self.game_object.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(570, 50, 630, 380)
								)
				self.logger.warn(pb_name + ' ' + str(match_rate))
				if loc_x != -1:
					self.lyb_mouse_click_location(loc_x, loc_y)
					self.game_object.get_scene('ready_scene').status = 0
					self.game_object.interval = self.period_bot(2)
				else:
					self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status


	def dungeon_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == self.get_work_status('요일 던전'):
			self.lyb_mouse_click('dungeon_scene_yoil', custom_threshold=0)
			self.game_object.get_scene('yoil_dungeon_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('무한의 탑'):
			self.lyb_mouse_click('dungeon_scene_muhantap', custom_threshold=0)
			self.game_object.get_scene('muhantap_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('제련의 전당'):
			self.lyb_mouse_click('dungeon_scene_jeryeon', custom_threshold=0)
			self.game_object.get_scene('jeryeon_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('황금의 방'):
			self.lyb_mouse_click('dungeon_scene_goldroom', custom_threshold=0)
			self.game_object.get_scene('goldroom_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		elif self.status == self.get_work_status('펫의 방'):
			self.lyb_mouse_drag('dungeon_scene_drag_right', 'dungeon_scene_drag_left')
			self.status += 1
		elif self.status == self.get_work_status('펫의 방') + 1:
			self.lyb_mouse_drag('dungeon_scene_drag_right', 'dungeon_scene_drag_left')
			self.status += 1
		elif self.status == self.get_work_status('펫의 방') + 2:
			self.status += 1
		elif self.status == self.get_work_status('펫의 방') + 3:
			self.lyb_mouse_click('dungeon_scene_petroom', custom_threshold=0)
			self.game_object.get_scene('petroom_scene').status = 0
			self.game_object.interval = self.period_bot(2)
			self.status += 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status


	def mail_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status >= 1 and self.status < 5:
			self.lyb_mouse_click('mail_scene_tab_' + str(self.status - 1), custom_threshold=0)
			self.game_object.interval = self.period_bot(2)
			self.status += 10
		elif self.status >= 11 and self.status < 15:	
			self.lyb_mouse_click('mail_scene_receive_all', custom_threshold=0)
			self.game_object.interval = self.period_bot(2)
			self.status += 1
			self.status -= 10
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def immu_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			# self.lyb_mouse_click('immu_scene_tab_' + str(self.status - 1), custom_threshold=0)

			pb_name = 'immu_scene_new'
			(loc_x, loc_y),  match_rate = self.game_object.locationOnWindowPart(
							self.window_image,
							self.game_object.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(170, 50, 630, 90)
							)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if loc_x != -1:
				self.lyb_mouse_click_location(loc_x, loc_y)
				self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.status = 99999
		elif self.status == 2:	
			pb_name = 'immu_scene_bosang'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.game_object.interval = self.period_bot(2)
			else:
				self.status -= 1
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def goldroom_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			cfg_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level')) - 1
			self.lyb_mouse_click('goldroom_scene_level_' + str(cfg_level), custom_threshold=0)
			self.status += 1
		elif self.status == 2:			
			pb_name = 'goldroom_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_checkpoint('clicked')
				self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.status = 99999
		elif self.status == 3:
			self.status += 1
		elif self.status == 4:
			self.status += 1
		elif self.status == 5:
			self.status += 1
		elif self.status == 6:
			elapsed_time = time.time() - self.get_checkpoint('clicked')
			if elapsed_time < self.period_bot(10):
				self.status = 99999
			else:
				self.status = 2
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def petroom_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.status += 1
		elif self.status == 1:
			cfg_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level')) - 1
			self.lyb_mouse_click('petroom_scene_level_' + str(cfg_level), custom_threshold=0)
			self.status += 1
		elif self.status == 2:			
			pb_name = 'petroom_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_checkpoint('clicked')
				self.game_object.interval = self.period_bot(2)
				self.status += 1
			else:
				self.status = 99999
		elif self.status == 3:
			self.status += 1
		elif self.status == 4:
			self.status += 1
		elif self.status == 5:
			self.status += 1
		elif self.status == 6:
			elapsed_time = time.time() - self.get_checkpoint('clicked')
			if elapsed_time < self.period_bot(10):
				self.status = 99999
			else:
				self.status = 2
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
			self.status = 0

		return self.status

	def yoil_dungeon_scene(self):

		if self.status == 0:
			self.logger.warn('scene: ' + self.scene_name)
			self.logger.warn('current day: ' + str(time.strftime("%a")))
			if time.strftime("%a") == "Sun":
				self.status = 100
			else:
				self.status += 1
		elif self.status == 1:
			self.lyb_mouse_click('yoil_dungeon_scene_level', custom_threshold=0)
			self.status += 1
		elif self.status == 2:
			cfg_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level')) - 1
			self.lyb_mouse_click('yoil_dungeon_scene_level_' + str(cfg_level), custom_threshold=0)
			self.status += 1
		elif self.status == 3:			
			pb_name = 'yoil_dungeon_scene_limit'
			match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.warn(pb_name + ' ' + str(match_rate))
			if match_rate < 0.9:
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_checkpoint('clicked')
				self.game_object.interval = self.period_bot(3)
				self.status += 1
			else:
				self.status = 99999
		elif self.status >= 4 and self.status < 10:
			elapsed_time = time.time() - self.get_checkpoint('clicked')
			if elapsed_time > 30:
				self.status = 3
			else:
				self.status += 1
		elif self.status == 10:
			self.status = 99999
		elif self.status == 100:
			self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday'))
			cfg_day = self.get_game_config(lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday')
			index = lybgamemiracle.LYBMiracle.yoil_dungeon_list.index(cfg_day)
			pb_name = 'yoil_dungeon_scene_list_' + str(index)
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			self.status = 2
		else:
			if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
				self.lyb_mouse_click(self.scene_name + '_close_icon')
				
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
			for each_icon in lybgamemiracle.LYBMiracle.nox_miracle_icon_list:
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
			for each_icon in lybgamemiracle.LYBMiracle.momo_miracle_icon_list:
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



























	# Main

	def main_scene(self):

		if self.game_object.current_schedule_work != self.current_work:
			self.game_object.current_schedule_work = self.current_work

		self.game_object.main_scene = self

		if self.pre_process_main_scene() == True:
			return self.status

		self.schedule_list = self.get_game_config('schedule_list')
		if len(self.schedule_list) == 1:
			self.logger.warn('스케쥴 작업이 없어서 종료합니다.')
			return -1

		if self.status == 0:
			self.status += 1
		elif self.status >= 1 and self.status < 1000:

			self.set_schedule_status()


		elif self.status == self.get_work_status('반복 모험'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_adventure', custom_threshold=0)
			self.game_object.get_scene('moheom_scene').status = 0

		elif self.status == self.get_work_status('결투장'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_arena', custom_threshold=0)
			self.game_object.get_scene('dejeon_scene').status = self.status

		elif (  self.status == self.get_work_status('무한의 탑') or
				self.status == self.get_work_status('제련의 전당') or
				self.status == self.get_work_status('요일 던전') or
				self.status == self.get_work_status('황금의 방') or
				self.status == self.get_work_status('펫의 방')
				):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_dungeon', custom_threshold=0)
			self.game_object.get_scene('dungeon_scene').status = self.status

		elif (  self.status == self.get_work_status('분해')
				):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
			self.game_object.get_scene('menu_scene').status = self.status

		elif self.status == self.get_work_status('무료 소환'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_shop', custom_threshold=0)
			self.game_object.get_scene('sangjeom_scene').status = 0

		elif self.status == self.get_work_status('우편함'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_mail', custom_threshold=0)
			self.game_object.get_scene('mail_scene').status = 0


		elif self.status == self.get_work_status('친구'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_chingu', custom_threshold=0)
			self.game_object.get_scene('chingu_scene').status = 0

		elif self.status == self.get_work_status('임무'):

			elapsed_time = self.get_elapsed_time()
			if elapsed_time > self.period_bot(5):
				self.set_option(self.current_work + '_end_flag', True)

			if self.get_option(self.current_work + '_end_flag') == True:
				self.set_option(self.current_work + '_end_flag', False)
				self.status = self.last_status[self.current_work] + 1
				return self.status

			self.lyb_mouse_click('main_scene_immu', custom_threshold=0)
			self.game_object.get_scene('immu_scene').status = 0

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

		pb_name = 'jeopsok_bosang_new'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate > 0.9:
			self.lyb_mouse_click(pb_name)
			return True

		return False


	def gosok_off(self):

		pb_name = 'gosok'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=80)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate > 0.95:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True

		return False

	def gosok_on(self):

		pb_name = 'gosok'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=80)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate < 0.95:
			auto_threshold = self.get_option(pb_name + 'threshold')
			if auto_threshold == None:
				auto_threshold = 0

			if auto_threshold > 3:	
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option(pb_name + 'threshold', 0)
				return True
			else:
				self.set_option(pb_name + 'threshold', auto_threshold + 1)
		else:
			self.set_option(pb_name + 'threshold', 0)

		return False

	def auto_off(self):

		pb_name = 'auto'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate > 0.95:
			self.lyb_mouse_click(pb_name, custom_threshold=0)
			return True

		return False

	def auto_on(self):

		pb_name = 'auto'
		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
		self.logger.debug(pb_name + ' ' + str(match_rate))
		if match_rate < 0.95:
			auto_threshold = self.get_option('auto_threshold')
			if auto_threshold == None:
				auto_threshold = 0

			if auto_threshold > 3:	
				self.lyb_mouse_click(pb_name, custom_threshold=0)
				self.set_option('auto_threshold', 0)
				return True
			else:
				self.set_option('auto_threshold', auto_threshold + 1)
		else:
			self.set_option('auto_threshold', 0)

		return False


	def is_same_rgb(self, src_rgb, tgt_rgb):
		src_rgb_n = self.normalize_rgb(src_rgb)
		tgt_rgb_n = self.normalize_rgb(tgt_rgb)

		for i in range(3):
			if abs(src_rgb_n[i] - tgt_rgb_n[i]) > 0.3:
				return False

		src_rgb_c = self.contrast_rgb(src_rgb)
		tgt_rgb_c = self.contrast_rgb(tgt_rgb)

		for i in range(3):
			if abs(src_rgb_c[i] - tgt_rgb_c[i]) > 50:
				return False

		return True

	def normalize_rgb(self, rgb):
		return (round(rgb[0]/255.0, 2), round(rgb[1]/255.0, 2), round(rgb[2]/255.0, 2))

	def contrast_rgb(self, rgb):
		return (rgb[0] - rgb[1], rgb[0] - rgb[2], rgb[1] - rgb[2])

	def get_work_status(self, work_name):
		if work_name in lybgamemiracle.LYBMiracle.work_list:
			return (lybgamemiracle.LYBMiracle.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999
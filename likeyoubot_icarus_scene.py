import likeyoubot_resource as lybrsc
import likeyoubot_message
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import math
import pyautogui
import operator
import random
import likeyoubot_game as lybgame
import likeyoubot_icarus as lybgameicarus
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time
import copy


class LYBIcarusScene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)

    def process(self, window_image, window_pixels):

        super(LYBIcarusScene, self).process(window_image, window_pixels)

        rc = 0
        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'login_0907_scene':
            rc = self.login_scene()
        elif self.scene_name == 'menu_scene':
            rc = self.menu_scene()
        elif self.scene_name == 'jeopsokbosang_scene':
            rc = self.jeopsokbosang_scene()
        elif self.scene_name == 'google_play_store_scene':
            rc = self.google_play_store_scene()
        elif self.scene_name == 'google_play_store_1113_scene':
            rc = self.google_play_store_scene()
        elif self.scene_name == 'connect_account_2_scene':
            rc = self.connect_account_scene()
        elif self.scene_name == 'connect_account_scene':
            rc = self.connect_account_scene()
        elif self.scene_name == 'google_play_account_select_scene':
            rc = self.google_play_account_select_scene()
        elif self.scene_name == 'quest_scene':
            rc = self.quest_scene()
        elif self.scene_name == 'death_scene':
            rc = self.death_scene()
        elif self.scene_name == 'fellow_tamheom_scene':
            rc = self.fellow_tamheom_scene()
        elif self.scene_name == 'tamheom_dungrok_scene':
            rc = self.tamheom_dungrok_scene()
        elif self.scene_name == 'gyeoljeong_bogwanham_scene':
            rc = self.gyeoljeong_bogwanham_scene()
        elif self.scene_name == 'fellow_sangse_scene':
            rc = self.monster_sangse_scene()
        elif self.scene_name == 'monster_sangse_scene':
            rc = self.monster_sangse_scene()
        elif self.scene_name == 'character_scene':
            rc = self.character_scene()
        elif self.scene_name == 'class_select_scene':
            rc = self.class_select_scene()
        elif self.scene_name == 'config_scene':
            rc = self.config_scene()
        elif self.scene_name == 'taming_scene':
            rc = self.taming_scene()
        elif self.scene_name == 'mail_scene':
            rc = self.mail_scene()
        elif self.scene_name == 'gabang_scene':
            rc = self.gabang_scene()
        elif self.scene_name == 'item_onemore_scene':
            rc = self.item_onemore_scene()
        elif self.scene_name == 'middlas_npc_map_scene':
            rc = self.middlas_npc_map_scene()
        elif self.scene_name == 'today_todo_scene':
            rc = self.today_todo_scene()
        elif self.scene_name == 'today_todo_2_scene':
            rc = self.today_todo_2_scene()
        elif self.scene_name == 'sangjeom_scene':
            rc = self.sangjeom_scene()
        elif self.scene_name == 'fellow_set_scene':
            rc = self.fellow_set_scene()








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

    def fellow_set_scene(self):
        self.game_object.current_matched_scene['name'] = ''

        resource_name = 'fellow_set_scene_sort_config_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            pb_name = self.get_option('sort_pb_name')
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            return self.status

        resource_name = 'fellow_set_scene_register_disable_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            for i in range(5):
                self.lyb_mouse_click('fellow_set_scene_register_' + str(i), custom_threshold=0)
            return self.status

        resource_name = 'fellow_set_scene_register_enable_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            self.lyb_mouse_click('fellow_set_scene_register_enable', custom_threshold=0)
            return self.status

        pb_name = 'fellow_set_scene_enable'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(150, 70, 220, 170)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
        if loc_x != -1:
            self.lyb_mouse_click_location(loc_x, loc_y)
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('sort_pb_name', 'fellow_set_scene_sort_config_1')
            self.lyb_mouse_click('fellow_set_scene_sort', custom_threshold=0)
            self.status += 1
        elif self.status >= 1 and self.status < 7:
            pb_name = 'fellow_set_scene_list_' + str(self.status)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 7:
            self.set_option('sort_pb_name', 'fellow_set_scene_sort_config_0')
            self.status += 1
        elif self.status == 8:
            cfg_set_name = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name')
            index = lybgameicarus.LYBIcarus.fellow_set_list.index(cfg_set_name)
            if index > 0:
                pb_name = 'fellow_set_scene_list_' + str(index)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 9:
            self.lyb_mouse_click('fellow_set_scene_sort', custom_threshold=0)
            self.status += 1
        elif self.status == 10:
            self.lyb_mouse_click('fellow_set_scene_monster', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def sangjeom_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('sangjeom_scene_tab_1', custom_threshold=0)
            self.status += 1
        elif self.status >= 2 and self.status < 10:
            self.status += 1

            pb_name = 'sangjeom_scene_new_0'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(100, 100, 140, 370)
            )
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x - 80, loc_y + 5)
                self.set_option('last_status', self.status)
                self.status = 10
            else:
                self.status = 99999

        elif self.status >= 10 and self.status < 20:
            self.status += 1

            pb_name = 'sangjeom_scene_free'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_top_level=(255, 255, 255),
                custom_below_level=(190, 195, 215),
                custom_rect=(130, 90, 600, 370)
            )
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            pb_name = 'sangjeom_scene_today_fruit'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(130, 90, 600, 370)
            )
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            self.status = self.get_option('last_status')
        elif self.status == 20:
            self.status = 99999
        elif self.status == 100:
            self.status += 1
        elif self.status == 101:
            self.lyb_mouse_click('sangjeom_scene_normal_potion', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def today_todo_2_scene(self):

        self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

        return self.status

    def today_todo_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 10:
            self.status += 1
            pb_name = 'today_todo_scene_modu'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_top_level=(255, 255, 255),
                custom_below_level=(200, 200, 200),
                custom_rect=(10, 330, 120, 380)
            )
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def middlas_npc_map_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('fail_search_count', 0)
            self.set_option('flag_location', (-1, -1))
            self.status += 1
        elif self.status == 1:
            fail_search_count = self.get_option('fail_search_count')
            if fail_search_count > 2:
                self.status = 3
            else:
                pb_name = 'middlas_npc_map_scene_flag'
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_top_level=(255, 100, 40),
                    custom_below_level=(110, 30, 0),
                    custom_flag=1,
                    custom_rect=(110, 60, 420, 380)
                )
                self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option('flag_location', (loc_x, loc_y))
                    self.logger.info('깃발 클릭')
                    self.status += 1
                else:
                    self.set_option('flag_location', (-1, -1))
                    self.logger.info('깃발 탐색 실패(' + str(fail_search_count + 1) + '/3) - 도착 또는 오류')
                    self.set_option('fail_search_count', fail_search_count + 1)
        elif self.status == 2:
            for i in range(4):
                pb_name = 'middlas_npc_map_scene_player_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_top_level=(255, 255, 150),
                    custom_below_level=(195, 175, 0),
                    custom_flag=1,
                    custom_rect=(110, 60, 420, 380)
                )
                # self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    (flag_loc_x, flag_loc_y) = self.get_option('flag_location')
                    # self.logger.debug((flag_loc_x, flag_loc_y))
                    if flag_loc_x != -1:
                        distance = pow(abs(flag_loc_x - loc_x), 2) + pow(abs(flag_loc_y - loc_y), 2)
                        distance = math.sqrt(distance)
                        self.logger.info('깃발과 플레이어와의 거리: ' + str(distance) + ' < 10')
                        if distance < 10:
                            self.status += 1
                            return self.status
            self.status -= 1
        elif self.status >= 3 and self.status < 5:
            self.game_object.get_scene('monster_sangse_scene').set_option('arrived', True)
            self.game_object.get_scene('gyeoljeong_bogwanham_scene').status = 99999
            self.game_object.get_scene('fellow_set_scene').status = 99999
            self.game_object.get_scene('menu_scene').status = 99995
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def item_onemore_scene(self):

        elapsed_time = time.time() - self.get_checkpoint('start')
        if elapsed_time > self.period_bot(300) and elapsed_time < self.period_bot(310):
            self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_checkpoint('start')
            self.status += 1
        elif self.status == 1:
            pb_name = 'item_onemore_scene_confirm'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(320, 240, 430, 320)
            )
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            self.lyb_mouse_click('item_onemore_scene_continue', custom_threshold=0)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gabang_scene(self):

        pb_name = 'gabang_scene_confirm'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name)
            return self.status

        pb_name = 'gabang_scene_sell_confirm'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name)
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi') == True:
                self.lyb_mouse_click('gabang_scene_jangbi', custom_threshold=0)
                self.status = 100
            else:
                if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow') == True:
                    self.lyb_mouse_click('gabang_scene_fellow', custom_threshold=0)
                    self.status = 300
                else:
                    self.status = 99999
                # self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi'))
                # self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip'))
                # self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config'))
                # self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config'))
                # self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'))
                # self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'))
                # for i in range(3):
                # 	self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(i)))
                # for i in range(7):
                # 	self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i)))

                # for i in range(4):
                # 	self.logger.warn(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(i)))
        elif self.status == 100:
            self.set_option('sell_count', 0)
            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip') == True:
                self.lyb_mouse_click('gabang_scene_jadong_jangchak', custom_threshold=0)
            cfg_limit_count = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'))
            if cfg_limit_count == 0:
                self.status = 200
            else:
                self.status += 1
        elif self.status == 101:
            sell_count = self.get_option('sell_count')

            pb_name = 'gabang_scene_sell'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            pb_name = 'gabang_scene_sell_config'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                if sell_count == 0 and self.get_game_config(
                                lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config') == True:
                    self.lyb_mouse_click(pb_name)
                    self.status += 1
                else:
                    self.status = 110
            else:
                self.status = 200
        elif self.status >= 102 and self.status < 104:
            pb_name = 'gabang_scene_sell_config_popup'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                for i in range(3):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(i))
                    pb_name = 'gabang_scene_sell_catalog_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(7):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i))
                    pb_name = 'gabang_scene_sell_rank_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(4):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(i))
                    pb_name = 'gabang_scene_sell_gakseong_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

            self.status += 1
        elif self.status >= 104 and self.status < 110:
            pb_name = 'gabang_scene_sell_apply'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status = 110
            else:
                self.status += 1
        elif self.status == 110:
            pb_name = 'gabang_scene_sell_ok'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate < 0.9:
                self.logger.info('판매할 아이템 없음')
                self.lyb_mouse_click('gabang_scene_sell_close_icon', custom_threshold=0)
                self.status = 200
            else:
                self.lyb_mouse_click(pb_name)
                sell_count = self.get_option('sell_count')
                sell_count += 1
                self.set_option('sell_count', sell_count)
                cfg_limit_count = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'))
                if sell_count >= cfg_limit_count:
                    self.status = 200
                else:
                    self.logger.info('가방 일괄 판매 (' + str(sell_count) + '/' + str(cfg_limit_count) + ')')
                    self.status = 101
        elif self.status == 200:
            self.set_option('bunhe_count', 0)
            cfg_limit_count = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'))
            if cfg_limit_count == 0:
                self.status = 300
            else:
                self.status += 1
        elif self.status == 201:
            bunhe_count = self.get_option('bunhe_count')

            pb_name = 'gabang_scene_bunhe'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            pb_name = 'gabang_scene_bunhe_config'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                if bunhe_count == 0 and self.get_game_config(
                                lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config') == True:
                    self.lyb_mouse_click(pb_name)
                    self.status += 1
                else:
                    self.status = 210
            else:
                self.status = 300
        elif self.status >= 202 and self.status < 204:
            pb_name = 'gabang_scene_sell_config_popup'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                for i in range(3):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(i))
                    pb_name = 'gabang_scene_sell_catalog_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(7):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i))
                    pb_name = 'gabang_scene_sell_rank_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(4):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(i))
                    pb_name = 'gabang_scene_sell_gakseong_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

            self.status += 1
        elif self.status >= 204 and self.status < 210:
            pb_name = 'gabang_scene_sell_apply'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status = 210
            else:
                self.status += 1
        elif self.status == 210:
            pb_name = 'gabang_scene_bunhe_empty'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.logger.info('분해할 아이템 없음')
                self.lyb_mouse_click('gabang_scene_bunhe_close_icon', custom_threshold=0)
                self.status = 300
            else:
                self.lyb_mouse_click('gabang_scene_bunhe_ok', custom_threshold=0)
                bunhe_count = self.get_option('bunhe_count')
                bunhe_count += 1
                self.set_option('bunhe_count', bunhe_count)
                cfg_limit_count = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'))
                if bunhe_count >= cfg_limit_count:
                    self.status = 300
                else:
                    self.logger.info('가방 일괄 분해 (' + str(bunhe_count) + '/' + str(cfg_limit_count) + ')')
                    self.status = 201
        elif self.status == 300:
            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow') == True:
                self.lyb_mouse_click('gabang_scene_fellow', custom_threshold=0)
                self.status += 1
            else:
                self.status = 99999
        elif self.status == 301:
            self.set_option('sell_count', 0)
            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip') == True:
                self.lyb_mouse_click('gabang_scene_jadong_jangchak', custom_threshold=0)
            cfg_limit_count = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'))
            if cfg_limit_count == 0:
                self.status = 400
            else:
                self.status += 1
        elif self.status == 302:
            sell_count = self.get_option('sell_count')

            pb_name = 'gabang_scene_sell_fellow'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            pb_name = 'gabang_scene_sell_fellow_config'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                if sell_count == 0 and self.get_game_config(
                                lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config') == True:
                    self.lyb_mouse_click(pb_name)
                    self.status += 1
                else:
                    self.status = 310
            else:
                self.status = 400
        elif self.status >= 303 and self.status < 305:
            pb_name = 'gabang_scene_sell_fellow_config_popup'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                for i in range(3):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(i))
                    pb_name = 'gabang_scene_sell_fellow_catalog_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(7):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i))
                    pb_name = 'gabang_scene_sell_fellow_rank_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(6):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i))
                    pb_name = 'gabang_scene_sell_fellow_level_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

            self.status += 1
        elif self.status >= 305 and self.status < 310:
            pb_name = 'gabang_scene_sell_fellow_apply'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status = 310
            else:
                self.status += 1
        elif self.status == 310:
            pb_name = 'gabang_scene_sell_fellow_ok'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate < 0.9:
                self.logger.info('판매할 펠로우 없음')
                self.lyb_mouse_click('gabang_scene_sell_fellow_close_icon', custom_threshold=0)
                self.status = 400
            else:
                if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config') == True:
                    pb_name2 = 'gabang_scene_fellow_yougu'
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name2],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(5, 100, 320, 360)
                    )
                    self.logger.info(pb_name2 + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        return self.status

                self.lyb_mouse_click(pb_name)
                sell_count = self.get_option('sell_count')
                sell_count += 1
                self.set_option('sell_count', sell_count)
                cfg_limit_count = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'))
                if sell_count >= cfg_limit_count:
                    self.status = 400
                else:
                    self.logger.info('펠로우 일괄 판매 (' + str(sell_count) + '/' + str(cfg_limit_count) + ')')
                    self.status = 302
        elif self.status == 400:
            self.set_option('bunhe_count', 0)
            cfg_limit_count = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'))
            if cfg_limit_count == 0:
                self.status = 99999
            else:
                self.status += 1
        elif self.status == 401:
            bunhe_count = self.get_option('bunhe_count')

            pb_name = 'gabang_scene_bunhe_fellow'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            pb_name = 'gabang_scene_bunhe_fellow_config'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                if bunhe_count == 0 and self.get_game_config(
                                lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config') == True:
                    self.lyb_mouse_click(pb_name)
                    self.status += 1
                else:
                    self.status = 410
            else:
                self.status = 99999
        elif self.status >= 402 and self.status < 405:
            pb_name = 'gabang_scene_bunhe_fellow_config_popup'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:

                for i in range(7):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i))
                    pb_name = 'gabang_scene_bunhe_fellow_rank_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

                for i in range(6):
                    is_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i))
                    pb_name = 'gabang_scene_bunhe_fellow_level_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)

                    if is_checked == True and match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif is_checked == False and match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)

            self.status += 1
        elif self.status >= 405 and self.status < 410:
            pb_name = 'gabang_scene_bunhe_fellow_apply'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status = 410
            else:
                self.status += 1
        elif self.status == 410:
            pb_name = 'gabang_scene_bunhe_fellow_ok'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate < 0.9:
                self.logger.info('추출할 펠로우 없음')
                self.lyb_mouse_click('gabang_scene_bunhe_fellow_close_icon', custom_threshold=0)
                self.status = 99999
            else:
                if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config') == True:
                    pb_name2 = 'gabang_scene_fellow_yougu'
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name2],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(20, 105, 300, 230)
                    )
                    self.logger.info(pb_name2 + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        return self.status

                self.lyb_mouse_click(pb_name)
                bunhe_count = self.get_option('bunhe_count')
                bunhe_count += 1
                self.set_option('bunhe_count', bunhe_count)
                cfg_limit_count = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'))
                if bunhe_count >= cfg_limit_count:
                    self.status = 99999
                else:
                    self.logger.info('펠로우 추출 (' + str(bunhe_count) + '/' + str(cfg_limit_count) + ')')
                    self.status = 401
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
            for i in range(2):
                pb_name = 'mail_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(60, 50, 280, 90)
                )
                self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.status += 1
                    return self.status
            self.status = 99999
        elif self.status == 2:
            self.lyb_mouse_click('mail_scene_modu')
            self.status += 1
        elif self.status == 3:
            self.status = 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def taming_scene(self):

        if self.status == 0:

            (s_loc_x, s_loc_y) = self.get_location('taming_s')
            (e_loc_x, e_loc_y) = self.get_location('taming_e')

            adjust_rgb = (30, 30, 30)
            sub_pb_name = 'taming_sub_inner_s'
            sub_pb = self.get_center_pixel_info(sub_pb_name)
            sub_pb_rgb = sub_pb[1]

            dx = 0
            total_length = e_loc_x - s_loc_x
            while True:
                (r, g, b) = self.game_object.get_pixel_info(self.window_pixels, s_loc_x + dx, s_loc_y)
                if abs(sub_pb_rgb[0] - r) < adjust_rgb[0] and abs(sub_pb_rgb[1] - g) < adjust_rgb[1] and abs(
                                sub_pb_rgb[2] - b) < adjust_rgb[2]:
                    self.logger.warn('Found Start: ' + str((s_loc_x + dx, s_loc_y)))
                    break

                dx += 1
                if dx > total_length:
                    break

            if dx > total_length:
                return self.status

            s_loc_x = s_loc_x + dx - 10

            dx = 0
            total_length = e_loc_x - s_loc_x
            while True:
                (r, g, b) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x - dx, e_loc_y)
                if abs(sub_pb_rgb[0] - r) < adjust_rgb[0] and abs(sub_pb_rgb[1] - g) < adjust_rgb[1] and abs(
                                sub_pb_rgb[2] - b) < adjust_rgb[2]:
                    self.logger.warn('Found End: ' + str((e_loc_x - dx, s_loc_y)))
                    break

                dx += 1
                if dx > total_length:
                    break

            if dx > total_length:
                return self.status

            e_loc_x = e_loc_x - dx + 10

            self.set_option('s_loc', (s_loc_x, s_loc_y))
            self.set_option('e_loc', (e_loc_x, e_loc_y))
            self.status += 1
        elif self.status == 1:
            self.status += 1
            cfg_response = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response')) * 0.001
            # self.logger.warn(cfg_response)
            self.game_object.interval = self.period_bot(cfg_response)
        elif self.status == 2:
            (s_loc_x, s_loc_y) = self.get_option('s_loc')
            (e_loc_x, e_loc_y) = self.get_option('e_loc')
            dx = 0
            total_length = e_loc_x - s_loc_x
            # self.logger.debug('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            while True:
                (r, g, b) = self.game_object.get_pixel_info(self.window_pixels, e_loc_x - dx, e_loc_y)
                # self.logger.debug(str(((e_loc_x - dx), e_loc_y)) + ' ' + str((r, g, b)))

                if (r, g, b) == (75, 0, 0):
                    self.lyb_mouse_click('taming_scene_touch', custom_threshold=0)
                    self.status += 1
                    break

                if r > 170 and g > 170 and b > 170:
                    self.lyb_mouse_click('taming_scene_touch', custom_threshold=0)
                    self.status += 1
                    break

                dx += 1
                if dx > total_length:
                    break

            # self.logger.debug('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

            cfg_response = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response')) * 0.001
            self.game_object.interval = self.period_bot(cfg_response)
        elif self.status >= 3 and self.status < 5:
            self.status += 1
        else:
            self.status = 0

        return self.status

    def config_scene(self):

        resource_name = 'config_scene_character_confirm_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            self.lyb_mouse_click('config_scene_character_confirm_button', custom_threshold=0)
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == self.get_work_status('캐릭터 선택'):
            self.lyb_mouse_click('config_scene_tab_0', custom_threshold=0)
            self.status = 10
        elif self.status == 10:
            self.status += 1
        elif self.status >= 11 and self.status < 13:
            self.lyb_mouse_click('config_scene_character', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def class_select_scene(self):

        self.lyb_mouse_click('back', custom_threshold=0)

        return self.status

    def character_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            cfg_index = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number'))
            self.logger.info('캐릭터 선택 번호: ' + str(cfg_index) + '번')
            pb_name = 'character_scene_list_' + str(cfg_index - 1)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        else:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def monster_sangse_scene(self):

        pb_name = 'monster_sangse_scene_lock'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            self.logger.warn('이동 불가능한 몬스터 감지됨')
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            return self.status

        current_work = self.game_object.get_scene('main_scene').current_work

        if self.status == 0:
            if current_work != None:
                self.game_object.get_scene('main_scene').set_option(current_work + '_done', True)
            self.lyb_mouse_click(self.scene_name + '_go', custom_threshold=0)
        elif self.status == 100:
            cfg_threshold = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')) * 0.01

            for i in range(len(lybgameicarus.LYBIcarus.area_list)):
                for j in range(len(lybgameicarus.LYBIcarus.area_sub_list[i])):
                    resource_name = 'monster_sangse_scene_boss_' + str(i) + str(j) + '_loc'
                    (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                        self.window_image,
                        resource_name,
                        custom_threshold=cfg_threshold,
                        custom_top_level=(255, 120, 120),
                        custom_below_level=(240, 100, 100),
                        custom_flag=1,
                        custom_rect=(150, 340, 310, 370)
                    )
                    self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.logger.info('보스 감지. 다음 지역 진행')
                        self.game_object.get_scene('gyeoljeong_bogwanham_scene').status = 0
                        count = self.get_option('passed_boss_count')
                        if count == None:
                            count = 0

                        self.set_option('passed_boss_count', count + 1)
                        self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

                        self.status = 0
                        return self.status

            cfg_map = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map')
            if current_work == '펠로우 세트':
                cfg_map = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map')

            if cfg_map == True:
                self.set_option('arrived', False)
                self.game_object.get_scene('middlas_npc_map_scene').status = 0
                self.lyb_mouse_click(self.scene_name + '_map', custom_threshold=0)
                self.status += 1
            else:
                self.status = 200
        elif self.status >= 101 and self.status < 110:
            if self.get_option('arrived') == True:
                self.status = 300
            else:
                self.lyb_mouse_click(self.scene_name + '_map', custom_threshold=0)
                self.status += 1
        elif self.status == 200:
            if current_work != None:
                self.game_object.get_scene('main_scene').set_option(current_work + '_done', True)
            self.lyb_mouse_click(self.scene_name + '_go', custom_threshold=0)
            self.status = 0
        elif self.status == 300:
            if current_work != None:
                self.game_object.get_scene('main_scene').set_option(current_work + '_done', True)
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def gyeoljeong_bogwanham_scene(self):

        self.game_object.current_matched_scene['name'] = ''

        resource_name = 'gyeoljeong_bogwanham_scene_sort_config_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        # self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            self.logger.warn('미완료')
            self.lyb_mouse_click('gyeoljeong_bogwanham_scene_sort_incomplete', custom_threshold=0)
            return self.status

        pb_name = 'gyeoljeong_bogwanham_scene_all'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.warn(pb_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name)
            return self.status

        cfg_area = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area')
        cfg_area_index = lybgameicarus.LYBIcarus.area_list.index(cfg_area)
        cfg_sub_area = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area')
        cfg_sub_area_index = lybgameicarus.LYBIcarus.area_sub_list[cfg_area_index].index(cfg_sub_area)

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('drag_count', 0)
            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now') == True:
                self.status = 100
            else:
                self.status += 1
        elif self.status == 1:
            passed_boss_count = self.game_object.get_scene('monster_sangse_scene').get_option('passed_boss_count')
            if passed_boss_count == None:
                passed_boss_count = 0

            area_index = cfg_area_index
            area_len = len(lybgameicarus.LYBIcarus.area_list)

            sub_area_index = cfg_sub_area_index + passed_boss_count
            sub_area_len = len(lybgameicarus.LYBIcarus.area_sub_list[cfg_area_index])

            if sub_area_index >= sub_area_len:
                area_index = (cfg_area_index + 1) % area_len
                sub_area_index = 0

            self.set_option('area_index', area_index)
            self.set_option('sub_area_index', sub_area_index)

            pb_name = 'gyeoljeong_bogwanham_scene_list_' + str(area_index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 2:
            self.lyb_mouse_click('gyeoljeong_bogwanham_scene_sort', custom_threshold=0)
            self.status += 1
        elif self.status >= 3 and self.status < 6:
            self.logger.info('결정 보관함 페이지 정리 중... (' + str(self.status - 2) + '/3)')
            self.lyb_mouse_drag('gyeoljeong_bogwanham_scene_drag_top', 'gyeoljeong_bogwanham_scene_drag_bot')
            self.set_option('area_find_count', 0)
            self.status += 1
        elif self.status == 6:
            drag_count = self.get_option('drag_count')
            if drag_count == None:
                drag_count = 0

            if drag_count > 5:
                self.logger.info('탐색 실패')
                self.status = 99999
            else:
                area_index = self.get_option('area_index')
                sub_area_index = self.get_option('sub_area_index')

                self.logger.info(lybgameicarus.LYBIcarus.area_list[area_index] + '>' +
                                 lybgameicarus.LYBIcarus.area_sub_list[area_index][sub_area_index] + ' 탐색 중...(' + str(
                    drag_count + 1) + '/6)')

                cfg_threshold = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')) * 0.01
                if cfg_threshold < 0.8:
                    cfg_threshold = 0.8

                self.logger.info('인식 허용률 80%이하 80%로 강제 설정됩니다... 현재 인식 허용률: ' + str(int(cfg_threshold * 100)) + '%')

                resource_name = 'gyeoljeong_bogwanham_scene_sub_area_' + str(area_index) + str(sub_area_index) + '_loc'
                for k in range(4):
                    upper = 70 + (80 * k)
                    lower = 170 + (80 * k)

                    if lower >= 360:
                        upper = 260
                        lower = 360

                    (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                        self.window_image,
                        resource_name,
                        custom_threshold=cfg_threshold,
                        custom_flag=1,
                        custom_rect=(155, upper, 460, lower),
                        debug=True
                    )
                    self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y + 40)
                        self.game_object.get_scene('monster_sangse_scene').status = 100
                        break

                area_find_count = self.get_option('area_find_count')
                if area_find_count == None:
                    area_find_count = 0

                if area_find_count > 3:
                    self.set_option('area_find_count', 0)
                    self.status += 1
                else:
                    self.set_option('area_find_count', area_find_count + 1)
        elif self.status == 7:
            drag_count = self.get_option('drag_count')
            if drag_count == None:
                drag_count = 0
            self.set_option('drag_count', drag_count + 1)
            self.lyb_mouse_drag('gyeoljeong_bogwanham_scene_drag_bot', 'gyeoljeong_bogwanham_scene_drag_top', delay=1,
                                stop_delay=1)
            self.status += 1
        elif self.status == 8:
            self.status -= 2
        elif self.status == 100:
            self.lyb_mouse_click('gyeoljeong_bogwanham_scene_sort', custom_threshold=0)
            self.status += 1
        elif self.status >= 101 and self.status < 105:
            cfg_threshold = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')) * 0.01
            self.logger.info('인식 허용률 80%이하 80%로 강제 설정됩니다... 현재 인식 허용률: ' + str(int(cfg_threshold * 100)) + '%')
            for i in range(len(lybgameicarus.LYBIcarus.area_list)):
                for j in range(len(lybgameicarus.LYBIcarus.area_sub_list[i])):
                    resource_name = 'gyeoljeong_bogwanham_scene_sub_area_' + str(
                        len(lybgameicarus.LYBIcarus.area_list) - i - 1) + str(
                        len(lybgameicarus.LYBIcarus.area_sub_list[i]) - j - 1) + '_loc'
                    for k in range(4):
                        upper = 70 + (80 * k)
                        lower = 170 + (80 * k)

                        if lower >= 360:
                            upper = 260
                            lower = 360

                        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                            self.window_image,
                            resource_name,
                            custom_threshold=cfg_threshold,
                            custom_flag=1,
                            custom_rect=(155, upper, 460, lower)
                        )
                        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                        if loc_x != -1:
                            self.lyb_mouse_click_location(loc_x, loc_y + 40)
                            self.status += 1
                            return self.status
            self.logger.info('현재 지역 이름 탐색 실패(' + str(self.status - 100) + '/4)')
            self.lyb_mouse_drag('gyeoljeong_bogwanham_scene_drag_top', 'gyeoljeong_bogwanham_scene_drag_bot', delay=1,
                                stop_delay=1)
            self.status += 1
        elif self.status == 105:
            self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def menu_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == self.get_work_status('펠로우 탐험'):
            pb_name = 'menu_scene_fellow_sub_0'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                index = lybgameicarus.LYBIcarus.menu_fellow_sub_list.index('펠로우 탐험')
                self.lyb_mouse_click('menu_scene_fellow_sub_' + str(index), custom_threshold=0)
                self.game_object.get_scene('fellow_tamheom_scene').status = 0
                self.status = 99999
            else:
                self.lyb_mouse_click('menu_scene_fellow', custom_threshold=0)
        elif self.status == self.get_work_status('펠로우 세트'):
            self.logger.warn('길들이기 쿨타임을 설정해야 합니다. 현재 설정값: ' + str(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming')) + ' 초')
            pb_name = 'menu_scene_fellow_sub_0'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                index = lybgameicarus.LYBIcarus.menu_fellow_sub_list.index('펠로우 세트')
                self.lyb_mouse_click('menu_scene_fellow_sub_' + str(index), custom_threshold=0)
                self.game_object.get_scene('fellow_set_scene').status = 0
                self.status = 99999
            else:
                self.lyb_mouse_click('menu_scene_fellow', custom_threshold=0)
        elif self.status == self.get_work_status('몬스터 결정'):
            pb_name = 'menu_scene_seongjang_sub_1'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                index = lybgameicarus.LYBIcarus.menu_seongjang_sub_list.index('몬스터 결정')
                self.lyb_mouse_click('menu_scene_seongjang_sub_' + str(index), custom_threshold=0)
                self.game_object.get_scene('gyeoljeong_bogwanham_scene').status = 0
                self.status = 99999
            else:
                self.lyb_mouse_click('menu_scene_seongjang', custom_threshold=0)
        elif self.status == self.get_work_status('캐릭터 선택'):
            pb_name = 'menu_scene_config'
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.get_scene('config_scene').status = self.status
            self.status = 99999
        elif self.status >= 99996 and self.status <= 99999:
            self.status -= 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def tamheom_dungrok_scene(self):

        self.game_object.current_matched_scene['name'] = ''

        resource_name = 'tamheom_dungrok_scene_sort_config_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        if match_rate > 0.9:
            cfg_sort = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort')
            cfg_sort_index = lybgameicarus.LYBIcarus.fellow_sort_list.index(cfg_sort)
            self.logger.debug(cfg_sort + ' 클릭')
            pb_name = 'tamheom_dungrok_sort_scene_select_' + str(cfg_sort_index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('fellow_index', 0)
            self.set_option('time_index', 3)
            self.status += 1
        elif self.status == 1:
            # 추천 펠로우 팝업
            resource_name = 'tamheom_dungrok_scene_popup_chucheon_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                self.logger.debug('추천 펠로우')
                pb_name = 'tamheom_dungrok_scene_popup_chucheon_dungrok'
                if self.get_game_config(
                                lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom') == False:
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(130, 100, 190, 380)
                    )
                    self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                else:
                    for i in range(5):
                        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                            self.window_image,
                            self.game_object.resource_manager.pixel_box_dic[pb_name],
                            custom_threshold=0.7,
                            custom_flag=1,
                            custom_rect=(130, 350 - (i * 70) - 70, 190, 380)
                        )
                        self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                        if loc_x != -1:
                            break

                if loc_x != -1:
                    self.set_option('last_status', self.status)
                    self.status = 10
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status
                else:
                    self.lyb_mouse_click('tamheom_dungrok_scene_popup_chucheon_close_icon', custom_threshold=0)
                    return self.status

            pb_name = 'tamheom_dungrok_scene_chucheon'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9 and self.get_game_config(
                            lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend') == True:
                self.logger.warn('추천 펠로우를 보유하고 있습니다')
                self.lyb_mouse_click('tamheom_dungrok_scene_chucheon_button', custom_threshold=0)
                return self.status
            else:
                self.logger.warn('추천 펠로우 사용 안함')
                self.set_option('last_status', self.status)
                self.status = 20
                self.lyb_mouse_click('tamheom_dungrok_scene_dungrok_button', custom_threshold=0)
        elif self.status == 10:
            # 시간 선택할려고 왔는데 시간 선택 화면이 아냐? 그럼 다시 돌아간다.
            # 추천 펠로우 팝업
            resource_name = 'tamheom_dungrok_scene_time_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate < 0.8:
                self.status = self.get_option('last_status')
                return self.status

            # 일단 가장 오래 걸리는 걸로 셋팅해놓고...
            for i in range(4):
                pb_name = 'tamheom_dungrok_scene_time_' + str(i)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                time.sleep(0.1)

            current_area_index = -1
            for i in range(len(lybgameicarus.LYBIcarus.tamheom_duration_list)):
                self.logger.debug(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i)))
                is_ok = True
                for j in range(len(lybgameicarus.LYBIcarus.tamheom_duration_list[i])):
                    pb_name = 'tamheom_dungrok_scene_duration_' + str(i) + str(j)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name,
                                                                      custom_below_level=195, custom_top_level=255)
                    self.logger.debug(
                        pb_name + ' ' + str(lybgameicarus.LYBIcarus.tamheom_duration_list[i][j]) + ' ' + str(
                            round(match_rate, 2)))
                    if match_rate < 0.9:
                        is_ok = False
                        break
                if is_ok == True:
                    current_area_index = i
                    break

            if current_area_index != -1:
                cfg_duration_index = int(self.get_game_config(
                    lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(current_area_index)))
                pb_name = 'tamheom_dungrok_scene_time_' + str(cfg_duration_index)
                self.logger.debug(pb_name + ' ' + str(
                    lybgameicarus.LYBIcarus.tamheom_duration_list[current_area_index][cfg_duration_index]) + ' ' + str(
                    round(match_rate, 2)))
                self.lyb_mouse_click(pb_name, custom_threshold=0)
            # cfg_20_minute = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20')
            # if cfg_20_minute == True:
            # 	pb_name = 'tamheom_dungrok_scene_20'
            # 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            # 	self.logger.warn(pb_name + ' ' + str(round(match_rate, 2)))
            # 	if match_rate > 0.9:
            # 		self.logger.info('20분 탐험 수행')
            # 		self.lyb_mouse_click(pb_name, custom_threshold=0)
            # 		self.status = 100
            # 		return self.status

            # for i in range(4):
            # 	pb_name = 'tamheom_dungrok_scene_time_' + str(i)
            # 	self.lyb_mouse_click(pb_name, custom_threshold=0)
            # 	time.sleep(0.1)

            self.status = 100
        elif self.status == 20:
            # 정렬 탐색
            pb_name = 'tamheom_dungrok_scene_sort'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.status += 1
            else:
                self.status = self.get_option('last_status')
        elif self.status == 21:
            self.status += 1
        elif self.status == 22:
            # 시간 선택할려고 왔는데 시간 선택 화면이 아냐? 그럼 다시 돌아간다.
            # 추천 펠로우 팝업
            resource_name = 'tamheom_dungrok_scene_time_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate < 0.65:
                self.status = self.get_option('last_status')
                return self.status

            self.set_option('last_status', self.status)
            self.set_option('search_count', 0)
            self.set_option('fellow_index', 0)

            # 일단 가장 오래 걸리는 걸로 셋팅해놓고...
            time_index = self.get_option('time_index')
            for i in range(time_index + 1):
                pb_name = 'tamheom_dungrok_scene_time_' + str(i)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                time.sleep(0.1)

            current_area_index = -1
            for i in range(len(lybgameicarus.LYBIcarus.tamheom_duration_list)):
                self.logger.debug(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i)))
                is_ok = True
                for j in range(len(lybgameicarus.LYBIcarus.tamheom_duration_list[i])):
                    pb_name = 'tamheom_dungrok_scene_duration_' + str(i) + str(j)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name,
                                                                      custom_below_level=195, custom_top_level=255)
                    self.logger.debug(
                        pb_name + ' ' + str(lybgameicarus.LYBIcarus.tamheom_duration_list[i][j]) + ' ' + str(
                            round(match_rate, 2)))
                    if match_rate < 0.9:
                        is_ok = False
                        break
                if is_ok == True:
                    current_area_index = i
                    break

            if current_area_index > -1:
                cfg_duration_index = int(self.get_game_config(
                    lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(current_area_index)))
                cfg_duration_index -= (3 - time_index)

                self.logger.info('index=' + str(cfg_duration_index))
                if cfg_duration_index > -1:
                    pb_name = 'tamheom_dungrok_scene_time_' + str(cfg_duration_index)
                    self.logger.debug(pb_name + ' ' + str(
                        lybgameicarus.LYBIcarus.tamheom_duration_list[current_area_index][
                            cfg_duration_index]) + ' ' + str(round(match_rate, 2)))
                    self.lyb_mouse_click(pb_name, custom_threshold=0)

            # cfg_20_minute = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20')
            # if cfg_20_minute == True:
            # 	pb_name = 'tamheom_dungrok_scene_20'
            # 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            # 	self.logger.warn(pb_name + ' ' + str(round(match_rate, 2)))
            # 	if match_rate > 0.9:
            # 		self.logger.info('20분 탐험 수행')
            # 		self.lyb_mouse_click(pb_name, custom_threshold=0)
            # 		self.status += 1
            # 		return self.status

            # time_index = self.get_option('time_index')
            # for i in range(time_index + 1):
            # 	pb_name = 'tamheom_dungrok_scene_time_' + str(i)
            # 	self.lyb_mouse_click(pb_name, custom_threshold=0)
            # 	time.sleep(0.1)


            self.status += 1
        elif self.status == 23:
            # 등록할 펠로우 탐색
            fellow_index = self.get_option('fellow_index')
            if fellow_index == 0:
                custom_rect = (260, 210, 440, 250)
            elif fellow_index == 1:
                custom_rect = (350, 210, 600, 250)
            else:
                custom_rect = (500, 210, 639, 250)

            self.logger.debug('fellow_index: ' + str(fellow_index))

            is_found = False
            for i in range(3):
                pb_name = 'tamheom_dungrok_scene_fellow_list_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=custom_rect
                )
                self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    is_found = True
                    break;

            if is_found == False:
                self.set_option('fellow_index', 2)
                self.set_option('search_count', 3)

            self.status += 1
        elif self.status == 24:
            self.status += 1
        elif self.status == 25:
            # 등록 버튼 활성화
            pb_name = 'tamheom_dungrok_scene_dungrok'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.status = 100
            else:
                fellow_index = self.get_option('fellow_index')
                if fellow_index >= 2:
                    search_count = self.get_option('search_count')
                    if search_count > 2:
                        time_index = self.get_option('time_index')
                        if time_index <= 0:
                            self.logger.warn('탐험 가능한 펠로우 탐색 실패')
                            self.status = 99999
                        else:
                            self.set_option('time_index', time_index - 1)
                            self.lyb_mouse_drag('tamheom_dungrok_scene_drag_left', 'tamheom_dungrok_scene_drag_right')
                            self.status += 1
                    else:
                        self.logger.info('수평 드래그 탐색(' + str(search_count + 1) + '/3)')
                        self.set_option('search_count', search_count + 1)
                        self.set_option('fellow_index', 0)
                        self.lyb_mouse_drag('tamheom_dungrok_scene_drag_right', 'tamheom_dungrok_scene_drag_left')
                        self.status = 23
                else:
                    self.logger.info('펠로우 탐색(' + str(fellow_index + 1) + '/3)')
                    self.set_option('fellow_index', fellow_index + 1)
                    self.status = 23
        elif self.status >= 26 and self.status < 28:
            self.lyb_mouse_drag('tamheom_dungrok_scene_drag_left', 'tamheom_dungrok_scene_drag_right')
            self.status += 1
        elif self.status == 28:
            self.status = self.get_option('last_status')
        elif self.status == 100:
            self.set_option('sijak_lag_limit', 0)
            self.status += 1
        elif self.status == 101:
            # 시작 버튼 활성화
            lag_limit = self.get_option('sijak_lag_limit')
            if lag_limit > 5:
                self.logger.warn('[시작] 버튼 활성화 연속 감지 - 랙으로 판단')
                self.status = 99999
                return self.status

            self.set_option('sijak_lag_limit', lag_limit + 1)

            pb_name = 'tamheom_dungrok_scene_sijak'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status
            else:
                self.logger.warn('[시작] 버튼 탐색 실패')
                self.status = 99999
        else:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def fellow_tamheom_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.game_object.get_scene('tamheom_dungrok_scene').status = 0

            # 완료 탐색
            for i in range(2):
                pb_name = 'fellow_tamheom_scene_complete_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 60, 600, 380)
                )
                self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            # N 탐색
            for i in range(3):
                pb_name = 'fellow_tamheom_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 60, 600, 380)
                )
                self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            # 등록 가능 탐색
            for i in range(3):
                pb_name = 'fellow_tamheom_scene_available_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 60, 600, 380)
                )
                self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            self.status = 99999
        else:
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

            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death') == True:
                self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 캐릭터 사망 감지')
                png_name = self.game_object.save_image('character_death')
                self.game_object.telegram_send('', image=png_name)

            self.status = 0

        return self.status

    def quest_scene(self):

        self.game_object.current_matched_scene['name'] = ''
        qNumber = 5
        cfg_area = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area')
        cfg_area_sub = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub')
        cfg_area_index = lybgameicarus.LYBIcarus.area_list.index(cfg_area)
        cfg_area_sub_index = lybgameicarus.LYBIcarus.quest_area_sub_list[cfg_area_index].index(cfg_area_sub)

        self.logger.debug('area_index ' + str(cfg_area_index) + ' area_sub_index ' + str(cfg_area_sub_index))

        elapsed_time = time.time() - self.get_checkpoint('last_check')
        if elapsed_time > self.period_bot(10):
            self.set_option('last_clicked_go', None)

        self.set_checkpoint('last_check')

        if self.get_option('last_clicked_go') != None:
            self.logger.warn('이동 클릭했는데도 퀘스트창이 감지됨 - 다시 클릭')
            (loc_x, loc_y) = self.get_option('last_clicked_go')
            self.set_option('last_clicked_go', None)
            self.lyb_mouse_click_location(loc_x, loc_y)
            self.set_checkpoint('close')
            return self.status

        for i in range(1):
            pb_name = 'quest_scene_bosang_new_' + str(i)
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(230, 320, 639, 380)
            )
            # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
                return self.status

        pb_name = 'quest_accept_again_ok'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
            return self.status

        pb_name = 'queset_scene_dalseongdo_close_icon'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
            return self.status

        pb_name = 'quest_scene_bosang'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(580, 100, 620, 340)
        )
        # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            cfg_limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit'))
            complete_count = self.get_option('complete_count')
            if complete_count == None:
                complete_count = 0

            if cfg_limit_count != 0 and complete_count + 1 >= cfg_limit_count:
                self.logger.warn('정예 퀘스트 진행 횟수: ' + str(complete_count + 1) + ' / ' + str(cfg_limit_count))
                self.game_object.get_scene('main_scene').set_option('정예 퀘스트' + '_end_flag', True)
                self.status = 99999
            else:
                self.set_option('complete_count', complete_count + 1)

            self.game_object.addStatistic('정예 퀘스트 보상 횟수')
            self.lyb_mouse_click_location(loc_x, loc_y)
            self.game_object.interval = self.period_bot(3)

            if self.game_object.get_scene('main_scene').current_work == '정예 퀘스트':
                if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang') == True:
                    self.game_object.telegram_send(
                        '창 이름 [' + str(self.game_object.window_title) + '] 정예 퀘스트 완료 보상 수령 감지')
                    png_name = self.game_object.save_image('elite_quest_reward')
                    self.game_object.telegram_send('', image=png_name)

            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status = self.get_work_status('정예 퀘스트')
        elif self.status == self.get_work_status('메인 퀘스트'):
            self.status = 10
        elif self.status == self.get_work_status('정예 퀘스트'):
            self.set_option('enable_quest_count', 0)
            self.status = 20
        elif self.status == 10:
            self.logger.critical('지역 퀘스트 탐색 시작')
            self.logger.critical('수락할 퀘스트가 감지되면 모두 수락 후 이동합니다.')
            self.game_object.get_scene('main_scene').set_option('local_quest_done', False)
            self.lyb_mouse_click('quest_scene_tab_2', custom_threshold=0)
            # self.set_option('sub_tab_iterator', 0)
            self.status += 1
            self.set_option('last_status', self.status)
            self.status = 100
        elif self.status == 11:
            self.game_object.get_scene('main_scene').set_option('local_quest_done', True)
            self.status = 99999
        # sub_tab_iterator = self.get_option('sub_tab_iterator')
        # if sub_tab_iterator > 2:
        # 	self.game_object.get_scene('main_scene').set_option('local_quest_done', True)
        # 	self.status = 99999
        # else:
        # 	pb_name = 'quest_scene_sub_tab_' + str(sub_tab_iterator)
        # 	self.lyb_mouse_click(pb_name, custom_threshold=0)
        # 	self.set_option('last_status', self.status)
        # 	self.set_option('sub_tab_iterator', sub_tab_iterator + 1)
        # 	self.status = 100
        # elif self.status == 12:			
        # 	sub_tab_iterator = self.get_option('sub_tab_iterator')
        # 	if sub_tab_iterator > 2:
        # 		self.status = 99999
        # 	else:
        # 		pb_name = 'quest_scene_sub_tab_' + str(sub_tab_iterator)
        # 		self.lyb_mouse_click(pb_name, custom_threshold=0)
        # 		self.set_option('last_status', self.status)
        # 		self.set_option('sub_tab_iterator', sub_tab_iterator + 1)
        # 		self.status = 100

        elif self.status == 20:
            self.lyb_mouse_click('quest_scene_tab_3', custom_threshold=0)
            self.status += 1
        elif self.status == 21:
            # self.logger.warn('go: ' + self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'))
            # for i in range(5):
            # 	self.logger.warn('accept' + str(i) + ': ' + self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)))


            surak_list = []
            for i in range(qNumber):
                cfg_elite_quest = self.get_game_config(
                    lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i))
                # cfg_elite_quest_index = lybgameicarus.LYBIcarus.elite_quest_dic[cfg_area_sub].index(cfg_elite_quest)
                if cfg_elite_quest != lybgameicarus.LYBIcarus.elite_quest_dic[cfg_area_sub][
                    0] and cfg_elite_quest not in surak_list:
                    surak_list.append(cfg_elite_quest)

            self.logger.warn(surak_list)
            self.set_option('original_surak_list', copy.deepcopy(surak_list))
            self.set_option('surak_list', surak_list)
            self.set_option('drag_count', 0)
            self.set_option('page_find_count', 0)
            self.set_option('drag_direction', 'bot')
            self.set_option('pb_name', 'quest_scene_surak')
            # self.lyb_mouse_click('quest_scene_sub_tab_' + str(cfg_area_index), custom_threshold=0)

            self.status += 1
            self.lyb_mouse_click('quest_scene_area_0', custom_threshold=0)
            self.set_option('last_status', self.status)
            if cfg_area_index == 0:
                self.status = 400
            else:
                self.status = 410
        elif self.status == 22:
            page_find_count = self.get_option('page_find_count')
            page_find_count += 1
            self.set_option('page_find_count', page_find_count)

            self.logger.debug('page_find_count:' + str(page_find_count))
            surak_list = self.get_option('surak_list')
            if len(surak_list) == 0:
                self.status = 30
            else:
                remove_list = []
                cfg_threshold = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')) * 0.01
                # area_count = len(lybgameicarus.LYBIcarus.elite_quest_dic[cfg_area_sub])

                for each_surak in surak_list:
                    self.logger.info('정예 퀘스트 [' + str(each_surak) + '] 탐색 중...')
                    # if each_surak == area_count - 1:
                    # 	self.logger.info('마지막 정예 퀘스트는 인식 허용률 보정합니다.')
                    # 	cfg_threshold *= 0.9
                    # else:
                    cfg_threshold = int(
                        self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')) * 0.01
                    if cfg_threshold < 0.8:
                        cfg_threshold = 0.8

                    self.logger.info('정예 퀘스트 인식율이 80% 보다 낮으면 80%로 설정됩니다. 현재 설정값: ' + str(cfg_threshold * 100) + '%')
                    resource_name = 'quest_scene_elite_' + str(each_surak) + '_loc'
                    for i in range(5):
                        self.logger.debug(str(i + 1) + ' 라인 탐색')
                        self.logger.debug('수행 가능 여부 탐색')
                        if each_surak in remove_list:
                            continue

                        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                            self.window_image,
                            resource_name,
                            custom_threshold=cfg_threshold,
                            custom_top_level=(155, 155, 155),
                            custom_below_level=(110, 110, 110),
                            source_custom_top_level=(255, 255, 255),
                            source_custom_below_level=(170, 170, 170),
                            custom_flag=1,
                            custom_rect=(170, 135 + (i * 55) - 40, 420, 135 + (i * 55) + 30),
                            debug=True
                        )
                        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                        if loc_x != -1:
                            if not each_surak in remove_list:
                                remove_list.append(each_surak)
                            self.logger.warn('[' + str(each_surak) + ']는 더 이상 수행할 수 없습니다.')
                            break
                        else:
                            self.logger.debug('[' + str(each_surak) + '] 탐색')
                            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                                self.window_image,
                                resource_name,
                                custom_threshold=cfg_threshold,
                                custom_top_level=(255, 255, 255),
                                custom_below_level=(170, 170, 170),
                                custom_flag=1,
                                custom_rect=(170, 135 + (i * 55) - 40, 420, 135 + (i * 55) + 30),
                                debug=True
                            )
                            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                            if loc_x != -1:
                                enable_quest_count = self.get_option('enable_quest_count')
                                self.set_option('enable_quest_count', enable_quest_count + 1)

                                if not each_surak in remove_list:
                                    remove_list.append(each_surak)

                                pb_name = self.get_option('pb_name')
                                adj_x, adj_y = self.game_object.get_player_adjust()
                                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                                    self.window_image,
                                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                                    custom_threshold=0.8,
                                    custom_flag=1,
                                    custom_rect=(580, loc_y - 40 - adj_y, 635, loc_y + 10 - adj_y)
                                )
                                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                                if loc_x != -1:
                                    if pb_name == 'quest_scene_go':
                                        self.set_checkpoint('close')
                                        self.set_option('last_clicked_go', (loc_x, loc_y))
                                    else:
                                        self.set_option('last_clicked_go', None)
                                    self.lyb_mouse_click_location(loc_x, loc_y)
                                    break

                for each_remove in remove_list:
                    surak_list.remove(each_remove)

                if len(surak_list) == 0:
                    self.set_option('page_find_count', 0)
                    self.status = 30
                else:
                    if page_find_count > 5:
                        self.set_option('page_find_count', 0)
                        self.set_option('surak_list', surak_list)
                        self.status += 1
        elif self.status == 23:
            self.logger.debug('drag: ' + self.get_option('drag_direction'))
            if self.get_option('drag_direction') == 'top':
                self.lyb_mouse_drag('quest_scene_drag_top', 'quest_scene_drag_bot')
            else:
                self.lyb_mouse_drag('quest_scene_drag_bot', 'quest_scene_drag_top')
            drag_count = self.get_option('drag_count')
            if drag_count > 20:
                self.logger.warn('설정한 정예 퀘스트를 못 찾겠음')
                self.status = 30
            else:
                self.logger.info('정예 퀘스트 탐색 중... (' + str(drag_count + 1) + '/20)')
                if drag_count > 0 and drag_count % 20 == 0:
                    if self.get_option('drag_direction') == 'top':
                        self.set_option('drag_direction', 'bot')
                    else:
                        self.set_option('drag_direction', 'top')

                self.set_option('drag_count', drag_count + 1)
                self.game_object.interval = self.period_bot(3)
                self.status -= 1
        elif self.status == 30:
            if self.get_option('pb_name') == 'quest_scene_go':
                self.status = 99999
            else:
                cfg_elite_quest = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go')
                cfg_elite_quest_index = lybgameicarus.LYBIcarus.elite_quest_dic[cfg_area_sub].index(cfg_elite_quest)
                original_surak_list = self.get_option('original_surak_list')
                if cfg_elite_quest_index == 0:
                    self.logger.warn('정예 퀘스트 이동 선택 안함')
                    self.status = 99999
                elif cfg_elite_quest not in original_surak_list:
                    self.logger.warn('이동할 정예 퀘스트가 수락 퀘스트에 없음')
                    self.status = 99999
                else:
                    surak_list = []
                    surak_list.append(cfg_elite_quest)
                    self.set_option('pb_name', 'quest_scene_go')
                    self.set_option('drag_count', 0)
                    self.set_option('drag_direction', 'top')
                    self.set_option('surak_list', surak_list)
                    self.status = 22
        elif self.status == 100:
            pb_name = 'quest_scene_surak'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(580, 100, 620, 340)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            pb_name = 'quest_scene_go'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(580, 100, 635, 340)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.set_checkpoint('close')
                self.set_option('last_clicked_go', (loc_x, loc_y))
                self.lyb_mouse_click_location(loc_x, loc_y)
            else:
                self.set_option('last_clicked_go', None)
                self.status = self.get_option('last_status')
        elif self.status == 201:
            self.status = 200
        elif self.status == 300:
            self.logger.critical('서브 퀘스트 탐색을 시작(처치, 수집, 사냥 퀘스트만 수락)합니다.')
            self.logger.critical('탐색할 페이지를 크게 설정할수록 오래 걸리지만 정확도가 올라갑니다.')
            self.logger.critical('[작업>메인 퀘스트>서브 퀘스트 탐색 페이지 수] 에서 설정 가능합니다.')
            self.status += 1
        elif self.status == 301:
            self.set_option('acceptable_sub_quest', 0)
            self.lyb_mouse_click('quest_scene_tab_1', custom_threshold=0)
            self.set_option('sub_drag_count', 0)
            self.set_option('sub_quest_iterator', 0)
            self.status += 1
        elif self.status == 302:
            exclusive_sub_quest_list = [
                'quest_scene_sub_make_loc',
                'quest_scene_sub_taming_loc',
                'quest_scene_sub_dogam_loc'
            ]

            accept_sub_quest_list = [
                'quest_scene_sub_gather_loc',
                'quest_scene_sub_hunting_loc',
                'quest_scene_sub_kill_loc'
            ]

            cfg_threshold = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')) * 0.01

            is_clicked = False
            i = self.get_option('sub_quest_iterator')
            if i > 3:
                self.set_option('sub_quest_iterator', 0)
                self.status += 1
            else:
                self.logger.warn('수행 가능한 서브 퀘스트 탐색 중 ...(' + str(i + 1) + '/4)')
                for resource_name in exclusive_sub_quest_list:
                    (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                        self.window_image,
                        resource_name,
                        custom_threshold=cfg_threshold,
                        custom_top_level=(255, 255, 255),
                        custom_below_level=(200, 200, 200),
                        custom_flag=1,
                        custom_rect=(190, 95 + (50 * i), 350, 195 + (50 * i))
                    )
                    # self.logger.warn(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        pb_name = 'quest_scene_pogi'
                        adj_x, adj_y = self.game_object.get_player_adjust()
                        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                            self.window_image,
                            self.game_object.resource_manager.pixel_box_dic[pb_name],
                            custom_threshold=0.8,
                            custom_flag=1,
                            custom_rect=(550, loc_y - 30 - adj_y, 590, loc_y + 30 - adj_y)
                        )
                        # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                        if loc_x != -1:
                            self.logger.warn('자동 수행 불가능한 서브 퀘스트 인식됨: 포기 클릭')
                            self.lyb_mouse_click_location(loc_x, loc_y)
                            is_clicked = True
                            break

                if is_clicked == False:
                    for resource_name in accept_sub_quest_list:
                        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                            self.window_image,
                            resource_name,
                            custom_threshold=cfg_threshold,
                            custom_top_level=(255, 255, 255),
                            custom_below_level=(200, 200, 200),
                            custom_flag=1,
                            custom_rect=(190, 95 + (50 * i), 350, 195 + (50 * i))
                        )
                        # self.logger.warn(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                        if loc_x != -1:
                            acceptable_sub_quest = self.get_option('acceptable_sub_quest')
                            self.set_option('acceptable_sub_quest', acceptable_sub_quest + 1)
                            self.logger.warn('수행 가능한 서브 퀘스트 수락 ' + str(acceptable_sub_quest + 1))
                            pb_name = 'quest_scene_surak'
                            adj_x, adj_y = self.game_object.get_player_adjust()
                            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                                self.window_image,
                                self.game_object.resource_manager.pixel_box_dic[pb_name],
                                custom_threshold=0.8,
                                custom_flag=1,
                                custom_rect=(570, loc_y - 30 - adj_y, 610, loc_y + 30 - adj_y)
                            )
                            # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                            if loc_x != -1:
                                self.logger.info('자동 수행 가능한 서브 퀘스트 인식됨: 수락 클릭')
                                self.lyb_mouse_click_location(loc_x, loc_y)
                                break
                self.game_object.interval = self.period_bot(0.01)
                self.set_option('sub_quest_iterator', i + 1)
        elif self.status == 303:
            sub_drag_count = self.get_option('sub_drag_count')
            cfg_search_sub = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub'))
            if sub_drag_count > cfg_search_sub - 1:
                acceptable_sub_quest = self.get_option('acceptable_sub_quest')
                if acceptable_sub_quest > 0:
                    self.game_object.get_scene('main_scene').set_option('sub_quest_done', False)
                else:
                    self.game_object.get_scene('main_scene').set_option('sub_quest_done', True)

                self.status = 99999
            else:
                self.set_option('sub_drag_count', sub_drag_count + 1)
                self.logger.warn('서브 퀘스트 탐색 중...(' + str(sub_drag_count + 1) + '/' + str(cfg_search_sub) + ' 페이지)')
                self.lyb_mouse_drag('quest_scene_drag_bot', 'quest_scene_drag_top', delay=1, stop_delay=1)
                self.status += 1
        elif self.status == 304:
            self.status += 1
        elif self.status == 305:
            self.status -= 3
        elif self.status == 400:
            pb_name = 'quest_scene_area_sub_' + str(cfg_area_index) + str(cfg_area_sub_index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status = self.get_option('last_status')
        elif self.status == 410:
            pb_name = 'quest_scene_area_' + str(cfg_area_index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 411:
            pb_name = 'quest_scene_area_sub_' + str(cfg_area_index) + str(cfg_area_sub_index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status = self.get_option('last_status')
        elif self.status == 99999:
            if self.game_object.get_scene('main_scene').current_work == '정예 퀘스트':
                if self.get_option('enable_quest_count') == 0:
                    self.game_object.get_scene('main_scene').set_option('정예 퀘스트' + '_end_flag', True)

            self.set_checkpoint('close')
            self.logger.debug('Here: ' + str(self.get_checkpoint('close')))
            self.lyb_mouse_click(self.scene_name + '_close_icon')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def connect_account_scene(self):
        if self.status == 0:
            self.set_checkpoint('interval_login')
            self.game_object.set_option('search_google_account', True)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click(self.scene_name + '_google')
            self.status += 1
        elif self.status >= 2 and self.status < 5:
            self.status += 1
        elif self.status == 5:
            pb_name = self.scene_name + '_disconnect'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status += 1
                return self.status

            pb_name = self.scene_name + '_connect'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.status = 99999
                return self.status

            self.status = 10
        elif self.status >= 6 and self.status < 9:
            self.status += 1
        elif self.status == 9:
            self.status = 5
        elif self.status == 10:
            if time.time() - self.get_checkpoint('interval_login') > self.period_bot(100):
                self.status = 99999
            else:
                self.status = 5
        else:
            self.game_object.set_option('search_google_account', False)
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

        return self.status

    def google_play_account_select_scene(self):

        (top_loc_x, top_loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic['google_play_letter'],
            custom_flag=1,
            custom_rect=(150, 50, 370, 250)
        )
        self.logger.info('구글 계정 기준점: ' + str((top_loc_x, top_loc_y)))
        if top_loc_x == -1:
            return self.status

        if self.status == 0:
            (bottom_loc_x, bottom_loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic['google_play_add_account_letter'],
                custom_flag=1,
                custom_rect=(150, 180, 370, 380)
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
                self.logger.info('구글 계정 ' + str(self.google_account_number) + '개 감지됨')

        if self.status >= self.google_account_number:
            self.status = 0
            self.logger.info(str(self.google_account_number) + ' 개의 계정 작업 완료')
            return self.status
        else:
            self.logger.info(str(self.status + 1) + ' 번째 구글 계정 로그인 시도')
        # self.game_object.get_scene('connect_account_scene').set_option('select_complete_flag', True)

        if self.status >= 0 and self.status < 5:
            click_loc_x = top_loc_x + 10
            click_loc_y = top_loc_y + self.google_account_height * self.status + self.google_account_height * 0.8
            self.lyb_mouse_click_location(click_loc_x, click_loc_y)
            # self.lyb_mouse_move_location(click_loc_x, click_loc_y)
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
                (bottom_loc_x, bottom_loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic['google_play_add_account_letter'],
                    custom_flag=1,
                    custom_rect=(150, 180, 370, 380)
                )
                if bottom_loc_x > 0 and bottom_loc_y > 0:
                    self.lyb_mouse_click_location(top_loc_x - 150, top_loc_y)
                    # self.lyb_mouse_move_location(top_loc_x - 150, top_loc_y)
                    self.logger.warn(str(self.status + 1) + ' 번째 구글 계정 감지 실패')
                    self.logger.info('총 ' + str(self.status) + ' 개의 계정 작업 완료')
                    self.status = 0

                else:
                    click_loc_x = top_loc_x + 10
                    click_loc_y = top_loc_y + self.google_account_height * 4 + self.google_account_height * 0.8
                    self.lyb_mouse_click_location(click_loc_x, click_loc_y)
                    # self.lyb_mouse_move_location(click_loc_x, click_loc_y)
                    self.status += 1

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

    def jeopsokbosang_scene(self):

        self.game_object.current_matched_scene['name'] = ''

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            pb_name = 'jeopsokbosang_scene_modu'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

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
                self.logger.info('구글 계정 변경 시도')
                self.status = 300
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
            for each_icon in lybgameicarus.LYBIcarus.icarus_icon_list:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
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
            for each_icon in lybgameicarus.LYBIcarus.icarus_icon_list:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
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
            refresh_count = self.get_option(self.current_work + '_refreh')
            if refresh_count == None:
                refresh_count = 0

            if refresh_count > 60:
                self.game_object.current_matched_scene['name'] = ''
                refresh_count = 0

            self.set_option(self.current_work + '_refreh', refresh_count + 1)

            elapsed_time = self.get_elapsed_time()
            main_quest_duration = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration'))
            if elapsed_time > self.period_bot(main_quest_duration):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.set_option('sub_quest_done', None)
                self.set_option('local_quest_done', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.loggingElapsedTime('메인 퀘스트 진행 시간', elapsed_time, main_quest_duration, period=60)

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status == None:
                inner_status = 0

            self.logger.debug('inner_status: ' + str(inner_status))

            if inner_status == 0:
                self.logger.info('퀘스트 목록 체크...')
                if self.open_quest_list() == True:
                    return self.status
                else:
                    # 서브
                    if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub') == True:
                        if self.get_option('sub_quest_done') != True:
                            self.game_object.get_scene('quest_scene').status = 300
                            self.set_option(self.current_work + '_pb_name', 'main_scene_quest_sub')
                            self.set_option(self.current_work + 'custom_top_level', (30, 220, 240))
                            self.set_option(self.current_work + 'custom_below_level', (0, 145, 155))
                            self.lyb_mouse_click('main_scene_quest', custom_threshold=0)
                            self.set_option(self.current_work + '_inner_status', 100)
                            return self.status

                        self.set_option('sub_quest_done', None)

                    # 지역
                    if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local') == True:
                        if self.get_option('local_quest_done') != True:
                            self.game_object.get_scene('quest_scene').status = self.status
                            self.lyb_mouse_click('main_scene_quest', custom_threshold=0)
                            self.set_option(self.current_work + '_pb_name', 'main_scene_quest_local')
                            self.set_option(self.current_work + 'custom_top_level', (90, 210, 155))
                            self.set_option(self.current_work + 'custom_below_level', (50, 120, 95))
                            self.set_option(self.current_work + '_inner_status', 100)
                            return self.status

                        self.set_option('local_quest_done', None)

                    # 메인
                    self.set_option(self.current_work + '_pb_name', 'main_scene_quest_main')
                    self.set_option(self.current_work + 'custom_top_level', (255, 220, 30))
                    self.set_option(self.current_work + 'custom_below_level', (130, 125, 0))
                    self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status >= 1 and inner_status < 5:

                self.set_checkpoint('mainquest_check_lag')

                pb_name = self.get_option(self.current_work + '_pb_name')
                custom_top_level = self.get_option(self.current_work + 'custom_top_level')
                custom_below_level = self.get_option(self.current_work + 'custom_below_level')

                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.5,
                    custom_flag=1,
                    custom_top_level=custom_top_level,
                    custom_below_level=custom_below_level,
                    custom_rect=(510, 80, 540, 200)
                )
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
                if loc_x == -1:
                    self.logger.info('퀘스트 목록 체크...')
                    self.lyb_mouse_drag('main_scene_quest_drag_top', 'main_scene_quest_drag_bot')
                    self.set_option(self.current_work + '_inner_status', inner_status + 1)
                else:
                    self.logger.info('퀘스트 목록 체크... ok')
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option(self.current_work + '_inner_status', 6)
            elif inner_status == 5:
                self.logger.warn('퀘스트 감지 실패, 맨 위 퀘스트를 클릭')
                self.lyb_mouse_click('main_scene_quest_list_0', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', 6)
            elif inner_status == 6:

                # search_method = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local')
                # elapsed_time_click_quest = time.time() - self.game_object.get_scene('quest_scene').get_checkpoint('close')
                # if elapsed_time_click_quest > self.period_bot(30):
                # 	pb_name = 'main_scene_quest_new'
                # 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                # 	self.logger.debug(pb_name + ' ' + str(match_rate))
                # 	if match_rate > 0.9:
                # 		self.game_object.get_scene('quest_scene').status = self.status
                # 		self.lyb_mouse_click('main_scene_quest', custom_threshold=0)
                # 		return self.status

                if self.isAutoMainQuest() == False:
                    self.set_option(self.current_work + '_inner_status', 1)
                else:
                    if self.main_scene_is_quest_complete() == True:
                        return self.status

                    cfg_lag = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period'))
                    elapsed_last_checking = time.time() - self.get_checkpoint('mainquest_check_lag')
                    if cfg_lag != 0 and elapsed_last_checking > cfg_lag:
                        random_direction = int(random.random() * 8)
                        self.logger.warn(
                            '메인 퀘스트 랙 방지 움직임: ' + str(lybgameicarus.LYBIcarus.character_move_list[random_direction]))
                        self.set_checkpoint('mainquest_check_lag')
                        self.lyb_mouse_drag('character_move_direction_center',
                                            'character_move_direction_' + str(random_direction), stop_delay=1)
                    # self.lyb_mouse_click('auto', custom_threshold=0)
                    # self.set_option(self.current_work + '_inner_status', 0)
            elif inner_status >= 100 and inner_status < 110:
                if (self.get_option('sub_quest_done') == True or
                            self.get_option('local_quest_done') == True):
                    self.set_option(self.current_work + '_inner_status', 0)
                else:
                    elapsed_time_click_quest = time.time() - self.game_object.get_scene('quest_scene').get_checkpoint(
                        'close')
                    # self.logger.debug('퀘스트 창 닫은 후 경과 시간: ' + str(int(elapsed_time_click_quest)) + '초')
                    if elapsed_time_click_quest < self.period_bot(10):
                        self.set_option(self.current_work + '_inner_status', 1)
                    else:
                        self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 110:
                self.set_option(self.current_work + '_inner_status', 0)

        elif self.status == self.get_work_status('정예 퀘스트'):
            self.game_object.current_matched_scene['name'] = ''

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            elapsed_time = self.get_elapsed_time()
            cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration'))
            self.loggingElapsedTime('[정예 퀘스트] 경과 시간', elapsed_time, cfg_duration, period=60)
            if elapsed_time > self.period_bot(cfg_duration):
                self.set_option(self.current_work + '_end_flag', True)

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status == None:
                inner_status = 0

            # self.logger.debug('inner_status: ' + str(inner_status))

            if inner_status == 0:
                self.game_object.get_scene('quest_scene').set_option('complete_count', 0)
                self.set_checkpoint('checking_lag')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 1:
                if self.isAutoMainQuest() == False:
                    # cfg_area = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area')
                    cfg_area_sub = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub')
                    cfg_elite_quest = self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go')
                    cfg_elite_quest_index = lybgameicarus.LYBIcarus.elite_quest_dic[cfg_area_sub].index(cfg_elite_quest)
                    if cfg_elite_quest_index == 0:
                        # 정예 퀘스트 작업 중인데 이동을 선택 안함으로 했다. ==> 자동 사냥 하겠다는 의미
                        self.logger.info('이동할 정예 퀘스트가 "설정 안함"으로 되어 있어서 [자동]로 전환합니다.')
                        self.lyb_mouse_click('auto', custom_threshold=0)

                    self.set_option(self.current_work + '_inner_status', inner_status + 1)
                else:
                    if self.main_scene_is_quest_complete() == True:
                        return self.status

                    cfg_lag_period = int(
                        self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag'))
                    elapsed_last_checking = time.time() - self.get_checkpoint('checking_lag')
                    if cfg_lag_period != 0 and elapsed_last_checking > cfg_lag_period:
                        random_direction = int(random.random() * 8)
                        self.logger.warn(
                            '정예 퀘스트 랙 방지 움직임: ' + str(lybgameicarus.LYBIcarus.character_move_list[random_direction]))
                        self.set_checkpoint('checking_lag')
                        self.lyb_mouse_drag('character_move_direction_center',
                                            'character_move_direction_' + str(random_direction), stop_delay=1)
                        return self.status

                    cfg_check_period = int(
                        self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check'))
                    elapsed_time_click_quest = time.time() - self.game_object.get_scene('quest_scene').get_checkpoint(
                        'close')
                    if cfg_check_period != 0 and elapsed_time_click_quest > cfg_check_period:
                        self.logger.warn('정예 퀘스트 주기적인 체크 실시')
                        self.set_option(self.current_work + '_inner_status', inner_status + 1)
                        return self.status

            elif inner_status == 2:
                self.game_object.get_scene('quest_scene').status = self.status
                self.lyb_mouse_click('main_scene_quest', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status - 1)


        elif self.status == self.get_work_status('자동 사냥'):
            self.game_object.current_matched_scene['name'] = ''

            elapsed_time = self.get_elapsed_time()
            auto_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration'))
            if elapsed_time > self.period_bot(auto_duration):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            if self.isAutoMainQuest() == False:
                self.lyb_mouse_click('auto', custom_threshold=0)
            else:
                if self.main_scene_is_quest_complete() == True:
                    return self.status

                cfg_click_period = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period'))
                if time.time() - self.get_checkpoint(self.current_work + '_last_clicked') > cfg_click_period:
                    pb_name_list = []

                    if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite') == True:
                        pb_name_list.append('main_scene_quest_elite')

                    for pb_name in pb_name_list:
                        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                            self.window_image,
                            self.game_object.resource_manager.pixel_box_dic[pb_name],
                            custom_threshold=0.5,
                            custom_flag=1,
                            custom_rect=(510, 80, 540, 200)
                        )
                        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(round(match_rate, 2)))
                        if loc_x != -1:
                            self.logger.info('주기적인 퀘스트 클릭: ' + str(pb_name))
                            self.lyb_mouse_click_location(loc_x, loc_y)
                            self.set_checkpoint(self.current_work + '_last_clicked')
                            return self.status

            self.loggingElapsedTime('[자동 사냥] 경과 시간', elapsed_time, auto_duration, period=60)


        elif self.status == self.get_work_status('펠로우 탐험'):
            self.game_object.current_matched_scene['name'] = ''

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('menu_scene').status = self.status
            self.lyb_mouse_click('main_scene_menu', custom_threshold=0)


        elif (self.status == self.get_work_status('몬스터 결정') or
                      self.status == self.get_work_status('펠로우 세트')
              ):
            self.game_object.current_matched_scene['name'] = ''

            elapsed_time = self.get_elapsed_time()
            duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration'))
            if self.status == self.get_work_status('펠로우 세트'):
                duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration'))

            if elapsed_time > self.period_bot(duration):
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
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 1:
                if self.isAutoMainQuest() == False:
                    self.lyb_mouse_click('auto', custom_threshold=0)
                else:
                    cfg_period = int(
                        self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period'))
                    if self.status == self.get_work_status('펠로우 세트'):
                        cfg_period = int(
                            self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period'))

                    elapsed_last_checking = time.time() - self.get_checkpoint(self.current_work + '_last_check')
                    if cfg_period != 0 and elapsed_last_checking > cfg_period:
                        self.logger.warn('[' + str(self.current_work) + '] 체크')

                        if self.status == self.get_work_status('몬스터 결정'):
                            cfg_auto_off = self.get_game_config(
                                lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off')
                            if cfg_auto_off == True:
                                resource_name = 'main_scene_auto_loc'
                                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                                    self.window_image,
                                    resource_name,
                                    custom_threshold=0.6,
                                    custom_top_level=(245, 245, 245),
                                    custom_below_level=(140, 140, 140),
                                    custom_flag=1,
                                    custom_rect=(260, 290, 370, 320)
                                )
                                self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                                if loc_x != -1:
                                    self.lyb_mouse_click('auto', custom_threshold=0)

                        self.set_option(self.current_work + '_inner_status', inner_status + 1)
                        return self.status

                    if self.isFellowOn() == True:
                        is_clicked = self.lyb_mouse_click('main_scene_fellow_on', custom_threshold=0)
                        if is_clicked == True:
                            return self.status

            elif inner_status == 2:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0);
                self.game_object.get_scene('menu_scene').status = self.status
                self.set_checkpoint(self.current_work + '_last_check')
                self.set_option(self.current_work + '_done', False)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 3:
                if self.get_option(self.current_work + '_done') == False:
                    self.set_option(self.current_work + '_inner_status', inner_status - 1)
                else:
                    self.set_option(self.current_work + '_inner_status', inner_status - 2)

            self.loggingElapsedTime('[' + str(self.current_work) + '] 경과 시간', elapsed_time, duration, period=60)


        elif self.status == self.get_work_status('캐릭터 선택'):
            self.game_object.current_matched_scene['name'] = ''

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('menu_scene').status = self.status
            self.lyb_mouse_click('main_scene_menu', custom_threshold=0)


        elif self.status == self.get_work_status('가방 정리'):
            self.game_object.current_matched_scene['name'] = ''

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('gabang_scene').status = 0
            self.lyb_mouse_click('main_scene_gabang')

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
                              str(int(
                                  self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_LOOP)) - loop_count) + ' 회 남음')
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

        # 가방 풀
        if self.isFull() == True:
            self.logger.warn('가방 풀 감지됨')
            self.lyb_mouse_click('main_scene_gabang', custom_threshold=0)
            return True

        # 물약 감지
        if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion') == True:
            (loc_x, loc_y) = self.locPotionEmpty()
            if loc_x != -1:
                self.logger.warn('물약 없음 감지됨')
                self.game_object.get_scene('sangjeom_scene').status = 100
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True

        # 파티 초대 수락 여부
        resource_name = 'main_scene_invite_party_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        # self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite') == True:
                self.lyb_mouse_click('main_scene_invite_party_accept')
            else:
                self.lyb_mouse_click('main_scene_invite_party_reject')
            return True

        # 아이템 등록
        resource_name = 'main_scene_register_item_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        if match_rate > 0.9:
            self.logger.info('[아이템 등록] 감지됨')
            self.lyb_mouse_click('main_scene_register_item_close', custom_threshold=0)
            return True

        # 안내 - 상세 정보
        resource_name = 'information_detail_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        # self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > 0.9:
            self.logger.info('[안내] 팝업창 감지됨')
            pb_name = 'main_scene_info_move'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(480, 120, 550, 330)
            )
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            else:
                self.lyb_mouse_click('information_detail_close_icon', custom_threshold=0)
            # if self.current_work == '메인 퀘스트':
            # 	self.set_option(self.current_work + '_end_flag', True)
            # 	return True

        if self.is_moving() == True:
            return True

        # if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill') == True:
        # 	is_clicked = False
        # 	for i in range(2):
        # 		pb_name = 'main_scene_co_skill_' + str(i)
        # 		match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=200)
        # 		if match_rate > 0.9:
        # 			self.logger.info(pb_name + ' ' + str(round(match_rate, 2)))
        # 			self.lyb_mouse_click(pb_name, custom_threshold=0)
        # 			is_clicked = True

        # 	if is_clicked == True:
        # 		return True


        # # 펠로우 스킬
        # skill_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime'))
        # if skill_cooltime != 0:
        # 	if self.main_scene_click_periodically('main_scene_fellow_skill', skill_cooltime) == True:
        # 		return True		

        # 각성 스킬
        skill_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime'))
        if skill_cooltime != 0:
            if self.main_scene_click_periodically('main_scene_gakseong_skill', skill_cooltime, delay=1) == True:
                return True

        # 파티 스킬
        skill_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime'))
        if skill_cooltime != 0:
            if self.main_scene_click_periodically('main_scene_party_skill', skill_cooltime, delay=1) == True:
                return True

        for i in range(3):
            cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_' + str(i)))
            if cooltime != 0:
                if self.main_scene_click_periodically('main_scene_quickslot_' + str(i), cooltime) == True:
                    return True

        cfg_check_fellow_period = int(
            self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check'))
        elapsed_time = time.time() - self.get_checkpoint('elite_quest_fellow_check')
        if cfg_check_fellow_period != 0 and elapsed_time > cfg_check_fellow_period:
            self.logger.warn('주기적인 펠로우 탐험 체크')
            self.set_checkpoint('elite_quest_fellow_check')
            self.game_object.get_scene('menu_scene').status = self.get_work_status('펠로우 탐험')
            self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
            return self.status

        # 친구 상호 작용
        pb_name_list = [
            'main_scene_friend',
            'main_scene_sayhello',
            'main_scene_chukha'
        ]
        if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react') == True:
            for pb_name in pb_name_list:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(150, 230, 250, 290)
                )
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return True

                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                if match_rate > 0.9:
                    self.logger.debug(pb_name + ' ' + str(match_rate))
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return True

        # if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'cond_skill') == True:
        # 	pb_name = 'main_scene_co_skill_1'
        # 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=240)
        # 	if match_rate > 0.9:
        # 		self.lyb_mouse_click(pb_name, custom_threshold=0)
        # 		return True

        pb_name = 'main_scene_level'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(610, 180, 639, 210)
        )
        if loc_x != -1:
            self.lyb_mouse_click_location(loc_x, loc_y)
            return True

        # 길들이기
        taming_cooltime = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming'))
        if taming_cooltime != 0:
            pb_name = 'main_scene_taming'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            # self.logger.warn(pb_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                if self.main_scene_click_periodically(pb_name, taming_cooltime) == True:
                    return True

        # 새 우편함 확인
        if self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail') == True:
            pb_name = 'main_scene_new_mail'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(140, 330, 240, 380)
            )
            if match_rate > 0.8:
                self.logger.info('우편함 확인')
                self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
                return True

        return False

    def open_quest_list(self):
        pb_name_open = 'main_scene_quest_open'
        match_rate_open = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name_open, custom_below_level=240)
        self.logger.debug(pb_name_open + ' ' + str(match_rate_open))

        pb_name_close = 'main_scene_quest_close'
        match_rate_close = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name_close,
                                                                custom_below_level=240)
        self.logger.debug(pb_name_close + ' ' + str(match_rate_close))

        if match_rate_open < 0.9 and match_rate_close > 0.9:
            self.lyb_mouse_click(pb_name_close, custom_threshold=0)
            return True

        return False

    def main_scene_click_periodically(self, pb_name, cooltime, delay=0):
        if self.get_checkpoint(pb_name + 'last_clicked') == 0:
            self.set_checkpoint(pb_name + 'last_clicked')
        else:
            elapsed_time = time.time() - self.get_checkpoint(pb_name + 'last_clicked')
            if elapsed_time > cooltime:
                self.lyb_mouse_click(pb_name, custom_threshold=0, delay=delay)
                self.set_checkpoint(pb_name + 'last_clicked')
                return True

        return False

    def locPotionEmpty(self):
        check_count = self.get_option('empty_check_count')
        if check_count == None:
            check_count = 0

        # resource_name = 'main_quest_auto_loc'
        pb_name = 'main_scene_potion_empty'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.9,
            custom_top_level=(255, 255, 255),
            custom_below_level=(165, 165, 165),
            custom_flag=1,
            custom_rect=(250, 340, 280, 380)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            if check_count > 5:
                self.set_option('empty_check_count', 0)
                return (loc_x, loc_y)

            self.set_option('empty_check_count', check_count + 1)
            return (-1, -1)

        self.set_option('empty_check_count', 0)

        return (-1, -1)

    def isFull(self):
        check_count = self.get_option('full_check_count')
        if check_count == None:
            check_count = 0

        # resource_name = 'main_quest_auto_loc'
        pb_name = 'main_scene_full'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.6,
            custom_top_level=(255, 110, 110),
            custom_below_level=(230, 80, 80),
            custom_flag=1,
            custom_rect=(570, 50, 605, 70)
        )
        # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            if check_count > 2:
                self.set_option('full_check_count', 0)
                return True
            self.set_option('full_check_count', check_count + 1)
            return False

        self.set_option('full_check_count', 0)
        return False

    def isFellowOn(self):
        check_count = self.get_option('fellow_check_count')
        if check_count == None:
            check_count = 0

        # resource_name = 'main_quest_auto_loc'
        pb_name = 'main_scene_fellow_on'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_top_level=(220, 255, 255),
            custom_below_level=(190, 245, 245),
            custom_flag=1,
            custom_rect=(400, 340, 440, 380)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            if check_count > 2:
                self.set_option('fellow_check_count', 0)
                return True

            self.logger.debug('[탑승] 감지됨: ' + str(check_count) + '/2')
            self.set_option('fellow_check_count', check_count + 1)
            return False

        self.set_option('fellow_check_count', 0)
        return False

    def isAutoMainQuest(self):
        auto_check = self.get_option('auto_check')
        if auto_check == None:
            auto_check = 0

        # resource_name = 'main_quest_auto_loc'
        cfg_limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit'))

        resource_name = 'main_scene_auto_loc'
        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
            self.window_image,
            resource_name,
            custom_threshold=0.6,
            # custom_top_level=(245, 245, 245),
            # custom_below_level=(140, 140, 140),
            custom_flag=1,
            custom_rect=(260, 290, 370, 320),
            debug=True
        )
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x == -1:
            for i in range(3):
                pb_name = 'main_scene_combo_' + str(i)
                # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.9,
                    custom_top_level=(255, 255, 150),
                    custom_below_level=(200, 150, 0),
                    custom_flag=1,
                    custom_rect=(410, 150, 500, 200)
                )
                # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.set_option('auto_check', 0)
                    return True

            pb_name = 'auto_quest'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.8:
                self.set_option('auto_check', 0)
                return True

            if auto_check > cfg_limit_count:
                self.set_option('auto_check', 0)
                return False

            self.logger.debug('[자동] 감지 실패: ' + str(auto_check) + '/' + str(cfg_limit_count))
            self.set_option('auto_check', auto_check + 1)

            return True

        self.set_option('auto_check', 0)
        return True

    def is_moving(self):

        moving_threshold = self.get_option('main_scene_moving_threshold')
        if moving_threshold == None:
            moving_threshold = 0
        moving_limit = 120

        if moving_threshold < moving_limit:
            resource_name = 'main_scene_move_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                # custom_top_level=(255, 255, 255),
                # custom_below_level=(200, 200, 200),
                custom_flag=1,
                custom_rect=(260, 290, 370, 320)
            )
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
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

    def main_scene_is_quest_complete(self):
        cfg_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period'))
        if cfg_period != 0:
            last_drag = self.get_checkpoint('quest_complete_last_drag')
            if last_drag == 0:
                self.set_checkpoint('quest_complete_last_drag')
            else:
                quest_drag_count = self.get_option('quest_drag_count')
                if quest_drag_count == None:
                    quest_drag_count = 0

                quest_drag_start = self.get_option('quest_drag_start')
                quest_drag_end = self.get_option('quest_drag_end')
                if quest_drag_start == None:
                    quest_drag_start = 'bot'
                    quest_drag_end = 'top'

                if quest_drag_count > 4:
                    self.set_option('quest_drag_count', 0)
                    self.set_option('quest_drag_start', quest_drag_end)
                    self.set_option('quest_drag_end', quest_drag_start)
                else:
                    self.set_option('quest_drag_start', quest_drag_start)
                    self.set_option('quest_drag_end', quest_drag_end)

                elapsed_time = time.time() - last_drag
                if elapsed_time > cfg_period:
                    self.logger.debug('[퀘스트 완료] 탐색 중 ...')
                    self.lyb_mouse_drag('main_scene_quest_drag_' + quest_drag_start,
                                        'main_scene_quest_drag_' + quest_drag_end)
                    self.set_checkpoint('quest_complete_last_drag')
                    self.set_option('quest_drag_count', quest_drag_count + 1)
                    return True

        pb_name = 'main_scene_quest_complete'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.6,
            custom_flag=1,
            custom_rect=(480, 80, 520, 200)
        )
        # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.logger.warn('[퀘스트 완료] 감지됨')
            self.checkpoint[self.current_work + '_last_clicked'] = 0
            self.lyb_mouse_click_location(loc_x, loc_y)
            return True

        return False

    def get_work_status(self, work_name):
        if work_name in lybgameicarus.LYBIcarus.work_list:
            return (lybgameicarus.LYBIcarus.work_list.index(work_name) + 1) * 1000
        else:
            return 99999

import likeyoubot_resource as lybrsc
import likeyoubot_message
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import operator
import random
import likeyoubot_win
import likeyoubot_darkeden as lybgamedarkeden
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time


class LYBDarkEdenScene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)

    def process(self, window_image, window_pixels):

        super(LYBDarkEdenScene, self).process(window_image, window_pixels)

        rc = 0
        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'connect_account_scene':
            rc = self.connect_account_scene()
        elif self.scene_name == 'google_account_scene':
            rc = self.google_account_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'character_scene':
            rc = self.character_scene()
        elif self.scene_name == 'dejeon_scene':
            rc = self.dejeon_scene()
        elif self.scene_name == 'gyeoltoojang_scene':
            rc = self.gyeoltoojang_scene()
        elif self.scene_name == 'combat_scene':
            rc = self.combat_scene()
        elif self.scene_name == 'quest_scene':
            rc = self.quest_scene()
        elif self.scene_name == 'dungeon_scene':
            rc = self.dungeon_scene()
        elif self.scene_name == 'tobeolde_scene':
            rc = self.tobeolde_scene()
        elif self.scene_name == 'tobeolde_main_scene':
            rc = self.tobeolde_main_scene()
        elif self.scene_name == 'death_scene':
            rc = self.death_scene()
        elif self.scene_name == 'sangjeom_scene':
            rc = self.sangjeom_scene()
        elif self.scene_name == 'buy_confirm_scene':
            rc = self.buy_confirm_scene()
        elif self.scene_name == 'gejo_tutorial_scene':
            rc = self.gejo_tutorial_scene()
        elif self.scene_name == 'gabang_tutorial_scene':
            rc = self.gejo_tutorial_scene()
        elif self.scene_name == 'ilil_quest_limit_scene':
            rc = self.ilil_quest_limit_scene()
        elif self.scene_name == 'jido_scene':
            rc = self.jido_scene()
        elif self.scene_name == 'gabang_scene':
            rc = self.gabang_scene()
        elif self.scene_name == 'gabang_sell_scene':
            rc = self.gabang_sell_scene()
        elif self.scene_name == 'gasang_sooryeonjang_scene':
            rc = self.gasang_sooryeonjang_scene()
        elif self.scene_name == 'party_chode_scene':
            rc = self.party_chode_scene()
        elif self.scene_name == 'field_boss_scene':
            rc = self.field_boss_scene()
        elif self.scene_name == 'event_scene':
            rc = self.event_scene()
        elif self.scene_name == 'special_dungeon_scene':
            rc = self.special_dungeon_scene()
        elif self.scene_name == 'special_dungeon_create_scene':
            rc = self.special_dungeon_create_scene()
        elif self.scene_name == 'gejo_scene':
            rc = self.gejo_scene()
        elif self.scene_name == 'upjeok_scene':
            rc = self.upjeok_scene()
        elif self.scene_name == 'bosang_scene':
            rc = self.bosang_scene()
        elif self.scene_name == 'guild_scene':
            rc = self.guild_scene()






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

    def guild_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.click_resource('guild_scene_tab_길드 정보_loc')
            self.status += 1
        elif self.status == 2:
            self.click_resource('guild_scene_chulseok_loc')            
            if self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu') == True:
                self.click_resource('guild_scene_tab_길드 임무_loc')
                self.status = 100
            else:
                self.status += 1
        elif self.status == 100:
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def bosang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'bosang_scene_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(120, 90, 180, 250))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option('last_status', self.status)
                    self.status = 10
                    return self.status

            self.status = 99999
        elif 10 <= self.status < 20:
            self.status += 1

            pb_name = 'bosang_scene_chulseok'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.8:
                extra_x = 0
                for j in range(4):
                    for i in range(7):
                        if i == 6:
                            extra_x = 25
                        custom_rect = (260 + (70*i) - 30 + extra_x, 150 + (60*j) - 30, 260 + (70*i) + 30 + extra_x, 150 + (60*j) + 30)
                        pb_name = 'bosang_scene_check'
                        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                            self.window_image,
                            self.game_object.resource_manager.pixel_box_dic[pb_name],
                            custom_threshold=0.8,
                            custom_flag=1,
                            custom_top_level=(175, 220, 255),
                            custom_below_level=(160, 210, 250),
                            custom_rect=custom_rect)                    
                        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate) + ' ' + str(custom_rect))
                        if loc_x == -1:
                            self.lyb_mouse_click_location2(custom_rect[0] + 30, custom_rect[1] + 30)
                            self.status = self.get_option('last_status')
                            return self.status

            pb_name = 'bosang_scene_jeopsok'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.8:
                for i in range(5):
                    custom_rect = (240 + (120*i) - 30, 250, 240 + (120*i) + 30, 310)
                    pb_name = 'bosang_scene_jeopsok_check'
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.8,
                        custom_flag=1,
                        custom_top_level=(175, 220, 255),
                        custom_below_level=(160, 210, 250),
                        custom_rect=custom_rect)
                    self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate) + ' ' + str(custom_rect))
                    if loc_x == -1:
                        self.lyb_mouse_click_location2(custom_rect[0] + 30, custom_rect[1] + 30)
                        self.status = self.get_option('last_status')
                        return self.status

            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def upjeok_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('count', 0)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            if self.click_resource('upjeok_scene_bosang_loc') is True:
                return self.status

            if self.click_resource('upjeok_scene_surak_loc') is True:
                return self.status

            if self.click_resource('upjeok_scene_chujeok_loc') is True:
                self.status = 10
                return self.status

            self.status = 10
        elif self.status == 10:
            self.status += 1
            cfg_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count'))
            count = self.get_option('count')
            if count is None:
                count = 0
            if count >= cfg_count:
                if self.click_resource('upjeok_scene_out_loc') is True:
                    self.set_option('count', 0)
                    return self.status
            else:
                self.set_option('count', count + 1)
        elif self.status == self.get_work_status('종족임무'):
            self.status = 100
        elif self.status == 100:
            self.lyb_mouse_click('upjeok_scene_tab_2', custom_threshold=0)
            self.status += 1
        elif 101 <= self.status < 107:
            pb_name = 'upjeok_scene_jongjok_quest_list_' + str(self.status - 101)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option('last_status', self.status + 1)
            self.status = 110
        elif 110 <= self.status < 115:
            self.status += 1
            if self.click_resource('upjeok_scene_surak_loc') is True:
                self.status = self.get_option('last_status')
                return self.status

            if self.click_resource('upjeok_scene_bulga_loc') is True:
                self.status = 99999
                return self.status
        elif self.status == 115:
            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gejo_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            resource_name = 'gejo_scene_tab_bunhe_loc'
            self.click_resource(resource_name)
            self.status += 1
        elif 2 <= self.status < 10:
            is_clicked = False
            for i in range(len(lybgamedarkeden.LYBDarkEden.option_list)):
                cfg_item = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(i))
                pb_name = 'gejo_scene_bunhe_option_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9 and cfg_item is False:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                elif match_rate < 0.9 and cfg_item is True:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)

            for i in range(len(lybgamedarkeden.LYBDarkEden.item_quality_list)):
                cfg_item_quality = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(i))
                pb_name = 'gejo_scene_item_quality_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9 and cfg_item_quality is False:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                elif match_rate < 0.9 and cfg_item_quality is True:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)

            if is_clicked == False:
                self.status = 10
        elif self.status == 10:
            self.click_resource('gejo_scene_bunhe_loc')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def special_dungeon_create_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1   
            resource_name = 'special_dungeon_create_scene_invite_loc'         
            for i in range(4):
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(460, 190 + (i*50) - 30, 530, 190 + (i*50) + 30))
                self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status
            self.status = 10
        elif self.status == 10:
            self.click_resource('special_dungeon_create_open_loc')
            self.status += 1
        elif self.status == 11:
            self.click_resource('special_dungeon_create_scene_create_loc')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def special_dungeon_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            cfg_dungeon_name = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon')
            resource_name = 'special_dungeon_scene_tab_' + cfg_dungeon_name + '_loc'
            self.click_resource(resource_name)
            self.status += 1
        elif self.status == 2:
            cfg_difficulty = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty')
            resource_name = 'special_dungeon_scene_difficulty_' + cfg_difficulty + '_loc'
            self.click_resource(resource_name)
            self.status += 1
        elif self.status == 3:
            resource_name = 'special_dungeon_scene_ready_loc'
            self.game_object.get_scene('special_dungeon_create_scene').status = 0
            self.click_resource(resource_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def event_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            resource_name = 'event_scene_click_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]

            tutorial_iterator = self.get_option('tutorial_iterator')
            if tutorial_iterator is None:
                tutorial_iterator = 0

            if tutorial_iterator >= len(resource):
                self.set_option('tutorial_iterator', 0)
            else:
                pb_name = resource[tutorial_iterator]
                self.set_option('tutorial_iterator', tutorial_iterator + 1)
                self.logger.debug(pb_name)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.game_object.interval = 0.01
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def connect_account_scene(self):

        if time.time() - self.get_checkpoint('last_detected') > 120:
            self.set_checkpoint('last_detected')
            self.status = 0

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            for i in range(2):
                pb_name = 'connect_account_scene_check_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return self.status

            self.status = 10
        elif self.status == 10:
            self.lyb_mouse_click('connect_account_scene_google', custom_threshold=0)
            self.status += 1
        elif self.status == 11:
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def field_boss_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            self.click_resource('field_boss_scene_move')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def party_chode_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1  
            pb_name = 'party_chode_scene_check_all'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate < 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status

            if self.click_resource('party_chode_scene_seontek_chode_loc') is True:
                self.status = 10
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gasang_sooryeonjang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1

            resource_name = 'gasang_sooryeonjang_scene_limit_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            if match_rate > 0.9:
                self.status = 10
                return self.status

            resource_name = 'gasang_sooryeonjang_scene_enter_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_flag=1)
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gabang_sell_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            is_clicked = False
            for i in range(len(lybgamedarkeden.LYBDarkEden.item_list)):
                cfg_item = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(i))
                pb_name = 'gabang_sell_scene_item_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9 and cfg_item is False:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                elif match_rate < 0.9 and cfg_item is True:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)

            for i in range(len(lybgamedarkeden.LYBDarkEden.item_quality_list)):
                cfg_item_quality = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(i))
                pb_name = 'gabang_sell_scene_item_quality_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=10)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9 and cfg_item_quality is False:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                elif match_rate < 0.9 and cfg_item_quality is True:
                    is_clicked = True
                    self.lyb_mouse_click(pb_name, custom_threshold=0)

            if is_clicked == False:
                self.status = 10
        elif self.status == 10:
            self.click_resource('gabang_sell_scene_sell_loc')
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
        elif self.status == 1:
            resource_name = 'gabang_scene_jeongri_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_flag=1)
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            self.status += 1
        elif self.status == 2:
            resource_name = 'gabang_scene_sell_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_flag=1)
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            self.game_object.get_scene('gabang_sell_scene').status = 0
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status


    def jido_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('click_npc_tab', False)
            self.set_option('loc_first_monster', (-1, -1))
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('jido_scene_tab_0', custom_threshold=0)
            self.status += 1
        elif 2 <= self.status < 10:
            self.status += 1
            cfg_area = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area')
            cfg_sub_area = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area')
            cfg_monster = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster')
            cfg_npc = self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc')

            if cfg_monster == '선택안함' and cfg_npc == '선택안함':
                self.status = 99999
                return self.status

            pb_name = 'jido_scene_tab_pb_0'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                resource_name = 'jido_scene_area_' + cfg_area + '_loc'
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.7,
                    custom_flag=1)
                self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)

                return self.status

            pb_name = 'jido_scene_tab_pb_1'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                resource_name = 'jido_scene_sub_area_' + cfg_sub_area + '_loc'
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.7,
                    custom_flag=1)
                self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            pb_name = 'jido_scene_tab_pb_2'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                resource_name = 'jido_scene_monster_' + cfg_monster + '_loc'
                if cfg_monster == '선택안함':
                    if self.get_option('click_npc_tab') is False:
                        self.click_resource('jido_scene_npc_tab_loc')
                        self.set_option('click_npc_tab', True)
                        return self.status
                    resource_name = 'jido_scene_npc_' + cfg_npc + '_loc'

                for i in range(6):                    
                    (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                        self.window_image,
                        resource_name,
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(570, 180 + (i*40) - 60, 720, 180 + (i*40) + 60),
                        debug=True)
                    self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate) + str((570, 180 + (i*40) - 60, 720, 180 + (i*40) + 60)))
                    if loc_x != -1:
                        if cfg_monster != '선택안함' and self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_second_monster') is True:
                            last_loc_x, last_loc_y = self.get_option('loc_first_monster')
                            if last_loc_x != -1 and (last_loc_x != loc_x or last_loc_y != loc_y):
                                self.lyb_mouse_click_location(loc_x, loc_y)
                                self.status = 10
                                return self.status
                            else:
                                self.set_option('loc_first_monster', (loc_x, loc_y))
                        else:
                            self.lyb_mouse_click_location(loc_x, loc_y)
                            self.status = 10
                            return self.status

            is_end = True
            for i in range(4):
                pb_name = 'jido_scene_monster_last_' + str(i)
                (loc_x, loc_y) = self.get_location(pb_name)
                last_pixel = self.get_option('last_pixel_' + pb_name)
                if last_pixel == None:
                    is_end = False
                else:
                    self.logger.debug(str((loc_x, loc_y)) + ' ' + str(last_pixel) + ' ' + str(
                        self.game_object.window_pixels[loc_x, loc_y]))
                    if last_pixel != self.game_object.window_pixels[loc_x, loc_y]:
                        is_end = False

                self.set_option('last_pixel_' + pb_name, self.game_object.window_pixels[loc_x, loc_y])
            if is_end == True:
                self.logger.warn('몬스터 탐색 실패: ' + str(cfg_monster))
                self.status = 10
                return self.status

            self.lyb_mouse_drag('jido_scene_monster_drag_bot', 'jido_scene_monster_drag_top')
            self.set_option('loc_first_monster', (-1, -1))
            self.game_object.interval = self.period_bot(2)
        elif 10 <= self.status < 20:
            self.status += 1
            pb_name = 'jido_scene_monster_chujeok'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(700, 150, 780, 470))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def ilil_quest_limit_scene(self):

        self.game_object.get_scene('quest_scene').status = 20
        self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

        return self.status


    def gejo_tutorial_scene(self):

        resource_name = self.scene_name
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        if match_rate < 0.9:
            self.game_object.click_all_tutorial_point()
            return self.status

        resource_name = 'gejo_tutorial_loc'
        resource = self.game_object.resource_manager.resource_dic[resource_name]

        tutorial_iterator = self.get_option('tutorial_iterator')
        if tutorial_iterator is None:
            tutorial_iterator = 0

        if tutorial_iterator >= len(resource):
            self.set_option('tutorial_iterator', 0)
        else:
            pb_name = resource[tutorial_iterator]
            self.set_option('tutorial_iterator', tutorial_iterator + 1)
            self.logger.debug(pb_name)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.interval = 0.01

        return self.status

    def buy_confirm_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:

            pb_name = 'buy_confirm_scene_max'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(430, 210, 500, 260))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status += 1
            else:
                self.lyb_mouse_click('buy_confirm_scene_cancel', custom_threshold=0)
                self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def sangjeom_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'sangjeom_scene_tab_normal_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(160, 70, 790, 120))
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status = 10
                return self.status
        elif self.status == 10:
            self.status += 1
        elif self.status == 11:
            pb_name = self.get_option('potion_pb_name')
            if pb_name is None:
                pb_name = 'sangjeom_scene_hp_potion'
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.get_scene('buy_confirm_scene').status = 0
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def death_scene(self):

        if time.time() - self.get_checkpoint('last_death') > 60:
            self.status = 0

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_checkpoint('last_death')
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            pb_name = 'death_scene_help'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status

            pb_name = 'death_scene_help_guild'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status

            self.end_work()
            self.status = 10
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def tobeolde_main_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 6000:
            self.status += 1
            if self.isAutoCombat(limit_count=3) is False:
                self.lyb_mouse_click('main_scene_auto_0', custom_threshold=0)
                return self.status

            if self.isCenterAutoCombat(limit_count=3) is False:
                self.lyb_mouse_click('main_scene_auto_0', custom_threshold=0)
                return self.status

            resource_name = 'tobeolde_main_scene_portal_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
                self.window_image,
                resource_name,
                custom_threshold=0.6,
                custom_flag=1)
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status = 0
                return self.status
            
            if self.status % 5 == 0:
                self.lyb_mouse_drag('pad_direction_center', 'pad_direction_1', stop_delay=2)
                return self.status
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def dungeon_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == self.get_work_status('특수던전'):
            self.status = 100
        elif self.status == self.get_work_status('토벌대'):
            self.status = 200
        elif self.status == self.get_work_status('가상수련장'):
            self.status = 300
        elif self.status == 100:
            self.game_object.get_scene('special_dungeon_scene').status = 0
            self.lyb_mouse_click('dungeon_scene_special_dungeon', custom_threshold=0)
            self.status += 1
        elif self.status == 200:
            self.game_object.get_scene('tobeolde_scene').status = 0
            self.lyb_mouse_click('dungeon_scene_tobeolde', custom_threshold=0)
            self.status += 1
        elif self.status == 300:
            self.game_object.get_scene('tobeolde_scene').status = 0
            self.lyb_mouse_click('dungeon_scene_gasang_sooryeonjang', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def tobeolde_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('bottom_bosang_index', 0)
            self.status += 1
        elif self.status == 1:
            # pb_name = 'tobeolde_scene_tab_' + str(0)
            # self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif 2 <= self.status < 10:
            self.status += 1
            self.game_object.get_scene('tobeolde_combat_scene').status = 0
            self.lyb_mouse_click('tobeolde_scene_enter', custom_threshold=0)
        elif 10 <= self.status < 20:
            bottom_bosang_index = self.get_option('bottom_bosang_index')
            if bottom_bosang_index is None:
                bottom_bosang_index = 0

            if bottom_bosang_index > 2:
                self.set_option('bottom_bosang_index', 0)
                self.status = 20
            else:
                pb_name = self.scene_name + '_bosang_' + str(bottom_bosang_index)
                self.set_option('bottom_bosang_index', bottom_bosang_index + 1)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.status += 1

        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status



    def quest_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('bottom_bosang_index', 0)
            self.status += 1
        elif 1 <= self.status < 5:
            self.status += 1
            resource_name = 'quest_scene_ilil_count_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(30, 330, 130, 380))
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.status = 10
            else:
                self.lyb_mouse_click('quest_scene_tab_3', custom_threshold=0)
        elif 10 <= self.status < 20:
            self.status += 1

            for i in range(4):
                resource_name = 'quest_scene_bosang_loc'
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(125 + (180*i) - 100, 290, 125 + (180*i) + 100, 340))
                self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            for i in range(4):
                resource_name = 'quest_scene_surak_loc'
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(125 + (180*i) - 100, 290, 125 + (180*i) + 100, 340))
                self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            self.status = 20
        elif 20 <= self.status < 30:
            bottom_bosang_index = self.get_option('bottom_bosang_index')
            if bottom_bosang_index is None:
                bottom_bosang_index = 0

            if bottom_bosang_index > 2:
                self.set_option('bottom_bosang_index', 0)
                self.status = 30
            else:
                pb_name = 'quest_scene_bottom_bosang_' + str(bottom_bosang_index)
                self.set_option('bottom_bosang_index', bottom_bosang_index + 1)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def combat_scene(self):

        if self.isAutoCombat(limit_count=3) is False:
            self.lyb_mouse_click('combat_scene_auto_0', custom_threshold=0)
            return self.status

        return self.status

    def gyeoltoojang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:

            pb_name = 'gyeoltoojang_scene_limit'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.95:
                self.status = 10
                return self.status

            pb_name = 'gyeoltoojang_scene_match'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(650, 380, 700, 430))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)

            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def dejeon_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('dejeon_scene_gyeoltoojang', custom_threshold=0)
            self.game_object.get_scene('gyeoltoojang_scene').status = 0
            self.status += 1
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
            for each_icon in lybgamedarkeden.LYBDarkEden.darkeden_icon_list:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(80, 110, 700, 370)
                )
                # self.logger.debug(match_rate)
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    break
        else:
            for each_icon in lybgamedarkeden.LYBDarkEden.darkeden_icon_list:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 10, 740, 370)
                )
                # self.logger.debug(match_rate)
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    break

        # if loc_x == -1:
        # 	self.loggingToGUI('테라 아이콘 발견 못함')

        return 0

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
            self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
            self.status += 1
        elif self.status >= 2 and self.status < 6:
            self.status += 1
        elif self.status == 6:
            self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
            self.status += 1
        elif self.status >= 7 and self.status < 10:
            self.status += 1
        elif self.status >= 10 and self.status < 70:
            self.logger.info('로그인 화면 랙 인식: ' + str(self.status - 10) + '/60')
            self.status += 1
        elif self.status == 70:
            self.game_object.terminate_application()
            self.status += 1
        else:
            # self.lyb_mouse_click(self.scene_name + '_close_icon')
            self.status = 0

        return self.status

































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
        elif 0 < self.status < 1000:
            self.set_schedule_status()

        elif self.status == self.get_work_status('메인 퀘스트'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(600):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status is None:
                inner_status = 0

            self.logger.debug('inner_status: ' + str(inner_status))
            if inner_status == 0:
                self.lyb_mouse_drag('main_scene_quest_drag_top', 'main_scene_quest_drag_bot')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 1:                
                self.lyb_mouse_click('main_scene_quest_0', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 2 <= inner_status < 30:
                if self.is_complete_quest():
                    self.set_option(self.current_work + '_inner_status', 0)
                    return self.status

                if self.is_complete_accept(quest_index=0):
                    self.set_option(self.current_work + '_inner_status', 0)
                    return self.status

                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            else:
                self.set_option(self.current_work + '_inner_status', 0)

        elif self.status == self.get_work_status('자동 사냥'):

            cfg_check_workdmap = int(self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period'))
            cfg_check_sell = int(self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period'))
            cfg_check_ilil_quest = int(self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period'))
            cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration'))
            
            elapsed_time = self.get_elapsed_time()
            if elapsed_time > cfg_duration:
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.checkpoint['auto_sell_period'] = 0
                self.checkpoint['auto_ilil_quest_period'] = 0
                self.checkpoint['auto_move_check_period'] = 0
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.loggingElapsedTime('[' + str(self.current_work) + '] 경과 시간', elapsed_time, cfg_duration, period=60)
                        
            elapsed_time = time.time() - self.get_checkpoint('auto_sell_period')
            if cfg_check_sell != 0 and elapsed_time > cfg_check_sell:
                self.game_object.get_scene('gabang_scene').status = 0
                self.set_checkpoint('auto_sell_period')
                self.lyb_mouse_click('main_scene_gabang', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', 0)
                return self.status

            elapsed_time = time.time() - self.get_checkpoint('auto_ilil_quest_period')
            if cfg_check_ilil_quest != 0 and elapsed_time > cfg_check_sell:
                self.set_checkpoint('auto_ilil_quest_period')
                self.lyb_mouse_click('main_scene_menu_quest', custom_threshold=0)
                self.game_object.get_scene('quest_scene').status = 0
                self.set_option(self.current_work + '_inner_status', 0)
                return self.status

            elapsed_time = time.time() - self.get_checkpoint('auto_move_check_period')
            if cfg_check_workdmap != 0 and elapsed_time > cfg_check_workdmap:
                self.game_object.get_scene('jido_scene').status = 0
                self.set_checkpoint('auto_move_check_period')
                self.lyb_mouse_click('main_scene_map', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', 0)
                return self.status   

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status is None:
                inner_status = 0

            self.logger.debug('inner_status: ' + str(inner_status))
            if inner_status == 0:
                # self.lyb_mouse_click('main_scene_quest_3', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 0 < inner_status < 120:
                self.set_option(self.current_work + '_inner_status', inner_status + 1)

                if inner_status % 120 == 0:
                    if self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party') is True:
                        self.lyb_mouse_click('main_scene_tab_party', custom_threshold=0)
                        self.set_option(self.current_work + '_last_inner_status', inner_status + 1)
                        self.set_option(self.current_work + '_inner_status', 1000)
                        return self.status   
                elif inner_status % 40 == 0:
                    if self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok') is True:
                        self.set_option('quest_resource_name', 'main_scene_quest_jongjok_loc')
                        self.set_option(self.current_work + '_last_inner_status', inner_status + 1)
                        self.set_option(self.current_work + '_inner_status', 2000)
                        return self.status 
                elif inner_status % 30 == 0:
                    if self.drag_quest_list():
                        return self.status    
                elif inner_status % 20 == 0:
                    if self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok') is True:
                        self.set_option('quest_resource_name', 'main_scene_quest_jiyeok_loc')
                        self.set_option(self.current_work + '_last_inner_status', inner_status + 1)
                        self.set_option(self.current_work + '_inner_status', 2000)
                        return self.status  
                elif inner_status % 10 == 0:
                    self.click_resource('main_scene_quest_tab_loc')
                    return self.status 


                if self.is_complete_quest():
                    self.set_option(self.current_work + '_inner_status', 0)
                    return self.status

                if self.isAutoCombat(limit_count=5) is False:
                    self.lyb_mouse_click('main_scene_auto_0', custom_threshold=0)
                    return self.status

                if self.isCenterAutoCombat(limit_count=5) is False:
                    self.lyb_mouse_click('main_scene_auto_0', custom_threshold=0)
                    return self.status
            elif 1000 <= inner_status < 1010:
                self.set_option(self.current_work + '_inner_status', inner_status + 1)

                if self.click_resource('main_scene_party_chode_loc') is True:
                    self.game_object.get_scene('party_chode_scene').status = 0
                else:
                    self.set_option(self.current_work + '_inner_status', 1010)
            elif inner_status == 1010:
                self.click_resource('main_scene_quest_tab_loc')
                last_inner_status = self.get_option(self.current_work + '_last_inner_status')
                if last_inner_status == None:
                    last_inner_status = 0
                self.set_option(self.current_work + '_inner_status', last_inner_status)    
            elif inner_status == 2000:
                self.set_option('drag_start_pb_name', 'main_scene_quest_drag_bot')
                self.set_option('drag_end_pb_name', 'main_scene_quest_drag_top')
                self.drag_quest_list()
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 2001 <= inner_status < 2010:
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
                resource_name = self.get_option('quest_resource_name')
                for quest_index in range(5):
                    (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                        self.window_image,
                        resource_name,
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(5, 150 + (quest_index * 25), 35, 180 + (quest_index * 30)),
                        debug=True)
                    self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        self.set_option(self.current_work + '_inner_status', 1010)
                        break
            else:
                self.set_option(self.current_work + '_inner_status', 0)

        elif self.status == self.get_work_status('결투장'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status is None:
                inner_status = 0

            self.logger.debug('inner_status: ' + str(inner_status))
            if 0 <= inner_status < 10:
                pb_name = 'main_scene_menu_open'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9:
                    self.lyb_mouse_click('main_scene_menu_dejeon', custom_threshold=0)
                    self.game_object.get_scene('dejeon_scene').status = 0
                    self.set_option(self.current_work + '_inner_status', 10)
                else:
                    self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
                    self.set_option(self.current_work + '_inner_status', inner_status + 1)
            else:
                self.set_option(self.current_work + '_inner_status', 0)

        elif self.status == self.get_work_status('일일 퀘스트'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_quest', custom_threshold=0)
                self.game_object.get_scene('quest_scene').status = 0
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

        elif self.status == self.get_work_status('종족임무'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_upjeok', custom_threshold=0)
                self.game_object.get_scene('upjeok_scene').status = self.status
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

        elif self.status == self.get_work_status('특수던전'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_dungeon', custom_threshold=0)
                self.game_object.get_scene('dungeon_scene').status = self.status
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)


        elif self.status == self.get_work_status('토벌대'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_dungeon', custom_threshold=0)
                self.game_object.get_scene('dungeon_scene').status = self.status
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

        elif self.status == self.get_work_status('가상수련장'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_dungeon', custom_threshold=0)
                self.game_object.get_scene('dungeon_scene').status = self.status
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

        elif self.status == self.get_work_status('판매'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.lyb_mouse_click('main_scene_gabang', custom_threshold=0)
            self.game_object.get_scene('gabang_scene').status = 0

        elif self.status == self.get_work_status('분해'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status


            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_gejo', custom_threshold=0)
                self.game_object.get_scene('gejo_scene').status = 0
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

        elif self.status == self.get_work_status('보상'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            pb_name = 'main_scene_menu_open'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('main_scene_menu_bosang', custom_threshold=0)
                self.game_object.get_scene('bosang_scene').status = 0
            else:
                self.lyb_mouse_click('main_scene_menu', custom_threshold=0)

        elif self.status == self.get_work_status('알림'):

            try:
                self.game_object.telegram_send(str(self.get_game_config(lybconstant.LYB_DO_STRING_NOTIFY_MESSAGE)))
                self.status = self.last_status[self.current_work] + 1
            except:
                recovery_count = self.get_option(self.current_work + 'recovery_count')
                if recovery_count is None:
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

        elapsed_time = time.time() - self.get_checkpoint('hp_check')
        if elapsed_time > self.period_bot(5):
            hp = self.player_hp()        
            if hp != None:
                if hp < 50:
                    self.set_checkpoint('hp_check')
                    self.logger.warn('HP: ' + str(hp) + '%')
                    if hp < 20:
                        for i in range(2):
                            pb_name = 'main_scene_quick_slot_return_' + str(i)
                            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                                self.window_image,
                                self.game_object.resource_manager.pixel_box_dic[pb_name],
                                custom_threshold=0.7,
                                custom_flag=1,
                                custom_rect=(600, 260, 750, 320))
                            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                            if loc_x != -1:
                                self.lyb_mouse_click_location(loc_x, loc_y)
                                break 
                    
                    for i in range(2):
                        pb_name = 'main_scene_quick_slot_hp_potion_' + str(i)
                        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                            self.window_image,
                            self.game_object.resource_manager.pixel_box_dic[pb_name],
                            custom_threshold=0.7,
                            custom_flag=1,
                            custom_rect=(600, 260, 750, 320))
                        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                        if loc_x != -1:
                            self.lyb_mouse_click_location(loc_x, loc_y)
                            break
                    
                    for i in range(4):
                        pb_name = 'skill_' + str(i)
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        time.sleep(0.1)

        resource_name = 'skill_vampire_loc'
        elapsed_time = time.time() - self.get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(3):
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.6,
                custom_flag=1,
                custom_rect=(570, 350, 790, 420))
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.set_checkpoint(resource_name)
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

        pb_name = 'main_scene_mana_potion_empty'        
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(3600):
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.set_checkpoint(pb_name)
                self.game_object.get_scene('sangjeom_scene').status = 0
                self.game_object.get_scene('sangjeom_scene').set_option('potion_pb_name', 'sangjeom_scene_mp_potion')
                self.lyb_mouse_click('main_scene_sangjeom', custom_threshold=0)
                return True

        pb_name_list = [
            'main_scene_hp_potion_empty',
            'main_scene_hp_blood_pack_empty',
        ]
        for pb_name in pb_name_list:
            elapsed_time = time.time() - self.get_checkpoint(pb_name)
            if elapsed_time > self.period_bot(3600):
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9:
                    self.set_checkpoint(pb_name)
                    self.game_object.get_scene('sangjeom_scene').status = 0
                    self.game_object.get_scene('sangjeom_scene').set_option('potion_pb_name', 'sangjeom_scene_hp_potion')
                    self.lyb_mouse_click('main_scene_sangjeom', custom_threshold=0)
                    return True

        # pb_name = 'main_scene_gasang_sooryeonjang_loc'
        # elapsed_time = time.time() - self.get_checkpoint(pb_name)
        # if elapsed_time > self.period_bot(30):
        #     (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
        #         self.window_image,
        #         self.game_object.resource_manager.pixel_box_dic[pb_name],
        #         custom_threshold=0.9,
        #         custom_flag=1,
        #         custom_rect=(710, 260, 760, 300))
        #     self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        #     if loc_x != -1:
        #         self.logger.info('가상 수련장')
        #         self.set_checkpoint(pb_name)
        #         self.lyb_mouse_click_location(loc_x, loc_y)
        #         return True

        pb_name = 'main_scene_quick_move'
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(30):
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(480, 330, 520, 370))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.logger.info('즉시이동 클릭')
                self.set_checkpoint(pb_name)
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True

        # '보상'과 '재수락'은 탐색하는 순서 중요
        pb_name = 'main_scene_re'
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(30):
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(280, 330, 350, 360))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.logger.info('재수락 클릭')
                self.set_checkpoint(pb_name)
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True

        # '보상'과 '재수락'은 탐색하는 순서 중요
        pb_name = 'main_scene_quest_bosang'
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(5):
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(460, 330, 500, 360))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.logger.info('보상 클릭')
                self.set_checkpoint(pb_name)
                self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_inner_status', 0)
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True

        pb_name = 'main_scene_equip'
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(30):
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(710, 260, 760, 300))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.logger.info('장착 클릭')
                self.set_checkpoint(pb_name)
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True

        resource_name_list = [
            'main_scene_chatting_ban_loc',
            'main_scene_chatting_send_loc',
        ]
        for resource_name in resource_name_list:
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                pb_name = resource_name.replace('_loc', '', 1) + '_close_icon'
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return True


        if self.isOpenQuickSlot(limit_count=3) == False:
            self.lyb_mouse_click('main_scene_quick_slot', custom_threshold=0)
            return True

        pb_name = 'main_scene_looting'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.9,
            custom_top_level=(255, 255, 255),
            custom_below_level=(100, 100, 100),
            custom_flag=1,
            custom_rect=(180, 450, 230, 480))
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x == -1:           
            # 깜빡일 때 클릭            
            elapsed_time = time.time() - self.get_checkpoint(pb_name)
            if elapsed_time > self.period_bot(10):
                self.set_checkpoint(pb_name)
                self.set_option(pb_name + '_limit', 0)

            limit_count = self.get_option(pb_name + '_limit')
            if limit_count is None:
                limit_count = 0

            if limit_count > 1:
                self.set_checkpoint(pb_name)
                self.set_option(pb_name + '_limit', 0)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.logger.info('줍기 클릭')
                return True

        if self.click_resource('main_scene_tobeol_ipjang_loc') is True:
            return True

        return False

    def is_complete_quest(self, limit=1):
        complete_list = [
            'main_scene_quest_complete',
            'main_scene_quest_kill_loc',
        ]

        for pb_name in complete_list:
            if '_loc' in pb_name:
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    pb_name,
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(5, 150, 170, 350))
            else:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(5, 150, 170, 350))

            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                threshold = self.get_option(pb_name + '_threshold')
                if threshold is None:
                    threshold = 0

                self.logger.info('퀘스트 완료 감지됨: ' + str(threshold) + '/' + str(limit))

                if threshold >= limit:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option(pb_name + '_threshold', 0)

                    return True
                else:
                    self.set_option(pb_name + '_threshold', threshold + 1)
            else:
                self.set_option(pb_name + '_threshold', 0)

        return False

    def is_complete_accept(self, quest_index, limit=1):
        complete_list = [
            'main_scene_quest_accept_loc',
            'main_scene_quest_dehwa_loc',
        ]

        for resource_name in complete_list:
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.65,
                custom_flag=1,
                custom_rect=(5, 150 + (quest_index * 25), 200, 180 + (quest_index * 30)))
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                threshold = self.get_option(resource_name + '_threshold')
                if threshold is None:
                    threshold = 0

                self.logger.info('퀘스트 수락 감지됨: ' + str(threshold) + '/' + str(limit))

                if threshold >= limit:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option(resource_name + '_threshold', 0)

                    return True
                else:
                    self.set_option(resource_name + '_threshold', threshold + 1)
            else:
                self.set_option(resource_name + '_threshold', 0)

        return False

    def get_work_status(self, work_name):
        if work_name in lybgamedarkeden.LYBDarkEden.work_list:
            return (lybgamedarkeden.LYBDarkEden.work_list.index(work_name) + 1) * 1000
        else:
            return 99999

    def end_work(self):
        current_work = self.game_object.get_scene('main_scene').current_work
        if current_work is None:
            return

        self.game_object.get_scene('main_scene').set_option(current_work + '_end_flag', True)


    def isAutoCombat(self, limit_count=-1):
        return self.isStatusByResource(
            '[우측 자동전투 인식 실패 횟수]',
            'main_scene_auto_loc',
            0.5,
            (200, 200, 200), (50, 50, 50),
            (740, 340, 780, 370),
            limit_count=limit_count
        )

    def isAutoCombat2(self, limit_count=-1):
        return self.isStatusByResource(
            '[자동전투 인식 실패 횟수]',
            'combat_scene_auto_loc',
            0.8,
            (200, 200, 200), (50, 50, 50),
            (740, 340, 780, 370),
            limit_count=limit_count
        )

    def isCenterAutoCombat(self, limit_count=-1):
        return self.isStatusByResource(
            '[중앙 자동전투 인식 실패 횟수]',
            'main_scene_center_auto_loc',
            0.5,
            -1, -1,
            (350, 300, 450, 370),
            limit_count=limit_count
        )

    def isOpenQuickSlot(self, limit_count=-1):
        return self.isStatusByResource(
            '[퀵슬롯 닫힘 인식 횟수]',
            'main_scene_quick_slot_config_loc',
            0.8,
            -1, -1,
            (750, 260, 790, 320),
            limit_count=limit_count
        )

    def isStatusByResource(self, log_message, resource_name, custom_threshold, custom_top_level, custom_below_level,
                                   custom_rect, limit_count=-1):
        if limit_count == -1:
            limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'))

        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
            self.window_image,
            resource_name,
            custom_threshold=custom_threshold,
            custom_top_level=custom_top_level,
            custom_below_level=custom_below_level,
            custom_flag=1,
            custom_rect=custom_rect,
            average=True
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

        if check_count > 0:
            self.logger.debug(log_message + '..(' + str(check_count) + '/' + str(limit_count) + ')')
        self.set_option(resource_name + 'check_count', check_count + 1)

        return True

    def drag_quest_list(self):
        s = self.get_option('drag_start_pb_name')
        e = self.get_option('drag_end_pb_name')

        if s is None:
            s = 'main_scene_quest_drag_bot'
        if e is None:
            e = 'main_scene_quest_drag_top'

        self.lyb_mouse_drag(s, e)
        
        self.set_option('drag_start_pb_name', e)
        self.set_option('drag_end_pb_name', s)

        return True

    def player_hp(self):
        return self.horizontal_bar_percent('player_hp_s', 'player_hp_m', 'player_hp_e', adjust=(50, 50, 50))

    # def player_mp(self):
    #   return self.horizontal_bar_percent('player_mp_s', 'player_mp_m', 'player_mp_e', adjust=(50, 50, 50))

    def horizontal_bar_percent(self, hp_s, hp_m, hp_e, ignore_rgb=-1, adjust=(15, 15, 15), adjust_s=(0, 0),
                               adjust_e=(0, 0)):

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
            if abs(hp_rgb[0] - r) < adjust[0] and abs(hp_rgb[1] - g) < adjust[1] and abs(hp_rgb[2] - b) < adjust[2]:
                hp_percent = int(((total_length - j) / total_length) * 100)
                break
            if ignore_rgb != -1:
                if abs(ignore_rgb[0] - r) < adjust[0] and abs(ignore_rgb[1] - g) < adjust[1] and abs(
                                ignore_rgb[2] - b) < adjust[2]:
                    break

            j += 1
            if j > total_length:
                break

        return hp_percent

    def click_resource(self, resource_name):        
        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
            self.window_image,
            resource_name,
            custom_threshold=0.7,
            custom_flag=1)
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.lyb_mouse_click_location(loc_x, loc_y)
            return True
        return False
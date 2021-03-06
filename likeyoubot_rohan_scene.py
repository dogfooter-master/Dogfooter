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
import traceback
import likeyoubot_rohan as lybgamerohan
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time


class LYBRohanScene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)

    def process(self, window_image, window_pixels):

        super(LYBRohanScene, self).process(window_image, window_pixels)

        rc = 0
        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'character_scene':
            rc = self.character_scene()
        elif self.scene_name == 'jeoljeon_scene':
            rc = self.jeoljeon_scene()
        elif self.scene_name == 'bunhe_select_scene':
            rc = self.bunhe_select_scene()
        elif self.scene_name == 'japhwajeom_scene':
            rc = self.japhwajeom_scene()
        elif self.scene_name == 'japhwajeom_popup_scene':
            rc = self.japhwajeom_popup_scene()
        elif self.scene_name == 'event_scene':
            rc = self.event_scene()
        elif self.scene_name == 'guild_scene':
            rc = self.guild_scene()
        elif self.scene_name == 'amsijang_scene':
            rc = self.amsijang_scene()
        elif self.scene_name == 'costume_scene':
            rc = self.costume_scene()
        elif self.scene_name == 'quest_scene':
            rc = self.quest_scene()
        elif self.scene_name == 'georeso_scene':
            rc = self.georeso_scene()
        elif self.scene_name == 'rune_scene':
            rc = self.rune_scene()

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

    def rune_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def georeso_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('not_found', 0)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'georeso_scene_tab_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(60, 60, 600, 110))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.set_option('last_status', self.status)
                    self.status = 10
                    return self.status

            not_found = self.get_option('not_found')
            if not_found > 1:
                self.status = 99999
            else:
                self.set_option('not_found', not_found + 1)
        elif 10 <= self.status < 20:
            self.status += 1
            resource_name = 'georeso_scene_jeongsan_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.6,
                custom_flag=1,
                custom_rect=(480, 140, 580, 240),
                average=True
            )
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status
            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def quest_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('not_found', 0)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'quest_scene_tab_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(60, 60, 600, 110))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.set_option('last_status', self.status)
                    self.status = 10
                    return self.status

            not_found = self.get_option('not_found')
            if not_found > 1:
                self.status = 99999
            else:
                self.set_option('not_found', not_found + 1)
        elif 10 <= self.status < 20:
            self.status += 1
            resource_name = 'quest_scene_bosang_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.6,
                custom_top_level=(255, 255, 255),
                custom_below_level=(0, 0, 230),
                custom_flag=1,
                custom_rect=(680, 110, 780, 460),
                average=True
            )
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            resource_name = 'quest_scene_bosang_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.6,
                custom_top_level=(255, 255, 255),
                custom_below_level=(0, 0, 230),
                custom_flag=1,
                custom_rect=(320, 110, 400, 460),
                average=True
            )
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            resource_name = 'quest_scene_bosang_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(140, 120, 790, 170))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
                    return self.status

            resource_name = 'quest_scene_side_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(100, 115, 140, 470))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    return self.status

            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def costume_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'costume_scene_side_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(110, 110, 170, 340))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.set_option('last_status', self.status)
                    self.status = 20
                    return self.status
            self.status = 99999
        elif 20 <= self.status < 30:
            self.status += 1
            resource_name = 'costume_scene_dogam_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(420, 120, 470, 190))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 5, loc_y + 15)
                    self.status = self.get_option('last_status')
                    return self.status
            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def amsijang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'amsijang_scene_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(110, 120, 170, 340))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.set_option('last_status', self.status)
                    self.status = 20
                    return self.status
            self.status = 99999
        elif 20 <= self.status < 30:
            self.status += 1
            pb_name = 'amsijang_free_refresh'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click('amsijang_free_refresh', custom_threshold=0)
                self.status = self.get_option('last_status')
                return self.status

            resource_name = 'amsijang_free_upgrade_go_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            if match_rate > 0.9:
                self.click_resource2('amsijang_free_upgrade_go_loc', custom_threshold=0)
                return self.status

            resource_name = 'amsijang_free_upgrade_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            if match_rate > 0.9:
                self.lyb_mouse_click('amsijang_free_upgrade_item', custom_threshold=0)
                return self.status

            resource_name = 'amsijang_free_gotcha_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(160, 400, 780, 460))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.status = self.get_option('last_status')
                    return self.status
            self.status = self.get_option('last_status')
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
            self.lyb_mouse_click('guild_scene_check', custom_threshold=0)
            self.status += 1
        elif 2 <= self.status < 5:
            self.status += 1
        elif 5 <= self.status < 15:
            self.status += 1
            is_clicked, match_rate = self.click_resource2('guild_scene_gift_new_loc')
            if is_clicked is True:
                self.status = 15
        elif self.status == 15:
            # 기부
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
            self.status += 1
            resource_name = 'event_scene_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(120, 70, 170, 180))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.set_option('last_status', self.status)
                    self.status = 20
                    return self.status
            self.status = 99999
        elif 20 <= self.status < 30:
            self.status += 1
            resource_name = 'event_scene_bosang_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.6,
                    custom_flag=1,
                    custom_rect=(170, 360, 790, 460))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status
            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def japhwajeom_popup_scene(self):
        self.game_object.current_matched_scene['name'] = ''

        if self.status == 0:
            self.game_object.get_scene('japhwajeom_scene').status = 99999
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 5:
            self.lyb_mouse_click('japhwajeom_scene_numpad_100', custom_threshold=0)
            self.status = 5
        elif 5 <= self.status < 10:
            pb_name = 'japhwajeom_scene_numpad'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click('japhwajeom_scene_numpad_confirm', custom_threshold=0)
                self.status += 1
            else:
                self.status = 10
        elif 10 <= self.status < 15:
            pb_name = 'japhwajeom_scene_buy_title'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click('japhwajeom_scene_buy', custom_threshold=0)
                self.status += 1
            else:
                self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def japhwajeom_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.game_object.get_scene('japhwajeom_popup_scene').status = 0
            potion_pb_name = self.get_option('potion_name')
            if potion_pb_name is None:
                potion_pb_name = 'japhwajeom_scene_hp_potion'

            self.lyb_mouse_click(potion_pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 10:
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def bunhe_select_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 0 < self.status < 10:
            self.status += 1
            resource_name = 'bunhe_scene_option_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            i = 0
            for pb_name in resource:
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                cfg_check = self.get_game_config(lybconstant.LYB_DO_STRING_ROHAN_WORK + 'bunhe_item_option_' + str(i))
                if cfg_check is True and match_rate > 0.9:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return self.status
                elif cfg_check is False and match_rate < 0.9:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return self.status
                i += 1
            self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0
        return self.status

    def jeoljeon_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 0 < self.status < 6000:
            self.status += 1
            # elapsed_time = self.get_elapsed_time()
            # self.logger.info(str(elapsed_time))
            if self.is_jeoljeon_hp_empty():
                self.game_object.get_scene('main_scene').set_option('hp_potion_empty', True)
                self.status = 99999
            if self.is_jeoljeon_mp_empty():
                self.game_object.get_scene('main_scene').set_option('mp_potion_empty', True)
                self.status = 99999
            if self.is_jeoljeon_quest_complete():
                self.game_object.get_scene('main_scene').set_option('quest_complete', True)
                self.status = 99999

            current_work = self.game_object.get_scene('main_scene').current_work
            if current_work == '자동 사냥':
                cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ROHAN_WORK + 'auto_duration'))
                elapsed_time = time.time() - self.game_object.get_scene('main_scene').get_checkpoint(current_work + '_check_start')
                self.loggingElapsedTime('[' + str(current_work) + '] 경과 시간', elapsed_time, cfg_duration, period=30)
                if elapsed_time > self.period_bot(cfg_duration):
                    self.status = 99999
                    self.game_object.get_scene('main_scene').set_option(current_work + '_end_flag', True)
        else:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.game_object.interval = self.period_bot(0.1)
        return self.status

    def character_scene(self):
        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('character_scene_enter', custom_threshold=0)
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
            for each_icon in lybgamerohan.LYBRohan.rohan_icon_list:
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
            for each_icon in lybgamerohan.LYBRohan.rohan_icon_list:
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
        self.game_object.current_matched_scene['name'] = ''
        self.schedule_list = self.get_game_config('schedule_list')

        if '로그인' not in self.schedule_list:
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
        elif 2 <= self.status < 6:
            self.status += 1
        elif self.status == 6:
            self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
            self.status += 1
        elif 7 <= self.status < 10:
            self.status += 1
        elif 10 <= self.status < 70:
            self.logger.info('로그인 화면 랙 인식: ' + str(self.status - 10) + '/60')
            if self.status % 10 == 0:
                self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
            self.status += 1
        elif self.status == 70:
            self.game_object.terminate_application()
            self.status += 1
        else:
            self.status = 0

        return self.status

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
        if is_clicked is True:
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

            cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ROHAN_WORK + 'main_quest_duration'))

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(cfg_duration):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            if self.is_complete_quest():
                return True

            if self.is_move_to_quest():
                return True

        elif self.status == self.get_work_status('자동 사냥'):

            cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ROHAN_WORK + 'auto_duration'))

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(cfg_duration):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.loggingElapsedTime('[' + str(self.current_work) + '] 경과 시간', elapsed_time, cfg_duration, period=60)

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status is None:
                inner_status = 0

            if 0 <= inner_status <= 240:
                if self.is_menu_open():
                    self.game_object.get_scene('jeoljeon_scene').status = 0
                    self.lyb_mouse_click('menu_jeoljeon', custom_threshold=0)
                else:
                    self.lyb_mouse_click('main_scene_menu', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)

        elif self.status == self.get_work_status('분해'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(30):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status is None:
                inner_status = 0

            self.logger.info(inner_status)
            if 0 <= inner_status < 100:
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
                if self.is_gabang_open():
                    self.lyb_mouse_click('gabang_bunhe', custom_threshold=0)
                else:
                    if self.is_gabang_select():
                        self.lyb_mouse_click('gabang_select', custom_threshold=0)
                        self.game_object.get_scene('bunhe_select_scene').status = 0
                        self.set_option(self.current_work + '_inner_status', 100)
                    else:
                        self.lyb_mouse_click('menu_scene_gabang', custom_threshold=0)
            elif 100 <= inner_status < 102:
                self.lyb_mouse_click('gabang_select_ok', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 102 <= inner_status < 110:
                if self.is_gabang_open():
                    self.lyb_mouse_click('gabang_close', custom_threshold=0)
                    self.set_option(self.current_work + '_end_flag', True)
                    return self.status

                self.lyb_mouse_click('gabang_select_cancel', custom_threshold=0)
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

        if self.get_option('hp_potion_empty') is True:
            self.set_option('hp_potion_empty', False)
            self.lyb_mouse_click('main_scene_shop', custom_threshold=0)
            self.game_object.get_scene('japhwajeom_scene').status = 0
            self.game_object.get_scene('japhwajeom_scene').set_option('potion_name', 'japhwajeom_scene_hp_potion')
            return True

        if self.get_option('mp_potion_empty') is True:
            self.set_option('mp_potion_empty', False)
            self.lyb_mouse_click('main_scene_shop', custom_threshold=0)
            self.game_object.get_scene('japhwajeom_scene').status = 0
            self.game_object.get_scene('japhwajeom_scene').set_option('potion_name', 'japhwajeom_scene_mp_potion')
            return True

        if self.is_there_mail() is True:
            if self.click_resource2('main_scene_mail_receive_loc') is True:
                return True

        if self.is_there_new_event() is True:
            if self.click_resource2('main_scene_event_new_loc') is True:
                self.game_object.get_scene('event_scene').status = 0
                return True

        if self.is_there_new_menu() is True:
            if self.is_menu_open() is True:
                resource_name = 'menu_new_loc'
                resource = self.game_object.resource_manager.resource_dic[resource_name]
                for pb_name in resource:
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.6,
                        custom_flag=1,
                        custom_rect=(540, 80, 795, 385))
                    self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
                        self.init_menu_scene()
                        return True
            else:
                if self.click_resource2('menu_new_loc') is True:
                    self.game_object.get_scene('event_scene').status = 0
                    return True

        return False

    def init_menu_scene(self):
        self.game_object.get_scene('guild_scene').status = 0
        self.game_object.get_scene('amsijang_scene').status = 0

    def get_work_status(self, work_name):
        if work_name in lybgamerohan.LYBRohan.work_list:
            return (lybgamerohan.LYBRohan.work_list.index(work_name) + 1) * 1000
        else:
            return 99999

    def click_resource(self, resource_name, custom_threshold=0.7, near=32):
        isMatched, rate = self.click_resource2(resource_name, custom_threshold=custom_threshold, near=near)

        return isMatched

    def click_resource2(self, resource_name, custom_threshold=0.7, near=32):
        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart2(
            self.window_image,
            resource_name,
            custom_threshold=custom_threshold,
            near=near,
            debug=True,
            custom_flag=1)
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.lyb_mouse_click_location(loc_x, loc_y)
            return True, match_rate

        return False, match_rate

    def is_complete_quest(self, limit=3):
        complete_list = [
            'quest_complete_loc',
        ]

        for pb_name in complete_list:
            if '_loc' in pb_name:
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    pb_name,
                    custom_threshold=0.1,
                    custom_flag=1,
                    custom_top_level=(255, 255, 10),
                    custom_below_level=(125, 90, 0),
                    custom_rect=(10, 160, 40, 300),
                    average=True,
                )
            else:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.1,
                    custom_flag=1,
                    custom_top_level=(255, 255, 10),
                    custom_below_level=(125, 90, 0),
                    custom_rect=(10, 160, 40, 300),
                )

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

    def is_move_to_quest(self, limit=3):
        complete_list = [
            'quest_move_loc',
        ]

        for pb_name in complete_list:
            if '_loc' in pb_name:
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    pb_name,
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(150, 120, 230, 180),
                )

            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                threshold = self.get_option(pb_name + '_threshold')
                if threshold is None:
                    threshold = 0

                self.logger.info('즉시 이동 감지됨: ' + str(threshold) + '/' + str(limit))

                if threshold >= limit:
                    temp_loc_x = loc_x - 100
                    if temp_loc_x <= 50:
                        temp_loc_x = 50
                    self.lyb_mouse_click_location(temp_loc_x, loc_y)
                    self.set_option(pb_name + '_threshold', 0)

                    return True
                else:
                    self.set_option(pb_name + '_threshold', threshold + 1)
            else:
                self.set_option(pb_name + '_threshold', 0)

        return False

    def is_there_new_menu(self):
        return self.is_status_by_resource2('메뉴 알림 감지', 'menu_new_loc', 0.6, 0, reverse=True)

    def is_there_new_event(self):
        return self.is_status_by_resource2('Event 알림 감지', 'main_scene_event_new_loc', 0.6, 0, reverse=True)

    def is_gabang_select(self):
        return self.is_status_by_resource2('일괄 선택 감지', 'gabang_select_loc', 0.7, -1, reverse=True)

    def is_gabang_open(self):
        return self.is_status_by_resource2('가방 열림 감지', 'gabang_open_loc', 0.7, -1, reverse=True)

    def is_there_mail(self):
        return self.is_status_by_resource2('우편 받기 감지', 'main_scene_mail_receive_loc', 0.7, -1, reverse=True)

    def is_menu_open(self):
            return self.is_status_by_resource(
                '[메뉴 열림 감지]',
                'menu_open_loc',
                custom_top_level=(255, 250, 210),
                custom_below_level=(140, 130, 100),
                custom_rect=(740, 60, 790, 100),
                custom_threshold=0.8,
                limit_count=-1,
                reverse=True,
            )

    def is_jeoljeon_mp_empty(self):
        return self.is_status_by_resource2('절전모드 MP 포션 부족 감지', 'jeoljeon_scene_mp_potion_empty_loc', 0.95, 2, reverse=True)

    def is_jeoljeon_hp_empty(self):
        return self.is_status_by_resource2('절전모드 HP 포션 부족 감지', 'jeoljeon_scene_hp_potion_empty_loc', 0.95, 2, reverse=True)

    def is_jeoljeon_quest_complete(self):
        return self.is_status_by_resource2('절전모드 퀘스트 완료 감지', 'jeoljeon_scene_quest_complete_loc', 0.9, 3, reverse=True)

    def is_status_by_resource(self, log_message, resource_name, custom_threshold, custom_top_level, custom_below_level,
                           custom_rect, limit_count=-1, reverse=False):
        # if limit_count == -1:
        #     limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'))

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
        # self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1 and reverse == False:
            self.set_option(resource_name + 'check_count', 0)
            return False

        if loc_x == -1 and reverse == True:
            self.set_option(resource_name + 'check_count', 0)
            return False

        check_count = self.get_option(resource_name + 'check_count')
        if check_count is None:
            check_count = 0

        if check_count > limit_count:
            self.set_option(resource_name + 'check_count', 0)
            return True

        if check_count > 0:
            self.logger.debug(log_message + '..(' + str(check_count) + '/' + str(limit_count) + ')')
        self.set_option(resource_name + 'check_count', check_count + 1)

        return False

    def is_status_by_resource2(self, log_message, resource_name, custom_threshold, limit_count=-1, reverse=False):
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > custom_threshold and reverse == False:
            self.set_option(resource_name + 'check_count', 0)
            return False

        if match_rate < custom_threshold and reverse == True:
            self.set_option(resource_name + 'check_count', 0)
            return False

        check_count = self.get_option(resource_name + 'check_count')
        if check_count is None:
            check_count = 0

        if check_count > limit_count:
            self.set_option(resource_name + 'check_count', 0)
            return True

        if check_count > 0:
            self.logger.debug(log_message + '..(' + str(check_count) + '/' + str(limit_count) + ')')
        self.set_option(resource_name + 'check_count', check_count + 1)

        return False

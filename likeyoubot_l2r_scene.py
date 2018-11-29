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
import likeyoubot_l2r as lybgamel2r
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time


class LYBL2rScene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)

    def process(self, window_image, window_pixels):

        super(LYBL2rScene, self).process(window_image, window_pixels)

        rc = 0
        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'google_play_store_scene':
            rc = self.google_play_store_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'bosang_scene':
            rc = self.bosang_scene()
        elif self.scene_name == 'onulhwaldong_scene':
            rc = self.onulhwaldong_scene()
        elif self.scene_name == 'sangjeom_scene':
            rc = self.sangjeom_scene()
        elif self.scene_name == 'omantap_scene':
            rc = self.omantap_scene()
        elif self.scene_name == 'ilil_quest_scene':
            rc = self.ilil_quest_scene()
        elif self.scene_name == 'jugan_quest_scene':
            rc = self.jugan_quest_scene()
        elif self.scene_name == 'quest_scroll_scene':
            rc = self.quest_scroll_scene()
        elif self.scene_name == 'quest_scroll_limit_scene':
            rc = self.quest_scroll_limit_scene()
        elif self.scene_name == 'npc_talk_scene':
            rc = self.npc_talk_scene()
        elif self.scene_name == 'yoil_dungeon_scene':
            rc = self.yoil_dungeon_scene()
        elif self.scene_name == 'social_scene':
            rc = self.social_scene()
        elif self.scene_name == 'dungeon_list_scene':
            rc = self.dungeon_list_scene()
        elif self.scene_name == 'gabang_scene':
            rc = self.gabang_scene()
        elif self.scene_name == 'gyeoltoojang_scene':
            rc = self.gyeoltoojang_scene()
        elif self.scene_name == 'hyeolmeng_scene':
            rc = self.hyeolmeng_scene()
        elif self.scene_name == 'hyeolmeng_chulseok_check_scene':
            rc = self.hyeolmeng_chulseok_check_scene()
        elif self.scene_name == 'azit_scene':
            rc = self.azit_scene()
        elif self.scene_name == 'azit_manmulsang_scene':
            rc = self.azit_manmulsang_scene()
        elif self.scene_name == 'hyeolmeng_give_scene':
            rc = self.hyeolmeng_give_scene()
        elif self.scene_name == 'mail_scene':
            rc = self.mail_scene()
        elif self.scene_name == 'jeongye_dungeon_scene':
            rc = self.jeongye_dungeon_scene()
        elif self.scene_name == 'jangbi_dungeon_scene':
            rc = self.jangbi_dungeon_scene()
        elif self.scene_name == 'jadong_chamga_scene':
            rc = self.jadong_chamga_scene()
        elif self.scene_name == 'adena_dungeon_scene':
            rc = self.adena_dungeon_scene()
        elif self.scene_name == 'bosang_hesu_scene':
            rc = self.bosang_hesu_scene()
        elif self.scene_name == 'dungeon_clear_scene':
            rc = self.dungeon_clear_scene()
        elif self.scene_name == 'dungeon_clear_2_scene':
            rc = self.dungeon_clear_scene()
        elif self.scene_name == 'dungeon_clear_3_scene':
            rc = self.dungeon_clear_scene()
        elif self.scene_name == 'experience_dungeon_scene':
            rc = self.experience_dungeon_scene()
        elif self.scene_name == 'sohwanseok_dungeon_scene':
            rc = self.sohwanseok_dungeon_scene()





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

    def sohwanseok_dungeon_scene(self):

        pb_name = 'bosang_hesu'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(560, 70, 620, 120)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.game_object.get_scene('bosang_hesu_scene').status = 0
            self.lyb_mouse_click_location(loc_x, loc_y)
            return self.status

        pb_name = 'sohwanseok_dungeon_scene_limit'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.9:
            self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 7:
            pb_name = 'sohwanseok_dungeon_scene_difficulty_list_' + str(6 - self.status)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option('last_status', self.status + 1)
            self.status = 10
        elif self.status == 7:
            self.set_option('last_status', 99999)
            self.status = 10
        elif self.status == 10:
            pb_name = 'sohwanseok_dungeon_scene_green'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status += 1
            else:
                self.status = self.get_option('last_status')
        elif self.status >= 11 and self.status < 14:
            self.lyb_mouse_click('sohwanseok_dungeon_scene_ipjang', custom_threshold=0)
            self.status += 1
        elif self.status == 14:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def experience_dungeon_scene(self):

        pb_name = 'bosang_hesu'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(560, 70, 620, 120)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.game_object.get_scene('bosang_hesu_scene').status = 0
            self.lyb_mouse_click_location(loc_x, loc_y)
            return self.status

        pb_name = 'experience_dungeon_scene_limit'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.9:
            self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 8:
            pb_name = 'experience_dungeon_scene_difficulty_list_' + str(7 - self.status)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option('last_status', self.status + 1)
            self.status = 10
        elif self.status == 8:
            self.set_option('last_status', 99999)
            self.status = 10
        elif self.status == 10:
            pb_name = 'experience_dungeon_scene_green'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status += 1
            else:
                self.status = self.get_option('last_status')
        elif self.status >= 11 and self.status < 14:
            self.lyb_mouse_click('experience_dungeon_scene_ipjang', custom_threshold=0)
            self.status += 1
        elif self.status == 14:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def dungeon_clear_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def bosang_hesu_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('bosang_hesu_scene_gold', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def adena_dungeon_scene(self):

        pb_name = 'bosang_hesu'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(560, 70, 620, 120)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.game_object.get_scene('bosang_hesu_scene').status = 0
            self.lyb_mouse_click_location(loc_x, loc_y)
            return self.status

        pb_name = 'adena_dungeon_scene_limit'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 7:
            pb_name = 'adena_dungeon_scene_difficulty_list_' + str(6 - self.status)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option('last_status', self.status + 1)
            self.status = 10
        elif self.status == 7:
            self.set_option('last_status', 99999)
            self.status = 10
        elif self.status == 10:
            pb_name = 'adena_dungeon_scene_green'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status += 1
            else:
                self.status = self.get_option('last_status')
        elif self.status >= 11 and self.status < 14:
            self.lyb_mouse_click('adena_dungeon_scene_ipjang', custom_threshold=0)
            self.status += 1
        elif self.status == 14:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

        return self.status

    def jadong_chamga_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 300:
            if self.status % 10 == 0:
                self.logger.info('자동 참가 대기 중...(' + str(self.status) + '/300)')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jangbi_dungeon_scene(self):

        # pb_name = 'yoil_dungeon_scene_free_sotang'
        # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # if match_rate > 0.9:	
        # 	self.lyb_mouse_click(pb_name)
        # 	return self.status

        # pb_name = 'yoil_dungeon_scene_sotang_cancel'
        # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # if match_rate > 0.9:	
        # 	self.lyb_mouse_click(pb_name)
        # 	return self.status

        pb_name = 'bosang_hesu'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(560, 70, 620, 120)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.game_object.get_scene('bosang_hesu_scene').status = 0
            self.lyb_mouse_click_location(loc_x, loc_y)
            return self.status

        pb_name = 'jangbi_dungeon_scene_limit'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 8:
            pb_name = 'jangbi_dungeon_scene_difficulty_list_' + str(7 - self.status)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option('last_status', self.status + 1)
            self.status = 10
        elif self.status == 8:
            self.set_option('last_status', 99999)
            self.status = 10
        elif self.status == 10:
            pb_name = 'jangbi_dungeon_scene_green'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status += 1
            else:
                self.status = self.get_option('last_status')
        elif self.status >= 11 and self.status < 14:
            self.lyb_mouse_click('jangbi_dungeon_scene_ipjang', custom_threshold=0)
            self.status += 1
        elif self.status == 14:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jeongye_dungeon_scene(self):

        pb_name = 'jeongye_dungeon_scene_bosang_5'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.95:
            self.lyb_mouse_click('jeongye_dungeon_scene_bosang', custom_threshold=0)
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('row', 0)
            self.set_option('drag_count', 0)
            self.status += 1
        elif self.status >= 1 and self.status < 3:
            self.lyb_mouse_drag('jeongye_dungeon_scene_drag_top', 'jeongye_dungeon_scene_drag_bot')
            self.status += 1
        elif self.status == 3:
            row = self.get_option('row')
            if row >= 3:
                self.set_option('row', 0)
                self.set_option('last_status', self.status)
                self.status = 10
                return self.status

            pb_name = 'jeongye_dungeon_scene_lock'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(30, 130 + (60 * row) - 70, 70, 130 + (60 * row) + 70)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.status = 99999
                return self.status

            resource_name = 'jeongye_dungeon_scene_need_loc'
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_top_level=(120, 135, 150),
                custom_below_level=(60, 80, 100),
                custom_flag=1,
                custom_rect=(30, 130 + (60 * row) - 70, 300, 130 + (60 * row) + 70)
            )
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.set_option('last_status', self.status)
                self.status += 1

            self.set_option('row', row + 1)
        elif self.status >= 4 and self.status < 10:
            self.status += 1

            pb_name = 'jeongye_dungeon_scene_available'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate < 0.9:
                self.status = self.get_option('last_status')
                return self.status

            pb_name = 'jeongye_dungeon_scene_ipjang'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.set_option('row', 0)
                return self.status
        elif self.status == 10:
            drag_count = self.get_option('drag_count')
            if drag_count > 2:
                self.status = 99999
                return self.status

            self.set_option('drag_count', drag_count + 1)
            self.lyb_mouse_drag('jeongye_dungeon_scene_drag_bot', 'jeongye_dungeon_scene_drag_top', stop_delay=1)
            self.status += 1
        elif self.status == 11:
            self.status = self.get_option('last_status')
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def mail_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 10:
            for i in range(3):
                pb_name = 'mail_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(90, 60, 350, 100)
                )
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.status += 1
                    self.set_option('last_status', self.status)
                    self.status += 10
                    return self.status
            self.status = 10
        elif self.status == 10:
            self.status = 99999
        elif self.status >= 11 and self.status < 20:
            self.lyb_mouse_click('mail_scene_receive_all', custom_threshold=0)
            self.status = self.get_option('last_status')
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def hyeolmeng_give_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('hyeolmeng_give_scene_give', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def azit_manmulsang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('azit_manmulsang_scene_gift')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def azit_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 3:
            self.status += 1
            pb_name = 'azit_scene_new'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(600, 320, 635, 370)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.game_object.get_scene('main_scene').set_option('from_azit_scene', True)
                self.game_object.get_scene('azit_manmulsang_scene').status = 0
            else:
                self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def hyeolmeng_chulseok_check_scene(self):

        self.lyb_mouse_click('hyeolmeng_chulseok_check_scene_bosang', custom_threshold=0)

        return self.status

    def hyeolmeng_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('hyeolmeng_scene_tab_0', custom_threshold=0)
            self.status += 1
        elif self.status == 2:
            for i in range(4):
                pb_name = 'hyeolmeng_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(280, 70, 635, 370)
                )
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.game_object.get_scene('azit_scene').status = 0
                    self.game_object.get_scene('hyeolmeng_give_scene').status = 0
                    self.status += 1
                    return self.status

            self.status = 99999
        elif self.status == 3:
            for i in range(4):
                pb_name = 'hyeolmeng_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(480, 340, 560, 380)
                )
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            self.status = 1
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gyeoltoojang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 10:
            self.status += 1
            pb_name = 'gyeoltoojang_scene_limit'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.status = 10
                return self.status

            pb_name = 'gyeoltoojang_scene_bosang'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(20, 270, 160, 320)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            pb_name = 'gyeoltoojang_scene_sijak'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(540, 110, 630, 370)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            self.status += 1
        elif self.status == 10:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gabang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 10:
            self.status += 1
            pb_name = 'gabang_scene_limit'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.status = 10
                return self.status

            pb_name = 'gabang_scene_sell_all'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            pb_name = 'gabang_scene_sell'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

        elif self.status == 10:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def dungeon_list_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0

        return self.status

    def social_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 3:
            pb_name = 'social_scene_new'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(460, 340, 560, 380)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            self.status += 1
        elif self.status == 3:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def yoil_dungeon_scene(self):

        pb_name = 'yoil_dungeon_scene_free_sotang'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name)
            return self.status

        pb_name = 'yoil_dungeon_scene_sotang_cancel'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name)
            return self.status

        pb_name = 'yoil_dungeon_scene_limit'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 8:
            pb_name = 'yoil_dungeon_scene_difficulty_list_' + str(7 - self.status)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option('last_status', self.status + 1)
            self.status = 10
        elif self.status == 8:
            self.set_option('last_status', 99999)
            self.status = 10
        elif self.status == 10:
            pb_name = 'yoil_dungeon_scene_green'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('yoil_dungeon_scene_sotang', custom_threshold=0)
                self.status += 1
            else:
                self.status = self.get_option('last_status')
        elif self.status >= 11 and self.status < 14:
            self.lyb_mouse_click('yoil_dungeon_scene_ipjang', custom_threshold=0)
            self.status += 1
        elif self.status == 14:
            self.status = 99999
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def npc_talk_scene(self):

        match_rate = self.game_object.rateMatchedResource(self.window_pixels, self.scene_name)
        if match_rate < 0.9:
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def quest_scroll_limit_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('limit', True)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def quest_scroll_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            pb_name = 'quest_scroll_scene_do'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.status = 0
                return self.status

            self.lyb_mouse_click('quest_scroll_scene_list_0', custom_threshold=0)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jugan_quest_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 5:
            self.status += 1

            pb_name_list = [
                'jugan_quest_scene_do',
                'jugan_quest_scene_move',
                'jugan_quest_scene_complete',
            ]
            for pb_name in pb_name_list:
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return self.status

        elif self.status == 5:
            for i in range(7):
                self.lyb_mouse_click('jugan_quest_scene_progress_bosang_' + str(i), custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def ilil_quest_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 5:
            self.status += 1
            for i in range(3):
                pb_name = 'ilil_quest_scene_bosang_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(120, 240, 630, 300)
                )
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

            for i in range(3):
                pb_name = 'ilil_quest_scene_do_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(120, 240, 630, 300)
                )
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return self.status

        elif self.status == 5:
            for i in range(2):
                self.lyb_mouse_click('ilil_quest_scene_progress_bosang_' + str(i), custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def omantap_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            pb_name = 'omantap_scene_auto_next'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate < 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status

            pb_name = 'omantap_scene_limit'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('omantap_scene_sotang', custom_threshold=0)
                self.status = 99998
                return self.status

            self.lyb_mouse_click('omantap_scene_enter', custom_threshold=0)
        elif self.status == 99998:
            self.status += 1
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def sangjeom_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.status += 1
        elif self.status == 2:
            pb_name = 'sangjeom_scene_ilban'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status = 1
                return self.status

            for i in range(2):
                pb_name = 'sangjeom_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(90, 100, 125, 380)
                )
                self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.status += 1
                    return self.status

            self.status = 99999
        elif self.status == 3:
            self.status += 1
        elif self.status == 4:
            for i in range(2):
                pb_name = 'sangjeom_scene_inner_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(125, 190, 630, 220)
                )
                self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.game_object.get_scene('onulhwaldong_scene').set_option('activity_completed', True)
                    return self.status

                pb_name = 'sangjeom_scene_inner_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(125, 325, 630, 355)
                )
                self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.game_object.get_scene('onulhwaldong_scene').set_option('activity_completed', True)
                    return self.status

            self.status = 1
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def onulhwaldong_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('quest_index', 0)
            self.status += 1
        elif self.status == 1:
            pb_name = 'onulhwaldong_scene_bosang'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(20, 240, 630, 270)
            )
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            quest_index = self.get_option('quest_index')
            pb_name = 'onulhwaldong_scene_sugeng'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(20 + (155 * quest_index), 240, 170 + (155 * quest_index), 270)
            )
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.game_object.get_scene('sangjeom_scene').status = 0
                self.game_object.get_scene('omantap_scene').status = 0
                self.game_object.get_scene('yoil_dungeon_scene').status = 0
                self.game_object.get_scene('gyeoltoojang_scene').status = 0
                self.game_object.get_scene('social_scene').status = 0
                self.game_object.get_scene('ilil_quest_scene').status = 0
                self.game_object.get_scene('jugan_quest_scene').status = 0
                self.game_object.get_scene('jeongye_dungeon_scene').status = 0
                self.set_option('activity_completed', False)
                self.status += 1
            else:
                self.status = 99999
        elif self.status >= 2 and self.status < 5:
            self.status += 1
        elif self.status == 5:
            quest_index = self.get_option('quest_index')

            if self.get_option('activity_completed') == False:
                if quest_index >= 3:
                    self.set_option('quest_index', 0)
                else:
                    self.set_option('quest_index', quest_index + 1)

            for i in range(3):
                pb_name = 'onulhwaldong_scene_progress_bosang_' + str(i)
                self.lyb_mouse_click(pb_name, custom_threshold=0)

            self.status = 1
        else:
            if self.game_object.get_scene('main_scene').current_work == '메인 퀘스트':
                self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_end_flag', True)

            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def bosang_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.status += 1
        elif self.status == 2:
            for i in range(4):
                pb_name = 'bosang_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(145, 80, 190, 350))
                self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.logger.info('보상 알림 감지')
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.status += 1
                    return self.status
            self.status = 99999
        elif self.status == 3:
            self.status += 1
        elif self.status == 4:
            pb_name = 'bosang_scene_bosang'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
            else:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status = 1
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
            if self.status % 5 == 0:
                self.lyb_mouse_click('login_scene_touch', custom_threshold=0)
            self.logger.info('로그인 화면 랙 인식: ' + str(self.status) + '/30')
            self.status += 1
        elif self.status == 30:
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
            for each_icon in lybgamel2r.LYBL2r.l2r_icon_list:
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
        elif self.game_object.player_type == 'momo':
            for each_icon in lybgamel2r.LYBL2r.l2r_icon_list:
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

    #########################################
    #										#
    #										#
    #				MAIN 					#
    #										#
    #										#
    #########################################


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

            elapsed_time = self.get_elapsed_time()
            cfg_main_quest_duration = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration'))

            if elapsed_time > self.period_bot(cfg_main_quest_duration):
                self.set_option(self.current_work + '_end_flag', True)
            else:
                self.loggingElapsedTime("[메인 퀘스트] 작업 경과 시간", elapsed_time, cfg_main_quest_duration, period=10)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status == None:
                inner_status = 0

            if inner_status == 0:
                self.game_object.get_scene('quest_scroll_limit_scene').set_option('limit', False)
                self.set_option(self.current_work + '_inner_status', 10)
            else:
                if self.isAutoMainQuest() == True:
                    return self.status
                else:
                    if self.main_scene_process_main_quest() == True:
                        return self.status
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

        pb_name_list = [
            'main_scene_base_open',
            'main_scene_base_close'
        ]

        is_field = False
        for pb_name in pb_name_list:
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                is_field = True
                break

        # 던전 진행 중인 경우
        # 1. [던전] 퀘스트
        # 2. 요일 던전 - 제한 시간

        if is_field == False:
            self.logger.debug('not field')

            # [던전] 퀘스트는 60초마다 눌러주고...
            elapsed_time = time.time() - self.get_checkpoint(pb_name + '_last_clicked')
            if elapsed_time > 60:
                pb_name = 'main_scene_quest_dungeon'
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_top_level=(250, 80, 115),
                    custom_below_level=(145, 50, 60),
                    custom_flag=1,
                    custom_rect=(5, 95, 140, 240)
                )
                # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_checkpoint(pb_name + '_last_clicked')
                    return True

            # 던전에 더 이상 할 게 없다면...
            if self.main_scene_is_dungeon() == False:
                check_count = self.get_option(pb_name + '_check')
                if check_count == None:
                    check_count = 0

                self.logger.debug('던전 나가기 체크...(' + str(check_count) + '/3)')
                if check_count > 2:
                    pb_name = 'main_scene_out'
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_top_level=(255, 255, 255),
                        custom_below_level=(190, 190, 190),
                        custom_rect=(400, 50, 540, 90)
                    )
                    self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        self.set_option(pb_name + '_check', 0)
                        return True

                self.set_option(pb_name + '_check', check_count + 1)
            else:
                self.set_option(pb_name + '_check', 0)

        cfg_lag_check_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period'))
        if cfg_lag_check_period != 0:
            elapsed_time = time.time() - self.get_checkpoint('last_lag_check')
            if elapsed_time > cfg_lag_check_period:
                random_direction = int(random.random() * 8)
                self.logger.warn('랙 방지 움직임: ' + str(lybgamel2r.LYBL2r.character_move_list[random_direction]))
                self.lyb_mouse_drag('character_move_direction_center',
                                    'character_move_direction_' + str(random_direction), stop_delay=5)
                self.set_checkpoint('last_lag_check')
                return True

        if self.get_option('from_azit_scene') == True:
            pb_name = 'main_scene_new'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.6,
                custom_flag=1,
                custom_rect=(480, 80, 510, 110)
            )
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True

            pb_name = 'main_scene_out'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_top_level=(255, 255, 255),
                custom_below_level=(210, 210, 210),
                custom_rect=(400, 50, 540, 90)
            )
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.set_option('from_azit_scene', False)
                return True

        pb_name_list = [
            'main_scene_equip',
            'main_scene_use',
        ]

        for pb_name in pb_name_list:
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.logger.debug(pb_name + ' ' + str(match_rate))
                self.lyb_mouse_click(pb_name)
                self.game_object.get_scene('mail_scene').status = 0
                return True

        pb_name = 'main_scene_mail_new'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(510, 50, 540, 90)
        )
        if loc_x != -1:
            self.logger.info('메일함 확인')
            self.lyb_mouse_click_location(loc_x - 5, loc_y + 5)
            return True

        if self.isFull() == True:
            self.lyb_mouse_click('main_scene_gabang', custom_threshold=0)
            self.game_object.get_scene('gabang_scene').status = 0
            return True

        if self.isHorseOn() == True:
            self.logger.info('이동 중...')
            self.set_option('moving', True)
            return True

        pb_name = 'main_scene_potion_empty'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_top_level=(255, 255, 255),
            custom_below_level=(130, 130, 130),
            custom_rect=(480, 210, 635, 250)
        )
        if loc_x != -1:
            self.logger.info('물약 확인 ' + str(round(match_rate, 2)))
            self.lyb_mouse_click_location(loc_x, loc_y - 5)
            return True

        pb_name = 'main_scene_distance'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_top_level=(255, 255, 255),
            custom_below_level=(110, 110, 110),
            custom_flag=1,
            custom_rect=(250, 200, 400, 280)
        )
        if loc_x != -1:
            self.logger.info('목표 추적 중...')
            self.set_option('moving', True)
            return True

        # 이동 완료 후 자동 버튼 누르기
        if self.get_option('moving') == True:
            if self.isAutoCombat(limit_count=1) == False:
                self.lyb_mouse_click('auto', custom_threshold=0)
                self.set_option('moving', False)
                return self.status

        if is_field == False:
            if self.isAutoCombat() == False:
                self.lyb_mouse_click('auto', custom_threshold=0)

            return True

        return False

    def main_scene_process_main_quest(self):

        pb_name = 'main_quest_completed'
        # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name)
            return True

        pb_name_list = [
            ['main_quest_completed', -1, -1, (5, 125, 25, 240)],
            ['quest_complete', (110, 200, 235), (15, 60, 90), (100, 125, 140, 240)],
            ['main_quest', (250, 175, 60), (130, 80, 0), (5, 125, 25, 240)],
        ]

        if self.get_game_config(lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub') == True:
            if self.game_object.get_scene('quest_scroll_limit_scene').get_option('limit') == False:
                pb_name_list.insert(2, ['main_quest_sub', (80, 200, 235), (45, 130, 170), (5, 125, 25, 240)])

        for each_pb in pb_name_list:
            pb_name = each_pb[0]
            custom_top_level = each_pb[1]
            custom_below_level = each_pb[2]
            custom_rect = each_pb[3]

            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.65,
                custom_top_level=custom_top_level,
                custom_below_level=custom_below_level,
                custom_flag=1,
                custom_rect=custom_rect
            )
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.game_object.get_scene('ilil_quest_scene').status = 0
                self.game_object.get_scene('quest_scroll_scene').status = 0
                self.lyb_mouse_click_location(loc_x, loc_y)
                return True
            else:
                drag_start = 'bot'
                drag_end = 'top'

                drag_direction = self.get_option('drag_direction')
                if drag_direction == None:
                    drag_direction = 0

                if drag_direction % 6 < 3:
                    drag_start = 'top'
                    drag_end = 'bot'

        resource_name = 'main_quest_limit_loc'
        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
            self.window_image,
            resource_name,
            custom_threshold=0.7,
            custom_top_level=(250, 175, 60),
            custom_below_level=(130, 80, 0),
            custom_flag=1,
            custom_rect=(5, 120, 140, 240)
        )
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.set_option('메인 퀘스트' + '_end_flag', True)
            return True

        resource_name = 'main_quest_complete_loc'
        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
            self.window_image,
            resource_name,
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(5, 120, 140, 240)
        )
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.logger.info('자동 퀘스트 진행 완료')
            self.lyb_mouse_click_location(loc_x, loc_y)
            return True

        self.lyb_mouse_drag('main_scene_quest_drag_' + drag_start, 'main_scene_quest_drag_' + drag_end)

        return True

    def isAutoCombat(self, limit_count=-1):
        return self.isStatusByResource(
            '[자동전투 중]',
            'main_scene_auto_loc',
            0.7,
            (255, 255, 255), (100, 100, 100),
            (250, 200, 400, 320),
            limit_count=limit_count
        )

    def isAutoMainQuest(self, limit_count=-1):
        return self.isStatusByResource(
            '[자동퀘스트 중]',
            'main_scene_auto_quest_loc',
            0.7,
            (255, 255, 255), (100, 100, 100),
            (250, 200, 400, 320),
            limit_count=limit_count
        )

    def isFull(self):
        check_count = self.get_option('check_count')
        if check_count == None:
            check_count = 0

        pb_name = 'main_scene_full'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.8,
            custom_top_level=(80, 255, 255),
            custom_below_level=(30, 75, 110),
            custom_flag=1,
            custom_rect=(470, 30, 510, 70)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            if check_count > 2:
                self.set_option('check_count', 0)
                return True

            self.set_option('check_count', check_count + 1)
            return False

        self.set_option('check_count', 0)
        return False

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

        self.logger.debug(log_message + '..(' + str(check_count) + '/' + str(limit_count) + ')')
        self.set_option(resource_name + 'check_count', check_count + 1)

        return True

    def isHorseOn(self):
        count = 0
        for i in range(4):
            pb_name = 'horse_on_' + str(i)
            # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.2,
                custom_top_level=(30, 120, 180),
                custom_below_level=(10, 70, 60),
                custom_flag=1,
                custom_rect=(445, 335, 480, 370)
            )
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if match_rate > 0.5:
                return True
            else:
                if loc_x != -1:
                    count += 1

        if count > 2:
            return True

        return False

    def main_scene_is_dungeon(self):
        pb_name = 'main_scene_quest_dungeon'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_top_level=(250, 80, 115),
            custom_below_level=(145, 50, 60),
            custom_flag=1,
            custom_rect=(5, 95, 140, 240)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            return True

        pb_name = 'main_scene_dungeon_gold'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(5, 170, 35, 255)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            return True

        resource_name = 'main_scene_dungeon_time_loc'
        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
            self.window_image,
            resource_name,
            custom_threshold=0.7,
            custom_top_level=(255, 90, 125),
            custom_below_level=(125, 45, 60),
            custom_flag=1,
            custom_rect=(530, 130, 590, 160)
        )
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            return True

        return False

    def get_work_status(self, work_name):
        if work_name in lybgamel2r.LYBL2r.work_list:
            return (lybgamel2r.LYBL2r.work_list.index(work_name) + 1) * 1000
        else:
            return 99999

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
import likeyoubot_blade2 as lybgameblade2
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time


class LYBBlade2Scene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)

    def process(self, window_image, window_pixels):

        super(LYBBlade2Scene, self).process(window_image, window_pixels)

        rc = 0
        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'login_2_scene':
            rc = self.login_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'chulseokbosang_scene':
            rc = self.chulseokbosang_scene()
        elif self.scene_name == 'mail_scene':
            rc = self.mail_scene()
        elif self.scene_name == 'immu_scene':
            rc = self.mail_scene()
        elif self.scene_name == 'npc_scene':
            rc = self.npc_scene()
        elif self.scene_name == 'jeontoo_ready_scene':
            rc = self.jeontoo_ready_scene()
        elif self.scene_name == 'jeontoo_start_scene':
            rc = self.jeontoo_start_scene()
        elif self.scene_name == 'combat_scene':
            rc = self.combat_scene()
        elif self.scene_name == 'quest_complete_scene':
            rc = self.quest_complete_scene()
        elif self.scene_name == 'banbok_moheom_victory_scene':
            rc = self.victory_scene()
        elif self.scene_name == 'victory_scene':
            rc = self.victory_scene()
        elif self.scene_name == 'gyeoltoo_scene':
            rc = self.gyeoltoo_scene()
        elif self.scene_name == 'gyeoltoo_0_scene':
            rc = self.gyeoltoo_0_scene()
        elif self.scene_name == 'gyeoltoo_0_combat_scene':
            rc = self.gyeoltoo_0_combat_scene()
        elif self.scene_name == 'use_gem_scene':
            rc = self.use_gem_scene()
        elif self.scene_name == 'dojeon_scene':
            rc = self.dojeon_scene()
        elif self.scene_name == 'raid_scene':
            rc = self.raid_scene()
        elif self.scene_name == 'jangbiham_scene':
            rc = self.jangbiham_scene()
        elif self.scene_name == 'jeryo_levelup_scene':
            rc = self.modupalgi_scene()
        elif self.scene_name == 'modupalgi_scene':
            rc = self.modupalgi_scene()
        elif self.scene_name == 'raid_result_scene':
            rc = self.raid_result_scene()
        elif self.scene_name == 'raid_result_2_scene':
            rc = self.raid_result_scene()
        elif self.scene_name == 'raid_combat_scene':
            rc = self.raid_combat_scene()
        elif self.scene_name == 'gyeoltoo_1_scene':
            rc = self.gyeoltoo_1_scene()
        elif self.scene_name == 'gyeoltoo_1_junbi_scene':
            rc = self.gyeoltoo_1_junbi_scene()
        elif self.scene_name == 'gyeoltoo_victory_scene':
            rc = self.gyeoltoo_victory_scene()
        elif self.scene_name == 'moheom_scene':
            rc = self.moheom_scene()
        elif self.scene_name == 'banbok_moheom_stop_scene':
            rc = self.banbok_moheom_stop_scene()
        elif self.scene_name == 'jeontoo_defeat_scene':
            rc = self.jeontoo_defeat_scene()
        elif self.scene_name == 'chingu_scene':
            rc = self.chingu_scene()
        elif self.scene_name == 'youngwoongtap_scene':
            rc = self.youngwoongtap_scene()
        elif self.scene_name == 'google_play_store_scene':
            rc = self.google_play_store_scene()
        elif self.scene_name == 'menu_scene':
            rc = self.menu_scene()
        elif self.scene_name == 'bangyeok_dungeon_scene':
            rc = self.bangyeok_dungeon_scene()
        elif self.scene_name == 'bangyeok_dungeon_ipjang_scene':
            rc = self.bangyeok_dungeon_ipjang_scene()
        elif self.scene_name == 'ether_scene':
            rc = self.ether_scene()
        elif self.scene_name == 'jadong_bunhe_scene':
            rc = self.jadong_bunhe_scene()
        elif self.scene_name == 'ildeil_matching_scene':
            rc = self.ildeil_matching_scene()
        elif self.scene_name == 'raid_matching_scene':
            rc = self.raid_matching_scene()
        elif self.scene_name == 'jeomryoungjeon_scene':
            rc = self.jeomryoungjeon_scene()
        elif self.scene_name == 'jeomryoungjeon_combat_scene':
            rc = self.jeomryoungjeon_combat_scene()
        elif self.scene_name == 'jeomryoungjeon_match_scene':
            rc = self.jeomryoungjeon_match_scene()
        elif self.scene_name == 'moheom_select_scene':
            rc = self.moheom_select_scene()
        elif self.scene_name == 'myeongye_scene':
            rc = self.myeongye_scene()











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

    def myeongye_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('last_status', 0)
            self.status += 1
        elif self.status >= 1 and self.status < 5:
            self.status += 1

            for i in range(3):
                pb_name = 'myeongye_scene_new_' + str(i)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_top_level=(255, 10, 10),
                    custom_below_level=(250, 0, 0),
                    custom_rect=(190, 50, 640, 90))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x - 10, loc_y + 10)
                    self.set_option('last_status', self.status)
                    self.status = 10
                    return self.status
                else:
                    self.lyb_mouse_click('myeongye_scene_tab_2', custom_threshold=0)

        elif self.status >= 10 and self.status < 20:
            self.status += 1

            pb_name = 'myeongye_scene_remain_limit'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status = self.get_option('last_status')
                return self.status

            random_rank = int(random.random() * 3)
            self.logger.info('명예의 전당 랜덤 클릭: ' + str(random_rank + 1) + '위')
            pb_name = 'myeongye_scene_hello_' + str(random_rank)
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.status = self.get_option('last_status')
                return self.status
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def raid_matching_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 60:
            self.status += 1
            boss_index = self.indexOfRaidBoss()
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_' + str(
                    boss_index)) == True:
                self.lyb_mouse_click('raid_matching_scene_start', custom_threshold=0)
                return self.status

            pb_name = 'raid_matching_scene_match'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            self.logger.info('레이드 매칭 화면 닫기 카운트(' + str(self.status) + '/60)')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jeomryoungjeon_match_scene(self):

        if self.status >= 0 and self.status < 1000:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jeomryoungjeon_combat_scene(self):

        is_blue = False
        is_red = False
        # 블루팀
        pb_name = 'jeomryoungjeon_combat_scene_me'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(580, 40, 620, 70))
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.logger.debug('블루팀')
            is_blue = True

        pb_name = 'jeomryoungjeon_combat_scene_me'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(10, 40, 50, 70))
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.logger.debug('레드팀')
            is_red = True

        is_move = True
        for i in range(3):
            pb_name = 'jeomryoungjeon_combat_scene_direction_' + str(i)
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.1,
                custom_flag=1,
                custom_top_level=(250, 190, 160),
                custom_below_level=(230, 160, 120),
                custom_rect=(230, 150, 410, 260))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x == -1:
                is_move = False

        if is_move == True:
            random_direction = int(random.random() * 8)
            if is_blue == True:
                self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(5),
                                    stop_delay=5)
                self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(6),
                                    stop_delay=5)
                self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(7),
                                    stop_delay=5)
            elif is_red == True:
                self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(1),
                                    stop_delay=5)
                self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(2),
                                    stop_delay=5)
                self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(3),
                                    stop_delay=5)
            else:
                self.lyb_mouse_drag('character_move_direction_center',
                                    'character_move_direction_' + str(random_direction), stop_delay=5)
        else:
            for i in range(6):
                self.lyb_mouse_click('skill_' + str(i), custom_threshold=0, delay=1)
            self.lyb_mouse_click('attack', custom_threshold=0, delay=5)

        # self.lyb_mouse_click('attack', custom_threshold=0, delay=1)

        return self.status

    def jeomryoungjeon_scene(self):

        self.status = 99999

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            elapsed_time = time.time() - self.get_checkpoint('press_sijak')
            if elapsed_time < self.period_bot(30):
                self.status = 99999
            else:
                self.status += 1
        elif self.status >= 1 and self.status < 9:
            self.status += 1
            pb_name = 'jeomryoungjeon_scene_bosang'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(530, 180, 630, 320))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            pb_name = 'jeomryoungjeon_scene_junbi'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(450, 340, 540, 380))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                return self.status

            pb_name = 'jeomryoungjeon_scene_sijak'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(450, 340, 540, 380))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.status = 10
                return self.status
        elif self.status == 9:
            self.status = 99999
        elif self.status == 10:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use') == True:
                cfg_hero = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero')
                hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(cfg_hero))
                self.lyb_mouse_click('jeomryoungjeon_scene_hero_' + str(hero_index), custom_threshold=0)
            self.set_checkpoint('press_sijak')
            self.status += 1
        elif self.status >= 11 and self.status < 15:
            pb_name = 'jeomryoungjeon_scene_sijak'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(450, 340, 540, 380))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.game_object.get_scene('jeomryoungjeon_match_scene').status = 0
                self.status = 15
                return self.status

            self.status += 1
        elif self.status >= 15 and self.status < 17:
            self.status += 1
        elif self.status == 17:
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def ildeil_matching_scene(self):

        elapsed_time = time.time() - self.get_checkpoint('last_check')
        if elapsed_time > self.period_bot(10):
            self.status = 0

        self.set_checkpoint('last_check')

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_checkpoint('start')
            self.status += 1
        elif self.status >= 1 and self.status < 300:
            elapsed_time = time.time() - self.get_checkpoint('start')
            if elapsed_time >= 60:
                self.status = 99999
            else:
                self.logger.info('일대일 매칭 대기 시간...(' + str(elapsed_time) + '/60)')
                self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jadong_bunhe_scene(self):

        # for i in range(len(lybgameblade2.LYBBlade2.tier_list)):
        # 	self.logger.info(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + str(i)))

        # for i in range(6):
        # 	self.logger.info(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + str(i)))

        # self.logger.info(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa'))

        match_rate = self.game_object.rateMatchedResource(self.window_pixels, self.scene_name)
        if match_rate < 0.9:
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('limit_count', 0)
            self.status += 1
        elif self.status == 1:
            is_clicked = True
            limit_count = self.get_option('limit_count')
            if limit_count > 10:
                self.status = 10
            else:
                for i in range(len(lybgameblade2.LYBBlade2.tier_list)):
                    cfg_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + str(i))
                    pb_name = self.scene_name + '_tier_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.debug(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9 and cfg_checked == False:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif match_rate < 0.9 and cfg_checked == True:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    else:
                        is_clicked = False

                for i in range(6):
                    cfg_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + str(i))
                    pb_name = self.scene_name + '_rank_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.debug(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9 and cfg_checked == False:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif match_rate < 0.9 and cfg_checked == True:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    else:
                        is_clicked = False

                cfg_checked = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa')
                pb_name = self.scene_name + '_ganghwa'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.9 and cfg_checked == False:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                elif match_rate < 0.9 and cfg_checked == True:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                else:
                    is_clicked = False

                if is_clicked == False:
                    self.status = 10
                else:
                    self.set_option('limit_count', limit_count + 1)
                    self.status += 1
        elif self.status == 2:
            self.status = 1
        elif self.status == 10:
            self.status += 1
        elif self.status == 11:
            self.lyb_mouse_click(self.scene_name + '_bunhe', custom_threshold=0)
            self.status = 99999
        elif self.status >= 99994 and self.status < 99997:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
        elif self.status >= 99997 and self.status <= 99999:
            self.status -= 1
        else:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def ether_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('ether_scene_auto_bunhe', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def bangyeok_dungeon_ipjang_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('limit_count', 0)
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use') == True:
                self.status = 1
            else:
                self.status = 2
        elif self.status == 1:
            cfg_hero = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero')
            hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(cfg_hero))
            pb_name = 'bangyeok_dungeon_ipjang_scene_hero_' + str(hero_index)
            self.logger.info(str(cfg_hero) + ' 선택')
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 2:
            limit_count = self.get_option('limit_count')
            if limit_count > 4:
                self.status = 99999
                return self.status

            pb_name = 'bangyeok_dungeon_ipjang_scene_limit'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status = 99999
                return self.status

            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang') == True:
                self.lyb_mouse_click(self.scene_name + '_sotang', custom_threshold=0)
                self.set_option('limit_count', limit_count + 1)
                return self.status

            level = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level')) - 1
            if level != -1:
                pb_name = 'bangyeok_dungeon_ipjang_scene_level_' + str(level)
                self.lyb_mouse_click(pb_name, custom_threshold=0)

            self.logger.info('반격 던전 전투 진행 중...(' + str(limit_count + 1) + '/5)')
            self.set_option('limit_count', limit_count + 1)
            self.status += 1
        elif self.status == 3:
            self.lyb_mouse_click('bangyeok_dungeon_ipjang_scene_start', custom_threshold=0)
            self.game_object.get_scene('raid_combat_scene').status = 1
            self.status = 2
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def bangyeok_dungeon_scene(self):

        pb_name = 'bangyeok_dungeon_clear_receive'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.9:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            return self.status

        pb_name = 'bangyeok_dungeon_bosang_new'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_top_level=(255, 10, 10),
            custom_below_level=(250, 0, 0),
            custom_rect=(120, 320, 450, 360))
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            self.lyb_mouse_click_location(loc_x - 10, loc_y + 15)
            return self.status

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            # self.set_option('week_index', 3)
            # today = time.strftime("%a")
            # self.logger.info("요일: " + str(today))
            # if today == "Mon" or today == "Thu":
            # 	self.set_option('week_index', 0)
            # elif today == "Wed" or today == "Fri":
            # 	self.set_option('week_index', 1)
            # elif today == "Tue" or today == "Sat":
            # 	self.set_option('week_index', 2)

            self.status += 1
        elif self.status == 1:
            # week_index = self.get_option('week_index')
            for i in range(4):
                pb_name = 'bangyeok_dungeon_scene_lock_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate < 0.9:
                    self.game_object.get_scene('bangyeok_dungeon_scene').status = 0
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                else:
                    self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def menu_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status = self.get_work_status('친구')
        elif self.status >= self.get_work_status('친구') and self.status < self.get_work_status('친구') + 5:
            self.game_object.get_scene('chingu_scene').status = 0
            if self.status % 2 == 0:
                self.lyb_mouse_click('menu_scene_chingu', custom_threshold=0)
            self.status += 1
        elif self.status >= self.get_work_status('자동분해') and self.status < self.get_work_status('자동분해') + 5:
            self.game_object.get_scene('ether_scene').status = 0
            if self.status % 2 == 0:
                self.lyb_mouse_click('menu_scene_ether', custom_threshold=0)
            self.status += 1
        elif self.status >= self.get_work_status('명예의 전당') and self.status < self.get_work_status('명예의 전당') + 5:
            self.game_object.get_scene('myeongye_scene').status = 0
            if self.status % 2 == 0:
                self.lyb_mouse_click('menu_scene_myeongye', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

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

    def youngwoongtap_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 30:
            pb_name = 'youngwoongtap_scene_count_0'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click('youngwoongtap_scene_sotang', custom_threshold=0)
                self.status = 99999
                return self.status

            pb_name = 'youngwoongtap_scene_junbi'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            pb_name = 'youngwoongtap_scene_sijak'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.game_object.get_scene('jeontoo_defeat_scene').status = 99999
                return self.status
            self.status += 1
        else:
            self.game_object.get_scene('jeontoo_defeat_scene').status = 0
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def chingu_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('chingu_scene_tab_0', custom_threshold=0)
            self.status += 1
        elif self.status == 2:
            self.status += 1
        elif self.status == 3:
            self.lyb_mouse_click('chingu_scene_modu')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def jeontoo_defeat_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_checkpoint('start')
            self.status += 1
        elif self.status == 1:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat') == True:
                self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 전투패배 감지')
                png_name = self.game_object.save_image('jeontoo_defeat')
                self.game_object.telegram_send('', image=png_name)
            self.status += 1
        elif self.status == 2:
            elapsed_time = time.time() - self.get_checkpoint('start')
            if elapsed_time > 120 and elapsed_time < 240:
                self.status = 99999
            elif elapsed_time >= 240:
                self.set_checkpoint('start')
            else:
                self.loggingElapsedTime('전투패배 나가기 클릭 대기', elapsed_time, 120, 5)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def banbok_moheom_stop_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 10:
            self.status += 1
        elif self.status == 11:
            self.lyb_mouse_click('banbok_moheom_stop_scene_yes', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def moheom_select_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 10:
            self.lyb_mouse_click('moheom_select_scene_list_0', custom_threshold=0)
            self.game_object.get_scene('moheom_scene').status = 0
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
            cfg_level = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level')
            cfg_level_index = lybgameblade2.LYBBlade2.moheom_level_list.index(cfg_level)

            if cfg_level_index < len(lybgameblade2.LYBBlade2.moheom_level_list) - 1:
                pb_name = 'moheom_scene_level_' + str(cfg_level_index)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_top_level=(240, 199, 121),
                    custom_below_level=(200, 159, 91),
                    custom_flag=1,
                    custom_rect=(500, 350, 635, 389))
                self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
            else:
                # 임시용
                pb_name = 'moheom_scene_level_last'
                self.lyb_mouse_click(pb_name, custom_threshold=0)

            # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            # self.logger.debug(pb_name + ' ' + str(match_rate))
            # if match_rate < 0.7:
            # self.lyb_mouse_click(pb_name, custom_threshold=0)
            # self.status = 0
            # return self.status

            self.status += 1
        elif self.status == 2:
            cfg_act = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'))
            if cfg_act < 4:
                self.status = 11
            else:
                self.status = 15
            return self.status
        elif self.status == 11:
            pb_name = 'moheom_scene_act_1'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.set_option('move_count', 0)
                self.status = 20
            else:
                self.lyb_mouse_click('moheom_scene_move_left', custom_threshold=0)
        elif self.status == 15:
            pb_name = 'moheom_scene_act_5'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.set_option('move_count', 0)
                self.status = 30
            else:
                self.lyb_mouse_click('moheom_scene_move_right', custom_threshold=0)
        elif self.status == 20:
            cfg_act = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'))
            move_count = self.get_option('move_count')
            if move_count >= cfg_act - 1:
                self.status = 100
            else:
                self.lyb_mouse_click('moheom_scene_move_right', custom_threshold=0)
                self.set_option('move_count', move_count + 1)
                self.status += 1
        elif self.status == 21:
            self.status -= 1
        elif self.status == 30:
            cfg_act = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'))
            move_count = self.get_option('move_count')
            if move_count >= 5 - cfg_act:
                self.status = 200
            else:
                self.lyb_mouse_click('moheom_scene_move_left', custom_threshold=0)
                self.set_option('move_count', move_count + 1)
                self.status += 1
        elif self.status == 31:
            self.status -= 1
        elif self.status == 100:
            self.lyb_mouse_click('moheom_scene_move_right', custom_threshold=0)
            self.status += 1
        elif self.status == 101:
            self.lyb_mouse_click('moheom_scene_move_left', custom_threshold=0)
            self.status = 300
        elif self.status == 200:
            self.lyb_mouse_click('moheom_scene_move_left', custom_threshold=0)
            self.status += 1
        elif self.status == 201:
            self.lyb_mouse_click('moheom_scene_move_right', custom_threshold=0)
            self.status = 300
        elif self.status == 300:
            self.status += 1
        elif self.status == 301:
            cfg_act = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'))
            cfg_stage = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'))

            self.logger.warn(str(cfg_act) + ' ' + str(cfg_stage))
            pb_name = 'moheom_scene_stage_' + str(cfg_act - 1) + str(cfg_stage - 1)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status = 99999

        # for i in range(0, 5):
        # 	pb_name = 'moheom_scene_act_' + str(i + 1)
        # 	match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # 	self.logger.debug(pb_name + ' ' + str(match_rate))

        # self.lyb_mouse_click('moheom_scene_last', custom_threshold=0)
        # self.logger.info('마지막 모험으로 클릭')
        # self.status += 1
        # lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'
        elif self.status == 2:
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def gyeoltoo_victory_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def raid_combat_scene(self):

        # self.logger.debug('scene: ' + self.scene_name)
        if self.status == 0:
            self.status = 10
        elif self.status == 1:
            pb_name = 'bangyeok_time'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.4,
                custom_top_level=(255, 255, 100),
                custom_below_level=(240, 140, 40),
                custom_flag=1,
                custom_rect=(500, 240, 590, 330))
            # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click('attack', delay=2, custom_threshold=0)
                return self.status

            pb_name = 'bangyeok_time_2'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.4,
                custom_top_level=(255, 255, 100),
                custom_below_level=(240, 140, 40),
                custom_flag=1,
                custom_rect=(605, 230, 630, 250))
            # self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click('bangyeok_skill', delay=2, custom_threshold=0)
                time.sleep(0.01)

            self.lyb_mouse_click('bangyeok_combat_scene_defense', delay=0.2, custom_threshold=0)

            response_time = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response'))
            self.game_object.interval = self.period_bot(response_time * 0.001)
        elif self.status == 10:

            self.game_object.get_scene('raid_matching_scene').status = 0

            cfg_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit'))
            if cfg_limit != 0:
                elapsed_time = time.time() - self.get_checkpoint('last_check')
                if elapsed_time > 10:
                    self.set_checkpoint('start')

                self.set_checkpoint('last_check')

                elapsed_time = time.time() - self.get_checkpoint('start')
                if elapsed_time > cfg_limit:
                    self.status = 0
                    self.game_object.terminate_application()
                    return self.status

                self.loggingElapsedTime('레이드 경과 시간', int(elapsed_time), cfg_limit, period=5)

            self.auto_on(pb_name='raid_combat_auto_on')

        return self.status

    def raid_result_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            pb_name = 'raid_result_scene_bosang'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status

            boss_index = self.indexOfRaidBoss()
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_' + str(
                    boss_index)) == True:
                pb_name = 'raid_result_scene_raid'
            else:
                if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_' + str(boss_index)) == True:
                    pb_name = 'raid_result_scene_re_team'
                else:
                    pb_name = 'raid_result_scene_re'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return self.status

            self.status += 1
        else:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def modupalgi_scene(self):

        match_rate = self.game_object.rateMatchedResource(self.window_pixels, self.scene_name)
        if match_rate < 0.9:
            return self.status

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('limit_count', 0)

            pb_name = 'modupalgi_scene_bunhe'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_flag=1,
                custom_rect=(290, 320, 340, 360))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.set_option('bunhe', True)
            else:
                self.set_option('bunhe', False)

            self.status += 1
        elif self.status == 1:
            is_clicked = True
            limit_count = self.get_option('limit_count')
            if limit_count > 10:
                self.status = 10
            else:
                for i in range(len(lybgameblade2.LYBBlade2.item_equip_list)):
                    cfg_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + str(i))
                    pb_name = self.scene_name + '_item_equip_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.debug(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9 and cfg_checked == False:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif match_rate < 0.9 and cfg_checked == True:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    else:
                        is_clicked = False

                for i in range(7):
                    cfg_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + str(i))
                    if self.get_option('bunhe') == True:
                        index = i - 1
                    else:
                        index = i
                    if index < 0:
                        continue
                    elif index > 5:
                        continue

                    pb_name = self.scene_name + '_item_rank_' + str(index)

                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.debug(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9 and cfg_checked == False:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif match_rate < 0.9 and cfg_checked == True:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    else:
                        is_clicked = False

                for i in range(len(lybgameblade2.LYBBlade2.item_status_list)):
                    cfg_checked = self.get_game_config(
                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + str(i))
                    pb_name = self.scene_name + '_item_status_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.debug(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9 and cfg_checked == False:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    elif match_rate < 0.9 and cfg_checked == True:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                    else:
                        is_clicked = False

                # self.logger.warn(lybgameblade2.LYBBlade2.item_equip_list[i] + ' ' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + str(i))))
                # for i in range(6):
                # 	self.logger.warn(str(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + str(i))))
                # for i in range(len(lybgameblade2.LYBBlade2.item_status_list)):
                # 	self.logger.warn(lybgameblade2.LYBBlade2.item_status_list[i] + ' ' + str(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + str(i))))

                if is_clicked == False:
                    self.status = 10
                else:
                    self.set_option('limit_count', limit_count + 1)
                    self.status += 1
        elif self.status == 2:
            self.status = 1
        elif self.status == 10:
            self.status += 1
        elif self.status == 11:
            self.lyb_mouse_click(self.scene_name + '_sell', custom_threshold=0)
            self.status += 1
        else:
            last_close = self.get_checkpoint('close')
            if last_close != 0:
                elapsed_time = time.time() - last_close
                if elapsed_time > self.period_bot(3):
                    self.status = 0

            self.set_checkpoint('close')

            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

        return self.status

    def jangbiham_scene(self):

        item_rank_rgb_range_list = [
            [(200, 200, 200), (80, 80, 80)],  # 하얀색
            [(160, 255, 55), (50, 95, 0)],  # 녹색
            [(70, 150, 215), (40, 70, 100)],  # 파란색
            [(180, 95, 190), (95, 55, 100)],  # 보라색
            [(205, 150, 50), (105, 65, 30)],  # 주황색
            [(220, 185, 20), (100, 75, 0)],  # 노란색
        ]

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('hero_index', 0)
            self.set_checkpoint('start')
            self.status += 1
        elif self.status == 1:
            hero_index = self.get_option('hero_index')
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + str(hero_index)) == True:
                self.lyb_mouse_click('jangbiham_scene_hero_' + str(hero_index), custom_threshold=0)
                self.status += 1
            else:
                self.logger.info('[' + lybgameblade2.LYBBlade2.hero_list[hero_index] + '] 작업 수행 안함')
                self.status = 4
        elif self.status == 2:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock') == True:
                self.logger.info('[신성한 빛] 아이템 잠금 체크')
                self.set_option('item_list_tab_index', -1)

                for i in range(5):
                    pb_name = 'jangbiham_scene_last_' + str(i)
                    self.set_option('last_pixel_' + pb_name, None)

                self.status = 100
            else:
                self.status += 1
        elif self.status == 3:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe') == True:
                self.logger.warn('자동 분해')
                self.game_object.get_scene('modupalgi_scene').status = 0
                self.lyb_mouse_click('jangbiham_scene_bunhe', custom_threshold=0)
            elif self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup') == True:
                self.logger.warn('재료 레벨업')
                self.game_object.get_scene('jeryo_levelup_scene').status = 0
                self.lyb_mouse_click('jangbiham_scene_jeryo_levelup', custom_threshold=0)
            else:
                self.logger.warn('모두 팔기')
                self.game_object.get_scene('modupalgi_scene').status = 0
                self.lyb_mouse_click('jangbiham_scene_sell', custom_threshold=0)
            self.status += 1
        elif self.status == 4:
            hero_index = self.get_option('hero_index')
            if hero_index >= 3:
                self.status = 99999
            else:
                self.set_option('hero_index', hero_index + 1)
                self.status = 1
        elif self.status == 100:
            item_list_tab_index = self.get_option('item_list_tab_index')
            self.set_option('item_list_tab_index', item_list_tab_index + 1)
            self.game_object.get_scene('mail_scene').set_option('immediate_back', True)
            self.status += 1
        elif self.status == 101:
            if self.game_object.get_scene('mail_scene').get_option('immediate_back') == True:
                self.lyb_mouse_click('main_scene_mail', custom_threshold=0)
            else:
                self.status += 1
        elif self.status == 102:
            item_list_tab_index = self.get_option('item_list_tab_index')
            if item_list_tab_index > 2:
                self.status = 3
                return self.status

            self.set_option('current_rank', 0)
            self.set_option('current_row', 0)
            self.set_option('current_col', 0)
            self.set_option('drag_count', 0)

            self.lyb_mouse_click('jangbiham_scene_item_tab_' + str(item_list_tab_index), custom_threshold=0)
            self.status = 105
        elif self.status == 105:

            current_row = self.get_option('current_row')
            for row in range(current_row, 2):
                current_col = self.get_option('current_col')
                for col in range(current_col, 4):
                    current_rank = self.get_option('current_rank')
                    for i in range(current_rank, len(item_rank_rgb_range_list)):
                        if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + str(
                                i)) == False:
                            # self.logger.debug('[신성한 빛] 아이템 잠금 체크 패스 : ★'+str(i+1))
                            continue
                        # self.logger.debug('[신성한 빛] 아이템 잠금 체크: ★'+str(i+1))

                        resource_name = 'jangbiham_scene_holy_rank_1_loc'

                        (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                            self.window_image,
                            resource_name,
                            custom_threshold=0.8,
                            custom_top_level=item_rank_rgb_range_list[i][0],
                            custom_below_level=item_rank_rgb_range_list[i][1],
                            source_custom_top_level=item_rank_rgb_range_list[1][0],
                            source_custom_below_level=item_rank_rgb_range_list[1][1],
                            custom_flag=1,
                            custom_rect=(365 + (col * 75) - 35, 170 + (row * 100) - 70, 365 + (col * 75) + 35,
                                         170 + (row * 100) + 80)
                        )
                        self.logger.debug(str((365 + (col * 75) - 35, 170 + (row * 100) - 70, 365 + (col * 75) + 35,
                                               170 + (row * 100) + 80)) + ' ★' + str(i + 1) + ' ' + str(
                            (loc_x, loc_y)) + ' ' + str(int(match_rate * 100)) + '%')
                        if loc_x != -1:
                            self.logger.info('[신성한 빛] 아이템 발견됨: ★' + str(i + 1))

                            pb_name = 'jangbiham_scene_item_lock'
                            adj_x, adj_y = self.game_object.get_player_adjust()
                            (loc_x2, loc_y2), match_rate = self.game_object.locationOnWindowPart(
                                self.window_image,
                                self.game_object.resource_manager.pixel_box_dic[pb_name],
                                custom_threshold=0.8,
                                custom_flag=1,
                                custom_top_level=(175, 120, 50),
                                custom_below_level=(140, 100, 30),
                                custom_rect=(loc_x - 40 - adj_x, loc_y - 80 - adj_y, loc_x + 40 - adj_x, loc_y - adj_y)
                            )
                            self.logger.warn(pb_name + ' ' + str((loc_x2, loc_y2)) + ' ' + str(match_rate))
                            if loc_x2 != -1:
                                self.logger.info('잠금 상태')
                            else:
                                self.lyb_mouse_click_location(loc_x, loc_y)
                                self.set_option('current_rank', i + 1)
                                self.set_option('current_row', row)
                                self.set_option('current_col', col)
                                self.status = 110
                                return self.status
                    self.set_option('current_rank', 0)
                self.set_option('current_col', 0)
            self.status += 1
        elif self.status == 106:
            drag_count = self.get_option('drag_count')
            self.logger.info('장비 탐색 중...(' + str(drag_count) + '/20)')
            if drag_count >= 20:
                self.status = 100
            else:
                self.lyb_mouse_drag('jangbiham_scene_drag_bot', 'jangbiham_scene_drag_top', stop_delay=1)
                self.set_option('current_rank', 0)
                self.set_option('current_row', 0)
                self.set_option('current_col', 0)
                self.set_option('drag_count', drag_count + 1)
                self.status += 1
        elif self.status == 107:
            is_end = True
            for i in range(4):
                pb_name = 'jangbiham_scene_last_' + str(i)
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
                self.status = 100
            else:
                self.status = 105
        elif self.status >= 110 and self.status < 120:
            pb_name = 'jangbiham_scene_unlock'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.logger.debug(pb_name + ' ' + str(match_rate))
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.set_option('current_rank', 0)
                if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock') == True:
                    self.game_object.telegram_send(
                        '창 이름 [' + str(self.game_object.window_title) + ']에서 [신성한 빛 아이템 잠금] 감지')
                    png_name = self.game_object.save_image('holy_item_lock')
                    self.game_object.telegram_send('', image=png_name)
                return self.status

            pb_name = 'jangbiham_scene_lock'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.logger.debug(pb_name + ' ' + str(match_rate))
                self.lyb_mouse_click('jangbiham_scene_item_close_icon', custom_threshold=0)
                self.status = 105
                return self.status

            self.status += 1
        elif self.status == 120:
            self.status = 105
        elif self.status == self.get_work_status('모두팔기'):
            self.status = 0
        elif self.status == self.get_work_status('장비교체'):
            self.status = 200
        elif self.status == 200:
            cfg_hero = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero')
            cfg_hero_index = lybgameblade2.LYBBlade2.hero_list.index(cfg_hero)
            self.lyb_mouse_click('jangbiham_scene_hero_' + str(cfg_hero_index), custom_threshold=0)
            self.status += 1
        elif self.status == 201:
            cfg_set = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set'))
            if cfg_set != 0:
                self.lyb_mouse_click('jangbiham_scene_set_' + str(cfg_set), custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def raid_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            pb_name = 'raid_scene_help'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status = 2
                return self.status

            pb_name = 'raid_scene_start'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status = 3
                return self.status

            self.status = 99999
        elif self.status == 2:
            boss_index = self.indexOfRaidBoss()
            self.lyb_mouse_click('raid_scene_boss_' + str(boss_index), custom_threshold=0)
            self.status = 0
        elif self.status == 3:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use') == True:
                cfg_hero = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero')
                hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(cfg_hero))
                self.lyb_mouse_click('raid_scene_hero_' + str(hero_index), custom_threshold=0)
            self.status += 1
        elif self.status == 4:
            boss_index = self.indexOfRaidBoss()
            if boss_index == None or boss_index == 0:
                raid_level = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level')) - 1
            else:
                raid_level = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_' + str(boss_index))) - 1

            if raid_level != -1:
                pb_name = 'raid_scene_level_' + str(raid_level)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 5:

            boss_index = self.indexOfRaidBoss()
            self.game_object.get_scene('raid_combat_scene').status = 0
            self.game_object.get_scene('jeontoo_defeat_scene').status = 0
            self.game_object.get_scene('raid_matching_scene').status = 0
            self.game_object.get_scene('raid_matching_scene').set_option('boss_index', boss_index)
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_' + str(
                    boss_index)) == True:
                self.lyb_mouse_click('raid_scene_make_room', custom_threshold=0)
            else:
                self.lyb_mouse_click('raid_scene_start', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def dojeon_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.status = self.get_work_status('레이드')
        elif self.status >= self.get_work_status('레이드') and self.status < self.get_work_status('레이드') + 3:
            self.lyb_mouse_click('dojeon_scene_raid', custom_threshold=0)
            self.status += 1
        elif self.status >= self.get_work_status('영웅의 탑') and self.status < self.get_work_status('영웅의 탑') + 3:
            self.lyb_mouse_click('dojeon_scene_youngwoongtap', custom_threshold=0)
            self.status += 1
        elif self.status >= self.get_work_status('반격 던전') and self.status < self.get_work_status('반격 던전') + 3:
            self.lyb_mouse_click('dojeon_scene_bangyoek', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def use_gem_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.game_object.get_scene('gyeoltoo_0_scene').status = 99999
            self.game_object.get_scene('gyeoltoo_1_scene').status = 99999
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def gyeoltoo_1_junbi_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('gyeoltoo_1_junbi_scene_sijak', custom_threshold=0)
            self.status += 1
        elif self.status == 2:
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def gyeoltoo_1_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('count', 0)
            self.status += 1
        elif self.status == 1:
            cfg_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count'))
            count = self.get_option('count')
            if count >= cfg_count:
                self.status = 99999
                return self.status

            pb_name = 'gyeoltoo_1_scene_bosang'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                return self.status

            self.lyb_mouse_click('gyeoltoo_1_scene_junbi', custom_threshold=0)
            self.logger.info('팀 대전: ' + str(count) + '/' + str(cfg_count))
            self.set_option('count', count + 1)

            self.game_object.get_scene('gyeoltoo_1_junbi_scene').status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def gyeoltoo_0_combat_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.game_object.get_scene('gyeoltoo_0_scene').status = 1
            self.set_checkpoint('tag_period')
            self.set_checkpoint('start')
            self.status += 1
        elif self.status >= 1 and self.status < 1000:
            elapsed_time = time.time() - self.get_checkpoint('start')
            if elapsed_time > self.period_bot(300):
                self.game_object.terminate_application()
                return self.status

            self.loggingElapsedTime('일대일 결투 경과 시간', int(elapsed_time), 300, period=10)

            tag_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'))
            elapsed_time = time.time() - self.get_checkpoint('tag_period')
            if elapsed_time > tag_period:
                self.status = 1000
            else:
                self.loggingElapsedTime("TAG", int(elapsed_time), tag_period, period=2)
                self.auto_on(pb_name='gyeoltoo_auto_on')
            self.status += 1
        elif self.status >= 1000 and self.status < 1003:
            self.lyb_mouse_click('combat_scene_tag', custom_threshold=0)
            self.set_checkpoint('tag_period')
            self.status += 1
        else:
            self.status = 1

        return self.status

    def gyeoltoo_0_scene(self):

        hero1 = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1')
        hero2 = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2')
        cfg_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count'))

        first_hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(hero1))
        second_hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(hero2))

        if first_hero_index == second_hero_index:
            self.logger.warn('영웅 중복 선택됨: ' + hero1 + ' ' + hero2)
            second_hero_index = (first_hero_index + 1) % len(lybgameblade2.LYBBlade2.hero_list)

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('count', 0)
            self.status += 1
        elif self.status == 1:
            self.status += 1
        elif self.status == 2:
            count = self.get_option('count')
            if count == None:
                count = 0

            if count >= cfg_count:
                self.status = 99999
                return self.status

            pb_name = 'gyeoltoo_0_scene_junbi'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status = 3
                return self.status

            pb_name = 'gyeoltoo_0_scene_start'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.status = 4
                self.set_option('count', count + 1)
                self.logger.info('일대일 대전: ' + str(count) + '/' + str(cfg_count))
                return self.status

            self.status = 99999
        elif self.status == 3:
            pb_name = 'gyeoltoo_0_scene_bosang'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.warn(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
            else:
                self.lyb_mouse_click('gyeoltoo_0_scene_junbi', custom_threshold=0)
            self.status = 100
        elif self.status == 4:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use') == False:
                self.status = 7
                return self.status
            self.status += self.jeontoo_scene_clear_list('gyeoltoo_0_scene_hero_', first_hero_index, second_hero_index)
        elif self.status == 5:
            self.status += self.jeontoo_scene_select_first('gyeoltoo_0_scene_hero_', first_hero_index)
        elif self.status == 6:
            self.status += self.jeontoo_scene_select_second('gyeoltoo_0_scene_hero_', second_hero_index)
        elif self.status >= 7 and self.status < 10:
            self.lyb_mouse_click('gyeoltoo_0_scene_start', custom_threshold=0)
            self.game_object.get_scene('gyeoltoo_0_combat_scene').status = 0
            self.status += 1
        elif self.status == 100:
            self.status = 1
        elif self.status == 99999:
            self.lyb_mouse_click('back', custom_threshold=0)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def gyeoltoo_scene(self):

        match_rate = self.game_object.rateMatchedResource(self.window_pixels, self.scene_name)
        if match_rate < 0.9:
            return self.status

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('iterator', 0)
            self.status += 1
        elif self.status == 1:
            self.status += 1
        elif self.status == 2:
            iterator = self.get_option('iterator')
            if iterator > 2:
                self.status = 99999
            else:
                pb_name = 'gyeoltoo_scene_list_' + str(iterator)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.game_object.get_scene('gyeoltoo_' + str(iterator) + '_scene').status = 0
                self.set_option('iterator', iterator + 1)
                self.status += 1
        elif self.status == 3:
            self.status += 1
        elif self.status == 4:
            self.status = 1
        elif self.status == self.get_work_status('일대일 대전'):
            index = lybgameblade2.LYBBlade2.gyeoltoo_list.index('일대일 대전')
            pb_name = 'gyeoltoo_scene_list_' + str(index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.get_scene('gyeoltoo_0_scene').status = 0
            self.status = 99999
        elif self.status == self.get_work_status('팀 대전'):
            index = lybgameblade2.LYBBlade2.gyeoltoo_list.index('팀 대전')
            pb_name = 'gyeoltoo_scene_list_' + str(index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.get_scene('gyeoltoo_1_scene').status = 0
            self.status = 99999
        elif self.status == self.get_work_status('점령전'):
            index = lybgameblade2.LYBBlade2.gyeoltoo_list.index('점령전')
            pb_name = 'gyeoltoo_scene_list_' + str(index)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.get_scene('jeomryoungjeon_scene').status = 0
            self.status = 99999
        elif self.status == 99999:
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def victory_scene(self):

        match_rate = self.game_object.rateMatchedResource(self.window_pixels, self.scene_name)
        if match_rate < 0.9:
            return self.status

        self.game_object.get_scene('combat_scene').status = 0

        elapsed_time = time.time() - self.get_checkpoint('last_victory')
        if elapsed_time > 10:
            limit_count = self.game_object.get_scene('jeontoo_start_scene').get_option('limit_count')
            if limit_count == None:
                limit_count = 0

            limit_count += 1
            self.game_object.get_scene('jeontoo_start_scene').set_option('limit_count', limit_count)

            cfg_limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count'))

            self.logger.info(str(limit_count) + ' ' + str(cfg_limit_count))
            if cfg_limit_count != 0:
                if limit_count >= cfg_limit_count:

                    self.game_object.get_scene('main_scene').set_option('모험' + '_end_flag', True)

                    pb_name = 'victory_scene_banbok_close_icon'
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        self.game_object.get_scene('banbok_moheom_stop_scene').status = 10
                    else:
                        pb_name = 'victory_scene_banbok_close_icon2'
                        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                        self.logger.warn(pb_name + ' ' + str(match_rate))
                        if match_rate > 0.9:
                            self.lyb_mouse_click(pb_name, custom_threshold=0)
                            self.game_object.get_scene('banbok_moheom_stop_scene').status = 10

                    self.status = 99999
                else:
                    self.logger.info('모험 진행 중...(' + str(limit_count) + '/' + str(cfg_limit_count) + ')')

        self.set_checkpoint('last_victory')

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            if (self.game_object.get_scene('main_scene').current_work == '모험' and
                        self.game_object.get_scene('main_scene').get_option('모험' + '_end_flag') == True
                ):
                self.status = 99999
                return self.status

            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry') == True:
                self.logger.warn('다시 하기')
                self.lyb_mouse_click('victory_scene_re', custom_threshold=0)
                self.status = 0
            elif self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next') == True:
                self.logger.warn('다음 지역')
                self.lyb_mouse_click('victory_scene_next', custom_threshold=0)
                self.status = 0
            else:
                self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def quest_complete_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def combat_scene(self):

        elapsed_time = time.time() - self.get_checkpoint('last_detected')
        if elapsed_time > self.period_bot(15):
            self.status = 0

        bot_period = float(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period'))
        if bot_period != 0:
            self.game_object.interval = bot_period

        self.set_checkpoint('last_detected')

        pb_name = 'combat_scene_kill'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        if match_rate > 0.9:
            self.logger.warn(pb_name + ' ' + str(match_rate))
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            return self.status

        if (self.game_object.get_scene('main_scene').current_work == '모험' and
                    self.game_object.get_scene('main_scene').get_option('모험' + '_end_flag') == True
            ):
            pb_name = 'banbok_moheom_close_icon'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.warn(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.game_object.get_scene('banbok_moheom_stop_scene').status = 10
                return self.status

            pb_name = 'banbok_moheom_close_icon2'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.warn(pb_name + ' ' + str(match_rate))
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.game_object.get_scene('banbok_moheom_stop_scene').status = 10
                return self.status

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_checkpoint('tag_period')
            self.set_checkpoint('start')
            self.status += 1
        elif self.status >= 1 and self.status < 1000:
            tag_period = int(self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'))
            elapsed_time = time.time() - self.get_checkpoint('tag_period')
            if elapsed_time > tag_period:
                self.status = 1000
            else:
                self.loggingElapsedTime("TAG", int(elapsed_time), tag_period, period=2)
                if lybgameblade2.LYBBlade2.auto_combat_list.index(
                        self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto')) == 1:
                    self.auto_on()
                else:
                    self.auto_on_skill_off()

            elapsed_time = time.time() - self.get_checkpoint('start')
            if elapsed_time > 600:
                self.logger.warn('모험이 10분 이상 진행 중... 캐릭터 강제 이동 실행')
                if int(elapsed_time) % 20 < 4:
                    random_direction = int(random.random() * 8)
                    self.logger.warn('랙 방지 움직임: ' + str(lybgameblade2.LYBBlade2.character_move_list[random_direction]))
                    self.lyb_mouse_drag('character_move_direction_center',
                                        'character_move_direction_' + str(random_direction), stop_delay=5)

            self.status += 1
        elif self.status >= 1000 and self.status < 1003:
            self.lyb_mouse_click('combat_scene_tag', custom_threshold=0)
            self.set_checkpoint('tag_period')
            self.status += 1
        else:
            self.status = 1

        return self.status

    def jeontoo_start_scene(self):

        hero1 = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1')
        hero2 = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2')

        first_hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(hero1))
        second_hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(hero2))

        if first_hero_index == second_hero_index:
            self.logger.warn('영웅 중복 선택됨: ' + hero1 + ' ' + hero2)
            second_hero_index = (first_hero_index + 1) % len(lybgameblade2.LYBBlade2.hero_list)

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('limit_count', 0)
            self.status += 1

        elif self.status == 1:
            if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use') == False:
                self.status = 4
                return self.status

            self.status += self.jeontoo_scene_clear_list('jeontoo_start_scene_hero_', first_hero_index,
                                                         second_hero_index)
        elif self.status == 2:
            self.status += self.jeontoo_scene_select_first('jeontoo_start_scene_hero_', first_hero_index)
        elif self.status == 3:
            self.status += self.jeontoo_scene_select_second('jeontoo_start_scene_hero_', second_hero_index)
        elif self.status >= 4 and self.status < 8:

            pb_name = 'jeontoo_start_scene_repeat_lock'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.warn(pb_name + ' ' + str(match_rate))
            if match_rate < 0.9:
                pb_name = 'jeontoo_start_scene_repeat'
                if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat') == True:
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        return self.status
                else:
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        return self.status

                pb_name = 'jeontoo_start_scene_triple'
                if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple') == True:
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        return self.status
                else:
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate < 0.9:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        return self.status

            self.lyb_mouse_click('jeontoo_start_scene_start', custom_threshold=0)
            self.game_object.get_scene('combat_scene').status = 0
            self.game_object.get_scene('jeontoo_defeat_scene').status = 99999
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def jeontoo_ready_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status >= 1 and self.status < 5:
            self.lyb_mouse_click('jeontoo_ready_scene_junbi', custom_threshold=0)
            self.game_object.get_scene('jeontoo_start_scene').status = 0
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def npc_scene(self):

        if self.status >= 0 and self.status < 10:

            # 초기화
            self.game_object.get_scene('jeontoo_ready_scene').status = 0
            self.game_object.get_scene('gyeoltoo_scene').status = 0

            self.logger.warn('scene: ' + self.scene_name)
            pb_name = 'npc_scene_skip'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(570, 360, 610, 389))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status = 0
                return self.status

            pb_list = ['npc_scene_move', 'npc_scene_bosang', 'npc_scene_barogagi']
            for pb_name in pb_list:
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.8:
                    self.init_ililquest_scene();
                    if pb_name != 'npc_scene_barogagi':
                        self.lyb_mouse_click(pb_name)
                    else:
                        if self.get_option('clicked') != True:
                            if self.get_game_config(
                                            lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue') == False:
                                self.status = 10
                                return self.status
                        self.lyb_mouse_click(pb_name)

                    self.set_option('clicked', False)

                    self.status = 0
                    return self.status

            self.logger.info('대화창 닫기 대기 중...' + str(self.status) + '/10')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')
            self.status = 0

        return self.status

    def mail_scene(self):

        if self.get_option('immediate_back') == True:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.set_option('immediate_back', False)
            return self.status

        if self.scene_name == 'immu_scene':
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'immu_scene')
            if match_rate < 0.9:
                return self.status

            pb_name = 'immu_scene_suryeong'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.95:
                self.lyb_mouse_click(pb_name);
                return self.status

        if self.scene_name == 'mail_scene':
            pb_name = 'mail_scene_select_hero'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.95:
                cfg_hero = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero')
                hero_index = int(lybgameblade2.LYBBlade2.hero_list.index(cfg_hero))
                self.lyb_mouse_click('mail_scene_select_hero_' + str(hero_index), custom_threshold=0)
                self.game_object.current_matched_scene['name'] = ''
                self.set_option('limit_count_inner', 0)
                return self.status

            pb_name = 'mail_scene_select_stone'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate > 0.95:
                cfg_hero = self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone')
                hero_index = int(lybgameblade2.LYBBlade2.stone_list.index(cfg_hero))
                self.lyb_mouse_click('mail_scene_select_stone_' + str(hero_index), custom_threshold=0)
                self.game_object.current_matched_scene['name'] = ''
                self.set_option('limit_count_inner', 0)
                return self.status

        if self.status == 0:
            self.set_option('limit_count', 0)
            self.set_option('limit_count_inner', 0)
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            limit_count = self.get_option('limit_count')
            if limit_count > 3:
                self.status = 99999
            else:
                for i in range(3):
                    pb_name = 'mail_scene_new_' + str(i)
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(0, 50, 20, 360))
                    self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.set_option('limit_count_inner', 0)
                        self.set_option('limit_count', limit_count + 1)
                        self.lyb_mouse_click_location(loc_x + 10, loc_y + 5)
                        self.status += 1
                        return self.status
                self.status = 99999
        elif self.status == 2:
            self.status += 1
        elif self.status == 3:
            limit_count_inner = self.get_option('limit_count_inner')
            if limit_count_inner > 3:
                self.status = 1
            else:
                pb_name = 'immu_scene_new'
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(210, 330, 460, 360))
                self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.set_option('limit_count_inner', limit_count_inner + 1)
                    self.lyb_mouse_click_location(loc_x - 15, loc_y + 15)
                    self.status = 2
                    return self.status

                for i in range(2):
                    pb_name = 'mail_scene_bosang_' + str(i)
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(530, 70, 630, 380))
                    self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.set_option('limit_count_inner', limit_count_inner + 1)
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        self.game_object.get_scene('mail_select_hero_scene').status = 0
                        self.status = 2
                        return self.status

                self.status = 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def chulseokbosang_scene(self):

        match_rate = self.game_object.rateMatchedResource(self.window_pixels, 'chulseokbosang_scene')
        if match_rate < 0.9:
            return self.status

        if self.status == 0:
            self.set_option('limit_count', 0)
            self.set_option('limit_count_inner', 0)
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.status += 1
        elif self.status == 2:
            limit_count = self.get_option('limit_count')
            if limit_count > 3:
                self.status = 99999
            else:
                for i in range(2):
                    pb_name = 'chulseokbosang_scene_new_' + str(i)
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(90, 50, 125, 360))
                    self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.set_option('limit_count_inner', 0)
                        self.set_option('limit_count', limit_count + 1)
                        self.lyb_mouse_click_location(loc_x - 50, loc_y + 30)
                        self.status += 1
                        return self.status
                self.status = 99999
        elif self.status == 3:
            self.status += 1
        elif self.status == 4:
            limit_count_inner = self.get_option('limit_count_inner')
            if limit_count_inner > 1:
                self.status = 1
            else:
                for i in range(2):
                    pb_name = 'chulseokbosang_scene_bosang_' + str(i)
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.7,
                        custom_flag=1,
                        custom_rect=(120, 60, 620, 380))
                    self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.set_option('limit_count_inner', limit_count_inner + 1)
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        self.status = 3
                        return self.status
                self.status = 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

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
            for each_icon in lybgameblade2.LYBBlade2.blade2_icon_list:
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
            for each_icon in lybgameblade2.LYBBlade2.blade2_icon_list:
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

    # MAIN

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

        elif self.status == self.get_work_status('메인 퀘스트'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(600):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

        elif (self.status == self.get_work_status('일대일 대전') or
                      self.status == self.get_work_status('팀 대전') or
                      self.status == self.get_work_status('점령전')
              ):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('gyeoltoo_scene').status = self.status
            self.lyb_mouse_click('main_scene_gyeoltoo', custom_threshold=0)

        elif (self.status == self.get_work_status('레이드') or
                      self.status == self.get_work_status('영웅의 탑') or
                      self.status == self.get_work_status('반격 던전')
              ):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('dojeon_scene').status = self.status
            self.lyb_mouse_click('main_scene_dojeon', custom_threshold=0)

        elif (self.status == self.get_work_status('모두팔기') or
                      self.status == self.get_work_status('장비교체')
              ):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('jangbiham_scene').status = self.status
            self.lyb_mouse_click('main_scene_jangbiham', custom_threshold=0)

        elif self.status == self.get_work_status('모험'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('moheom_select_scene').status = 0
            self.lyb_mouse_click('main_scene_moheom', custom_threshold=0)

        elif self.status == self.get_work_status('우편함'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('mail_scene').status = 0
            self.lyb_mouse_click('main_scene_mail', custom_threshold=0)


        elif (self.status == self.get_work_status('친구') or
                      self.status == self.get_work_status('자동분해') or
                      self.status == self.get_work_status('명예의 전당')
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

        # [레이드] 알림 탐색	
        if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice') == True:
            pb_name = 'main_scene_notice_raid'
            elapsed_time = time.time() - self.get_checkpoint(pb_name)
            if elapsed_time > 60:
                self.set_checkpoint(pb_name)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_top_level=(255, 255, 255),
                    custom_below_level=(140, 200, 255),
                    custom_rect=(600, 60, 630, 110))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.logger.warn('레이드 알림 클릭')
                    self.game_object.get_scene('raid_scene').status = 0
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return True

        # [점령전] 알림 탐색	
        # if self.getPoint() > 100000000:
        # 	if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice') == True:
        # 		pb_name = 'main_scene_notice_jeomryoungjeon'		
        # 		elapsed_time = time.time() - self.get_checkpoint(pb_name)
        # 		if elapsed_time > 60:
        # 			self.set_checkpoint(pb_name)
        # 			(loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
        # 										self.window_image,
        # 										self.game_object.resource_manager.pixel_box_dic[pb_name],
        # 										custom_threshold=0.7,
        # 										custom_flag=1,
        # 										custom_top_level=(255, 255, 255),
        # 										custom_below_level=(140, 200, 255),
        # 										custom_rect=(600, 60, 630, 110))
        # 			self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        # 			if loc_x != -1:
        # 				self.logger.warn('점령전 알림 클릭')
        # 				self.game_object.get_scene('raid_scene').status = 0
        # 				self.lyb_mouse_click_location(loc_x, loc_y)
        # 				return True

        # 임무 완료 탐색		
        pb_name = 'main_scene_complete'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(20, 60, 50, 240))
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
            self.lyb_mouse_click_location(loc_x, loc_y)
            return True

        # [일일] 탐색	
        if self.get_game_config(lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest') == True:
            pb_name = 'main_scene_ilil'
            elapsed_time = time.time() - self.get_checkpoint(pb_name)
            if elapsed_time > 300:
                self.set_checkpoint(pb_name)
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(40, 60, 70, 240))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.init_ililquest_scene();
                    self.game_object.get_scene('npc_scene').set_option('clicked', True)
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    return True

        return False

    def auto_off(self, pb_name='auto_on'):

        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.95:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            return True

        return False

    def auto_on(self, pb_name='auto_on'):

        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate < 0.95:
            auto_threshold = self.get_option('auto_threshold')
            if auto_threshold == None:
                auto_threshold = 0

            if auto_threshold > 1:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.set_option('auto_threshold', 0)
                return True
            else:
                self.set_option('auto_threshold', auto_threshold + 1)
        else:
            self.set_option('auto_threshold', 0)

        return False

    def auto_on_skill_off(self, pb_name='auto_on_skill_off'):
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_flag=1,
            custom_top_level=(225, 180, 120),
            custom_below_level=(190, 145, 70),
            custom_rect=(520, 30, 560, 70)
        )
        self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x == -1:
            threshold = self.get_option(pb_name + 'threshold')
            if threshold == None:
                threshold = 0

            if threshold > 1:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.set_option(pb_name + 'threshold', 0)
                return True
            else:
                self.set_option(pb_name + 'threshold', threshold + 1)
        else:
            self.set_option(pb_name + 'threshold', 0)

        return False

    def jeontoo_scene_clear_list(self, prefix, first_hero_index, second_hero_index, last=3):

        first_pb_name = prefix + str(first_hero_index) + '_1'
        second_pb_name = prefix + str(second_hero_index) + '_2'
        first_match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, first_pb_name, custom_tolerance=70)
        self.logger.warn(first_pb_name + ' ' + str(first_match_rate))
        second_match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, second_pb_name,
                                                                 custom_tolerance=70)
        self.logger.warn(second_pb_name + ' ' + str(second_match_rate))

        if first_match_rate > 0.98 and second_match_rate > 0.98:
            return last

        for i in range(len(lybgameblade2.LYBBlade2.hero_list)):
            pb_name = prefix + str(i) + '_0'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
            self.logger.warn(pb_name + ' ' + str(match_rate))
            if match_rate < 0.98:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                return 0

        return 1

    def jeontoo_scene_select_first(self, prefix, first_hero_index):
        self.logger.info('영웅 선택 1 => ' + str(lybgameblade2.LYBBlade2.hero_list[first_hero_index]))
        for i in range(len(lybgameblade2.LYBBlade2.hero_list)):
            if i == first_hero_index:
                pb_name = prefix + str(i) + '_0'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.98:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return 0

                pb_name = prefix + str(i) + '_1'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.98:
                    return 1

                pb_name = prefix + str(i) + '_2'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.98:
                    return -1

        return 0

    def jeontoo_scene_select_second(self, prefix, second_hero_index):
        self.logger.info('영웅 선택 2 => ' + str(lybgameblade2.LYBBlade2.hero_list[second_hero_index]))

        for i in range(len(lybgameblade2.LYBBlade2.hero_list)):
            if i == second_hero_index:
                pb_name = prefix + str(i) + '_0'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.98:
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    return 0

                pb_name = prefix + str(i) + '_1'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.98:
                    return -2

                pb_name = prefix + str(i) + '_2'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=70)
                self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate > 0.98:
                    return 1

    def init_ililquest_scene(self):
        self.game_object.get_scene('gyeoltoo_0_scene').status = 0
        self.game_object.get_scene('gyeoltoo_1_scene').status = 0
        self.game_object.get_scene('moheom_scene').status = 0
        self.game_object.get_scene('jangbiham_scene').status = 0

    def indexOfRaidBoss(self):
        today = time.strftime("%a")
        boss_index = 0
        self.logger.info("요일: " + str(today))
        if today == "Tue" or today == "Thu" or today == "Sat":
            boss_index = 1

        return boss_index

    def getPoint(self):
        if self.game_object.lybhttp == None:
            self.game_object.lybhttp = self.game_object.login_gnu_board()
            self.game_object.lybhttp.get_chatid()

        return int(self.game_object.lybhttp.mb_point)

    def get_work_status(self, work_name):
        if work_name in lybgameblade2.LYBBlade2.work_list:
            return (lybgameblade2.LYBBlade2.work_list.index(work_name) + 1) * 1000
        else:
            return 99999

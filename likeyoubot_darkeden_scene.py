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
            self.lyb_mouse_click('sangjeom_scene_hp_potion', custom_threshold=0)
            self.game_object.get_scene('buy_confirm_scene').status = 0
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def death_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.end_work()
            self.status += 1
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
            (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(500, 420, 580, 470))
            self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status = 0
                return self.status
            
            if self.status > 60 and self.status % 5 == 0:
                self.lyb_mouse_click('character_move_1', custom_threshold=0)
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
        elif self.status == self.get_work_status('토벌대'):
            self.status = 200
        elif self.status == 200:
            self.game_object.get_scene('tobeolde_scene').status = 0
            self.lyb_mouse_click('dungeon_scene_tobeolde', custom_threshold=0)
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
            pb_name = 'tobeolde_scene_tab_' + str(0)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
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
                self.lyb_mouse_click('main_scene_quest_0', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 0 < inner_status < 60:
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
                self.lyb_mouse_click('main_scene_quest_3', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 0 < inner_status < 60:
                if self.is_complete_quest():
                    self.set_option(self.current_work + '_inner_status', 0)
                    return self.status

                if self.isAutoCombat(limit_count=3) is False:
                    self.lyb_mouse_click('main_scene_auto_0', custom_threshold=0)
                    return self.status

                if self.isCenterAutoCombat(limit_count=3) is False:
                    self.lyb_mouse_click('main_scene_auto_0', custom_threshold=0)
                    return self.status

                self.set_option(self.current_work + '_inner_status', inner_status + 1)
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
        pb_name = 'main_scene_quick_move'
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(5):
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

        pb_name = 'main_scene_looting'
        elapsed_time = time.time() - self.get_checkpoint(pb_name)
        if elapsed_time > self.period_bot(5):
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
                self.set_checkpoint(pb_name)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.logger.info('줍기 클릭')
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
                    custom_top_level=(20, 255, 20),
                    custom_below_level=(0, 100, 0),
                    custom_flag=1,
                    custom_rect=(5, 150, 170, 320))
            else:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.65,
                    custom_top_level=(20, 255, 20),
                    custom_below_level=(0, 100, 0),
                    custom_flag=1,
                    custom_rect=(5, 150, 170, 320))

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
                custom_threshold=0.6,
                custom_top_level=(255, 255, 255),
                custom_below_level=(100, 100, 100),
                custom_flag=1,
                custom_rect=(5, 150 + (quest_index * 25), 170, 180 + (quest_index * 30)))
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
            0.6,
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
            0.6,
            -1, -1,
            (350, 300, 450, 370),
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

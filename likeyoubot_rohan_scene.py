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
            if self.isJeolJeonHpEmpty():
                self.game_object.get_scene('main_scene').set_option('hp_potion_empty', True)
                self.status = 99999
            if self.isJeolJeonMpEmpty():
                self.game_object.get_scene('main_scene').set_option('mp_potion_empty', True)
                self.status = 99999
            if self.isJeolJeonQuestComplete():
                self.game_object.get_scene('main_scene').set_option('quest_complete', True)
                self.status = 99999

            current_work = self.game_object.get_scene('main_scene').current_work
            if current_work == '자동 사냥':
                cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_ROHAN_WORK + 'auto_duration'))
                elapsed_time = time.time() - self.game_object.get_scene('main_scene').get_checkpoint(current_work + '_check_start')
                self.loggingElapsedTime('[' + str(current_work) + '] 경과 시간', elapsed_time, cfg_duration, period=0)
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
            if elapsed_time > self.period_bot(600):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

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
                if self.isMenuOpen():
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
                if self.isGabangOpen():
                    self.lyb_mouse_click('gabang_bunhe', custom_threshold=0)
                else:
                    if self.isGabangSelect():
                        self.lyb_mouse_click('gabang_select', custom_threshold=0)
                        self.game_object.get_scene('bunhe_select_scene').status = 0
                        self.set_option(self.current_work + '_inner_status', 100)
                    else:
                        self.lyb_mouse_click('menu_scene_gabang', custom_threshold=0)
            elif 100 <= inner_status < 102:
                self.lyb_mouse_click('gabang_select_ok', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif 102 <= inner_status < 110:
                if self.isGabangOpen():
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

        if self.is_complete_quest():
            return True

        if self.is_move_to_quest():
            return True

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
        return False

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


    def isGabangSelect(self):
        return self.isStatusByResource2('일괄 선택 감지', 'gabang_select_loc', 0.7, -1, reverse=True)

    def isGabangOpen(self):
        return self.isStatusByResource2('가방 열림 감지', 'gabang_open_loc', 0.7, -1, reverse=True)

    def isMenuOpen(self):
        return self.isStatusByResource2('메뉴 열림 감지', 'menu_open_loc', 0.7, -1, reverse=True)

    def isJeolJeonMpEmpty(self):
        return self.isStatusByResource2('절전모드 MP 포션 부족 감지', 'jeoljeon_scene_mp_potion_empty_loc', 0.9, 2, reverse=True)

    def isJeolJeonHpEmpty(self):
        return self.isStatusByResource2('절전모드 HP 포션 부족 감지', 'jeoljeon_scene_hp_potion_empty_loc', 0.9, 2, reverse=True)

    def isJeolJeonQuestComplete(self):
        return self.isStatusByResource2('절전모드 퀘스트 완료 감지', 'jeoljeon_scene_quest_complete_loc', 0.9, 3, reverse=True)

    def isStatusByResource2(self, log_message, resource_name, custom_threshold, limit_count=-1, reverse=False):
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > custom_threshold and reverse == False:
            self.set_option(resource_name + 'check_count', 0)
            return False

        if match_rate < custom_threshold and reverse == True:
            self.set_option(resource_name + 'check_count', 0)
            return False

        check_count = self.get_option(resource_name + 'check_count')
        if check_count == None:
            check_count = 0

        if check_count > limit_count:
            self.set_option(resource_name + 'check_count', 0)
            return True

        if check_count > 0:
            self.logger.debug(log_message + '..(' + str(check_count) + '/' + str(limit_count) + ')')
        self.set_option(resource_name + 'check_count', check_count + 1)

        return False

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
import likeyoubot_kaiser as lybgamekaiser
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time


class LYBKaiserScene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)
        self.logger.warn('중요: 설정에서 그래픽 옵션을 낮음으로 설정해야 정상 동작합니다.')

    def process(self, window_image, window_pixels):

        super(LYBKaiserScene, self).process(window_image, window_pixels)

        rc = 0
        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'waiting_scene':
            rc = self.waiting_scene()
        elif self.scene_name == 'jeoljeonmode_scene':
            rc = self.jeoljeonmode_scene()
        elif self.scene_name == 'quest_accept_scene':
            rc = self.quest_accept_scene()
        elif self.scene_name == 'quest_complete_scene':
            rc = self.quest_complete_scene()
        elif self.scene_name == 'tutorial_14_0_scene':
            rc = self.tutorial_14_0_scene()
        elif self.scene_name == 'tutorial_14_1_scene':
            rc = self.tutorial_14_0_scene()
        elif self.scene_name == 'tutorial_14_2_scene':
            rc = self.tutorial_14_0_scene()
        elif self.scene_name == 'tutorial_0628_0_scene':
            rc = self.tutorial_14_0_scene()
        elif self.scene_name == 'tutorial_0628_1_scene':
            rc = self.tutorial_14_0_scene()
        elif self.scene_name == 'popup_scene':
            rc = self.popup_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'login_12_scene':
            rc = self.login_scene()
        elif self.scene_name == 'wanted_scene':
            rc = self.wanted_scene()
        elif self.scene_name == 'menu_scene':
            rc = self.menu_scene()
        elif self.scene_name == 'mail_scene':
            rc = self.mail_scene()
        elif self.scene_name == 'quickslot_scene':
            rc = self.quickslot_scene()
        elif self.scene_name == 'death_scene':
            rc = self.death_scene()
        elif self.scene_name == 'quest_scene':
            rc = self.quest_scene()
        elif self.scene_name == 'chulseok_0707_scene':
            rc = self.chulseok_0707_scene()





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

    def chulseok_0707_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            for i in range(7):
                pb_name = 'chulseok_0707_scene_receive_' + str(i)
                self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def quest_scene(self):

        limit_count = self.get_option('limit_count')
        if limit_count == None:
            limit_count = 0

        if limit_count > 100:
            self.status = 99999
        else:
            self.set_option('limit_count', limit_count + 1)

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('limit_count', 0)
            self.status += 1
        elif self.status == 1:
            pb_name = 'quest_scene_alert'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(1, 90, 25, 320))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status += 1
            else:
                self.status = 99999
        elif self.status == 2:
            pb_name = 'quest_scene_alert'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(80, 90, 120, 360))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            self.status += 1
        elif self.status == 3:
            pb_name = 'quest_scene_receive_1'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(100, 270, 630, 320))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            else:
                self.status += 1
        elif self.status == 4:
            pb_name = 'quest_scene_receive_2'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(520, 100, 630, 370))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            else:
                self.status = 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def death_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            if self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death') == True:
                self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 캐릭터 사망 감지')
                png_name = self.game_object.save_image('character_death')
                self.game_object.telegram_send('', image=png_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def quickslot_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.set_option('slot_iterator', 0)
            self.lyb_mouse_click('quickslot_scene_etc', custom_threshold=0)
            self.status += 1
        elif self.status == 1:
            iterator = self.get_option('slot_iterator')
            if iterator == None:
                iterator = 0

            for i in range(iterator, 12):
                pb_name = 'main_scene_slot_' + str(i)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=70,
                                                                  custom_top_level=110)
                # self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate < 0.8:
                    self.logger.warn(pb_name + ' not empty pass')
                    continue

                cfg_quickslot_item = self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(i))
                slot_item_index = lybgamekaiser.LYBKaiser.slot_item_list.index(cfg_quickslot_item)
                self.logger.warn(str(i + 1) + ' 번 슬롯: ' + str(cfg_quickslot_item) + ' (' + str(slot_item_index) + ')')
                if slot_item_index == 0:
                    continue
                elif (slot_item_index == lybgamekaiser.LYBKaiser.slot_item_list.index('소형 체력 물약') or
                              slot_item_index == lybgamekaiser.LYBKaiser.slot_item_list.index('중형 체력 물약') or
                              slot_item_index == lybgamekaiser.LYBKaiser.slot_item_list.index('속도의 물약') or
                              slot_item_index == lybgamekaiser.LYBKaiser.slot_item_list.index('전투의 물약') or
                              slot_item_index == lybgamekaiser.LYBKaiser.slot_item_list.index('펫 소환 주문서')
                      ):
                    self.lyb_mouse_click('quickslot_scene_somopum', custom_threshold=0)
                    self.set_option('slot_iterator', i)
                    self.status += 1
                    return self.status
                else:
                    self.lyb_mouse_click('quickslot_scene_etc', custom_threshold=0)
                    self.set_option('slot_iterator', i)
                    self.status += 1
                    return self.status

            self.status = 99999
        elif self.status == 2:
            # iterator = self.get_option('slot_iterator')
            # pb_name = 'main_scene_slot_' + str(iterator)
            # self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 3 or self.status == 5 or self.status == 7:
            iterator = self.get_option('slot_iterator')
            cfg_quickslot_item = self.get_game_config(
                lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(iterator))
            slot_item_index = lybgamekaiser.LYBKaiser.slot_item_list.index(cfg_quickslot_item)

            pb_name = 'quickslot_scene_item_' + str(slot_item_index)
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(430, 110, 635, 335))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
                self.status = 10
            else:
                self.status += 1
        elif self.status == 4 or self.status == 6:
            self.lyb_mouse_drag('quickslot_scene_drag_bot', 'quickslot_scene_drag_top')
            self.status += 1
        elif self.status == 8:
            iterator = self.get_option('slot_iterator')
            cfg_quickslot_item = self.get_game_config(
                lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(iterator))
            self.logger.warn(str(iterator + 1) + ' 번 슬롯 아이템 등록 실패')
            if self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty') == True:
                self.game_object.telegram_send(
                    '창 이름 [' + str(self.game_object.window_title) + ']에서 ' + str(iterator + 1) + '번 슬롯에 [' + str(
                        cfg_quickslot_item) + '] 아이템 등록 실패')
                png_name = self.game_object.save_image('quickslot_item_empty')
                self.game_object.telegram_send('', image=png_name)

            self.status = 20
        elif self.status == 10:
            iterator = self.get_option('slot_iterator')
            pb_name = 'main_scene_slot_' + str(iterator)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status += 1
        elif self.status == 11:
            self.status += 1
        elif self.status == 12:
            iterator = self.get_option('slot_iterator')
            pb_name = 'quickslot_scene_auto_on_' + str(iterator)
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=190,
                                                              custom_top_level=255)
            # self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate < 0.9:
                self.lyb_mouse_click('main_scene_slot_' + str(iterator), custom_threshold=0)
            self.status = 20
        elif self.status == 20:
            iterator = self.get_option('slot_iterator')
            self.lyb_mouse_click('quickslot_scene_etc', custom_threshold=0)
            self.set_option('slot_iterator', iterator + 1)
            self.status = 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def mail_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('mail_scene_receive_all')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def menu_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == self.get_work_status('우편'):
            self.game_object.get_scene('mail_scene').status = 0
            self.lyb_mouse_click('menu_scene_mail', custom_threshold=0)
            self.status += 1
        elif self.status == self.get_work_status('퀘스트'):
            self.game_object.get_scene('quest_scene').status = 0
            self.lyb_mouse_click('menu_scene_quest', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def wanted_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            pb_name = 'wanted_scene_bosang'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(130, 310, 520, 360))
            self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y)
            else:
                self.status += 1
        elif self.status == 2:
            quest_number = 2
            cfg_quest_number = int(
                self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number')) - 1
            if cfg_quest_number == -1:
                for i in range(3):
                    pb_name = 'wanted_scene_rank_limit_' + str(i)
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate < 0.9:
                        quest_number = i
                        break
            else:
                quest_number = cfg_quest_number

            self.logger.info(
                "수락 번호를 (0)으로 설정하면 [현상 수배] 3개를 10단계가 될 때까지 순서대로 진행합니다. 현상 수배 번호 클릭==> " + str(quest_number))
            self.lyb_mouse_click('wanted_scene_quest_' + str(quest_number))
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def popup_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('popup_scene_today')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def tutorial_14_0_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        else:
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            time.sleep(0.1)
            self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)
            self.status = 0

        return self.status

    def waiting_scene(self):

        if self.status >= 0 and self.status < 1000:
            self.logger.warn('scene: ' + self.scene_name)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def quest_accept_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_inner_status', 0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon')

            self.status = 0

        return self.status

    def quest_complete_scene(self):

        if self.status == 0:
            self.logger.warn('scene: ' + self.scene_name)
            self.game_object.get_scene('main_scene').set_option('메인 퀘스트' + '_inner_status', 0)
            self.status += 1
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
            for each_icon in lybgamekaiser.LYBKaiser.nox_kaiser_icon_list:
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
            for each_icon in lybgamekaiser.LYBKaiser.momo_kaiser_icon_list:
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

    #
    # MAIN SCENE
    #

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

        elif (self.status == self.get_work_status('메인 퀘스트') or
                      self.status == self.get_work_status('지역 퀘스트')
              ):

            elapsed_time = self.get_elapsed_time()

            if self.status == self.get_work_status('메인 퀘스트'):

                duration_limit = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration'))
                distance_check_limit = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance'))
                distance_green_pb = 'main_quest_distance_green'
                gold_pb = 'main_quest_gold'
                distance_green_rect = (110, 135, 140, 165)
                alert_color = 'yellow'
                alert_below_level = (250, 215, 55)
                alert_top_level = (255, 225, 65)
                auto_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto'))
                quest_letter_pb = 'main_quest_main'
                quest_letter_below_level = (70, 90, 20)
                quest_letter_top_level = (120, 140, 40)
                quest_index = 0
                quest_distance_limit = 0

            elif self.status == self.get_work_status('지역 퀘스트'):

                duration_limit = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration'))
                distance_check_limit = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance'))
                distance_green_pb = 'main_quest_distance_green_2'
                gold_pb = 'main_quest_gold_2'
                distance_green_rect = (110, 165, 140, 185)
                alert_color = 'green'
                alert_below_level = (60, 220, 25)
                alert_top_level = (70, 235, 50)
                auto_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto'))
                quest_letter_pb = 'main_quest_jiyeok'
                quest_letter_below_level = (130, 100, 10)
                quest_letter_top_level = (180, 130, 30)
                quest_index = 1
                quest_distance_limit = 100

            if duration_limit != 0 and elapsed_time > duration_limit:
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', 0)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status == None:
                inner_status = 0

            # self.logger.debug('main_scene: inner_status ' + str(inner_status))

            if inner_status == 0:
                self.lyb_mouse_click('main_scene_quest_tab', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 1:
                if self.auto_off() == True:
                    return self.status

                if self.target_off() == True:
                    return self.status

                self.lyb_mouse_drag('main_scene_drag_left', 'main_scene_drag_right')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 2:
                self.lyb_mouse_click('main_scene_camera_h', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 3:
                self.lyb_mouse_click('main_scene_camera_h', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 4:
                pb_name = 'main_scene_camera_h'
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
                # self.logger.warn(pb_name + ' ' + str(match_rate))
                if match_rate < 0.9:
                    self.lyb_mouse_click('main_scene_camera_h', custom_threshold=0)
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 5:
                self.lyb_mouse_drag('main_scene_drag_top', 'main_scene_drag_bot')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 6:
                self.lyb_mouse_drag('main_scene_drag_top', 'main_scene_drag_bot')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 7:
                self.lyb_mouse_drag('main_scene_drag_bot', 'main_scene_drag_top')
                self.set_option(self.current_work + '_inner_status', 10)
            elif inner_status >= 10 and inner_status < 999:

                # self.main_scene_check_distance(quest_index)
                pb_name = distance_green_pb

                if self.is_complete_quest(quest_index) == True:
                    # self.lyb_mouse_click(pb_name, custom_threshold=0)
                    self.set_option(self.current_work + '_inner_status', 1000)
                    self.game_object.get_scene('wanted_scene').status = 0

                    self.game_object.addStatistic('퀘스트 완료 횟수')
                    if self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete') == True:
                        self.game_object.telegram_send('창 이름 [' + str(self.game_object.window_title) + ']에서 퀘스트 완료 감지됨')
                        png_name = self.game_object.save_image('quest_complete')
                        self.game_object.telegram_send('', image=png_name)

                    return self.status

                if quest_distance_limit == 0 or inner_status < 15:
                    # 1. 퀘스트 거리 색상이 녹색인가?
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.9,
                        custom_below_level=(50, 100, 100),
                        custom_top_level=(110, 210, 200),
                        custom_flag=1,
                        custom_rect=distance_green_rect)
                # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                elif quest_distance_limit == 100:
                    cfg_distance = int(
                        self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit'))

                    distance, (loc_x, loc_y) = self.main_scene_check_distance(quest_index)
                    if loc_x != -1:
                        if cfg_distance < 100:
                            self.logger.warn('퀘스트 위치로부터 100 미터 이상 감지됨')
                            # 100미터 이상 벗어났다는 의미이다.
                            loc_x = -1
                    else:

                        distance, (loc_x, loc_y) = self.main_scene_check_distance2(quest_index)
                        if loc_x != -1:
                            if distance * 10 >= cfg_distance:
                                self.logger.warn('퀘스트 위치로부터 ' + str(cfg_distance) + '미터 이상 감지됨')
                                loc_x = -1
                        else:
                            # 10미터 이하라는 뜻
                            loc_x = 0

                # 거리를 벗어났는가?
                if loc_x == -1:
                    distance_check = self.get_option('distance_check')
                    if distance_check == None:
                        distance_check = distance_check_limit
                    else:
                        self.logger.info('퀘스트 지역 이탈 감지됨: ' + str(distance_check) + '/' + str(distance_check_limit))

                    if distance_check >= distance_check_limit:
                        self.lyb_mouse_click(pb_name, custom_threshold=0)
                        self.set_option(self.current_work + '_inner_status', 1000)
                        self.set_option('distance_check', 0)
                        self.game_object.get_scene('wanted_scene').status = 0
                        return self.status
                    else:
                        self.set_option('distance_check', distance_check + 1)

                if inner_status < 30:
                    if self.target_off() == True:
                        return self.status

                    if self.status == self.get_work_status('지역 퀘스트'):
                        # 현상 수배 NPC를 찾자.
                        s = time.time()
                        for i in range(3):
                            pb_name = 'main_scene_wanted_npc_' + str(i)
                            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                                self.window_image,
                                self.game_object.resource_manager.pixel_box_dic[pb_name],
                                custom_threshold=0.75,
                                custom_flag=1,
                                custom_rect=(135, 60, 520, 290))
                            e = time.time()
                            # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate) + ' ' + str(round(e-s, 2)))
                            if loc_x != -1:
                                if self.auto_off() == True:
                                    time.sleep(1)
                                self.lyb_mouse_click_location(loc_x, loc_y)
                                self.set_option('distance_check', None)
                                self.set_option(self.current_work + '_inner_status', 1200)
                                return self.status
                            # 2. 퀘스트 느낌표를 찾았는가?
                    s = time.time()
                    for i in range(3):
                        pb_name = 'main_scene_' + alert_color + '_alert_' + str(i)
                        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                            self.window_image,
                            self.game_object.resource_manager.pixel_box_dic[pb_name],
                            custom_threshold=0.6,
                            custom_below_level=alert_below_level,
                            custom_top_level=alert_top_level,
                            custom_flag=1,
                            custom_rect=(135, 60, 520, 290))
                        e = time.time()
                        # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate) + ' ' + str(round(e-s, 2)))
                        # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
                        if loc_x != -1:
                            if self.auto_off() == True:
                                time.sleep(1)
                            self.lyb_mouse_click_location(loc_x, loc_y)
                            self.set_option('distance_check', None)
                            self.set_option(self.current_work + '_inner_status', 1200)
                            return self.status

                else:
                    pb_name = 'main_scene_camera_h'
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_tolerance=100)
                    # self.logger.warn(pb_name + ' ' + str(match_rate))
                    if match_rate > 0.9:
                        self.lyb_mouse_click('main_scene_camera_h', custom_threshold=0)

                if inner_status > 15:
                    if self.main_scene_check_quest(quest_letter_pb, quest_letter_top_level,
                                                   quest_letter_below_level) == False:
                        quest_letter_pb_check_count = self.get_option(quest_letter_pb + '_check_count')
                        if quest_letter_pb_check_count == None:
                            quest_letter_pb_check_count = 0

                        if quest_letter_pb_check_count > 5:
                            self.lyb_mouse_click('main_scene_quest_tab', custom_threshold=0)
                            self.set_option(self.current_work + '_inner_status', 2)
                            # self.auto_off()
                            if self.get_game_config(
                                            lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop') == True:
                                self.game_object.telegram_send(
                                    '창 이름 [' + str(self.game_object.window_title) + ']에서 지역 퀘스트 탐색 실패 감지. 확인 바랍니다.')
                                png_name = self.game_object.save_image('local_quest_stop')
                                self.game_object.telegram_send('', image=png_name)
                        else:
                            self.lyb_mouse_drag('main_scene_drag_left', 'main_scene_drag_right')
                            self.set_option(quest_letter_pb + '_check_count', quest_letter_pb_check_count + 1)
                            self.logger.info('지역 퀘스트 감지 실패(' + str(quest_letter_pb_check_count) + '/5)')

                        self.set_option('auto_threshold', 0)
                        return self.status
                    else:
                        self.set_option(quest_letter_pb + '_check_count', 0)

                    if self.auto_on(auto_limit=auto_limit) == True:
                        return self.status

                if inner_status % 3 == 0:
                    self.lyb_mouse_drag('main_scene_drag_left', 'main_scene_drag_right')
                # elif inner_status % 10 == 0:
                # 	direction_index = int(inner_status / 10) % 8
                # 	self.lyb_mouse_drag('character_move_direction_center', 'character_move_direction_' + str(direction_index), stop_delay=1)

                self.set_option(self.current_work + '_inner_status', inner_status + 1)

            elif inner_status >= 1000 and inner_status < 1200:
                self.logger.warn('퀘스트 추적 중...')

                if self.horse_on() == True:
                    return self.status

                pb_name = gold_pb
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                # self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate < 0.8:
                    self.set_option(self.current_work + '_inner_status', 0)
                    return self.status

                # 100. 퀘스트 거리 색상이 녹색인가?
                pb_name = distance_green_pb
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.9,
                    custom_below_level=(50, 100, 100),
                    custom_top_level=(110, 210, 200),
                    custom_flag=1,
                    custom_rect=distance_green_rect)
                # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.set_option(self.current_work + '_inner_status', 0)
                    return self.status
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status >= 1200 and inner_status < 1210:
                self.logger.warn('퀘스트 상호 작용 중...')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            else:
                self.logger.warn('퀘스트 변동 사항 체크')
                self.set_option(self.current_work + '_inner_status', 0)

        elif self.status == self.get_work_status('퀵슬롯 등록'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.current_matched_scene['name'] = ''
            self.lyb_mouse_click('main_scene_quickslot', custom_threshold=0)
            self.game_object.get_scene('quickslot_scene').status = 0

        elif self.status == self.get_work_status('자동 사냥'):

            elapsed_time = self.get_elapsed_time()
            limit_time = int(self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration'))
            auto_limit = int(self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count'))
            if elapsed_time > self.period_bot(limit_time):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            if self.auto_on(auto_limit=auto_limit) == True:
                return self.status

            self.loggingElapsedTime(self.current_work, int(elapsed_time), limit_time, period=60)

        elif self.status == self.get_work_status('일괄 분해'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(60):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            inner_status = self.get_option(self.current_work + '_inner_status')
            if inner_status == None:
                inner_status = 0

            self.logger.info('inner_status ' + str(inner_status))
            if inner_status == 0:
                resource_name = 'main_scene_inventory_loc'
                match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
                if match_rate > 0.8:
                    self.lyb_mouse_click('inventory_sort', custom_threshold=0)
                    self.set_option(self.current_work + '_inner_status', inner_status + 1)
                else:
                    self.lyb_mouse_click('main_scene_gabang', custom_threshold=0)
            elif inner_status == 1:
                resource_name = 'main_scene_ilgwalbunhe_loc'
                match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
                if match_rate > 0.8:
                    self.set_option(self.current_work + '_inner_status', inner_status + 1)
                    self.set_option(self.current_work + '_check_gold', 0)
                else:
                    self.lyb_mouse_click('main_scene_inventory_bunhe')
            elif inner_status == 2:
                check_gold = self.get_option(self.current_work + '_check_gold')
                if check_gold > 2:
                    self.set_option(self.current_work + '_inner_status', 99)
                else:
                    pb_name = 'main_scene_ilgwalbunhe_gold_0'
                    match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                    if match_rate < 0.9:
                        self.set_option(self.current_work + '_inner_status', inner_status + 1)
                    else:
                        self.lyb_mouse_click('main_scene_ilgwalbunhe_all')

                    self.set_option(self.current_work + '_check_gold', check_gold + 1)
            elif inner_status == 3:
                self.lyb_mouse_click('main_scene_ilgwalbunhe_bunhe')
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
            elif inner_status == 4:
                self.set_option(self.current_work + '_inner_status', inner_status + 1)
                self.set_option(self.current_work + '_check_gold', 0)
            else:
                self.set_option(self.current_work + '_end_flag', True)

        elif (self.status == self.get_work_status('우편') or
                      self.status == self.get_work_status('퀘스트')
              ):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.game_object.get_scene('menu_scene').status = self.status
            self.game_object.current_matched_scene['name'] = ''
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

            # self.logger.debug('[반복 종료] ' + str(loop_count) + ' 회 수행 완료, ' +
            # str(int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_LOOP)) - loop_count) + ' 회 남음')
            if loop_count >= int(self.get_game_config(lybconstant.LYB_DO_STRING_COUNT_LOOP)):
                self.status = self.last_status[self.current_work] + 1
                self.set_option('loop_count', 1)
                self.set_option('loop_start', None)
            else:
                self.status = self.get_option('loop_start')
                # print('DEBUG LOOP STATUS = ', self.status )

                if self.status == None:
                    # self.logger.debug('[반복 시작] 점을 찾지 못해서 다음 작업을 수행합니다')
                    self.status = self.last_status[self.current_work] + 1

                self.set_option('loop_count', loop_count + 1)

        else:
            self.status = self.last_status[self.current_work] + 1

        return self.status

    def pre_process_main_scene(self):

        pb_name = 'main_scene_chat'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.9:
            self.lyb_mouse_click('main_scene_chat_close_icon')
            return True

        hp = self.player_hp()
        if hp != None:

            # self.logger.debug('player hp: ' + str(hp) + '%')

            if self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set') == True:
                cfg_potion_slot = int(
                    self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number'))
                pb_name = 'main_scene_slot_' + str(cfg_potion_slot - 1)
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=70,
                                                                  custom_top_level=100)
                # self.logger.debug(pb_name + ' ' + str(match_rate))
                if match_rate > 0.8:
                    if self.current_work != None and self.current_work != '퀵슬롯 등록':
                        self.set_option(self.current_work + '_end_flag', True)
                        self.logger.info(
                            str(cfg_potion_slot) + '번 슬롯에 자동 물약 없음 ==> [' + str(self.current_work) + '] 작업을 종료합니다.')
                        return False

            cfg_potion_hp = int(self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp'))
            cfg_potion_slot = int(self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number'))
            pb_name = 'main_scene_slot_' + str(cfg_potion_slot - 1)
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name, custom_below_level=70,
                                                              custom_top_level=100)
            # self.logger.debug(pb_name + ' ' + str(match_rate))
            if match_rate < 0.8:
                if hp <= cfg_potion_hp:
                    self.logger.warn('HP: ' + str(hp) + '% < ' + str(cfg_potion_hp) + '% 수동 물약 사용(슬롯 번호: ' + str(
                        cfg_potion_slot) + ')')
                    self.lyb_mouse_click('main_scene_slot_' + str(cfg_potion_slot - 1), custom_threshold=0)
                    return True
            else:
                if self.get_game_config(lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set') == True:
                    if self.current_work != None and self.current_work != '퀵슬롯 등록':
                        self.set_option(self.current_work + '_end_flag', True)
                        self.logger.info(
                            str(cfg_potion_slot) + '번 슬롯에 수동 물약 없음 ==> [' + str(self.current_work) + '] 작업을 종료합니다.')
                        return False

        if self.current_work != '일괄 분해':
            resource_name = 'main_scene_inventory_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            if match_rate > 0.8:
                self.lyb_mouse_click('main_scene_inventory_close_icon')
                return True

            resource_name = 'main_scene_ilgwalbunhe_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            if match_rate > 0.8:
                self.lyb_mouse_click('main_scene_ilgwalbunhe_close_icon')
                return True

        resource_name = 'main_scene_character_loc'
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        if match_rate > 0.8:
            self.lyb_mouse_click('main_scene_character_close_icon')
            return True

        return False

    def player_hp(self):
        return self.horizontal_bar_percent('player_hp_s', 'player_hp_m', 'player_hp_e', adjust=(50, 50, 50))

    # def player_mp(self):
    # 	return self.horizontal_bar_percent('player_mp_s', 'player_mp_m', 'player_mp_e', adjust=(50, 50, 50))

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

    def main_scene_check_distance(self, quest_index):
        distance_list = [
            '1',
            '2',
        ]
        for each_distance in distance_list:
            pb_name = 'quest_distance_' + str(each_distance)
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.65,
                custom_top_level=(180, 170, 5),
                custom_below_level=(60, 60, 0),
                custom_flag=1,
                custom_rect=(90, 140 + (quest_index * 25), 115, 165 + (quest_index * 25)))
            # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                return int(each_distance), (loc_x, loc_y)

        return -1, (-1, -1)

    def main_scene_check_distance2(self, quest_index):

        for each_distance in range(1, 10):
            pb_name = 'quest_distance_' + str(each_distance)
            # self.game_object.getImagePixelBox(pb_name).save(pb_name +'.png')
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.65,
                custom_top_level=(180, 170, 5),
                custom_below_level=(60, 60, 0),
                custom_flag=1,
                custom_rect=(105, 140 + (quest_index * 25), 120, 165 + (quest_index * 25)))
            # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                return int(each_distance), (loc_x, loc_y)

        return -1, (-1, -1)

    def main_scene_check_quest(self, pb_name, custom_top_level, custom_below_level):
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.7,
            custom_top_level=custom_top_level,
            custom_below_level=custom_below_level,
            custom_flag=1,
            custom_rect=(5, 140, 30, 250))
        # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1:
            return True

        return False

    def is_complete_quest(self, quest_index, limit=3):
        complete_list = [
            'main_scene_quest_back',
            'main_scene_quest_talk',
            'main_scene_quest_bogo',
        ]

        for pb_name in complete_list:
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.9,
                custom_top_level=(255, 255, 255),
                custom_below_level=(80, 80, 80),
                custom_flag=1,
                custom_rect=(5, 140 + (quest_index * 25), 100, 170 + (quest_index * 30)))
            # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                threshold = self.get_option(pb_name + '_threshold')
                if threshold == None:
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

    def auto_off(self):

        # pb_name = 'auto'
        # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug('auto off ' + pb_name + ' ' + str(match_rate))
        # if match_rate < 0.6 and self.get_option(pb_name + '_clicked') != True:
        pb_name = 'auto_on'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.2,
            custom_top_level=(200, 170, 130),
            custom_below_level=(170, 140, 100),
            custom_flag=1,
            custom_rect=(480, 300, 510, 330))
        # self.logger.debug('auto off ' + pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))		
        if loc_x != -1 and self.get_option(pb_name + '_clicked') != True:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option(pb_name + '_clicked', True)
            return True
        else:
            self.set_option(pb_name + '_clicked', False)

        return False

    def auto_on(self, auto_limit=5):

        # pb_name = 'auto'
        # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug('auto on ' + pb_name + ' ' + str(match_rate))

        pb_name = 'auto_on'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.2,
            custom_top_level=(200, 170, 130),
            custom_below_level=(170, 140, 100),
            custom_flag=1,
            custom_rect=(480, 300, 510, 330))
        # self.logger.debug('auto on ' + pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        # self.game_object.getImagePixelBox(pb_name).save(pb_name + '.png')
        # if match_rate > 0.6:
        if loc_x == -1:
            auto_threshold = self.get_option('auto_threshold')
            if auto_threshold == None:
                auto_threshold = 0
            self.logger.info('수동 태세 감지됨: ' + str(auto_threshold) + '/' + str(auto_limit))
            if auto_threshold >= auto_limit:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.set_option('auto_threshold', 0)
                return True
            else:
                self.set_option('auto_threshold', auto_threshold + 1)
        else:
            self.set_option('auto_threshold', 0)

        return False

    def horse_off(self):

        # pb_name = 'main_scene_horse'
        # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        # if match_rate < 0.95 and self.get_option(pb_name + '_clicked') != True:
        pb_name = 'main_scene_horse_on'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.2,
            custom_top_level=(150, 115, 130),
            custom_below_level=(110, 85, 100),
            custom_flag=1,
            custom_rect=(605, 300, 635, 330))
        self.logger.warn('horse off ' + pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1 and self.get_option(pb_name + '_clicked') != True:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option(pb_name + '_clicked', True)
            return True
        else:
            self.set_option(pb_name + '_clicked', False)

        return False

    def horse_on(self, auto_limit=5):

        # pb_name = 'main_scene_horse'
        # match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        # if match_rate > 0.95:
        pb_name = 'main_scene_horse_on'
        (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
            self.window_image,
            self.game_object.resource_manager.pixel_box_dic[pb_name],
            custom_threshold=0.2,
            custom_top_level=(150, 115, 130),
            custom_below_level=(110, 85, 100),
            custom_flag=1,
            custom_rect=(605, 300, 635, 330))
        self.logger.warn('horse off ' + pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x == -1:
            threshold = self.get_option(pb_name + '_threshold')
            if threshold == None:
                threshold = 0
            self.logger.info('미탑승 감지됨: ' + str(threshold) + '/' + str(auto_limit))
            if threshold >= auto_limit:
                self.lyb_mouse_click(pb_name, custom_threshold=0)
                self.set_option(pb_name + '_threshold', 0)
                return True
            else:
                self.set_option(pb_name + '_threshold', threshold + 1)
        else:
            self.set_option(pb_name + '_threshold', 0)

        return False

    def target_off(self):

        pb_name = 'main_scene_target_npc'
        match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
        # self.logger.debug(pb_name + ' ' + str(match_rate))
        if match_rate > 0.9 and self.get_option(pb_name + '_clicked') != True:
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.set_option(pb_name + '_clicked', True)
            return True
        else:
            self.set_option(pb_name + '_clicked', False)

        return False

    def get_work_status(self, work_name):
        if work_name in lybgamekaiser.LYBKaiser.work_list:
            return (lybgamekaiser.LYBKaiser.work_list.index(work_name) + 1) * 1000
        else:
            return 99999

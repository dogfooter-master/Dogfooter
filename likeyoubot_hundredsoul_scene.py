import operator
import likeyoubot_hundredsoul as lybgamehundredsoul
from likeyoubot_configure import LYBConstant as lybconstant
import likeyoubot_scene
import time


class LYBHundredSoulScene(likeyoubot_scene.LYBScene):
    def __init__(self, scene_name):
        likeyoubot_scene.LYBScene.__init__(self, scene_name)

    def process(self, window_image, window_pixels):

        super(LYBHundredSoulScene, self).process(window_image, window_pixels)

        if self.scene_name == 'init_screen_scene':
            rc = self.init_screen_scene()
        elif self.scene_name == 'main_scene':
            rc = self.main_scene()
        elif self.scene_name == 'login_scene':
            rc = self.login_scene()
        elif self.scene_name == 'notification_scene':
            rc = self.notification_scene()
        elif self.scene_name == 'dashboard_scene':
            rc = self.dashboard_scene()
        elif self.scene_name == 'immu_scene':
            rc = self.immu_scene()
        elif self.scene_name == 'config_scene':
            rc = self.config_scene()
        elif self.scene_name == 'logout_scene':
            rc = self.logout_scene()
        elif self.scene_name == 'connect_account_scene':
            rc = self.connect_account_scene()
        elif self.scene_name == 'terms_scene':
            rc = self.terms_scene()
        elif self.scene_name == 'google_play_account_select_scene':
            rc = self.google_play_account_select_scene()
        elif self.scene_name == 'google_play_account_select_1_scene':
            rc = self.google_play_account_select_1_scene()
        elif self.scene_name == 'google_play_account_select_2_scene':
            rc = self.google_play_account_select_2_scene()
        elif self.scene_name == 'gisadan_scene':
            rc = self.gisadan_scene()
        elif self.scene_name == 'seong_scene':
            rc = self.seong_scene()
        elif self.scene_name == 'mail_scene':
            rc = self.mail_scene()
        elif self.scene_name == 'cash_sangjeom_scene':
            rc = self.cash_sangjeom_scene()
        elif self.scene_name == 'nova_stone_free_scene':
            rc = self.nova_stone_free_scene()
        elif self.scene_name == 'build_up_scene':
            rc = self.build_up_scene()
        elif self.scene_name == 'gisadan_sangjeom_scene':
            rc = self.gisadan_sangjeom_scene()
        elif self.scene_name == 'tamheom_scene':
            rc = self.tamheom_scene()
        elif self.scene_name == 'tobeol_scene':
            rc = self.tobeol_scene()
        elif self.scene_name == 'jeontoo_junbi_scene':
            rc = self.jeontoo_junbi_scene()
        elif self.scene_name == 'combat_main_scene':
            rc = self.combat_main_scene()
        elif self.scene_name == 'event_immu_scene':
            rc = self.event_immu_scene()
        elif self.scene_name == 'jeontoo_victory_scene':
            rc = self.jeontoo_victory_scene()
        elif self.scene_name == 'jeontoo_fail_scene':
            rc = self.jeontoo_fail_scene()
        elif self.scene_name == 'aura_daeryuk_scene':
            rc = self.aura_daeryuk_scene()












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

    def aura_daeryuk_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.click_resource('aura_daeryuk_scene_yuhwang_loc')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def event_immu_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 9:
            self.status += 1
            resource_name = 'immu_scene_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(200, 80, 700, 130))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option('last_status', self.status)
                    self.status = 10
                    return self.status
            self.status = 99999
        elif 10 <= self.status < 20:
            self.status += 1
            resource_name = 'event_immu_scene_bosang_loc'
            self.click_resource(resource_name)
            # resource = self.game_object.resource_manager.resource_dic[resource_name]
            # for pb_name in resource:
            #     match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            #     if match_rate > 0.9:
            #         self.lyb_mouse_click(pb_name, custom_threshold=0)
            #         return self.status
            self.status = self.get_option('last_status')
        elif self.status == 20:
            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jeontoo_victory_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 0 <= self.status < 10:
            self.click_resource('jeontoo_victory_scene_nagagi_loc')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jeontoo_fail_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            elapsed_time = time.time() - self.get_checkpoint(self.scene_name)
            if elapsed_time > 60:
                message = '창 이름 [' + str(self.game_object.window_title) + ']에서 전투 실패 감지'
                self.game_object.telegram_send(message)
                png_name = self.game_object.save_image('전투 실패')
                self.game_object.telegram_send('', image=png_name)
                self.set_checkpoint(self.scene_name)

            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def combat_main_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.game_object.get_scene('jeontoo_victory_scene').status = 0
            self.game_object.get_scene('jeontoo_fail_scene').status = 0

            resource_name = 'skill_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                self.set_option(pb_name, time.time() + 10)
            self.set_option('skill_evade' + 'custom_rect', (620, 390, 670, 430))
            self.set_option('skill_sub' + 'custom_rect', (630, 320, 680, 360))
            self.set_option('skill_main' + 'custom_rect', (700, 300, 750, 340))
            self.set_option('skill_fellow' + 'custom_rect', (710, 230, 760, 270))
            self.set_option('skill_fellow2' + 'custom_rect', (710, 160, 760, 270))
            self.status += 1
        elif 1 <= self.status < 600:
            self.status += 1
            if self.isEasyPlayOn(limit_count=3) is False:
                if self.click_resource('combat_main_scene_easy_play_button_loc') is True:
                    return self.status

            if 0 <= self.status % 10 < 9:
                resource_name = 'combo_loc'
                resource = self.game_object.resource_manager.resource_dic[resource_name]
                for pb_name in resource:
                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.8,
                        custom_flag=1,
                        custom_rect=(550, 150, 720, 320))
                    # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        return self.status

                    (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                        self.window_image,
                        self.game_object.resource_manager.pixel_box_dic[pb_name],
                        custom_threshold=0.8,
                        custom_flag=1,
                        custom_rect=(550, 310, 640, 400))
                    # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                    if loc_x != -1:
                        self.lyb_mouse_click_location(loc_x, loc_y)
                        return self.status

            resource_name = 'skill_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.8,
                    custom_top_level=(45, 200, 255),
                    custom_below_level=(20, 180, 200),
                    custom_flag=1,
                    custom_rect=self.get_option(pb_name + 'custom_rect'),
                )
                # self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.set_option(pb_name, time.time() + 2)

            resource_name = 'skill_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                if time.time() - self.get_option(pb_name) > 0:
                    self.logger.debug('스킬 클릭: ' + str(pb_name))
                    self.lyb_mouse_click(pb_name, custom_threshold=0)
                    self.set_option(pb_name, time.time() + 99)
                    return self.status
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def jeontoo_junbi_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.game_object.get_scene('tamheom_scene').status = 0
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1

            if self.click_resource('jeontoo_junbi_scene_sijak_loc') is False:
                self.status = 99999
            else:
                self.game_object.get_scene('combat_main_scene').status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def tobeol_scene(self):

        if self.status == 0:
            self.logger.info(' scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.lyb_mouse_click('tobeol_scene_tamheom', custom_threshold=0)
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    # 탐험 맵

    def tamheom_scene(self):

        if self.status == 0:
            self.logger.info(' scene: ' + self.scene_name)
            locations = []
            self.set_option('locations', locations)
            self.status += 1
        elif 1 <= self.status < 20:
            self.status += 1
            locations = self.get_option('locations')
            pb_name = 'tamheom_scene_current'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.6,
                custom_flag=1,
                custom_top_level=(255, 255, 255),
                custom_below_level=(254, 254, 254),
                custom_rect=(20, 130, 720, 340))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                locations.append((loc_x, loc_y))
                if len(locations) >= 3:
                    self.set_option('locations', locations)
                    self.status = 100
                    return self.status
        elif 20 <= self.status < 40:
            self.status += 1
            pb_name = 'tamheom_scene_boss'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(20, 130, 720, 340))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.lyb_mouse_click_location(loc_x, loc_y + 50)
                self.game_object.get_scene('jeontoo_junbi_scene').status = 0
                self.status = 40
        elif 40 <= self.status < 45:
            self.status += 1
        elif self.status == 45:
            self.lyb_mouse_click('main_scene_config', custom_threshold=0)
            self.game_object.get_scene('config_scene').status = 200
            self.status += 1
        elif self.status == 100:
            loc_x_list = []
            loc_y_list = []
            locations = self.get_option('locations')
            for (loc_x, loc_y) in locations:
                loc_x_list.append(loc_x)
                loc_y_list.append(loc_y)

            loc_x_list.sort()
            loc_y_list.sort()

            self.logger.debug(loc_x_list)
            self.logger.debug(loc_y_list)

            self.lyb_mouse_click_location(loc_x_list[1], loc_y_list[1])
            self.lyb_mouse_click_location(loc_x_list[1], loc_y_list[1] - 20)
            self.lyb_mouse_click_location(loc_x_list[1], loc_y_list[1] + 20)
            self.lyb_mouse_click_location(loc_x_list[1] - 20, loc_y_list[1])
            self.lyb_mouse_click_location(loc_x_list[1] + 20, loc_y_list[1])
            self.game_object.get_scene('jeontoo_junbi_scene').status = 0
            self.status = 40
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def nova_stone_free_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.click_resource('nova_stone_free_scene_free_loc')
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def cash_sangjeom_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            if self.click_resource('cash_sangjeom_scene_nova_stone_new_loc') is False:
                self.status = 99999
                return self.status
            else:
                self.status += 1

            pb_name = 'cash_sangjeom_scene_nova_stone'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.status = 10

        elif self.status == 10:
            pb_name = 'cash_sangjeom_scene_nova_stone'
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.game_object.get_scene('nova_stone_free_scene').status = 0
            self.status += 1
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def mail_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            pb_name = 'mail_scene_receive'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate < 0.9:
                self.status = 99999
            else:
                self.click_resource('mail_scene_receive_all_loc')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gisadan_sangjeom_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 100 <= self.status < 110:
            self.status += 1
            if self.click_resource('gisadan_sangjeom_scene_item_speed_up_loc') is True:
                self.status = 120
        elif self.status == 120:
            self.lyb_mouse_click('gisadan_sangjeom_scene_buy')
            self.status += 1
        elif 121 <= self.status < 130:
            self.status += 1
            self.lyb_mouse_click('back', custom_threshold=0)
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def build_up_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 5:
            self.status += 1

            pb_name = 'build_up_scene_speed_up'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click(pb_name)
                self.status = 99999
                return self.status

            pb_name = 'build_up_scene_empty'
            match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
            if match_rate > 0.9:
                self.lyb_mouse_click('back', custom_threshold=0)
                self.game_object.get_scene('gisadan_scene').status = 100
                self.game_object.get_scene('gisadan_sangjeom_scene').status = 100
                return self.status
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def seong_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            resource_name = 'seong_scene_give_' + 'emerald' + '_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                self.click_resource(resource_name)
            else:
                self.status = 10
        elif self.status == 10:
            self.lyb_mouse_click('back', custom_threshold=0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def gisadan_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('gisadan_scene_chulseok_bosang', custom_threshold=0)
            self.status += 1
        elif self.status == 2:
            if self.click_resource('gisadan_scene_give_new_loc') is True:
                self.game_object.get_scene('seong_scene').status = 0
            self.status += 1
        elif self.status == 3:
            if self.click_resource('gisadan_scene_build_up_aura_loc') is True:
                self.game_object.get_scene('build_up_scene').status = 0
            self.status += 1
        elif self.status == 4:
            if self.click_resource('gisadan_scene_build_up_castle_loc') is True:
                self.game_object.get_scene('build_up_scene').status = 0
            self.status += 1
        elif self.status == 100:
            self.lyb_mouse_click('gisadan_scene_sangjeom', custom_threshold=0)
            self.status = 3
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def login_scene(self):
        self.game_object.current_matched_scene['name'] = ''
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
            if self.status % 10 == 0:
                self.lyb_mouse_click(self.scene_name + '_touch', custom_threshold=0)
            self.status += 1
        elif self.status == 70:
            self.game_object.terminate_application()
            self.status += 1
        else:
            self.status = 0

        return self.status

    def google_play_account_select_1_scene(self):
        return self.game_object.get_scene('google_play_account_select_scene').process(self.window_image,
                                                                                      self.window_pixels)

    def google_play_account_select_2_scene(self):
        return self.game_object.get_scene('google_play_account_select_scene').process(self.window_image,
                                                                                      self.window_pixels)

    def google_play_account_select_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            account_index = self.get_option('account_index')
            if account_index is None:
                account_index = 0
                self.set_option('account_index', account_index)

            self.set_option('click_index', account_index)

            resource_name = 'google_play_account_select_scene_account_1_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                self.set_option('click_index', 10)
                self.status = 200
                return self.status

            resource_name = 'google_play_account_select_scene_account_2_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                if account_index > 1:
                    self.set_option('account_index', 0)
                    account_index = 0

                self.set_option('click_index', 20 + account_index)
                self.status = 200
                return self.status

            resource_name = 'google_play_account_select_scene_account_3_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
            if match_rate > 0.9:
                if account_index > 2:
                    self.set_option('account_index', 0)
                    account_index = 0

                self.set_option('click_index', account_index)
                self.status = 200
                return self.status

            self.set_option('last_status', 99999)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1

            pb_name = 'google_play_account_select_scene_add'
            (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                self.window_image,
                self.game_object.resource_manager.pixel_box_dic[pb_name],
                custom_threshold=0.6,
                custom_flag=1,
                custom_rect=(180, 400, 210, 460))
            self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.status = 1000
            else:
                click_index = self.get_option('click_index')
                if click_index > 3:
                    if loc_x != -1:
                        self.status = 1000
                    else:
                        self.set_option('last_status', self.status)
                        self.set_option('click_index', click_index - 1)
                        self.status = 100
                else:
                    self.status = 200
        elif self.status == 100:
            self.lyb_mouse_drag('google_play_account_drag_bot', 'google_play_account_drag_top', delay=2)
            self.status += 1
        elif self.status == 101:
            self.status = self.get_option('last_status')
        elif self.status == 200:
            index = str(self.get_option('click_index'))
            self.logger.warn('index=' + index)
            pb_name = 'google_play_account_select_scene_list_' + index
            account_index = self.get_option('account_index')
            self.set_option('account_index', account_index + 1)
            self.lyb_mouse_click(pb_name, custom_threshold=0)
            self.status = 99999
        elif 1000 <= self.status < 1005:
            self.lyb_mouse_drag('google_play_account_select_scene_drag_top',
                                'google_play_account_select_scene_drag_bot')
            self.status += 1
        elif self.status == 1005:
            self.set_option('account_index', 0)
            self.status = 0
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def terms_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1

            isClicked = False
            resource_name = 'terms_scene_check_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                match_rate = self.game_object.rateMatchedPixelBox(self.window_pixels, pb_name)
                if match_rate > 0.9:
                    self.lyb_mouse_click(pb_name)
                    isClicked = True

            if isClicked is False:
                self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def connect_account_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        else:
            self.game_object.get_scene('terms_scene').status = 0
            self.game_object.get_scene('google_play_account_select_scene').status = 0
            self.lyb_mouse_click(self.scene_name + '_google', custom_threshold=0)

            self.status = 0

        return self.status

    def logout_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif 100 <= self.status < 110:
            self.status += 1
            if self.click_resource('logout_scene_ok_loc') is True:
                self.game_object.get_scene('connect_account_scene').status = 0
                self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def config_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 100:
            self.game_object.get_scene('logout_scene').status = 100
            self.status += 1
        elif 101 <= self.status < 110:
            self.status += 1
            if self.click_resource('config_scene_logout_loc') is False:
                self.lyb_mouse_click('config_scene_tab_account', custom_threshold=0)
            else:
                self.status = 99999
        elif self.status == 200:
            self.status += 1
        elif 201 <= self.status < 210:
            self.status += 1
            if self.click_resource('config_scene_korean_loc') is False:
                self.lyb_mouse_click('config_scene_tab_language', custom_threshold=0)
            else:
                self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def immu_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('last_status', 99999)
            self.status += 1
        elif 1 <= self.status < 9:
            self.status += 1
            resource_name = 'immu_scene_new_loc'
            resource = self.game_object.resource_manager.resource_dic[resource_name]
            for pb_name in resource:
                (loc_x, loc_y), match_rate = self.game_object.locationOnWindowPart(
                    self.window_image,
                    self.game_object.resource_manager.pixel_box_dic[pb_name],
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(200, 80, 700, 130))
                self.logger.debug(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    self.lyb_mouse_click_location(loc_x, loc_y)
                    self.set_option('last_status', self.status)
                    self.status = 10
                    return self.status
            self.status = 99999
        elif 10 <= self.status < 20:
            self.status += 1
            resource_name = 'immu_scene_bosang_loc'
            match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
            if match_rate > 0.9:
                self.lyb_mouse_click('immu_scene_bosang_0', custom_threshold=0)
                return self.status
            self.status = self.get_option('last_status')
        elif self.status == 20:
            self.status = self.get_option('last_status')
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def notification_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.status += 1
        elif self.status == 1:
            self.lyb_mouse_click('notification_scene_dashboard', custom_threshold=0)
            self.status += 1
        elif self.status == 100:
            self.status += 1
        elif 100 <= self.status < 110:
            self.status += 1
            if self.click_resource('notification_scene_bosang_loc') is True:
                self.game_object.get_scene('immu_scene').status = 0
                return self.status

            self.status = 99999
        else:
            if self.scene_name + '_close_icon' in self.game_object.resource_manager.pixel_box_dic:
                self.lyb_mouse_click(self.scene_name + '_close_icon', custom_threshold=0)

            self.status = 0

        return self.status

    def dashboard_scene(self):

        if self.status == 0:
            self.logger.info('scene: ' + self.scene_name)
            self.set_option('resource_name', 'dashboard_scene_jeontoo_loc')
            self.game_object.get_scene('tamheom_scene').status = 0
            self.status += 1
        elif 1 <= self.status < 10:
            self.status += 1
            button_loc_x, button_loc_y = self.get_location('dashboard_scene_button')
            pDic = {}
            resource_name = self.get_option('resource_name')
            for i in range(5):
                (loc_x, loc_y), match_rate = self.game_object.locationResourceOnWindowPart(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.7,
                    custom_flag=1,
                    custom_rect=(120, 130 + (i * 60) - 30, 200, 130 + (i * 60) + 30),
                )
                if loc_x != -1:
                    pDic[(loc_x, loc_y)] = match_rate

            sorted_list = sorted(pDic.items(), key=operator.itemgetter(1), reverse=True)
            self.logger.warn(sorted_list)
            if len(sorted_list) > 0:
                loc_x, loc_y = sorted_list[0][0]
                self.lyb_mouse_click_location(button_loc_x + 50, loc_y + 10)
            else:
                self.status = 99999
        elif self.status == self.get_work_status('광산'):
            self.set_option('resource_name', 'dashboard_scene_gwangsan_loc')
            self.game_object.get_scene('aura_daeryuk_scene').status = 0
            self.status = 1
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
            for each_icon in lybgamehundredsoul.LYBHundredSoul.hundredsoul_icon_list:
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
            for each_icon in lybgamehundredsoul.LYBHundredSoul.hundredsoul_icon_list:
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

        return 0

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

            cfg_duration = int(self.get_game_config(lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration'))
            elapsed_time = self.get_elapsed_time()

            if elapsed_time > self.period_bot(cfg_duration):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.process_main_quest()

        elif self.status == self.get_work_status('기사단'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.click_resource('main_scene_gisadan_loc')
            self.game_object.get_scene('gisadan_scene').status = 0


        elif self.status == self.get_work_status('우편'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.click_resource('main_scene_mail_loc')
            self.game_object.get_scene('mail_scene').status = 0

        elif self.status == self.get_work_status('노바스톤'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag') == True:
                self.set_option(self.current_work + '_end_flag', False)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            if self.click_resource('main_scene_cash_sangjeom_new_loc') is False:
                self.set_option(self.current_work + '_end_flag', True)
                return self.status

            self.game_object.get_scene('cash_sangjeom_scene').status = 0

        elif self.status == self.get_work_status('광산'):

            elapsed_time = self.get_elapsed_time()
            if elapsed_time > self.period_bot(5):
                self.set_option(self.current_work + '_end_flag', True)

            if self.get_option(self.current_work + '_end_flag'):
                self.set_option(self.current_work + '_end_flag', False)
                self.set_option(self.current_work + '_inner_status', None)
                self.status = self.last_status[self.current_work] + 1
                return self.status

            self.lyb_mouse_click('main_scene_alarm', custom_threshold=0)
            self.game_object.get_scene('notification_scene').status = 0
            self.game_object.get_scene('dashboard_scene').status = self.status

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

    def callback_logoff(self):
        self.lyb_mouse_click('main_scene_config', custom_threshold=0)
        self.game_object.get_scene('config_scene').status = 100

    def pre_process_main_scene(self):

        return False

    def process_main_quest(self):
        if self.process_notification() is True:
            return True

        if self.process_dashboard(self.current_work) is True:
            return True

        return False

    def process_notification(self):
        resource_name = 'main_scene_notification_new_loc'
        elapsed_time = time.time() - self.get_checkpoint(resource_name)
        if elapsed_time < self.period_bot(60):
            return False

        self.set_checkpoint(resource_name)

        if self.click_resource(resource_name, near=4) == True:
            self.game_object.get_scene('notification_scene').status = 100
            return True

        return False

    def process_dashboard(self, current_work):
        cs = current_work + '_inner_status'

        inner_status = self.get_option(cs)
        if inner_status is None:
            inner_status = 0

        if 0 <= inner_status < 1000:
            self.lyb_mouse_click('main_scene_alarm', custom_threshold=0)
            self.game_object.get_scene('notification_scene').status = 0
            self.game_object.get_scene('dashboard_scene').status = 0
            self.set_option(cs, inner_status + 1)
        else:
            self.set_option(cs, 0)
            return False

        return True

    def get_work_status(self, work_name):
        if work_name in lybgamehundredsoul.LYBHundredSoul.work_list:
            return (lybgamehundredsoul.LYBHundredSoul.work_list.index(work_name) + 1) * 1000
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

    def isEasyPlayOn(self, limit_count=-1):

        # if limit_count == -1:
        #     limit_count = int(self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count'))

        return self.isStatusByResource(
            '[Easy Play 꺼짐 인식 횟수]',
            'combat_main_scene_easy_play_loc',
            custom_top_level=(255, 255, 255),
            custom_below_level=(255, 255, 100),
            custom_rect=(360, 400, 440, 460),
            custom_threshold=0.7,
            limit_count=limit_count,
        )

    def isStatusByResource(self, log_message, resource_name, custom_threshold, custom_top_level, custom_below_level,
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
        self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
        if loc_x != -1 and reverse == False:
            self.set_option(resource_name + 'check_count', 0)
            return True

        if loc_x == -1 and reverse == True:
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

    def isStatusByResource2(self, log_message, resource_name, custom_threshold, limit_count=-1, reverse=False):
        match_rate = self.game_object.rateMatchedResource(self.window_pixels, resource_name)
        self.logger.debug(resource_name + ' ' + str(round(match_rate, 2)))
        if match_rate > custom_threshold and reverse == False:
            self.set_option(resource_name + 'check_count', 0)
            return True

        if match_rate < custom_threshold and reverse == True:
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

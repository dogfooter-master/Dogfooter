import likeyoubot_game as lybgame
import likeyoubot_hundredsoul_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy


class LYBHundredSoul(lybgame.LYBGame):
    work_list = [
        '게임 시작',
        '로그인',
        '메인 퀘스트',
        '우편',
        '기사단',
        '노바스톤',
        '광산',
        '환영의 전당',
        '이벤트전',
        '소환의탑',
        '결투장',
        '협동전',

        '알림',
        '[반복 시작]',
        '[반복 종료]',
        '[작업 대기]',
        '[작업 예약]',
        '']

    hundredsoul_icon_list = [
        'hundredsoul_icon',
        'hundredsoul_icon_1'
    ]

    bugwan_list = [
        '나즈리엘',
        '기간틱',
        '라리엘',
        '루신다',
        '카렌',
    ]

    def __init__(self, game_name, game_data_name, window):
        lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_HUNDREDSOUL, lybconstant.LYB_GAME_DATA_HUNDREDSOUL, window)

    def process(self, window_image):
        rc = super(LYBHundredSoul, self).process(window_image)
        if rc < 0:
            return rc

        return rc

    def custom_check(self, window_image, window_pixel):
        resource_name = 'skip_dehwa_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(2):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(720, 410, 760, 450)
            )
            # self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('대화 스킵: ' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        resource_name = 'center_bosang_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(5):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(300, 90, 600, 300)
            )
            # self.logger.debug(resource_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('보상: ' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        confirm_list = [
            'confirm_loc',
            'gotcha_loc',
            'open_new_boss_loc',
            'gotcha_20190123_loc',
            'bosang_20190124_loc',
            'close_20190124_loc',
        ]

        for resource_name in confirm_list:
            elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
            if elapsed_time > self.period_bot(5):
                (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                    self.window_image,
                    resource_name,
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(200, 100, 600, 450),
                )
                # self.logger.warn(resource_name + ' ' + str(match_rate))
                if loc_x != -1:
                    # self.get_scene('quest_scene').status = 20
                    self.get_scene('main_scene').set_checkpoint(resource_name)
                    self.logger.info(resource_name + ':' + str(match_rate))
                    self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                    return 'skip'

        resource_name = 'notice_20190124_loc'
        match_rate = self.rateMatchedResource(self.window_pixels, resource_name)
        if match_rate > 0.8:
            self.click_back()
            return 'skip'

        resource_name = 'close_popup_20190124_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(5):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(660, 380, 730, 430),
            )
            if loc_x != -1:
                # self.get_scene('quest_scene').status = 20
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info(resource_name + ':' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        # 패배!
        # (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
        # 					self.window_image,
        # 					'defeat_press_key_loc',
        # 					custom_below_level=(250, 250, 250),
        # 					custom_top_level=(255, 255, 255),
        # 					custom_threshold=0.7,
        # 					custom_flag=1,
        # 					custom_rect=(280, 190, 360, 230)
        # 					)
        # if loc_x != -1:
        # 	self.logger.warn('전투 패배: ' + str(match_rate))
        # 	self.mouse_click('defeat_press_key_0')

        return ''

    def get_screen_by_location(self, window_image):

        scene_name = self.scene_init_screen(window_image)
        if len(scene_name) > 0:
            return scene_name

        # scene_name = self.jeontoo_scene(window_image)
        # if len(scene_name) > 0:
        # 	return scene_name

        # scene_name = self.scene_google_play_account_select(window_image)
        # if len(scene_name) > 0:
        # 	return scene_name

        self.return_to_back()

        return ''

    # def jeontoo_scene(self, window_image):
    # 	(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
    # 						self.window_image,
    # 						'jeontoo_scene_loc',
    # 						custom_below_level=(100, 100, 100),
    # 						custom_top_level=(255, 255, 255),
    # 						custom_threshold=0.7,
    # 						custom_flag=1,
    # 						custom_rect=(5, 90, 80, 130)
    # 						)
    # 	if match_rate > 0.7:
    # 		return 'jeontoo_scene'

    # 	return ''

    def return_to_back(self):

        return_to_back_threshold = self.get_option('return_to_back_threshold')
        if return_to_back_threshold == None:
            return_to_back_threshold = 0

        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint('return_to_back_last_check_time')

        if elapsed_time > self.period_bot(3):
            return_to_back_threshold = 0

        self.get_scene('main_scene').set_checkpoint('return_to_back_last_check_time')

        if return_to_back_threshold > 30:
            self.mouse_click('back')
        else:
            self.set_option('return_to_back_threshold', return_to_back_threshold + 1)
            # self.logger.debug('return to back after ' + str(return_to_back_threshold) + '/30')

    def scene_init_screen(self, window_image):

        loc_x = -1
        loc_y = -1

        if self.player_type == 'nox':
            for each_icon in LYBHundredSoul.hundredsoul_icon_list:
                (loc_x, loc_y), match_rate = self.locationOnWindowPart(
                    window_image,
                    self.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(80, 110, 700, 370)
                )
                # print('[DEBUG] nox yh icon:', (loc_x, loc_y), match_rate)
                if loc_x != -1:
                    break
        else:
            for each_icon in LYBHundredSoul.hundredsoul_icon_list:
                (loc_x, loc_y), match_rate = self.locationOnWindowPart(
                    window_image,
                    self.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 10, 740, 370)
                )
                # print('[DEBUG] momo yh icon:', (loc_x, loc_y), match_rate)
                if loc_x != -1:
                    break

        if loc_x == -1:
            return ''

        return 'init_screen_scene'

    def scene_google_play_account_select(self, window_image):
        loc_x_list = []
        loc_y_list = []

        (loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
            window_image,
            self.resource_manager.pixel_box_dic['google_play_letter']
        )
        loc_x_list.append(loc_x)
        loc_y_list.append(loc_y)

        for i in range(6):
            (loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
                window_image,
                self.resource_manager.pixel_box_dic['google_play_letter_' + str(i)]
            )

            loc_x_list.append(loc_x)
            loc_y_list.append(loc_y)

        for each_loc in loc_x_list:
            if each_loc == -1:
                return ''
            else:
                continue

        return 'google_play_account_select_scene'

    def clear_scene(self):
        last_scene = self.scene_dic
        self.scene_dic = {}
        for scene_name, scene in last_scene.items():
            if ('google_play_account_select_scene' in scene_name or
                    'logo_screen_scene' in scene_name or
                    'connect_account_scene' in scene_name
            ):
                self.scene_dic[scene_name] = last_scene[scene_name]

    def add_scene(self, scene_name):
        self.scene_dic[scene_name] = lybscene.LYBHundredSoulScene(scene_name)
        self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
        self.scene_dic[scene_name].setGameObject(self)


class LYBHundredSoulTab(lybgame.LYBGameTab):
    def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height,
                 game_name=lybconstant.LYB_GAME_HUNDREDSOUL):
        lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height,
                                    game_name)

    def set_work_list(self):
        lybgame.LYBGameTab.set_work_list(self)

        for each_work in LYBHundredSoul.work_list:
            self.option_dic['work_list_listbox'].insert('end', each_work)
            self.configure.common_config[self.game_name]['work_list'].append(each_work)

    def set_option(self):
        # PADDING
        frame = ttk.Frame(
            master=self.master,
            relief=self.frame_relief
        )
        frame.pack(pady=5)

        self.inner_frame_dic['options'] = ttk.Frame(
            master=self.master,
            relief=self.frame_relief
        )

        self.option_dic['option_note'] = ttk.Notebook(
            master=self.inner_frame_dic['options']
        )

        self.inner_frame_dic['common_tab_frame'] = ttk.Frame(
            master=self.option_dic['option_note'],
            relief=self.frame_relief
        )

        self.inner_frame_dic['common_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
        self.option_dic['option_note'].add(self.inner_frame_dic['common_tab_frame'], text='일반')

        self.inner_frame_dic['work_tab_frame'] = ttk.Frame(
            master=self.option_dic['option_note'],
            relief=self.frame_relief
        )
        self.inner_frame_dic['work_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
        self.option_dic['option_note'].add(self.inner_frame_dic['work_tab_frame'], text='작업')

        self.inner_frame_dic['notify_tab_frame'] = ttk.Frame(
            master=self.option_dic['option_note'],
            relief=self.frame_relief
        )
        self.inner_frame_dic['notify_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
        self.option_dic['option_note'].add(self.inner_frame_dic['notify_tab_frame'], text='알림')

        # ------

        # 일반 탭 좌측
        frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 일반 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 일반 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 좌측
        frame_l = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_label = ttk.LabelFrame(frame_l, text='메인 퀘스트')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text('진행 시간(초)', width=27)
        )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration'].trace(
            'w', lambda *args: self.main_quest_duration(args,
                                                        lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration')
        )
        combobox_list = []
        for i in range(0, 86401, 60):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration'] = 3600

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration'],
            state="readonly",
            height=10,
            width=7,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][
                         lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'main_quest_duration'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_l, text='환영의 전당')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame,
            text                = self.get_option_text('부관 선택', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan'].trace(
            'w', lambda *args: self.hwanyoung_bugwan(args, lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan')
            )
        combobox_list = LYBHundredSoul.bugwan_list

        if not lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan'] = combobox_list[0]

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list,
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan'],
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'hwanyoung_bugwan'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_l, text='이벤트전')

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'event_skill_point'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'event_skill_point'].trace(
            'w', lambda *args: self.event_skill_point(args, lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'event_skill_point')
        )
        if not lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'event_skill_point' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'event_skill_point'] = False

        check_box = ttk.Checkbutton(
            master=frame,
            text=self.get_option_text('스킬 포인트', width=35),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_WORK + 'event_skill_point'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 알림 탭 좌
        frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
        frame_label = ttk.Frame(frame_l)
        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_NOTIFY + 'notify_jeontoo_defeat'] = tkinter.BooleanVar(
            frame)
        self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_NOTIFY + 'notify_jeontoo_defeat'].trace(
            'w', lambda *args: self.notify_jeontoo_defeat(args,
                                                          lybconstant.LYB_DO_STRING_HUNDREDSOUL_NOTIFY + 'notify_jeontoo_defeat')
        )
        if not lybconstant.LYB_DO_STRING_HUNDREDSOUL_NOTIFY + 'notify_jeontoo_defeat' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_HUNDREDSOUL_NOTIFY + 'notify_jeontoo_defeat'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('전투 패배', width=27),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_HUNDREDSOUL_NOTIFY + 'notify_jeontoo_defeat'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)
        # 알림 탭 중
        frame_m = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)
        # 알림 탭 우
        frame_r = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # ------

        self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
        self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)

        self.set_game_option()

    def main_quest_duration(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def notify_jeontoo_defeat(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        
    def hwanyoung_bugwan(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def event_skill_point(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())



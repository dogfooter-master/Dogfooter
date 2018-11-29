import likeyoubot_game as lybgame
import likeyoubot_blade2_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy


class LYBBlade2(lybgame.LYBGame):
    work_list = [
        '게임 시작',
        '로그인',
        '모험',
        '모두팔기',
        '장비교체',
        '자동분해',
        '우편함',
        '반격 던전',
        '영웅의 탑',
        '레이드',
        '일대일 대전',
        '팀 대전',
        '점령전',
        '친구',
        '명예의 전당',

        '알림',
        '[반복 시작]',
        '[반복 종료]',
        '[작업 대기]',
        '[작업 예약]',
        '']

    blade2_icon_list = [
        'blade2_icon'
    ]

    hero_list = [
        '검투사',
        '암살자',
        '마법사',
        '격투가',
    ]

    stone_list = [
        '무기 승급석',
        '방어구 승급석',
        '장신구 승급석'
    ]

    gyeoltoo_list = [
        '일대일 대전',
        '팀 대전',
        '점령전',
    ]

    item_equip_list = [
        '무기',
        '방어구',
        '장신구',
    ]

    item_status_list = [
        '레벨업 중',
        '강화 중',
        '정수',
    ]

    moheom_level_list = [
        '일반',
        '정예',
        '악몽',
        '지옥'
    ]

    character_move_list = [
        "↑",
        "↗",
        "→",
        "↘",
        "↓",
        "↙",
        "←",
        "↖"
    ]

    tier_list = [
        'T1',
        'T2',
        'T3',
        'T4'
    ]

    auto_combat_list = [
        'AUTO',
        'SKILL AUTO'
    ]

    def __init__(self, game_name, game_data_name, window):
        lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_BLADE2, lybconstant.LYB_GAME_DATA_BLADE2, window)

    def process(self, window_image):
        rc = super(LYBBlade2, self).process(window_image)
        if rc < 0:
            return rc

        return rc

    def custom_check(self, window_image, window_pixel):

        pb_name = 'confirm'
        (loc_x, loc_y), match_rate = self.locationOnWindowPart(
            self.window_image,
            self.resource_manager.pixel_box_dic[pb_name],
            custom_below_level=(200, 170, 100),
            custom_top_level=(230, 190, 120),
            custom_threshold=0.8,
            custom_flag=1,
            custom_rect=(540, 350, 590, 380)
        )
        if loc_x != -1:
            self.logger.warn('확인: ' + str(match_rate))
            self.mouse_click(pb_name)

        (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
            self.window_image,
            'jeomryoungjeon_combat_scene_result_loc',
            custom_top_level=(235, 235, 235),
            custom_below_level=(115, 115, 115),
            custom_threshold=0.7,
            custom_flag=1,
            custom_rect=(515, 350, 580, 380)
        )
        if loc_x != -1:
            self.logger.warn('결과 보기: ' + str(match_rate))
            self.mouse_click('jeomryoungjeon_combat_scene_result_0')

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

    def scene_init_screen(self, window_image):

        loc_x = -1
        loc_y = -1

        if self.player_type == 'nox':
            for each_icon in LYBBlade2.blade2_icon_list:
                (loc_x, loc_y), match_rate = self.locationOnWindowPart(
                    window_image,
                    self.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(80, 110, 570, 300)
                )
                # self.logger.debug(each_icon + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
                if loc_x != -1:
                    break
        elif self.player_type == 'momo':
            for each_icon in LYBBlade2.blade2_icon_list:
                (loc_x, loc_y), match_rate = self.locationOnWindowPart(
                    window_image,
                    self.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 10, 610, 300)
                )
                # self.logger.debug(each_icon + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
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
        self.scene_dic[scene_name] = lybscene.LYBBlade2Scene(scene_name)
        self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
        self.scene_dic[scene_name].setGameObject(self)


class LYBBlade2Tab(lybgame.LYBGameTab):
    def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height,
                 game_name=lybconstant.LYB_GAME_BLADE2):
        lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height,
                                    game_name)

    def set_work_list(self):
        lybgame.LYBGameTab.set_work_list(self)

        for each_work in LYBBlade2.work_list:
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

        self.inner_frame_dic['work_2_tab_frame'] = ttk.Frame(
            master=self.option_dic['option_note'],
            relief=self.frame_relief
        )
        self.inner_frame_dic['work_2_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
        self.option_dic['option_note'].add(self.inner_frame_dic['work_2_tab_frame'], text='작업2')

        self.inner_frame_dic['notify_tab_frame'] = ttk.Frame(
            master=self.option_dic['option_note'],
            relief=self.frame_relief
        )
        self.inner_frame_dic['notify_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
        self.option_dic['option_note'].add(self.inner_frame_dic['notify_tab_frame'], text='알림')

        # ------

        # 일반 탭 좌측
        frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_label = ttk.LabelFrame(frame_l, text='설정')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("TAG 클릭 주기(초)")
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'].trace(
            'w', lambda *args: self.callback_moheom_tag_period(args,
                                                               lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period')
        )
        combobox_list = []
        for i in range(0, 3601):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'] = 20

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_tag_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest'].trace(
            'w', lambda *args: self.callback_ilil_quest(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('일일 퀘스트 클릭'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue'].trace(
            'w', lambda *args: self.callback_ilil_quest_continue(args,
                                                                 lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('일일 퀘스트 연속 수행'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ilil_quest_continue'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice'].trace(
            'w', lambda *args: self.callback_raid_notice(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('레이드 알림 클릭'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_notice'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice'].trace(
            'w', lambda *args: self.callback_jeomryoungjeon_notice(args,
                                                                   lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('점령전 알림 클릭'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_notice'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        # frame.pack(anchor=tkinter.NW)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 일반 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 일반 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 좌측
        frame_l = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_label = ttk.LabelFrame(frame_l, text='모험')

        frame = ttk.Frame(frame_label)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level'].trace(
            'w', lambda *args: self.callback_moheom_level(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level')
        )
        combobox_list = LYBBlade2.moheom_level_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level'] = \
            combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_level'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'].trace(
            'w', lambda *args: self.callback_moheom_act(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act')
        )
        combobox_list = []
        for i in range(1, 6):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'] = \
            combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'],
            state="readonly",
            height=10,
            width=3,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_act'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        label = ttk.Label(
            master=frame,
            text="막"
        )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'].trace(
            'w', lambda *args: self.callback_moheom_stage(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage')
        )
        combobox_list = []
        for i in range(1, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'] = \
            combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'],
            state="readonly",
            height=10,
            width=3,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_stage'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        label = ttk.Label(
            master=frame,
            text="스테이지"
        )
        label.pack(side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("진행 횟수(0:무한)")
        )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count'].trace(
            'w', lambda *args: self.callback_moheom_limit_count(args,
                                                                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count')
        )
        combobox_list = []
        for i in range(0, 1001):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count'] = 0

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_limit_count'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("봇 주기(초)(0:설정 안함)")
        )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period'].trace(
            'w', lambda *args: self.callback_moheom_bot_period(args,
                                                               lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period')
        )
        combobox_list = []
        for i in range(0, 100, 1):
            combobox_list.append("{0:.2f}".format(i * 0.01))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period'] = 0.00

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_bot_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat'].trace(
            'w',
            lambda *args: self.callback_moheom_repeat(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('반복 전투', width=10),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_repeat'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple'].trace(
            'w',
            lambda *args: self.callback_moheom_triple(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('3배 모험', width=10),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_triple'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next'].trace(
            'w', lambda *args: self.callback_moheom_next(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text='다음 지역',
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_next'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use'].trace(
            'w',
            lambda *args: self.callback_moheom_hero_use(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('영웅 자동 선택 사용', width=20),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_use'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry'].trace(
            'w', lambda *args: self.callback_moheom_retry(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text='다시 하기',
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_retry'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택 1")
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1'].trace(
            'w',
            lambda *args: self.callback_moheom_hero_1(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1'] = \
            combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_1'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택 2")
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2'].trace(
            'w',
            lambda *args: self.callback_moheom_hero_2(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2'] = \
            combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_hero_2'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("자동 방식", width=28)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto'].trace(
            'w', lambda *args: self.callback_moheom_auto(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto')
        )
        combobox_list = LYBBlade2.auto_combat_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto'] = \
            combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto'],
            state="readonly",
            height=10,
            width=10,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'moheom_auto'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_l, text='자동분해')

        frame_label_inner = ttk.LabelFrame(frame_label, text='티어')
        frame = ttk.Frame(frame_label_inner)

        for i in range(len(LYBBlade2.tier_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + str(i)] = tkinter.BooleanVar(
                frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '0'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_tier_0(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '1'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_tier_1(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '2'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_tier_2(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '2')
                )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '3'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_tier_3(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + '3')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + str(i) in self.configure.common_config[
                self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + str(i)] = False

            check_box = ttk.Checkbutton(

                master=frame,
                text=LYBBlade2.tier_list[i],
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_tier' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label_inner = ttk.LabelFrame(frame_label, text='등급')
        frame = ttk.Frame(frame_label_inner)

        for i in range(6):
            self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + str(i)] = tkinter.BooleanVar(
                frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '0'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_rank_0(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '1'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_rank_1(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '2'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_rank_2(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '2')
                )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '3'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_rank_3(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '3')
                )
            elif i == 4:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '4'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_rank_4(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '4')
                )
            elif i == 5:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '5'].trace(
                    'w', lambda *args: self.callback_jadong_bunhe_rank_5(args,
                                                                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + '5')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + str(i) in self.configure.common_config[
                self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + str(i)] = False

            check_box = ttk.Checkbutton(

                master=frame,
                text='★' + str(i + 1),
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_rank' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label_inner = ttk.LabelFrame(frame_label, text='기타')
        frame = ttk.Frame(frame_label_inner)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa'].trace(
            'w', lambda *args: self.callback_jadong_bunhe_ganghwa(args,
                                                                  lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa')
        )

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text='강화',
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jadong_bunhe_ganghwa'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_label = ttk.LabelFrame(frame_m, text='일대일 대전')
        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use'].trace(
            'w',
            lambda *args: self.callback_ildeil_hero_use(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('영웅 자동 선택 사용'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_use'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("진행 횟수")
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count'].trace(
            'w', lambda *args: self.callback_ildeil_count(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count')
        )
        combobox_list = []
        for i in range(1, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count'] = \
            combobox_list[2]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count'],
            state="readonly",
            height=10,
            width=3,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_count'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택 1", width=25)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1'].trace(
            'w',
            lambda *args: self.callback_ildeil_hero_1(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1'] = \
            combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_1'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택 2", width=25)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2'].trace(
            'w',
            lambda *args: self.callback_ildeil_hero_2(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2'] = \
            combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'ildeil_hero_2'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_m, text='팀 대전')
        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("진행 횟수")
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count'].trace(
            'w', lambda *args: self.callback_team_count(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count')
        )
        combobox_list = []
        for i in range(1, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count'] = \
            combobox_list[2]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count'],
            state="readonly",
            height=10,
            width=3,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'team_count'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_m, text='점령전')

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use'].trace(
            'w', lambda *args: self.callback_jeomryoungjeon_hero_use(args,
                                                                     lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('영웅 자동 선택 사용', width=25),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero_use'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택", width=25)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero'].trace(
            'w', lambda *args: self.callback_jeomryoungjeon_hero(args,
                                                                 lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero'] = combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jeomryoungjeon_hero'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)
        # frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_m, text='반격 던전')

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang'].trace(
            'w', lambda *args: self.callback_bangyeok_dungeon_sotang(args,
                                                                     lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('소탕', width=25),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_sotang'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use'].trace(
            'w', lambda *args: self.callback_bangyeok_dungeon_hero_use(args,
                                                                       lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('영웅 자동 선택 사용'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero_use'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택", width=25)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero'].trace(
            'w', lambda *args: self.callback_bangyeok_dungeon_hero(args,
                                                                   lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero'] = combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][
                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_hero'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("입장 레벨", width=28)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level'].trace(
            'w', lambda *args: self.callback_bangyeok_dungeon_level(args,
                                                                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level')
        )
        combobox_list = []
        for i in range(0, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level'] = 6

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][
                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_level'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("방어 아이콘 클릭 주기(ms)", width=28)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response'].trace(
            'w', lambda *args: self.callback_bangyeok_dungeon_response(args,
                                                                       lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response')
        )
        combobox_list = []
        for i in range(1, 2001):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response'] = 10

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][
                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'bangyeok_dungeon_response'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_m, text='장비교체')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택", width=25)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero'].trace(
            'w', lambda *args: self.callback_jangbi_change_set_hero(args,
                                                                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero'] = combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][
                         lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set_hero'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("장비 세트 번호(0:안함)", width=28)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set'].trace(
            'w', lambda *args: self.callback_jangbi_change_set(args,
                                                               lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set')
        )
        combobox_list = []
        for i in range(0, 4):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set'] = 1

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'jangbi_change_set'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_label = ttk.LabelFrame(frame_r, text='우편함')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택", width=27)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero'].trace(
            'w', lambda *args: self.callback_mail_select_hero(args,
                                                              lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero'] = \
            combobox_list[1]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_hero'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("승급석 선택", width=19)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone'].trace(
            'w', lambda *args: self.callback_mail_select_stone(args,
                                                               lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone')
        )
        combobox_list = LYBBlade2.stone_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone'] = \
            combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone'],
            state="readonly",
            height=10,
            width=16,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'mail_select_stone'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label = ttk.LabelFrame(frame_r, text='레이드')

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use'].trace(
            'w',
            lambda *args: self.callback_raid_hero_use(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('영웅 자동 선택 사용', width=25),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero_use'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("영웅 선택", width=27)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero'].trace(
            'w', lambda *args: self.callback_raid_hero(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero')
        )
        combobox_list = LYBBlade2.hero_list

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero'] = \
            combobox_list[0]

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero'],
            state="readonly",
            height=10,
            width=8,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_hero'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("전투 제한 시간(초)(0:없음)")
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit'].trace(
            'w', lambda *args: self.callback_raid_combat_limit(args,
                                                               lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit')
        )
        combobox_list = []
        for i in range(0, 3601, 10):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit'] = 0

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_combat_limit'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label_inner = ttk.LabelFrame(frame_label, text='난폭한 하랑')

        frame = ttk.Frame(frame_label_inner)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_0'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_0'].trace(
            'w', lambda *args: self.callback_raid_make_room_0(args,
                                                              lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_0')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_0' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_0'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('방 만들기', width=15),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_0'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_0'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_0'].trace(
            'w', lambda *args: self.callback_raid_team_0(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_0')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_0' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_0'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('팀원과 다시하기', width=19),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_0'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label_inner)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("입장 레벨", width=28)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level'].trace(
            'w', lambda *args: self.callback_raid_level(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level')
        )
        combobox_list = []
        for i in range(0, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level'] = 3

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label_inner = ttk.LabelFrame(frame_label, text='사르곤')
        frame = ttk.Frame(frame_label_inner)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_1'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_1'].trace(
            'w', lambda *args: self.callback_raid_make_room_1(args,
                                                              lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_1')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_1' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_1'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('방 만들기', width=15),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_make_room_1'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_1'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_1'].trace(
            'w', lambda *args: self.callback_raid_team_1(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_1')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_1' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_1'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('팀원과 다시하기', width=19),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_team_1'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label_inner)
        label = ttk.Label(
            master=frame,
            text=self.get_option_text("입장 레벨", width=28)
        )
        label.pack(side=tkinter.LEFT)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1'].trace(
            'w', lambda *args: self.callback_raid_level_1(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1')
        )
        combobox_list = []
        for i in range(0, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1'] = 3

        combobox = ttk.Combobox(
            master=frame,
            values=combobox_list,
            textvariable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1'],
            state="readonly",
            height=10,
            width=5,
            font=lybconstant.LYB_FONT
        )
        combobox.set(
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'raid_level_1'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 탭 좌측
        frame_l = ttk.Frame(self.inner_frame_dic['work_2_tab_frame'])

        frame_label = ttk.LabelFrame(frame_l, text='모두팔기')

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup'].trace(
            'w', lambda *args: self.callback_sell_levelup(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('모두팔기 대신 재료 레벨업하기'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_levelup'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe'].trace(
            'w', lambda *args: self.callback_sell_bunhe(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe'] = False

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('모두팔기 대신 자동 분해하기'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_bunhe'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame_label_inner = ttk.LabelFrame(frame_label, text='작업을 수행할 영웅 선택')
        frame = ttk.Frame(frame_label_inner)

        for i in range(len(LYBBlade2.hero_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + str(i)] = tkinter.BooleanVar(
                frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '0'].trace(
                    'w', lambda *args: self.callback_sell_item_hero_0(args,
                                                                      lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '1'].trace(
                    'w', lambda *args: self.callback_sell_item_hero_1(args,
                                                                      lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '2'].trace(
                    'w', lambda *args: self.callback_sell_item_hero_2(args,
                                                                      lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '2')
                )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '3'].trace(
                    'w', lambda *args: self.callback_sell_item_hero_3(args,
                                                                      lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + '3')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + str(i) in self.configure.common_config[
                self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + str(i)] = True

            check_box = ttk.Checkbutton(

                master=frame,
                text=LYBBlade2.hero_list[i],
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_hero' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock'].trace(
            'w',
            lambda *args: self.callback_sell_holy_lock(args, lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock'] = False

        s = ttk.Style()
        s.configure('red_label.TCheckbutton', foreground='red')
        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('[신성한 빛] 아이템 잠금하기'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock'],
            onvalue=True,
            offvalue=False,
            style='red_label.TCheckbutton'
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        # frame.pack(anchor=tkinter.NW)

        frame_label_inner = ttk.LabelFrame(frame_label, text='잠금할 [신성한 빛] 아이템 등급')
        frame = ttk.Frame(frame_label_inner)

        for i in range(6):
            self.option_dic[
                lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + str(i)] = tkinter.BooleanVar(frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '0'].trace(
                    'w', lambda *args: self.callback_sell_holy_lock_rank_0(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '1'].trace(
                    'w', lambda *args: self.callback_sell_holy_lock_rank_1(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '2'].trace(
                    'w', lambda *args: self.callback_sell_holy_lock_rank_2(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '2')
                )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '3'].trace(
                    'w', lambda *args: self.callback_sell_holy_lock_rank_3(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '3')
                )
            elif i == 4:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '4'].trace(
                    'w', lambda *args: self.callback_sell_holy_lock_rank_4(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '4')
                )
            elif i == 5:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '5'].trace(
                    'w', lambda *args: self.callback_sell_holy_lock_rank_5(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + '5')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + str(i) in \
                    self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + str(i)] = True

            check_box = ttk.Checkbutton(

                master=frame,
                text='★' + str(i + 1),
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_holy_lock_rank' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        # frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label_inner = ttk.LabelFrame(frame_label, text='분류')
        frame = ttk.Frame(frame_label_inner)

        for i in range(len(LYBBlade2.item_equip_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + str(i)] = tkinter.BooleanVar(
                frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + '0'].trace(
                    'w', lambda *args: self.callback_sell_item_equip_0(args,
                                                                       lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + '1'].trace(
                    'w', lambda *args: self.callback_sell_item_equip_1(args,
                                                                       lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + '2'].trace(
                    'w', lambda *args: self.callback_sell_item_equip_2(args,
                                                                       lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + '2')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + str(i) in self.configure.common_config[
                self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + str(i)] = True

            check_box = ttk.Checkbutton(

                master=frame,
                text=LYBBlade2.item_equip_list[i],
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_equip' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label_inner = ttk.LabelFrame(frame_label, text='등급')
        frame = ttk.Frame(frame_label_inner)

        for i in range(7):
            self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + str(i)] = tkinter.BooleanVar(
                frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '0'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_0(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '1'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_1(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '2'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_2(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '2')
                )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '3'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_3(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '3')
                )
            elif i == 4:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '4'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_4(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '4')
                )
            elif i == 5:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '5'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_5(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '5')
                )
            elif i == 6:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '6'].trace(
                    'w', lambda *args: self.callback_sell_sell_item_rank_6(args,
                                                                           lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + '6')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + str(i) in self.configure.common_config[
                self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + str(i)] = False

            check_box = ttk.Checkbutton(

                master=frame,
                text='★' + str(i + 1),
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_rank' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label_inner = ttk.LabelFrame(frame_label, text='상태')
        frame = ttk.Frame(frame_label_inner)

        for i in range(len(LYBBlade2.item_status_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + str(i)] = tkinter.BooleanVar(
                frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + '0'].trace(
                    'w', lambda *args: self.callback_sell_item_status_0(args,
                                                                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + '0')
                )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + '1'].trace(
                    'w', lambda *args: self.callback_sell_item_status_1(args,
                                                                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + '1')
                )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + '2'].trace(
                    'w', lambda *args: self.callback_sell_item_status_2(args,
                                                                        lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + '2')
                )

            if not lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + str(i) in self.configure.common_config[
                self.game_name]:
                self.configure.common_config[self.game_name][
                    lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + str(i)] = True

            check_box = ttk.Checkbutton(

                master=frame,
                text=LYBBlade2.item_status_list[i],
                variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_WORK + 'sell_item_status' + str(i)],
                onvalue=True,
                offvalue=False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.NW)
        frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['work_2_tab_frame'])
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['work_2_tab_frame'])
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 알림 탭 좌
        frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
        frame_label = ttk.Frame(frame_l)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat'].trace(
            'w', lambda *args: self.callback_notify_jeontoo_defeat(args,
                                                                   lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('전투패배'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'jeontoo_defeat'],
            onvalue=True,
            offvalue=False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.NW)

        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock'].trace(
            'w', lambda *args: self.callback_notify_holy_item_lock(args,
                                                                   lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock')
        )
        if not lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock' in self.configure.common_config[
            self.game_name]:
            self.configure.common_config[self.game_name][
                lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock'] = True

        check_box = ttk.Checkbutton(

            master=frame,
            text=self.get_option_text('신성한 빛 아이템 잠금'),
            variable=self.option_dic[lybconstant.LYB_DO_STRING_BLADE2_NOTIFY + 'holy_item_lock'],
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

    def callback_jadong_bunhe_ganghwa(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_rank_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_rank_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_rank_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_rank_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_rank_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_rank_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_tier_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_tier_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_tier_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jadong_bunhe_tier_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_mail_select_stone(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_mail_select_hero(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_notify_holy_item_lock(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_notify_jeontoo_defeat(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_levelup(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_bunhe(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_hero_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_hero_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_hero_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_hero_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock_rank_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock_rank_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock_rank_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock_rank_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock_rank_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_holy_lock_rank_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jangbi_change_set_hero(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jangbi_change_set(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_bangyeok_dungeon_response(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_bangyeok_dungeon_hero_use(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_bangyeok_dungeon_sotang(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_bangyeok_dungeon_hero(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_bangyeok_dungeon_level(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_team_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_make_room_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_team_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_make_room_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_hero_use(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_hero(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_combat_limit(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_level_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_level(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_status_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_status_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_status_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_sell_item_rank_6(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_equip_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_equip_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_sell_item_equip_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jeomryoungjeon_hero_use(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jeomryoungjeon_hero(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_team_count(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_ildeil_count(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_ildeil_hero_use(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_ildeil_hero_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_ildeil_hero_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_ilil_quest(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_ilil_quest_continue(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_jeomryoungjeon_notice(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_raid_notice(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_tag_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_next(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_triple(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_limit_count(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_bot_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_level(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_act(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_stage(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_repeat(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_retry(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_hero_use(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_hero_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_hero_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_moheom_auto(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_main_quest_stringvar(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def callback_main_quest_each_stringvar(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

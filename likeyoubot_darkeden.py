import likeyoubot_game as lybgame
import likeyoubot_darkeden_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy


class LYBDarkEden(lybgame.LYBGame):
    work_list = [
        '게임 시작',
        '로그인',
        '자동 사냥',
        '메인 퀘스트',
        '일일 퀘스트',
        '지역 퀘스트',
        '종족임무',
        '일일임무',
        '결투장',
        '토벌대',
        '판매',
        '분해',
        '가상수련장',
        '특수던전',
        '보상',
        '이벤트',
        '길드',
        '뽑기',
        '도감',

        '알림',
        '[반복 시작]',
        '[반복 종료]',
        '[작업 대기]',
        '[작업 예약]',
        '']

    darkeden_icon_list = [
        'darkeden_icon',
        'darkeden_icon_2',
    ]

    area_list = [
        '에슬라니안 시',
        '림보성 지역',
        '드로베타 공단',
        '브랑코 시티'
        ]

    sub_area_list = [
        [
            '페이악 터널',
        ],
        [
            '고르고바 터널',
        ],
        [
            '드로베타 MID',
            '드로베타 SW',
            '드로베타 NE',
            '드로베타 NW',
            '아이센 던전 B1',
            '라옴 던전 B1',
            '드로베타 SE',
        ],
        [
            '브랑코 MID',
            '브랑코 NW',
        ]
    ]

    sub_area_dic = {
        area_list[0]: sub_area_list[0],
        area_list[1]: sub_area_list[1],
        area_list[2]: sub_area_list[2],
        area_list[3]: sub_area_list[3],
    }
    sub_area_monster_dic = {
        sub_area_list[0][0] : [
            '선택안함',
            '미누투스',
            '디오네아',
        ],
        sub_area_list[1][0] : [
            '선택안함',
            '미누투스',
            '디오네아',
        ],
        sub_area_list[2][0] : [
            '선택안함',
            '거터미누투스',
            '블루케니스',
            '미스트앵글러', 
            '튜머뮤턴트',
            '튜커클링커',  
            '인펙티드월딩봇',  
            '인펙티드트랜스포트봇',           
        ],
        sub_area_list[2][1] : [
            '선택안함',
            '빅맨티스',            
        ],
        sub_area_list[2][2] : [
            '선택안함',
            '알칸',            
        ],
        sub_area_list[2][3] : [
            '선택안함',      
            '솔져',
            '인페스트 레이디',
        ],
        sub_area_list[2][4] : [
            '선택안함',  
        ],
        sub_area_list[2][5] : [
            '선택안함',  
        ],
        sub_area_list[2][6] : [
            '선택안함',  
            '앵글러',
        ],
        sub_area_list[3][0] : [
            '선택안함',
            '디케이리서치',            
        ],
        sub_area_list[3][1] : [
            '선택안함',
            'B-봇',   
            '세크워치봇',         
        ],
    }
    sub_area_npc_dic = {
        sub_area_list[0][0] : [
            '선택안함',
        ],
        sub_area_list[1][0] : [
            '선택안함',
        ],
        sub_area_list[2][0] : [
            '선택안함',          
        ],
        sub_area_list[2][1] : [
            '선택안함',           
        ],
        sub_area_list[2][2] : [
            '선택안함',      
        ],
        sub_area_list[2][3] : [
            '선택안함',    
            '애슬라니안 SW',  
        ],
        sub_area_list[2][4] : [
            '선택안함',    
            '아이센 던전 B2',  
        ],
        sub_area_list[2][5] : [
            '선택안함',    
            '라옴 던전 B2',  
        ],
        sub_area_list[3][0] : [
            '선택안함',         
        ],
        sub_area_list[3][1] : [
            '선택안함',    
        ],
    }
    item_list = [
        '무기',
        '방어구',
        '악세사리',
        '제작재료',
    ]

    item_quality_list = [
        '일반',
        '고급',
        '희귀',
        '영웅',
        '전설',
    ]

    special_dungeon_list = [
        '재료',
        '경험치',
        '스킬',
        '골드',
    ]

    difficulty_list = [
        '쉬움',
        '보통',
        '어려움',
    ]

    option_list = [
        '강화 아이템 포함',
        '거래가능 아이템 포함',
    ]

    guild_immu_list = [
        '길드 레벨업',
        '부수고 또 부수고',
        '골드 사용',
        '포션 사용',
        '종족임무 수행',
        '일일퀘스트 수행',
        '지역퀘스트 완료',

    ]

    dungeon_floor_list = [
        '선택안함',
        '아이센 던전 B2',
        '아이센 던전 B3',
        '아이센 던전 B4',
        '라옴 던전 B2',
        '라옴 던전 B3',
        '라옴 던전 B4',
        '라옴 던전 B5',
    ]

    dungeon_floor_monster_list = [
        [
            '선택안함',
        ],
        [
            '선택안함',
            '상급 페스트네일',
        ],
        [
            '선택안함',
        ],
        [
            '선택안함',
            '다크헤이즈',
            '인세이나',
        ],
        [
            '선택안함',
        ],
        [
            '선택안함',
        ],
        [
            '선택안함',
        ],
        [
            '선택안함',
        ],
    ]

    dungeon_floor_npc_list = [
        [
            '선택안함',
        ],
        [
            '선택안함',
            '아이센 던전 B3',
        ],
        [
            '선택안함',
            '아이센 던전 B4',
        ],
        [
            '선택안함',
            '아이센 던전 B3',
        ],
        [
            '선택안함',
            '라옴 던전 B3',
        ],
        [
            '선택안함',
            '라옴 던전 B4',
        ],
        [
            '선택안함',
            '라옴 던전 B5',
        ],
        [
            '선택안함',
        ],
    ]

    dungeon_floor_monster_dic = {
        dungeon_floor_list[0]: dungeon_floor_monster_list[0],
        dungeon_floor_list[1]: dungeon_floor_monster_list[1],
        dungeon_floor_list[2]: dungeon_floor_monster_list[2],
        dungeon_floor_list[3]: dungeon_floor_monster_list[3],
        dungeon_floor_list[4]: dungeon_floor_monster_list[4],
        dungeon_floor_list[5]: dungeon_floor_monster_list[5],
        dungeon_floor_list[6]: dungeon_floor_monster_list[6],
        dungeon_floor_list[7]: dungeon_floor_monster_list[7],
    }

    dungeon_floor_npc_dic = {
        dungeon_floor_list[0]: dungeon_floor_npc_list[0],
        dungeon_floor_list[1]: dungeon_floor_npc_list[1],
        dungeon_floor_list[2]: dungeon_floor_npc_list[2],
        dungeon_floor_list[3]: dungeon_floor_npc_list[3],
        dungeon_floor_list[4]: dungeon_floor_npc_list[4],
        dungeon_floor_list[5]: dungeon_floor_npc_list[5],
        dungeon_floor_list[6]: dungeon_floor_npc_list[6],
        dungeon_floor_list[7]: dungeon_floor_npc_list[7],
    }

    quest_scene_jiyeok_list = [
        '드로베타',
        '브랑코',
    ]

    quest_scene_jiyeok_quest_list = [
        [
            '드로베타 정화8',
        ],
        [
            '브랑코 정화1',
            '브랑코 정화2',
        ]

    ]

    quest_scene_jiyeok_quest_dic = {
        quest_scene_jiyeok_list[0] : quest_scene_jiyeok_quest_list[0],
        quest_scene_jiyeok_list[1] : quest_scene_jiyeok_quest_list[1],
    }

    def __init__(self, game_name, game_data_name, window):
        lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_DARKEDEN, lybconstant.LYB_GAME_DATA_DARKEDEN, window)

    def process(self, window_image):
        rc = super(LYBDarkEden, self).process(window_image)
        if rc < 0:
            return rc

        return rc

    def custom_check(self, window_image, window_pixel):

        resource_name = 'skip_dehwa_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(5):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(710, 335, 790, 360)
            )
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('대화 스킵: ' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        resource_name = 'skip_npc_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(5):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(710, 400, 790, 450)
            )
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('NPC 대화: ' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        resource_name = 'confirm_20181129_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(3):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(360, 300, 450, 450)
            )
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('확인: ' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        resource_name = 'confirm_20181129_1_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(3):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.8,
                custom_flag=1,
                custom_rect=(360, 300, 450, 450)
            )
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('확인: ' + str(match_rate))
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

        if True:
            self.process_tutorial()


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

        self.click_all_tutorial_point()

        return ''

    def click_all_tutorial_point(self):

        tutorial_check_threshold = self.get_option('tutorial_check_threshold')
        if tutorial_check_threshold == None:
            tutorial_check_threshold = 0

        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint('tutorial_last_check_time')

        if elapsed_time > self.period_bot(3):
            tutorial_check_threshold = 0

        self.get_scene('main_scene').set_checkpoint('tutorial_last_check_time')

        if tutorial_check_threshold > 5:
            resource_name = 'tutorial_loc'
            if not resource_name in self.resource_manager.resource_dic:
                return

            resource = self.resource_manager.resource_dic[resource_name]

            tutorial_iterator = self.get_option('tutorial_iterator')
            if tutorial_iterator is None:
                tutorial_iterator = 0

            if tutorial_iterator >= len(resource):
                self.set_option('tutorial_check_threshold', 0)
                self.set_option('tutorial_iterator', 0)
            else:
                pb_name = resource[tutorial_iterator]
                self.set_option('tutorial_iterator', tutorial_iterator + 1)
                self.logger.debug(pb_name)
                self.mouse_click(pb_name)
                self.interval = 0.01
        else:
            self.set_option('tutorial_check_threshold', tutorial_check_threshold + 1)

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
            for each_icon in LYBDarkEden.darkeden_icon_list:
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
            for each_icon in LYBDarkEden.darkeden_icon_list:
                (loc_x, loc_y), match_rate = self.locationOnWindowPart(
                    window_image,
                    self.resource_manager.pixel_box_dic[each_icon],
                    custom_threshold=0.8,
                    custom_flag=1,
                    custom_rect=(30, 10, 740, 370)
                )
                # self.logger.info(each_icon + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
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
        self.scene_dic[scene_name] = lybscene.LYBDarkEdenScene(scene_name)
        self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
        self.scene_dic[scene_name].setGameObject(self)

    def process_tutorial(self):
        # resource_name = 'control_pad_tutorial_loc'
        # elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        # if elapsed_time > self.period_bot(10):
        #     (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
        #         self.window_image,
        #         resource_name,
        #         custom_threshold=0.7,
        #         custom_flag=1,
        #         custom_rect=(130, 300, 400, 340)
        #     )
        #     if loc_x != -1:
        #         self.get_scene('main_scene').set_checkpoint(resource_name)
        #         self.logger.info('콘트롤 패드 튜토리얼: ' + str(match_rate))
        #         self.get_scene('main_scene').lyb_mouse_drag('pad_direction_center', 'pad_direction_1', stop_delay=2)
        #         return 'skip'
    
        resource_name = 'potion_tutorial_loc'
        elapsed_time = time.time() - self.get_scene('main_scene').get_checkpoint(resource_name)
        if elapsed_time > self.period_bot(10):
            (loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
                self.window_image,
                resource_name,
                custom_threshold=0.7,
                custom_flag=1,
                custom_rect=(5, 180, 150, 210),
            )
            if loc_x != -1:
                self.get_scene('main_scene').set_checkpoint(resource_name)
                self.logger.info('상점에서 회복 물약 구입' + str(match_rate))
                self.get_scene('sangjeom_scene').status = 0
                self.get_scene('main_scene').lyb_mouse_click_location(loc_x, loc_y)
                return 'skip'

class LYBDarkEdenTab(lybgame.LYBGameTab):
    def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height,
                 game_name=lybconstant.LYB_GAME_DARKEDEN):
        lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height,
                                    game_name)

    def set_work_list(self):
        lybgame.LYBGameTab.set_work_list(self)

        for each_work in LYBDarkEden.work_list:
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
        frame_label = ttk.LabelFrame(frame_l, text='전투')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('자동 전환 감지 횟수(회)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count'].trace(
            'w', lambda *args: self.auto_limit_count(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count')
            )
        combobox_list = []
        for i in range(1, 11):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count'] = 5

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'auto_limit_count'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_l, text='이동')
        frame = ttk.Frame(frame_label)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'quick_move_gold'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'quick_move_gold'].trace(
            'w', lambda *args: self.quick_move_gold(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'quick_move_gold')
            )
        if not lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'quick_move_gold' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'quick_move_gold'] = False

        check_box = ttk.Checkbutton(

            master              = frame,
            text                = '골드 사용 즉시 이동', 
            variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'quick_move_gold'],
            onvalue             = True, 
            offvalue            = False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 일반 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_label = ttk.LabelFrame(frame_m, text='던전 이동 세부 설정')

        self.dungeon_floor_monster_combobox = []
        self.dungeon_floor_npc_combobox = []

        for i in range(6):
            frame = ttk.Frame(frame_label)
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i)] = tkinter.StringVar(frame)            
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(i)] = tkinter.StringVar(frame)  
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(i)] = tkinter.StringVar(frame)
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(i)] = tkinter.StringVar(frame)

            combobox_list = LYBDarkEden.dungeon_floor_list

            if not lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i) in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i)] = combobox_list[0]

            combobox = ttk.Combobox(
                master              = frame,
                values              = combobox_list, 
                textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i)], 
                state               = "readonly",
                height              = 10,
                width               = 15,
                font                = lybconstant.LYB_FONT 
                )
            combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i)])
            combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        
            label = ttk.Label(
                master              = frame, 
                text                = '>>'
                )
            label.pack(side=tkinter.LEFT)

            try:
                area_index = LYBDarkEden.dungeon_floor_list.index(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i)])
                combobox_list = LYBDarkEden.dungeon_floor_monster_list[area_index]

                if not lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(i) in self.configure.common_config[self.game_name]:                    
                    self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(i)] = combobox_list[0]
            except ValueError:
                area_index = 0
                combobox_list = LYBDarkEden.dungeon_floor_monster_list[area_index]
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(i)] = combobox_list[0]

            self.dungeon_floor_monster_combobox.append(
                ttk.Combobox(
                    master              = frame,
                    values              = combobox_list, 
                    textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(i)], 
                    state               = "readonly",
                    height              = 10,
                    width               = 15,
                    font                = lybconstant.LYB_FONT 
                    )
                )
            self.dungeon_floor_monster_combobox[i].set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(i)])
            self.dungeon_floor_monster_combobox[i].pack(anchor=tkinter.W, side=tkinter.LEFT)


            try:
                area_index = LYBDarkEden.dungeon_floor_list.index(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(i)])
                combobox_list = LYBDarkEden.dungeon_floor_npc_list[area_index]

                if not lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(i) in self.configure.common_config[self.game_name]:                    
                    self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(i)] = combobox_list[0]
            except ValueError:
                area_index = 0
                combobox_list = LYBDarkEden.dungeon_floor_npc_list[area_index]
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(i)] = combobox_list[0]

            self.dungeon_floor_npc_combobox.append(
                ttk.Combobox(
                    master              = frame,
                    values              = combobox_list, 
                    textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(i)], 
                    state               = "readonly",
                    height              = 10,
                    width               = 15,
                    font                = lybconstant.LYB_FONT 
                    )
                )
            self.dungeon_floor_npc_combobox[i].set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(i)])
            self.dungeon_floor_npc_combobox[i].pack(anchor=tkinter.W, side=tkinter.LEFT)

            combobox_list = []
            for j in range(1, 5):
                combobox_list.append(str(j))

            if not lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(i) in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(i)] = 1

            combobox = ttk.Combobox(
                master              = frame,
                values              = combobox_list, 
                textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(i)], 
                state               = "readonly",
                height              = 10,
                width               = 7,
                font                = lybconstant.LYB_FONT 
                )
            combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(i)])
            combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(0)].trace(
                    'w', lambda *args: self.dungeon_floor_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(0))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(0)].trace(
                    'w', lambda *args: self.dungeon_floor_monster_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(0))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(0)].trace(
                    'w', lambda *args: self.dungeon_floor_npc_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(0))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(0)].trace(
                    'w', lambda *args: self.dungeon_floor_order_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(0))
                    )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(1)].trace(
                    'w', lambda *args: self.dungeon_floor_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(1))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(1)].trace(
                    'w', lambda *args: self.dungeon_floor_monster_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(1))
                    )  
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(1)].trace(
                    'w', lambda *args: self.dungeon_floor_npc_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(1))
                    ) 
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(1)].trace(
                    'w', lambda *args: self.dungeon_floor_order_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(1))
                    ) 
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(2)].trace(
                    'w', lambda *args: self.dungeon_floor_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(2))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(2)].trace(
                    'w', lambda *args: self.dungeon_floor_monster_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(2))
                    )  
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(2)].trace(
                    'w', lambda *args: self.dungeon_floor_npc_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(2))
                    ) 
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(2)].trace(
                    'w', lambda *args: self.dungeon_floor_order_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(2))
                    ) 
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(3)].trace(
                    'w', lambda *args: self.dungeon_floor_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(3))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(3)].trace(
                    'w', lambda *args: self.dungeon_floor_monster_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(3))
                    )  
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(3)].trace(
                    'w', lambda *args: self.dungeon_floor_npc_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(3))
                    ) 
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(3)].trace(
                    'w', lambda *args: self.dungeon_floor_order_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(3))
                    ) 
            elif i == 4:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(4)].trace(
                    'w', lambda *args: self.dungeon_floor_4(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(4))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(4)].trace(
                    'w', lambda *args: self.dungeon_floor_monster_4(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(4))
                    )  
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(4)].trace(
                    'w', lambda *args: self.dungeon_floor_npc_4(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(4))
                    ) 
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(4)].trace(
                    'w', lambda *args: self.dungeon_floor_order_4(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(4))
                    ) 
            elif i == 5:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(5)].trace(
                    'w', lambda *args: self.dungeon_floor_5(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor' + str(5))
                    )
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(5)].trace(
                    'w', lambda *args: self.dungeon_floor_monster_5(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(5))
                    )  
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(5)].trace(
                    'w', lambda *args: self.dungeon_floor_npc_5(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(5))
                    ) 
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(5)].trace(
                    'w', lambda *args: self.dungeon_floor_order_5(args, lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_order' + str(5))
                    ) 

            frame.pack(anchor=tkinter.W)        

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 일반 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 좌측
        frame_l = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_label = ttk.LabelFrame(frame_l, text='자동 사냥')

        frame = ttk.Frame(frame_label)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party'].trace(
            'w', lambda *args: self.auto_party(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party')
            )
        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party'] = False

        check_box = ttk.Checkbutton(

            master              = frame,
            text                = '파티 초대', 
            variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_party'],
            onvalue             = True, 
            offvalue            = False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)
        frame = ttk.Frame(frame_label)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok'].trace(
            'w', lambda *args: self.auto_jiyeok(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok')
            )
        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok'] = False

        check_box = ttk.Checkbutton(

            master              = frame,
            text                = '지역 퀘스트', 
            variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jiyeok'],
            onvalue             = True, 
            offvalue            = False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok'].trace(
            'w', lambda *args: self.auto_jongjok(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok')
            )
        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok'] = False

        check_box = ttk.Checkbutton(

            master              = frame,
            text                = '종족 퀘스트', 
            variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok'],
            onvalue             = True, 
            offvalue            = False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

        frame.pack(anchor=tkinter.W)
        
        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('클릭할 인식 순서(번째)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order'].trace(
            'w', lambda *args: self.auto_order(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order')
            )
        combobox_list = []
        for i in range(1, 5):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order'] = 1

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_order'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('진행 시간(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration'].trace(
            'w', lambda *args: self.auto_duration(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration')
            )
        combobox_list = []
        for i in range(0, 86401, 60):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration'] = 3600

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_duration'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('판매 체크 주기(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period'].trace(
            'w', lambda *args: self.auto_sell_period(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period')
            )
        combobox_list = []
        for i in range(0, 3601):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period'] = 300

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sell_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('분해 체크 주기(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period'].trace(
            'w', lambda *args: self.auto_bunhe_period(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period')
            )
        combobox_list = []
        for i in range(0, 3601):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period'] = 300

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_bunhe_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('일일 퀘스트 체크 주기(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period'].trace(
            'w', lambda *args: self.auto_ilil_quest_period(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period')
            )
        combobox_list = []
        for i in range(0, 3601):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period'] = 1800

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_ilil_quest_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('도감 체크 주기(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period'].trace(
            'w', lambda *args: self.auto_dogam_period(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period')
            )
        combobox_list = []
        for i in range(0, 3601):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period'] = 1200

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_dogam_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('종족 퀘스트 수행 횟수(회)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count'].trace(
            'w', lambda *args: self.auto_jongjok_quest_count(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count')
            )
        combobox_list = []
        for i in range(0, 101):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count'] = 10

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_jongjok_quest_count'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)


        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('월드맵 체크 주기(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period'].trace(
            'w', lambda *args: self.auto_move_check_period(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period')
            )
        combobox_list = []
        for i in range(0, 3601):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period'] = 120

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_move_check_period'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('월드맵(대분류)', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area'].trace(
            'w', lambda *args: self.auto_area(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area')
            )
        combobox_list = LYBDarkEden.area_list

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area'] = combobox_list[0]

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)        

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('지역맵(중분류)', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area'].trace(
            'w', lambda *args: self.auto_sub_area(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area')
            )

        try:
            area_index = LYBDarkEden.area_list.index(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_area'])
            combobox_list = LYBDarkEden.sub_area_list[area_index]
            if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area' in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area'] = combobox_list[0]
        except ValueError:
            area_index = 0
            combobox_list = LYBDarkEden.sub_area_list[area_index]
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area'] = combobox_list[0]


        self.auto_sub_area_combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        self.auto_sub_area_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area'])
        self.auto_sub_area_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('몬스터(소분류1)', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster'].trace(
            'w', lambda *args: self.auto_monster(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster')
            )

        combobox_list = LYBDarkEden.sub_area_monster_dic[self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area']]

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster'] = combobox_list[0]

        self.auto_monster_combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        self.auto_monster_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster'])
        self.auto_monster_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('NPC/포탈(소분류2)', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc'].trace(
            'w', lambda *args: self.auto_npc(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc')
            )

        combobox_list = LYBDarkEden.sub_area_npc_dic[self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area']]

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc'] = combobox_list[0]

        self.auto_npc_combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        self.auto_npc_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc'])
        self.auto_npc_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_l, text='특수던전')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('던전 선택', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon'].trace(
            'w', lambda *args: self.special_dungeon(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon')
            )
        combobox_list = LYBDarkEden.special_dungeon_list

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon'] = combobox_list[1]

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W) 

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('난이도 선택', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty'].trace(
            'w', lambda *args: self.special_dungeon_difficulty(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty')
            )
        combobox_list = LYBDarkEden.difficulty_list

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty'] = combobox_list[1]

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'special_dungeon_difficulty'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W) 

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
        frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)
        # 작업 탭 중간
        frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
        frame_label = ttk.LabelFrame(frame_m, text='판매')

        frame = ttk.Frame(frame_label)
        for i in range(len(LYBDarkEden.item_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(i)] = tkinter.BooleanVar(frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(0)].trace(
                    'w', lambda *args: self.sell_item_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(0))
                    )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(1)].trace(
                    'w', lambda *args: self.sell_item_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(1))
                    )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(2)].trace(
                    'w', lambda *args: self.sell_item_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(2))
                    )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(3)].trace(
                    'w', lambda *args: self.sell_item_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(3))
                    )
            if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(i) in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(i)] = False

            check_box = ttk.Checkbutton(

                master              = frame,
                text                = LYBDarkEden.item_list[i], 
                variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_' + str(i)],
                onvalue             = True, 
                offvalue            = False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)


        frame = ttk.Frame(frame_label)
        for i in range(len(LYBDarkEden.item_quality_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(i)] = tkinter.BooleanVar(frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(0)].trace(
                    'w', lambda *args: self.sell_item_quality_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(0))
                    )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(1)].trace(
                    'w', lambda *args: self.sell_item_quality_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(1))
                    )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(2)].trace(
                    'w', lambda *args: self.sell_item_quality_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(2))
                    )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(3)].trace(
                    'w', lambda *args: self.sell_item_quality_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(3))
                    )
            elif i == 4:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(4)].trace(
                    'w', lambda *args: self.sell_item_quality_4(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(4))
                    )
            if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(i) in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(i)] = False

            check_box = ttk.Checkbutton(

                master              = frame,
                text                = LYBDarkEden.item_quality_list[i], 
                variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'sell_item_quality_' + str(i)],
                onvalue             = True, 
                offvalue            = False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

        frame_label = ttk.LabelFrame(frame_m, text='분해')

        frame = ttk.Frame(frame_label)
        for i in range(len(LYBDarkEden.option_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(i)] = tkinter.BooleanVar(frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(0)].trace(
                    'w', lambda *args: self.bunhe_option_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(0))
                    )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(1)].trace(
                    'w', lambda *args: self.bunhe_option_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(1))
                    )

            if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(i) in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(i)] = False

            check_box = ttk.Checkbutton(

                master              = frame,
                text                = LYBDarkEden.option_list[i], 
                variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_option_' + str(i)],
                onvalue             = True, 
                offvalue            = False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame = ttk.Frame(frame_label)
        for i in range(len(LYBDarkEden.item_quality_list)):
            self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(i)] = tkinter.BooleanVar(frame)
            if i == 0:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(0)].trace(
                    'w', lambda *args: self.bunhe_item_quality_0(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(0))
                    )
            elif i == 1:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(1)].trace(
                    'w', lambda *args: self.bunhe_item_quality_1(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(1))
                    )
            elif i == 2:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(2)].trace(
                    'w', lambda *args: self.bunhe_item_quality_2(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(2))
                    )
            elif i == 3:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(3)].trace(
                    'w', lambda *args: self.bunhe_item_quality_3(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(3))
                    )
            elif i == 4:
                self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(4)].trace(
                    'w', lambda *args: self.bunhe_item_quality_4(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(4))
                    )
            if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(i) in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(i)] = False

            check_box = ttk.Checkbutton(

                master              = frame,
                text                = LYBDarkEden.item_quality_list[i], 
                variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'bunhe_item_quality_' + str(i)],
                onvalue             = True, 
                offvalue            = False
            )
            check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)        

        frame_label = ttk.LabelFrame(frame_m, text='길드')
        frame = ttk.Frame(frame_label)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu'] = tkinter.BooleanVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu'].trace(
            'w', lambda *args: self.guild_immu(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu'
            ))
        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu'] = True

        check_box = ttk.Checkbutton(

            master              = frame,
            text                = '길드 임무', 
            variable            = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'guild_immu'],
            onvalue             = True, 
            offvalue            = False
        )
        check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)   
        frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 작업 탭 우측
        frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])

        frame_label = ttk.LabelFrame(frame_r, text='메인 퀘스트')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('진행 시간(초)', width=27)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration'].trace(
            'w', lambda *args: self.main_quest_duration(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration')
            )
        combobox_list = []
        for i in range(0, 86401, 60):
            combobox_list.append(str(i))

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration'] = 3600

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration'], 
            state               = "readonly",
            height              = 10,
            width               = 7,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'main_quest_duration'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)

        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5) 

        frame_label = ttk.LabelFrame(frame_r, text='지역 퀘스트')

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('지역(대분류)', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area'].trace(
            'w', lambda *args: self.jiyeok_quest_area(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area')
            )
        combobox_list = LYBDarkEden.quest_scene_jiyeok_list

        if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area' in self.configure.common_config[self.game_name]:
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area'] = combobox_list[0]

        combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area'])
        combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)        

        frame = ttk.Frame(frame_label)
        label = ttk.Label(
            master              = frame, 
            text                = self.get_option_text('퀘스트(중분류)', width=19)
            )
        label.pack(side=tkinter.LEFT)

        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select'] = tkinter.StringVar(frame)
        self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select'].trace(
            'w', lambda *args: self.jiyeok_quest_select(args, lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select')
            )

        try:
            area_index = LYBDarkEden.quest_scene_jiyeok_list.index(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_area'])
            combobox_list = LYBDarkEden.quest_scene_jiyeok_quest_list[area_index]
            if not lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select' in self.configure.common_config[self.game_name]:
                self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select'] = combobox_list[0]
        except ValueError:
            area_index = 0
            combobox_list = LYBDarkEden.quest_scene_jiyeok_quest_list[area_index]
            self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select'] = combobox_list[0]


        self.jiyeok_quest_select_combobox = ttk.Combobox(
            master              = frame,
            values              = combobox_list, 
            textvariable        = self.option_dic[lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select'], 
            state               = "readonly",
            height              = 10,
            width               = 15,
            font                = lybconstant.LYB_FONT 
            )
        self.jiyeok_quest_select_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select'])
        self.jiyeok_quest_select_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
        frame.pack(anchor=tkinter.W)
        frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)   

        frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

        # 알림 탭 좌
        frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
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

    def auto_duration(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_sell_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())        

    def auto_bunhe_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_ilil_quest_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())   

    def auto_dogam_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())  

    def auto_jongjok_quest_count(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())       

    def auto_move_check_period(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_area(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.sub_area_dic[self.option_dic[option_name].get()]

        self.auto_sub_area_combobox['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_sub_area') in new_list:
                self.auto_sub_area_combobox.set(new_list[0])
        except KeyError:
            pass

    def auto_sub_area(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.sub_area_monster_dic[self.option_dic[option_name].get()]
        self.auto_monster_combobox['values'] = new_list
        # self.logger.warn("DEBUG1: " + self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'elite_quest_go'))
        if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_monster') in new_list:
            self.auto_monster_combobox.set(new_list[0])

        new_list = LYBDarkEden.sub_area_npc_dic[self.option_dic[option_name].get()]
        self.auto_npc_combobox['values'] = new_list
        # self.logger.warn("DEBUG1: " + self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'elite_quest_go'))
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'auto_npc') in new_list:
                self.auto_npc_combobox.set(new_list[0])
        except KeyError:
            pass
        # if not self.elite_quest_go_combobox.get() in new_list:
        #   self.elite_quest_go_combobox.set(new_list[0])

        # for i in range(5):
        #     # self.logger.warn("DEBUG2: " + self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'elite_quest_accept' + str(i)))
        #     self.elite_quest_accept_combobox[i]['values'] = new_list
        #     if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'elite_quest_accept' + str(i)) in new_list:
        #         self.elite_quest_accept_combobox[i].set(new_list[0])
        #     # if not self.elite_quest_accept_combobox[i].get() in new_list:
        #     #   self.elite_quest_accept_combobox[i].set( new_list[0])

    def dungeon_floor_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        new_list = LYBDarkEden.dungeon_floor_monster_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_monster_combobox[0]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(0)) in new_list:
                self.dungeon_floor_monster_combobox[0].set(new_list[0])
        except KeyError:
            pass

        new_list = LYBDarkEden.dungeon_floor_npc_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_npc_combobox[0]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(0)) in new_list:
                self.dungeon_floor_npc_combobox[0].set(new_list[0])
        except KeyError:
            pass

    def dungeon_floor_monster_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_npc_combobox[0].set(self.dungeon_floor_npc_combobox[0]['values'][0])
        except KeyError:
            pass


    def dungeon_floor_npc_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_monster_combobox[0].set(self.dungeon_floor_monster_combobox[0]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_order_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def dungeon_floor_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.dungeon_floor_monster_dic[self.option_dic[option_name].get()]

        self.dungeon_floor_monster_combobox[1]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(1)) in new_list:
                self.dungeon_floor_monster_combobox[1].set(new_list[0])
        except KeyError:
            pass

        new_list = LYBDarkEden.dungeon_floor_npc_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_npc_combobox[1]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(1)) in new_list:
                self.dungeon_floor_npc_combobox[1].set(new_list[0])
        except KeyError:
            pass

    def dungeon_floor_monster_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_npc_combobox[1].set(self.dungeon_floor_npc_combobox[1]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_npc_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_monster_combobox[1].set(self.dungeon_floor_monster_combobox[1]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_order_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def dungeon_floor_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.dungeon_floor_monster_dic[self.option_dic[option_name].get()]

        self.dungeon_floor_monster_combobox[2]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(2)) in new_list:
                self.dungeon_floor_monster_combobox[2].set(new_list[0])
        except KeyError:
            pass

        new_list = LYBDarkEden.dungeon_floor_npc_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_npc_combobox[2]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(2)) in new_list:
                self.dungeon_floor_npc_combobox[2].set(new_list[0])
        except KeyError:
            pass

    def dungeon_floor_monster_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_npc_combobox[2].set(self.dungeon_floor_npc_combobox[2]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_npc_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_monster_combobox[2].set(self.dungeon_floor_monster_combobox[2]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_order_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def dungeon_floor_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.dungeon_floor_monster_dic[self.option_dic[option_name].get()]

        self.dungeon_floor_monster_combobox[3]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(3)) in new_list:
                self.dungeon_floor_monster_combobox[3].set(new_list[0])
        except KeyError:
            pass

        new_list = LYBDarkEden.dungeon_floor_npc_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_npc_combobox[3]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(3)) in new_list:
                self.dungeon_floor_npc_combobox[3].set(new_list[0])
        except KeyError:
            pass

    def dungeon_floor_monster_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_npc_combobox[3].set(self.dungeon_floor_npc_combobox[3]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_npc_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_monster_combobox[3].set(self.dungeon_floor_monster_combobox[3]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_order_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def dungeon_floor_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.dungeon_floor_monster_dic[self.option_dic[option_name].get()]

        self.dungeon_floor_monster_combobox[4]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(4)) in new_list:
                self.dungeon_floor_monster_combobox[4].set(new_list[0])
        except KeyError:
            pass

        new_list = LYBDarkEden.dungeon_floor_npc_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_npc_combobox[4]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(4)) in new_list:
                self.dungeon_floor_npc_combobox[4].set(new_list[0])
        except KeyError:
            pass

    def dungeon_floor_monster_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_npc_combobox[4].set(self.dungeon_floor_npc_combobox[4]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_npc_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_monster_combobox[4].set(self.dungeon_floor_monster_combobox[4]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_order_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())


    def dungeon_floor_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.dungeon_floor_monster_dic[self.option_dic[option_name].get()]

        self.dungeon_floor_monster_combobox[5]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_monster' + str(5)) in new_list:
                self.dungeon_floor_monster_combobox[5].set(new_list[0])
        except KeyError:
            pass

        new_list = LYBDarkEden.dungeon_floor_npc_dic[self.option_dic[option_name].get()]
        self.dungeon_floor_npc_combobox[5]['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_ETC + 'dungeon_floor_npc' + str(5)) in new_list:
                self.dungeon_floor_npc_combobox[5].set(new_list[0])
        except KeyError:
            pass

    def dungeon_floor_monster_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_npc_combobox[5].set(self.dungeon_floor_npc_combobox[5]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_npc_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

        try:
            if self.option_dic[option_name].get() != '선택안함':
                self.dungeon_floor_monster_combobox[5].set(self.dungeon_floor_monster_combobox[5]['values'][0])
        except KeyError:
            pass

    def dungeon_floor_order_5(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def quick_move_gold(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def main_quest_duration(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_limit_count(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_monster(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_npc(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def special_dungeon(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def special_dungeon_difficulty(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_party(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_jiyeok(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_jongjok(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def auto_order(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_quality_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_quality_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_quality_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_quality_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def sell_item_quality_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_option_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_option_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_item_quality_0(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_item_quality_1(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_item_quality_2(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_item_quality_3(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def bunhe_item_quality_4(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())

    def guild_immu(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())


    def jiyeok_quest_area(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
        new_list = LYBDarkEden.quest_scene_jiyeok_quest_dic[self.option_dic[option_name].get()]

        self.jiyeok_quest_select_combobox['values'] = new_list
        try:
            if not self.get_game_config(lybconstant.LYB_DO_STRING_DARKEDEN_WORK + 'jiyeok_quest_select') in new_list:
                self.jiyeok_quest_select_combobox.set(new_list[0])
        except KeyError:
            pass

    def jiyeok_quest_select(self, args, option_name):
        self.set_game_config(option_name, self.option_dic[option_name].get())
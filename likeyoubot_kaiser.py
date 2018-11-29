import likeyoubot_game as lybgame
import likeyoubot_kaiser_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBKaiser(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'자동 사냥',
		'메인 퀘스트',
		'지역 퀘스트',
		'퀵슬롯 등록',
		'퀘스트',
		'우편',
		'일괄 분해',
		
		'알림',
		'[반복 시작]',
		'[반복 종료]',
		'[작업 대기]',
		'[작업 예약]',
		'' ]

	nox_kaiser_icon_list = [
		'nox_kaiser_icon'
		]


	momo_kaiser_icon_list = [
		'momo_kaiser_icon'
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

	slot_item_list = [
		'없음',
		'소형 체력 물약',
		'중형 체력 물약',
		'속도의 물약',
		'전투의 물약',
		'증폭 마법석',
		'펫 소환 주문서',
	]
	
	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_KAISER, lybconstant.LYB_GAME_DATA_KAISER, window)

	def process(self, window_image):

		rc = super(LYBKaiser, self).process(window_image)
		if rc < 0:
			return rc

		return rc

	def custom_check(self, window_image, window_pixel):

		pb_name = 'skip'
		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
							self.window_image,
							self.resource_manager.pixel_box_dic[pb_name],
							custom_below_level=(130, 130, 130),
							custom_top_level=(255, 255, 255),
							custom_threshold=0.9,
							custom_flag=1,
							custom_rect=(560, 240, 600, 280)
							)
		if loc_x != -1:
			self.logger.warn('건너뛰기: ' + str(match_rate))
			self.mouse_click(pb_name)

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

		scene_name = self.popup_scene(window_image)
		if len(scene_name) > 0:
			return scene_name

		# scene_name = self.jeontoo_scene(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		# scene_name = self.scene_google_play_account_select(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		return ''

	def popup_scene(self, window_image):
		loc_name = 'popup_scene_loc'
		match_rate = self.rateMatchedResource(self.window_pixels, loc_name, custom_below_level=100,	custom_top_level=255)
		self.logger.debug(loc_name + ' ' + str(match_rate))
		if match_rate > 0.7:
			return 'popup_scene'

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
			for each_icon in LYBKaiser.nox_kaiser_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				# print('[DEBUG] nox yh icon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					break
		elif self.player_type == 'momo':
			for each_icon in LYBKaiser.momo_kaiser_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
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
			if (	'google_play_account_select_scene' in scene_name or
					'logo_screen_scene' in scene_name or
					'connect_account_scene' in scene_name
					):
				self.scene_dic[scene_name] = last_scene[scene_name]

	def add_scene(self, scene_name):
		self.scene_dic[scene_name] = lybscene.LYBKaiserScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBKaiserTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_KAISER):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBKaiser.work_list:
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

	def set_option(self):

		###############################################
		#                메인 퀘스트 진행             #
		###############################################

		# frame = ttk.Frame(self.inner_frame_dic['frame_top'], relief=self.frame_relief)
		# label = tkinter.Label(
		# 	master 				= frame, 
		# 	text 				= "메인 퀘스트를 ",
		# 	anchor 				= tkinter.W,
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	# fg='White' if brightness < 120 else 'Black', 
		# 	# bg=bg_colour
		# 	)

		
		# # countif.place(
		# # 	x=lybconstant.LYB_PADDING,
		# # 	y=lybconstant.LYB_PADDING,
		# # 	width=lybconstant.LYB_LABEL_WIDTH, height=lybconstant.LYB_LABEL_HEIGHT
		# # 	)
		# label.pack(side=tkinter.LEFT)
		# option_name_mq = lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST
		# self.option_dic[option_name_mq] = tkinter.StringVar(frame)
		# self.option_dic[option_name_mq].trace('w', lambda *args: self.callback_main_quest_stringvar(args, option_name=option_name_mq))

		# if not option_name_mq in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][option_name_mq] = 20
		
		# entry = tkinter.Entry(
		# 	master 				= frame, 
		# 	relief 				= 'sunken', 
		# 	textvariable 		= self.option_dic[option_name_mq],
		# 	justify 			= tkinter.RIGHT, 
		# 	width 				= 5,
		# 	font 				= lybconstant.LYB_FONT
		# 	)

		# entry.pack(side=tkinter.LEFT)		
		# label = tkinter.Label(
		# 	master 				= frame, 
		# 	text 				= "분 동안 진행합니다.",
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	# fg='White' if brightness < 120 else 'Black', 
		# 	# bg=bg_colour
		# 	)
		# label.pack(side=tkinter.LEFT)
		# frame.pack(anchor=tkinter.W)

		
		# PADDING
		frame = ttk.Frame(
			master 				= self.master,
			relief 				= self.frame_relief
			)
		frame.pack(pady=5)


		self.inner_frame_dic['options'] = ttk.Frame(
			master 				= self.master, 
			relief 				= self.frame_relief
			)

		self.option_dic['option_note'] = ttk.Notebook(
			master 				= self.inner_frame_dic['options']
			)


		self.inner_frame_dic['common_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['common_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['common_tab_frame'], text='일반')

		self.inner_frame_dic['work_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)
		self.inner_frame_dic['work_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['work_tab_frame'], text='작업')

		self.inner_frame_dic['notify_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)
		self.inner_frame_dic['notify_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['notify_tab_frame'], text='알림')


		# ------

		# 일반 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_label = ttk.LabelFrame(frame_l, text='설정')

		frame_label_inner = ttk.LabelFrame(frame_label, text='소형 체력 물약')
		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set'].trace(
			'w', lambda *args: self.callback_auto_potion_set(args, lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set')
			)
		if not lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '물약 소진시 현재 작업 종료', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_set'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("물약 슬롯 번호")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number'].trace(
			'w', lambda *args: self.callback_auto_potion_number(args, lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number')
			)
		combobox_list = []
		for i in range(1, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number'] = 1

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'auto_potion_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)
		frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label_inner = ttk.LabelFrame(frame_label, text='수동 체력 물약')

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set'].trace(
			'w', lambda *args: self.callback_potion_set(args, lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set')
			)
		if not lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '물약 소진시 현재 작업 종료', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_set'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("수동 회복 물약 사용(HP %)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp'].trace(
			'w', lambda *args: self.callback_potion_hp(args, lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp')
			)
		combobox_list = []
		for i in range(50, 91):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp'] = 70

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_hp'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("수동 회복 물약 슬롯 번호")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number'].trace(
			'w', lambda *args: self.callback_potion_number(args, lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number')
			)
		combobox_list = []
		for i in range(1, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number'] = 2

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_CONFIG + 'potion_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)
		frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
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
		frame_label = ttk.LabelFrame(frame_l, text='자동 사냥')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("진행 시간(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration'].trace(
			'w', lambda *args: self.callback_auto_play_duration(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration')
			)
		combobox_list = []
		for i in range(0, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration'] = 1800

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_play_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("자동 전환 감지 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count'].trace(
			'w', lambda *args: self.callback_auto_limit_count(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count')
			)
		combobox_list = []
		for i in range(2, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'auto_limit_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_label = ttk.LabelFrame(frame_l, text='메인 퀘스트')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("진행 시간(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration'].trace(
			'w', lambda *args: self.callback_main_quest_duration(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration')
			)
		combobox_list = []
		for i in range(0, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration'] = 1800

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 지역 이탈 판정 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance'].trace(
			'w', lambda *args: self.callback_main_quest_distance(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance')
			)
		combobox_list = []
		for i in range(1, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance'] = 3

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_distance'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("자동 전환 감지 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto'].trace(
			'w', lambda *args: self.callback_main_quest_auto(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto')
			)
		combobox_list = []
		for i in range(2, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'main_quest_auto'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)


		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_l, text='지역 퀘스트')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("진행 시간(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration'].trace(
			'w', lambda *args: self.callback_local_quest_duration(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration')
			)
		combobox_list = []
		for i in range(0, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration'] = 1800

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 지역 이탈 판정 거리(m)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit'].trace(
			'w', lambda *args: self.callback_local_quest_distance_limit(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit')
			)
		combobox_list = []
		for i in range(1, 11):
			combobox_list.append(str(i * 10))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit'] = 40

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 지역 이탈 판정 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance'].trace(
			'w', lambda *args: self.callback_local_quest_distance(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance')
			)
		combobox_list = []
		for i in range(1, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance'] = 60

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_distance'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("자동 전환 감지 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto'].trace(
			'w', lambda *args: self.callback_local_quest_auto(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto')
			)
		combobox_list = []
		for i in range(2, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_auto'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("현상 수배 퀘스트 수락 번호")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number'].trace(
			'w', lambda *args: self.callback_local_quest_wanted_number(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number')
			)
		combobox_list = []
		for i in range(0, 4):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number'] = 1

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'local_quest_wanted_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_label = ttk.LabelFrame(frame_m, text='퀵슬롯 등록')
		frame_label_inner = ttk.LabelFrame(frame_label, text='퀵슬롯 번호')
		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= "⑨ ⑩ ⑪ ⑫"
			)
		label.pack()
		frame.pack()
		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= "⑤ ⑥ ⑦ ⑧"
			)
		label.pack()
		frame.pack()
		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= "① ② ③ ④"
			)
		label.pack()
		frame.pack()

		frame_label_inner.pack(padx=5, pady=5)

		for i in range(12):
			frame = ttk.Frame(frame_label)
			label = ttk.Label(
				master 				= frame, 
				text 				= self.get_option_text(str(i + 1)+'.', width=3)
				)
			label.pack(side=tkinter.LEFT)

			self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(i)] = tkinter.StringVar(frame)

			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '0'].trace(
					'w', lambda *args: self.callback_work_slot_item_0(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '0'))
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '1'].trace(
					'w', lambda *args: self.callback_work_slot_item_1(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '1'))
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '2'].trace(
					'w', lambda *args: self.callback_work_slot_item_2(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '2'))
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '3'].trace(
					'w', lambda *args: self.callback_work_slot_item_3(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '3'))
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '4'].trace(
					'w', lambda *args: self.callback_work_slot_item_4(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '4'))
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '5'].trace(
					'w', lambda *args: self.callback_work_slot_item_5(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '5'))
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '6'].trace(
					'w', lambda *args: self.callback_work_slot_item_6(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '6'))
			elif i == 7:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '7'].trace(
					'w', lambda *args: self.callback_work_slot_item_7(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '7'))
			elif i == 8:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '8'].trace(
					'w', lambda *args: self.callback_work_slot_item_8(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '8'))
			elif i == 9:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '9'].trace(
					'w', lambda *args: self.callback_work_slot_item_9(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '9'))
			elif i == 10:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '10'].trace(
					'w', lambda *args: self.callback_work_slot_item_10(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '10'))
			elif i == 11:
				self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '11'].trace(
					'w', lambda *args: self.callback_work_slot_item_11(args, lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + '11'))

			combobox_list = LYBKaiser.slot_item_list

			if not lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(i)] = combobox_list[0]

			combobox = ttk.Combobox(
				master 				= frame,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(i)], 
				state 				= "readonly",
				height				= 10,
				width 				= 28,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_WORK + 'slot_item_' + str(i)])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

			frame.pack(anchor=tkinter.NW)


		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)




		# 알림 탭 좌
		frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
		frame_label = ttk.Frame(frame_l)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty'].trace(
			'w', lambda *args: self.callback_notify_quickslot_item_empty(args, lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty')
			)
		if not lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('퀵슬롯 등록 아이템 부족'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quickslot_item_empty'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death'].trace(
			'w', lambda *args: self.callback_notify_character_death(args, lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death')
			)
		if not lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('캐릭터 사망'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'character_death'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop'].trace(
			'w', lambda *args: self.callback_notify_local_quest_stop(args, lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop')
			)
		if not lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('지역 퀘스트 탐색 실패'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'local_quest_stop'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete'].trace(
			'w', lambda *args: self.callback_notify_quest_complete(args, lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete')
			)
		if not lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('퀘스트 완료'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_KAISER_NOTIFY + 'quest_complete'],
			onvalue 			= True, 
			offvalue 			= False
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






		# # 알림 탭 좌
		# frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
		# frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)
		# # 알림 탭 중
		# frame_m = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
		# frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)
		# # 알림 탭 우
		# frame_r = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
		# frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)
	

		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()


	def callback_notify_quest_complete(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_notify_local_quest_stop(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_notify_character_death(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_notify_quickslot_item_empty(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_slot_item_11(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_10(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_9(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_8(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_7(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_6(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_slot_item_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_set(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_potion_set(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_potion_number(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_hp(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_number(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_local_quest_wanted_number(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_main_quest_auto(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_local_quest_auto(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_local_quest_distance_limit(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_local_quest_distance(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_distance(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_local_quest_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_limit_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_play_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



import likeyoubot_game as lybgame
import likeyoubot_l2r_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBL2r(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'메인 퀘스트',
		
		'알림',
		'[반복 시작]',
		'[반복 종료]',
		'[작업 대기]',
		'[작업 예약]',
		'' ]

	l2r_icon_list = [
		'l2r_icon'
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

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_L2R, lybconstant.LYB_GAME_DATA_L2R, window)

	def process(self, window_image):
		rc = super(LYBL2r, self).process(window_image)
		if rc < 0:
			return rc

		return rc

	def custom_check(self, window_image, window_pixel):

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

		pb_name = 'use_item'
		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
					self.window_image,
					self.resource_manager.pixel_box_dic[pb_name],
					custom_threshold=0.8,
					custom_flag=1,
					custom_rect=(300, 290, 390, 330)
					)
		if loc_x != -1:
			# self.mouse_click('use_item')
			self.window.mouse_click(self.hwnd, loc_x, loc_y)
			return pb_name

		pb_name = 'popup_close_icon'
		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
					self.window_image,
					self.resource_manager.pixel_box_dic[pb_name],
					custom_threshold=0.8,
					custom_flag=1,
					custom_top_level=(190, 190, 190),
					custom_below_level=(150, 150, 150),
					custom_rect=(520, 50, 630, 160)
					)
		if loc_x != -1:
			# self.mouse_click('use_item')
			self.window.mouse_click(self.hwnd, loc_x, loc_y)
			return pb_name

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
			for each_icon in LYBL2r.l2r_icon_list:
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
			for each_icon in LYBL2r.l2r_icon_list:
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
		self.scene_dic[scene_name] = lybscene.LYBL2rScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBL2rTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_L2R):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBL2r.work_list:
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

	def set_option(self):

		###############################################
		#                메인 퀘스트 진행             #
		###############################################
		
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


		# ------

		# 일반 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_label = ttk.LabelFrame(frame_l, text='공통')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("자동 체크 횟수(회)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'].trace(
			'w', lambda *args: self.callback_etc_auto_limit(args, lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit')
			)
		combobox_list = []
		for i in range(1, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'] = 2

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_ETC + 'auto_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("랙 체크 주기(초)(0:안함)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period'].trace(
			'w', lambda *args: self.callback_etc_lag_check_period(args, lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period')
			)
		combobox_list = []
		for i in range(0, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period'] = 300

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_ETC + 'lag_check_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)
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
		frame_label = ttk.LabelFrame(frame_l, text='메인 퀘스트')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("진행 시간(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration'].trace(
			'w', lambda *args: self.callback_main_quest_duration(args, lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration')
			)
		combobox_list = []
		for i in range(0, 86401):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration'] = 1800

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub'].trace(
			'w', lambda *args: self.callback_main_quest_sub(args, lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub')
			)

		if not lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub'] = True

		check_box = ttk.Checkbutton(
			master 				= frame,
			text 				= self.get_option_text('서브 퀘스트 우선 수행'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_L2R_WORK + 'main_quest_sub'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)
		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()

	def callback_etc_auto_limit(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_lag_check_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_sub(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



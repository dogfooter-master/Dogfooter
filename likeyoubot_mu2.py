import likeyoubot_game as lybgame
import likeyoubot_mu2_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBMu2(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'메인 퀘스트',
		'일일 퀘스트',
		'길드 퀘스트',
		'우편',
		'아티팩트 - 분해',
		'무료 교환',
		
		'알림',
		'[반복 시작]',
		'[반복 종료]',
		'[작업 대기]',
		'[작업 예약]',
		'' ]

	nox_mu2_icon_list = [
		'nox_mu2_icon'
		]


	momo_mu2_icon_list = [
		'momo_mu2_icon',
		'momo_mu2_icon2'
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

	item_rank_list = [
		'매직',
		'레어',
		'유니크',
		'에픽',
		'레전드'
	]

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_MU2, lybconstant.LYB_GAME_DATA_MU2, window)

	def process(self, window_image):
		rc = super(LYBMu2, self).process(window_image)
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

		return ''

	def custom_event(self, event_name):
		if (	event_name == 'tutorial_19_event' or
				event_name == 'tutorial_20_event'):
			self.get_scene('main_scene').lyb_mouse_drag('skill_4', 'skill_1')
			return True

		return False

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
			for each_icon in LYBMu2.nox_mu2_icon_list:
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
			for each_icon in LYBMu2.momo_mu2_icon_list:
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
		self.scene_dic[scene_name] = lybscene.LYBMu2Scene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBMu2Tab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_MU2):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		print('DEBUG 1--')
		for each_work in LYBMu2.work_list:
			print(each_work)
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

		# ------
		# 일반 탭 설정
		# 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 중간
		frame_m = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 우측
		frame_r = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)
	
		# 작업 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_label = ttk.LabelFrame(frame_l, text='메인 퀘스트')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("작업 수행 시간(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration'].trace(
			'w', lambda *args: self.callback_quest_duration_stringvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration')
			)
		combobox_list = []
		for i in range(60, 3601, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration'] = 600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("클릭 퀘스트 번호")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number'].trace(
			'w', lambda *args: self.callback_quest_number_stringvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number')
			)
		combobox_list = []
		for i in range(1, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number'] = 1

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 클릭 주기(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period'].trace(
			'w', lambda *args: self.callback_quest_click_period_stringvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period')
			)
		combobox_list = []
		for i in range(30, 301, 10):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period'] = 30

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_click_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("랙방지 캐릭터 움직임 주기(초)")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period'].trace(
			'w', lambda *args: self.callback_quest_move_period(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period')
			)
		combobox_list = []
		for i in range(0, 301, 10):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period'] = 30

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'quest_move_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_l, text='아티팩트 - 분해')
		frame = ttk.Frame(frame_label)

		i = 0
		for item_rank in LYBMu2.item_rank_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '0'].trace(
					'w', lambda *args: self.callback_artifact_item_rank_0_booleanvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '1'].trace(
					'w', lambda *args: self.callback_artifact_item_rank_1_booleanvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '2'].trace(
					'w', lambda *args: self.callback_artifact_item_rank_2_booleanvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '2')
					)
			elif i == 3:
				frame.pack(anchor=tkinter.NW)
				frame = ttk.Frame(frame_label)
				self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '3'].trace(
					'w', lambda *args: self.callback_artifact_item_rank_3_booleanvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '4'].trace(
					'w', lambda *args: self.callback_artifact_item_rank_4_booleanvar(args, lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + '4')
					)

			if i < 4:
				if not lybconstant.LYB_DO_STRING_MU2_WORK +  'artifact_item_rank' + str(i) in self.configure.common_config[self.game_name]:
					self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + str(i)] = True
			else:
				if not lybconstant.LYB_DO_STRING_MU2_WORK +  'artifact_item_rank' + str(i) in self.configure.common_config[self.game_name]:
					self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= item_rank, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MU2_WORK + 'artifact_item_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)



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


	def callback_artifact_item_rank_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_artifact_item_rank_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_artifact_item_rank_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_artifact_item_rank_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_artifact_item_rank_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_quest_move_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_quest_click_period_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_quest_duration_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_quest_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



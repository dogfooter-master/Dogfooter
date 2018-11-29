import likeyoubot_game as lybgame
import likeyoubot_miracle_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBMiracle(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'임무',
		'친구',
		'반복 모험',
		'요일 던전',
		'무한의 탑',
		'제련의 전당',
		'황금의 방',
		'펫의 방',
		'결투장',
		'우편함',
		'무료 소환',
		'분해',
		'알림',
		'[반복 시작]',
		'[반복 종료]',
		'[작업 대기]',
		'[작업 예약]',
		'',
		'' ]

	nox_miracle_icon_list = [
		'nox_miracle_icon'
		]


	momo_miracle_icon_list = [
		'momo_miracle_icon'
		]

	item_list = [
		'무기',
		'갑옷',
		'투구',
		'문장',
		'반지',
		'목걸이'
	]

	item_group_list = [
		'장비',
		'소모품'
	]

	rank_list = [
		'일반',
		'고급',
		'희귀',
		'영웅',
		'전설',
		'불멸'
	]

	etc_list = [
		'1레벨만',
		'강화없음'
	]

	moheom_level_list = [
		'쉬움',
		'보통',
		'어려움',
		'지옥'
	]

	moheom_area_list = [
		'쿠맷족의 숲',
		'폐쇄된 광산',
		'오염된 늪지대',
		'킬라우 분화구'
	]

	yoil_dungeon_list = [
		'월요일',
		'화요일',
		'수요일',
		'목요일',
		'금요일',
		'토요일'
		]



	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_MIRACLE, lybconstant.LYB_GAME_DATA_MIRACLE, window)

	def process(self, window_image):
		rc = super(LYBMiracle, self).process(window_image)
		if rc < 0:
			return rc

		return rc

	def custom_check(self, window_image, window_pixel):

		# 패배!
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'defeat_press_key_loc',
							custom_below_level=(250, 250, 250),
							custom_top_level=(255, 255, 255),
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(280, 190, 360, 230)
							)
		if loc_x != -1:
			self.logger.warn('전투 패배: ' + str(match_rate))
			self.mouse_click('defeat_press_key_0')

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
			for each_icon in LYBMiracle.nox_miracle_icon_list:
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
			for each_icon in LYBMiracle.momo_miracle_icon_list:
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
		self.scene_dic[scene_name] = lybscene.LYBMiracleScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBMiracleTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_MIRACLE):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBMiracle.work_list:
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

		self.inner_frame_dic['work2_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)
		self.inner_frame_dic['work2_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['work2_tab_frame'], text='작업2')

		# ------

		# 일반 탭 설정
		# 좌측

		frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_label = ttk.LabelFrame(frame_l, text='설정')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_CONFIG + 'auto'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_CONFIG + 'auto'].trace(
			'w', lambda *args: self.callback_auto_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_CONFIG + 'auto')
			)
		if not lybconstant.LYB_DO_STRING_MIRACLE_CONFIG +  'auto' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_CONFIG + 'auto'] = False
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '전투 중 자동/고속 자동 변환', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_CONFIG + 'auto'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 중간
		frame_m = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 우측
		frame_r = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)



		# 작업 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['work_tab_frame'])

		frame_label = ttk.LabelFrame(frame_l, text='반복 모험')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("모험 난이도", width=28)
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level'].trace(
			'w', lambda *args: self.callback_moheom_level_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level')
			)
		combobox_list = LYBMiracle.moheom_level_list

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level'] = combobox_list[2]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_level'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("모험 지역", width=20)
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area'].trace(
			'w', lambda *args: self.callback_moheom_area_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area')
			)
		combobox_list = LYBMiracle.moheom_area_list

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area'] = combobox_list[-1]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area'], 
			state 				= "readonly",
			height				= 10,
			width 				= 15,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("지역 세부 번호")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number'].trace(
			'w', lambda *args: self.callback_moheom_area_number_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number')
			)
		combobox_list = []
		for i in range(1, 11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number'] = combobox_list[-1]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'moheom_area_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_label = ttk.LabelFrame(frame_l, text='분해')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("분해 또는 판매 선택")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count'].trace(
			'w', lambda *args: self.callback_bunhe_count(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count')
			)
		combobox_list = [ '분해', '판매' ]

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label2 = ttk.LabelFrame(frame_label, text='종류별')
		frame = ttk.Frame(frame_label2)

		i = 0
		for item in LYBMiracle.item_group_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + '0'].trace(
					'w', lambda *args: self.callback_bunhe_item_0_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + '1'].trace(
					'w', lambda *args: self.callback_bunhe_item_1_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + '1')
					)

			if not lybconstant.LYB_DO_STRING_MIRACLE_WORK +  'bunhe_item' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + str(i)] = False
			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= item, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_item' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)
		frame_label2.pack(anchor=tkinter.NW)

		frame_label2 = ttk.LabelFrame(frame_label, text='등급순')
		frame = ttk.Frame(frame_label2)

		i = 0
		for rank in LYBMiracle.rank_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '0'].trace(
					'w', lambda *args: self.callback_bunhe_rank_0_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '1'].trace(
					'w', lambda *args: self.callback_bunhe_rank_1_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '2'].trace(
					'w', lambda *args: self.callback_bunhe_rank_2_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '2')
					)
			elif i == 3:
				frame.pack(anchor=tkinter.NW)
				frame = ttk.Frame(frame_label2)
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '3'].trace(
					'w', lambda *args: self.callback_bunhe_rank_3_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '4'].trace(
					'w', lambda *args: self.callback_bunhe_rank_4_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '4')
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '5'].trace(
					'w', lambda *args: self.callback_bunhe_rank_5_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + '5')
					)

			if not lybconstant.LYB_DO_STRING_MIRACLE_WORK +  'bunhe_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + str(i)] = False
			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= rank, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)
		frame_label2.pack(anchor=tkinter.NW)

		frame_label2 = ttk.LabelFrame(frame_label, text='기타')
		frame = ttk.Frame(frame_label2)

		i = 0
		for etc in LYBMiracle.etc_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + '0'].trace(
					'w', lambda *args: self.callback_bunhe_etc_0_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + '1'].trace(
					'w', lambda *args: self.callback_bunhe_etc_1_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + '1')
					)

			if not lybconstant.LYB_DO_STRING_MIRACLE_WORK +  'bunhe_etc' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + str(i)] = False

			check_box = ttk.Checkbutton(
				master 				= frame,
				text 				= etc, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'bunhe_etc' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)
		frame_label2.pack(anchor=tkinter.NW)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_label = ttk.LabelFrame(frame_m, text='요일 던전')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("입장 단계")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level'].trace(
			'w', lambda *args: self.callback_yoil_level_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level')
			)
		combobox_list = []
		for i in range(1, 6):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_level'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("일요일 던전 선택", width=28)
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday'].trace(
			'w', lambda *args: self.callback_yoil_sunday_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday')
			)
		combobox_list = LYBMiracle.yoil_dungeon_list

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'yoil_sunday'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_m, text='황금의 방')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("입장 단계")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level'].trace(
			'w', lambda *args: self.callback_goldroom_level_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level')
			)
		combobox_list = []
		for i in range(1, 6):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level'] = 3

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'goldroom_level'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_m, text='펫의 방')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("입장 단계")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level'].trace(
			'w', lambda *args: self.callback_petroom_level_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level')
			)
		combobox_list = []
		for i in range(1, 6):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level'] = 3

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'petroom_level'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_label = ttk.LabelFrame(frame_r, text='제련의 전당')

		frame = ttk.Frame(frame_label)		
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem'].trace(
			'w', lambda *args: self.callback_jeryeon_use_gem(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem')
			)

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '추가 진행', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'use_gem'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("입장 단계")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level'].trace(
			'w', lambda *args: self.callback_jeryeon_level_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level')
			)
		combobox_list = []
		for i in range(1, 6):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level'] = 4

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_level'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("제련 아이템 갯수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target'].trace(
			'w', lambda *args: self.callback_jeryeon_target_stringvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target')
			)
		combobox_list = []
		for i in range(1, 6):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_target'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)

		frame_label2 = ttk.LabelFrame(frame_label, text='종류별')
		frame = ttk.Frame(frame_label2)

		i = 0
		for item in LYBMiracle.item_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '0'].trace(
					'w', lambda *args: self.callback_jeryeon_item_0_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '1'].trace(
					'w', lambda *args: self.callback_jeryeon_item_1_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '2'].trace(
					'w', lambda *args: self.callback_jeryeon_item_2_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '2')
					)
			elif i == 3:
				frame.pack(anchor=tkinter.NW)
				frame = ttk.Frame(frame_label2)
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '3'].trace(
					'w', lambda *args: self.callback_jeryeon_item_3_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '4'].trace(
					'w', lambda *args: self.callback_jeryeon_item_4_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '4')
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '5'].trace(
					'w', lambda *args: self.callback_jeryeon_item_5_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + '5')
					)

			if not lybconstant.LYB_DO_STRING_MIRACLE_WORK +  'jeryeon_item' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + str(i)] = True
			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= item, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_item' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)
		frame_label2.pack(anchor=tkinter.NW)


		frame_label2 = ttk.LabelFrame(frame_label, text='등급순')
		frame = ttk.Frame(frame_label2)

		i = 0
		for rank in LYBMiracle.rank_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '0'].trace(
					'w', lambda *args: self.callback_jeryeon_rank_0_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '1'].trace(
					'w', lambda *args: self.callback_jeryeon_rank_1_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '2'].trace(
					'w', lambda *args: self.callback_jeryeon_rank_2_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '2')
					)
			elif i == 3:
				frame.pack(anchor=tkinter.NW)
				frame = ttk.Frame(frame_label2)
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '3'].trace(
					'w', lambda *args: self.callback_jeryeon_rank_3_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '4'].trace(
					'w', lambda *args: self.callback_jeryeon_rank_4_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '4')
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '5'].trace(
					'w', lambda *args: self.callback_jeryeon_rank_5_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + '5')
					)

			if not lybconstant.LYB_DO_STRING_MIRACLE_WORK +  'jeryeon_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + str(i)] = True
				
			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= rank, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)
		frame_label2.pack(anchor=tkinter.NW)

		frame_label2 = ttk.LabelFrame(frame_label, text='기타')
		frame = ttk.Frame(frame_label2)

		i = 0
		for etc in LYBMiracle.etc_list:
			self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + str(i)] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + '0'].trace(
					'w', lambda *args: self.callback_jeryeon_etc_0_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + '1'].trace(
					'w', lambda *args: self.callback_jeryeon_etc_1_booleanvar(args, lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + '1')
					)

			if not lybconstant.LYB_DO_STRING_MIRACLE_WORK +  'jeryeon_etc' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + str(i)] = True
			check_box = ttk.Checkbutton(
				master 				= frame,
				text 				= etc, 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MIRACLE_WORK + 'jeryeon_etc' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.NW)
		frame_label2.pack(anchor=tkinter.NW)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])
		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()


	def callback_bunhe_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_yoil_sunday_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_goldroom_level_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_petroom_level_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_yoil_level_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_moheom_area_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_moheom_area_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_moheom_level_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_auto_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_target_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_etc_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_etc_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_rank_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_item_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_item_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_item_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_item_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_item_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_bunhe_item_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())





	def callback_jeryeon_etc_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_etc_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_rank_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_rank_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_rank_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_rank_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_rank_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_rank_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_item_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_item_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_item_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_item_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_item_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_item_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeryeon_use_gem(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_jeryeon_level_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



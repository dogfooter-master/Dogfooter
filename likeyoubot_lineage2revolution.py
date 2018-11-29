import likeyoubot_game as lybgame
import likeyoubot_lin2rev_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBLineage2Revolution(lybgame.LYBGame):
	
	work_list = [ 
		#'상점',
		'게임 시작',
		'로그인', 
		'우편함',

		'소환 상자',
		'우정포인트 상자',
		'자동 장착',
		#'일괄 판매',
		#'업적 보상', 
		#'아이템 열기',
		#'퀘스트 보상', 
		'혈맹',
		'친구 인사',
		'일괄 판매',
		'일일 퀘스트',
		'주간 퀘스트',
		'메인 퀘스트',
		'' ]

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_LIN2REV, lybconstant.LYB_GAME_DATA_LIN2REV, window)

	def process(self, window_image):
		rc = super(LYBLineage2Revolution, self).process(window_image)
		if rc < 0:
			return rc

		return rc

		# s_time = time.time()
		# rate = self.rateMatchedPixelBox(window_pixels, 'lineage2_revolution_icon')
		# e_time = time.time()
		# print('rateMatchedPixelBox()='+str(rate*100)+' Elapsed Time: %s' % (e_time - s_time))

		# s_time = time.time()
		# rate = self.rateMatchedResource(window_pixels, 'nox_init_screen_scene')
		# e_time = time.time()
		# print('rateMatchedResource()='+str(rate*100)+' Elapsed Time: %s' % (e_time - s_time))
		# (loc_x, loc_y) = self.locationOnWindow(window_image, self.resource_manager.pixel_box_dic['lineage2_revolution_icon'])
		# print(loc_x, loc_y)

	def get_screen_by_location(self, window_image):

		scene_name = self.scene_google_play_account_select(window_image)
		if len(scene_name) > 0:
			return scene_name

		return ''
		
	def scene_google_play_account_select(self, window_image):
		loc_x_list = []
		loc_y_list = []

		(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
			window_image, 
			self.resource_manager.pixel_box_dic['lin2rev_google_play_letter']
			)
		loc_x_list.append(loc_x)
		loc_y_list.append(loc_y)

		for i in range(6):
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				window_image, 
				self.resource_manager.pixel_box_dic['lin2rev_google_play_letter_' + str(i)]
				)

			loc_x_list.append(loc_x)
			loc_y_list.append(loc_y)

		for each_loc in loc_x_list:
			if each_loc == -1:
				return ''
			else:
				continue

		return 'lin2rev_google_play_account_select_scene'

	def clear_scene(self):
		last_scene = self.scene_dic
		self.scene_dic = {}
		for scene_name, scene in last_scene.items():
			if (	'google_play_account_select_scene' in scene_name or
					'lin2rev_logo_screen_scene' in scene_name or
					'lin2rev_connect_account_scene' in scene_name
					):
				self.scene_dic[scene_name] = last_scene[scene_name]

	def add_scene(self, scene_name):
		self.scene_dic[scene_name] = lybscene.LYBLin2RevScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBLineage2RevolutionTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_LIN2REV):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		print('DEBUG 1--')
		for each_work in LYBLineage2Revolution.work_list:
			# print(each_work)
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

	def set_option(self):

		###############################################
		#                메인 퀘스트 진행             #
		###############################################

		frame = ttk.Frame(self.inner_frame_dic['frame_top'], relief=self.frame_relief)
		label = tkinter.Label(
			master 				= frame, 
			text 				= "메인 퀘스트를 ",
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)

		
		# countif.place(
		# 	x=lybconstant.LYB_PADDING,
		# 	y=lybconstant.LYB_PADDING,
		# 	width=lybconstant.LYB_LABEL_WIDTH, height=lybconstant.LYB_LABEL_HEIGHT
		# 	)
		label.pack(side=tkinter.LEFT)
		option_name_mq = lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST
		self.option_dic[option_name_mq] = tkinter.StringVar(frame)
		self.option_dic[option_name_mq].trace('w', lambda *args: self.callback_main_quest_stringvar(args, option_name=option_name_mq))

		if not option_name_mq in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_mq] = 20
		
		entry = tkinter.Entry(
			master 				= frame, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[option_name_mq],
			justify 			= tkinter.RIGHT, 
			width 				= 5,
			font 				= lybconstant.LYB_FONT
			)

		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame, 
			text 				= "분 동안 진행합니다.",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(self.inner_frame_dic['frame_top'], relief=self.frame_relief)
		label = tkinter.Label(
			master 				= frame, 
			text 				= "메인 퀘스트를 ",
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)

		
		# countif.place(
		# 	x=lybconstant.LYB_PADDING,
		# 	y=lybconstant.LYB_PADDING,
		# 	width=lybconstant.LYB_LABEL_WIDTH, height=lybconstant.LYB_LABEL_HEIGHT
		# 	)
		label.pack(side=tkinter.LEFT)
		option_name_mqe = lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST_EACH
		self.option_dic[option_name_mqe] = tkinter.StringVar(frame)
		self.option_dic[option_name_mqe].trace('w', lambda *args: self.callback_main_quest_each_stringvar(args, option_name=option_name_mqe))

		if not option_name_mqe in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_mqe] = 120
		
		entry = tkinter.Entry(
			master 				= frame, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[option_name_mqe],
			justify 			= tkinter.RIGHT, 
			width 				= 5,
			font 				= lybconstant.LYB_FONT
			)

		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame, 
			text 				= "초 마다 주기적으로 클릭합니다.(이미지 인식 실패 대비)",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		# ----
		frame = ttk.Frame(self.inner_frame_dic['frame_top'], relief=self.frame_relief)
		label = tkinter.Label(
			master 				= frame, 
			text 				= "주간 퀘스트를 ",
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			)

		label.pack(side=tkinter.LEFT)
		option_name_wq = lybconstant.LYB_DO_STRING_DURATION_WEEKLY_QUEST
		self.option_dic[option_name_wq] = tkinter.StringVar(frame)
		self.option_dic[option_name_wq].trace('w', lambda *args: self.callback_weekly_quest_stringvar(args, option_name=option_name_wq))

		if not option_name_wq in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_wq] = 20
		
		entry = tkinter.Entry(
			master 				= frame, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[option_name_wq],
			justify 			= tkinter.RIGHT, 
			width 				= 5,
			font 				= lybconstant.LYB_FONT
			)

		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame, 
			text 				= "분 동안 진행합니다.",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		# ----
		frame = ttk.Frame(self.inner_frame_dic['frame_top'], relief=self.frame_relief)
		label = tkinter.Label(
			master 				= frame, 
			text 				= "주간 퀘스트를 ",
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			)

		label.pack(side=tkinter.LEFT)
		option_name_wqe = lybconstant.LYB_DO_STRING_DURATION_WEEKLY_QUEST_EACH
		self.option_dic[option_name_wqe] = tkinter.StringVar(frame)
		self.option_dic[option_name_wqe].trace('w', lambda *args: self.callback_weekly_quest_each_stringvar(args, option_name=option_name_wqe))

		if not option_name_wqe in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_wqe] = 60
		
		entry = tkinter.Entry(
			master 				= frame, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[option_name_wqe],
			justify 			= tkinter.RIGHT, 
			width 				= 5,
			font 				= lybconstant.LYB_FONT
			)

		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame, 
			text 				= "초 마다 주기적으로 확인합니다.",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		###############################################
		#                 포션 구매 여부              #
		###############################################

		frame = ttk.LabelFrame(self.inner_frame_dic['frame_top'], text='상점', relief=self.frame_relief)
		frame_t = ttk.Frame(frame, relief=self.frame_relief)
		option_name_0 = lybconstant.LYB_DO_BOOLEAN_BUY_HP_POTION
		self.option_dic[option_name_0] = tkinter.BooleanVar(frame_t)
		self.option_dic[option_name_0].trace('w', lambda *args: self.callback_hp_potion_buy_booleanvar(args, option_name_0))

		if not option_name_0 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_0] = True

		check_box = tkinter.Checkbutton(

			master 				= frame_t,
			text 				= 'HP포션 소진 시 [HP포션 20개] 를', 
			variable 			= self.option_dic[option_name_0],
			onvalue 			= True, 
			offvalue 			= False,
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		option_name_1 = lybconstant.LYB_DO_STRING_NUMBER_HP_POTION
		self.option_dic[option_name_1] = tkinter.StringVar(frame_t)
		self.option_dic[option_name_1].trace('w', lambda *args: self.callback_hp_potion_number_stringvar(args, option_name_1))

		if not option_name_1 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_1] = 2

		entry = tkinter.Entry(
			master 				= frame_t, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[option_name_1],
			justify 			= tkinter.RIGHT, 
			width 				= 3,
			font 				= lybconstant.LYB_FONT
			)
		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame_t, 
			text 				= "번 구매합니다",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)

		frame_t.pack(anchor=tkinter.W)
		frame_b = ttk.Frame(frame, relief=self.frame_relief)

		option_name_2 = lybconstant.LYB_DO_BOOLEAN_BUY_MP_POTION
		self.option_dic[option_name_2] = tkinter.BooleanVar(frame_b)
		self.option_dic[option_name_2].trace('w', lambda *args: self.callback_mp_potion_buy_booleanvar(args, option_name_2))

		if not option_name_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_2] = True

		check_box = tkinter.Checkbutton(

			master 				= frame_b,
			text 				= 'MP포션 소진 시 [MP포션 20개] 를', 
			variable 			= self.option_dic[option_name_2],
			onvalue 			= True, 
			offvalue 			= False,
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		option_name_3 = lybconstant.LYB_DO_STRING_NUMBER_MP_POTION
		self.option_dic[option_name_3] = tkinter.StringVar(frame_b)
		self.option_dic[option_name_3].trace('w', lambda *args: self.callback_mp_potion_number_stringvar(args, option_name_3))

		if not option_name_3 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_3] = 2

		entry = tkinter.Entry(
			master 				= frame_b, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[option_name_3],
			justify 			= tkinter.RIGHT, 
			width 				= 3,
			font 				= lybconstant.LYB_FONT
			)
		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame_b, 
			text 				= "번 구매합니다",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
	
		frame_b.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)

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
		# 이벤트 탭
		self.inner_frame_dic['clan_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		# -- 아데나
		frame_b = ttk.Frame(self.inner_frame_dic['clan_tab_frame'], relief=self.frame_relief)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA] = tkinter.BooleanVar(frame_b)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA].trace('w', lambda *args: self.callback_clan_donate_adena_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA))

		if not lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA] = True

		check_box = tkinter.Checkbutton(

			master 				= frame_b,
			text 				= '혈맹 [기부하기]에서 [아데나] 기부를 ', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_ADENA],
			onvalue 			= True, 
			offvalue 			= False,
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA] = tkinter.StringVar(frame_b)
		self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA].trace('w', lambda *args: self.callback_clan_donate_adena_stringvar(args, lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA))

		if not lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA] = 30

		entry = tkinter.Entry(
			master 				= frame_b, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_ADENA],
			justify 			= tkinter.RIGHT, 
			width 				= 3,
			font 				= lybconstant.LYB_FONT
			)
		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame_b, 
			text 				= "회 실시 합니다",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame_b.pack(anchor=tkinter.W)
	
		# -- 피의 증거
		frame_b = ttk.Frame(self.inner_frame_dic['clan_tab_frame'], relief=self.frame_relief)
		
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD] = tkinter.BooleanVar(frame_b)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD].trace('w', lambda *args: self.callback_clan_donate_blood_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD))

		if not lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD] = False

		check_box = tkinter.Checkbutton(

			master 				= frame_b,
			text 				= '혈맹 [기부하기]에서 [피의증거] 기부를 ', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_BLOOD],
			onvalue 			= True, 
			offvalue 			= False,
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD] = tkinter.StringVar(frame_b)
		self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD].trace('w', lambda *args: self.callback_clan_donate_blood_stringvar(args, lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD))

		if not lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD] = 2

		entry = tkinter.Entry(
			master 				= frame_b, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_BLOOD],
			justify 			= tkinter.RIGHT, 
			width 				= 3,
			font 				= lybconstant.LYB_FONT
			)
		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame_b, 
			text 				= "회 실시 합니다",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame_b.pack(anchor=tkinter.W)

		# -- 붉은 스타 스톤
		frame_b = ttk.Frame(self.inner_frame_dic['clan_tab_frame'], relief=self.frame_relief)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED] = tkinter.BooleanVar(frame_b)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED].trace('w', lambda *args: self.callback_clan_donate_red_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED))

		if not lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED] = False

		check_box = tkinter.Checkbutton(

			master 				= frame_b,
			text 				= '혈맹 [기부하기]에서 [붉은스타스톤] 기부를 ', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_CLAN_DONATE_RED],
			onvalue 			= True, 
			offvalue 			= False,
			anchor 				= tkinter.W,
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_RED] = tkinter.StringVar(frame_b)
		self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_RED].trace('w', lambda *args: self.callback_clan_donate_red_stringvar(args, lybconstant.LYB_DO_STRING_CLAN_DONATE_RED))

		if not lybconstant.LYB_DO_STRING_CLAN_DONATE_RED in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_CLAN_DONATE_RED] = 1

		entry = tkinter.Entry(
			master 				= frame_b, 
			relief 				= 'sunken', 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_CLAN_DONATE_RED],
			justify 			= tkinter.RIGHT, 
			width 				= 3,
			font 				= lybconstant.LYB_FONT
			)
		entry.pack(side=tkinter.LEFT)		
		label = tkinter.Label(
			master 				= frame_b, 
			text 				= "회 실시 합니다",
			justify 			= tkinter.LEFT,
			font 				= lybconstant.LYB_FONT
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame_b.pack(anchor=tkinter.W)

		self.inner_frame_dic['clan_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['clan_tab_frame'], text='혈맹')

		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()


	def callback_clan_donate_adena_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_clan_donate_adena_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_clan_donate_blood_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_clan_donate_blood_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_clan_donate_red_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_clan_donate_red_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hp_potion_buy_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hp_potion_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_mp_potion_buy_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_mp_potion_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_weekly_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_weekly_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



import likeyoubot_game as lybgame
import likeyoubot_talion_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBTalion(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'메인 퀘스트',
		'스토리 던전',
		'고브의 금고',
		'시련의 동굴',
		'골렘 연구소',
		'도전의 탑',
		'정예 던전',
		'분해',
		'키키 지원단',
		'유물',
		'날개',
		
		'알림',
		'[반복 시작]',
		'[반복 종료]',
		'[작업 대기]',
		'[작업 예약]',
		'' ]

	talion_icon_list = [
		'talion_icon_0923'
		]

	story_dungeon_list = [
		'선택 안함',
		'제2전초기지',
		'타락한 기사단',
		'야수의 구덩이',
		'불타는 지옥',
		'이교도의 사원',
		# '지옥의 문',
		# '신들의 유산',
		# '사악한 둥지',
		# '심연의 망자들',
		# '마룡 봉인지',
	]

	story_dungeon_difficulty_list = [
		'일반',
		'숙련',
		'극악',
	]

	dungeon_difficulty_list = [
		'일반',
		'숙련',
		'극악',
		'지옥',
	]

	kiki_support_list = [
		'엘모스트 광산',
		'사냥꾼의 쉼터',
		'티아민의 의상실',
		'모르헨 아카데미',
	]

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_TALION, lybconstant.LYB_GAME_DATA_TALION, window)

	def process(self, window_image):
		rc = super(LYBTalion, self).process(window_image)
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
		pb_name = 'auto_register'
		(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
						window_image,
						self.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(500, 280, 560, 320)
						)
		# self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return 'auto_register'

		pb_name = 'popup_1005'
		(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
						window_image,
						self.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_top_level=(180, 180, 180),
						custom_below_level=(60, 60, 60),
						custom_rect=(550, 50, 580, 80)
						)
		# self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return pb_name


		pb_name = 'auto_equip'
		(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
						window_image,
						self.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_rect=(500, 280, 560, 320)
						)
		# self.logger.info(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
		if loc_x != -1:
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return 'auto_equip'

		# SKIP
		skip_area_list = [
			(570, 250, 630, 280),
			(570, 35, 630, 80)
		]
		resource_name = 'skip_0_loc'
		if self.get_option(resource_name + 'clicked') == False:
			for each_area in skip_area_list:
				(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
									self.window_image,
									resource_name,
									custom_threshold=0.8,
									custom_flag=1,
									custom_rect=each_area  
									)
				if loc_x != -1:
					self.logger.info('skip:' + str(each_area) + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
					self.window.mouse_click(self.hwnd, loc_x, loc_y)	
					self.set_option(resource_name + 'clicked', True)
					return 'skip'
		else:
			self.set_option(resource_name + 'clicked', False)
		# >>
		continue_area_list = [
			(580, 340, 630, 385)
		]
		pb_name = 'continue'
		if self.get_option(pb_name + 'clicked') == False:
			for each_area in continue_area_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[pb_name],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=each_area
								)
				if loc_x != -1:
					self.logger.info(pb_name + ' ' + str(each_area) + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
					self.window.mouse_click(self.hwnd, loc_x, loc_y)
					self.set_option(pb_name + 'clicked', True)	
					return 'continue'
		else:
			self.set_option(pb_name + 'clicked', False)

		if self.main_scene != None and self.main_scene.get_option('menu_click') == True:
			pb_name = 'menu_0'
			match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				return self.menu_scene(window_image)

			pb_name = 'menu_1'
			match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
			self.logger.debug(pb_name + ' ' + str(match_rate))
			if match_rate > 0.9:
				return self.menu_scene(window_image)

		return ''

	def menu_scene(self, window_image):
		menu_status = self.main_scene.get_option('menu_status')

		if (	menu_status == self.main_scene.get_work_status('스토리 던전') or
			 	menu_status == self.main_scene.get_work_status('고브의 금고') or
			 	menu_status == self.main_scene.get_work_status('시련의 동굴') or
			 	menu_status == self.main_scene.get_work_status('골렘 연구소') or
			 	menu_status == self.main_scene.get_work_status('도전의 탑') or
			 	menu_status == self.main_scene.get_work_status('정예 던전')			 	
			 	):
			self.main_scene.set_option('menu_status', 0)

		elif menu_status == self.main_scene.get_work_status('분해'):
			self.main_scene.lyb_mouse_click('menu_character', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == self.main_scene.get_work_status('분해') + 1:
			self.main_scene.lyb_mouse_click('menu_character_gabang', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)	

		elif menu_status == self.main_scene.get_work_status('키키 지원단'):
			self.main_scene.lyb_mouse_click('menu_seongjang', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == self.main_scene.get_work_status('키키 지원단') + 1:
			self.main_scene.lyb_mouse_click('menu_seongjang_kiki', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)

		elif menu_status == self.main_scene.get_work_status('날개'):
			self.main_scene.lyb_mouse_click('menu_seongjang', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == self.main_scene.get_work_status('날개') + 1:
			self.main_scene.lyb_mouse_click('menu_seongjang_nalge', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)

		elif menu_status == self.main_scene.get_work_status('유물'):
			self.main_scene.lyb_mouse_click('menu_sangjeom', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == self.main_scene.get_work_status('유물') + 1:
			self.main_scene.lyb_mouse_click('menu_sangjeom_youmul', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)

		elif menu_status == 0:
			self.main_scene.lyb_mouse_click('menu_tamheom', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == 1:
			self.main_scene.lyb_mouse_click('menu_tamheom_dungeon', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == 10:
			self.main_scene.lyb_mouse_click('menu_sangjeom', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		elif menu_status == 11:
			self.main_scene.lyb_mouse_click('menu_sangjeom_jungke', custom_threshold=0)
			self.main_scene.set_option('menu_status', menu_status + 1)
		else:
			self.main_scene.set_option('menu_click', False)

		return 'menu_scene'

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
			for each_icon in LYBTalion.talion_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.9,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				# print('[DEBUG] nox yh icon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					break
		else:
			for each_icon in LYBTalion.talion_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.9,
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
			if (	'google_play_account_select_scene' in scene_name or
					'logo_screen_scene' in scene_name or
					'connect_account_scene' in scene_name
					):
				self.scene_dic[scene_name] = last_scene[scene_name]

	def add_scene(self, scene_name):
		self.scene_dic[scene_name] = lybscene.LYBTalionScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBTalionTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_TALION):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBTalion.work_list:
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

	def set_option(self):

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

		frame_label = ttk.LabelFrame(frame_l, text='전투')
		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on'].trace(
			'w', lambda *args: self.callback_combat_auto_on(args, lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on')
			)
		if not lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('항상 [자동전투] 전환하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'combat_auto_on'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)		
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('자동 [분해] 작업 주기(초)', width=26)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period'].trace(
			'w', lambda *args: self.callback_combat_bunhe_period(args, lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period')
			)
		combobox_list = []
		for i in range(0, 3600):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period'] = 60

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_ETC + 'bunhe_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_l, text='이벤트')
		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match'].trace(
			'w', lambda *args: self.callback_event_death_match(args, lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match')
			)
		if not lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('데스매치'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_death_match'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)		
		frame.pack(anchor=tkinter.NW)
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp'].trace(
			'w', lambda *args: self.callback_event_team_pvp(args, lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp')
			)
		if not lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('팀 전투'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_team_pvp'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)		
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon'].trace(
			'w', lambda *args: self.callback_event_jeomryeongjeon(args, lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon')
			)
		if not lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('점령전'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_ETC + 'event_jeomryeongjeon'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)		
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
			text 				= self.get_option_text('진행 시간(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration'].trace(
			'w', lambda *args: self.callback_main_quest_duration(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration'] = 3600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub'].trace(
			'w', lambda *args: self.callback_main_quest_sub(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub')
			)
		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '보조', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_sub'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day'].trace(
			'w', lambda *args: self.callback_main_quest_day(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day')
			)
		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '일일', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_day'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat'].trace(
			'w', lambda *args: self.callback_main_quest_repeat(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat')
			)
		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '반복', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_repeat'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main'].trace(
			'w', lambda *args: self.callback_main_quest_main(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main')
			)
		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '메인', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'main_quest_main'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])

		frame_label = ttk.LabelFrame(frame_m, text='스토리 던전')

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol'].trace(
			'w', lambda *args: self.callback_story_dungeon_tobeol(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol')
			)
		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '[토벌] 가능하면 클릭하기', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_tobeol'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('던전 선택', width=14)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select'].trace(
			'w', lambda *args: self.callback_story_dungeon_select(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select')
			)
		combobox_list = LYBTalion.story_dungeon_list

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select'], 
			state 				= "readonly",
			height				= 10,
			width 				= 20,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_select'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('난이도 선택', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty'].trace(
			'w', lambda *args: self.callback_story_dungeon_difficulty(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty')
			)
		combobox_list = LYBTalion.story_dungeon_difficulty_list

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_difficulty'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('진행 횟수(회)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count'].trace(
			'w', lambda *args: self.callback_story_dungeon_count(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count')
			)
		combobox_list = []
		for i in range(0, 11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'story_dungeon_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_m, text='고브의 금고')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('난이도 선택', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty'].trace(
			'w', lambda *args: self.callback_gob_dungeon_difficulty(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty')
			)
		combobox_list = LYBTalion.dungeon_difficulty_list

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'gob_dungeon_difficulty'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_m, text='시련의 동굴')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('난이도 선택', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty'].trace(
			'w', lambda *args: self.callback_siryeon_dungeon_difficulty(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty')
			)
		combobox_list = LYBTalion.dungeon_difficulty_list

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'siryeon_dungeon_difficulty'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_m, text='골렘 연구소')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('난이도 선택', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty'].trace(
			'w', lambda *args: self.callback_golem_dungeon_difficulty(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty')
			)
		combobox_list = LYBTalion.dungeon_difficulty_list

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'golem_dungeon_difficulty'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_m, text='정예 던전')
		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon'].trace(
			'w', lambda *args: self.callback_jeongye_dungeon(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon')
			)
		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('즉시 입장'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'jeongye_dungeon'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])

		frame_label = ttk.LabelFrame(frame_r, text='키키 지원단')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('선택', width=10)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select'].trace(
			'w', lambda *args: self.callback_kiki_support_select(args, lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select')
			)
		combobox_list = LYBTalion.kiki_support_list

		if not lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select'], 
			state 				= "readonly",
			height				= 10,
			width 				= 24,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_WORK + 'kiki_support_select'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 알림 탭 좌
		frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])		

		frame_label = ttk.Frame(frame_l)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death'].trace(
			'w', lambda *args: self.callback_notify_character_death(args, lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death')
			)
		if not lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '캐릭터 사망', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TALION_NOTIFY + 'character_death'],
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
		
		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()

	def callback_combat_bunhe_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_combat_auto_on(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_event_death_match(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_event_team_pvp(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_event_jeomryeongjeon(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_story_dungeon_tobeol(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_story_dungeon_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_story_dungeon_select(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_story_dungeon_difficulty(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gob_dungeon_difficulty(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_siryeon_dungeon_difficulty(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_golem_dungeon_difficulty(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeongye_dungeon(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_kiki_support_select(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_character_death(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_sub(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_day(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_repeat(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_main(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())




import likeyoubot_game as lybgame
import likeyoubot_yeolhyul_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBYeolhyul(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'비밀 상자',

		'무기 - 승급',
		'무기 - 승급 재료',

		'상의 - 승급',
		'상의 - 승급 재료',

		'하의 - 승급',
		'하의 - 승급 재료',

		'견장 - 승급',
		'견장 - 승급 재료',

		'허리띠 - 승급',
		'허리띠 - 승급 재료',


		'신발 - 승급',
		'신발 - 승급 재료',

		'목장식 - 승급',
		'목장식 - 승급 재료',

		'팔찌 - 승급',
		'팔찌 - 승급 재료',

		'가락지 - 승급',
		'가락지 - 승급 재료',
		'' ]

	nox_yh_icon_list = [
		'nox_yh_icon'
		]

	momo_yh_icon_list = [
	]

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_YEOLHYUL, lybconstant.LYB_GAME_DATA_YEOLHYUL, window)

	def process(self, window_image):
		rc = super(LYBYeolhyul, self).process(window_image)
		if rc < 0:
			return rc

		return rc

	def custom_check(self, window_image, window_pixel):

		# print('[DEBUG] CustomCheck 1')
		if not 'skip_event' in self.event_limit:
			self.event_limit['skip_event'] = time.time()

		# skip_limit = int(self.get_game_config(lybconstant.LYB_GAME_YEOLHYUL, lybconstant.LYB_DO_STRING_SKIP_PERIOD))
		skip_limit = 0

		# print('[DEBUG] CustomCheck 2')

		# print('[DEBUG] SKIP COOLTIME:',  time.time() - self.event_limit['skip_event'], 'P:', skip_limit)
		if time.time() - self.event_limit['skip_event'] > skip_limit:
			self.event_limit['skip_event'] = time.time()
			skip_loc_list = [
				'next_bottom_loc',
				'next_npc_loc',
				'next_top_loc',
				'next_top_right_loc',
				'next_bottom_center_loc',
				'next_bottom_right_loc',
				'back_to_the_main_loc'
				]

			s = time.time()
			for each_loc in skip_loc_list:
				# if not each_loc in self.event_limit:
				# 	self.event_limit[each_loc] = time.time()
				# 	self.event_limit[each_loc +'_count'] = 0
				# else:			
				# 	# 동일한 이벤트 10초마다 발생
				# 	if time.time() - self.event_limit[each_loc] < 10:
				# 		if self.event_limit[each_loc +'_count'] > 1:
				# 			continue
				# 	else:
				# 		self.event_limit[each_loc + '_count'] = 0

				# self.event_limit[each_loc + '_count'] += 1

				# adjust_level = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_SKIP_LEVEL_ADJUST))
				adjust_threshold = int(self.get_game_config(lybconstant.LYB_GAME_YEOLHYUL, lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT)) * 0.01
				# print('[DEBUG] adjust_threshold=', adjust_threshold)
				# skip_match_rate = self.rateMatchedResource(
				# 						window_pixel, 
				# 						each_loc,
				# 						custom_below_level=adjust_level
				# 									)

				if each_loc == 'next_bottom_loc':
					each_rect = (580, 365, 610, 385)
				elif each_loc == 'next_npc_loc':
					each_rect = (550, 360, 575, 380)
				elif each_loc == 'next_top_loc':
					each_rect = (345, 120, 370, 135)
				elif each_loc == 'next_top_right_loc':
					each_rect = (425, 120, 450, 135)
				elif each_loc == 'next_bottom_center_loc':
					each_rect = (345, 365, 365, 385)
				elif each_loc == 'next_bottom_right_loc':
					each_rect = (425, 365, 450, 385)
				elif each_loc == 'back_to_the_main_loc':
					each_rect = (510, 30, 635, 55)

				(loc_x, loc_y), skip_match_rate	= self.locationResourceOnWindowPart(
											self.window_image,
											each_loc,
											custom_below_level=(100, 100, 100),
											custom_top_level=(220, 210, 190),
											custom_threshold=adjust_threshold,
											custom_flag=1,
											custom_rect=each_rect
											)

				if loc_x != -1 and skip_match_rate >= adjust_threshold:
					print('Clicked SKIP:', each_loc + ':' + str((loc_x, loc_y)) +'  '+ str(int(skip_match_rate * 100)) + '%')
					self.loggingToGUI('[클릭 성공] 다음:' + str((loc_x, loc_y)))
					self.mouse_click(each_loc.replace('_loc', '', 1) + '_0')
					self.event_limit[each_loc] = time.time()

					return 'skip'
				else:
					pass
					# print('SKIP:', each_loc + ':' + str((loc_x, loc_y)) +'  '+ str(int(skip_match_rate * 100)) + '%')

			e = time.time()
			# print('[DEBUG] ElapsedTime SKIP:', round(e - s, 2))


		return ''

	def get_screen_by_location(self, window_image):
		
		scene_name = self.scene_nox_init_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		# scene_name = self.scene_google_play_account_select(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		return ''
	
	def scene_nox_init_screen(self, window_image):

		loc_x = -1
		loc_y = -1

		if self.player_type == 'nox':
			for each_icon in LYBYeolhyul.nox_yh_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				# print('[DEBUG] nox yh icon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					break
		elif self.player_type == 'momo':
			for each_icon in LYBTera.momo_yh_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.6,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
								)
				# print('[DEBUG] momo yh icon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					break

		if loc_x == -1:
			return ''

		return 'nox_init_screen_scene'

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
		self.scene_dic[scene_name] = lybscene.LYBYeolhyulScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBYeolhyulTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_YEOLHYUL):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBYeolhyul.work_list:
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

	def set_option(self):

		###############################################
		#                메인 퀘스트 진행             #
		###############################################

		frame = ttk.Frame(self.inner_frame_dic['frame_top'], relief=self.frame_relief)
		frame.pack(anchor=tkinter.W)

		
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




















		frame_label = ttk.LabelFrame(self.inner_frame_dic['common_tab_frame'], text='공통')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[다음] 문자 이미지 인식 허용치:"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT].trace(
			'w', lambda *args: self.callback_threshold_next_stringvar(args, lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT)
			)

		if not lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT] = 80

		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)
		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "%"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.W, padx=5, pady=5)














		frame_label = ttk.LabelFrame(self.inner_frame_dic['common_tab_frame'], text='관문')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[관문] 이미지 인식 허용치:"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE].trace(
			'w', lambda *args: self.callback_threshold_gate_stringvar(args, lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE)
			)

		if not lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE] = 70

		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_YH_THRESHOLD_GATE],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)
		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "%"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.W, padx=5, pady=5)







































		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()



	def callback_threshold_gate_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_next_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



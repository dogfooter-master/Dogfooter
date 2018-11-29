import likeyoubot_game as lybgame
import likeyoubot_tera_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBTera(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'메인 퀘스트',
		'' ]

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_TERA, lybconstant.LYB_GAME_DATA_TERA, window)

	def process(self, window_image):
		rc = super(LYBTera, self).process(window_image)
		if rc < 0:
			return rc

		return rc

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
		self.scene_dic[scene_name] = lybscene.LYBTeraScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBTeraTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_TERA):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		print('DEBUG 1--')
		for each_work in LYBTera.work_list:
			print(each_work)
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

		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()

	def callback_main_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



import likeyoubot_game as lybgame
import likeyoubot_clans_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBClans(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'자동전투 설정',

		'보너스',
		'방파 기부',
		'방파 선물',
		'귀보당',

		'영웅 도전',
		'무신전',
		'상단 임무',
		'명상하기',
		'임무 보상',

		'메인 퀘스트',

		'안전 지대로 이동',
		'자동 사냥',


		'동료 무료 소환',

		'무림 맹주 도전',

		'보물 탐색',
		'[작업 예약]',
		'' ]

	nox_clans_icon_list = [
		'clans_icon',
	]

	momo_clans_icon_list = [
		'clans_icon',	
	]
	
	gibodang_item_list = [ 
		'황금상자', 
		'특급 경험약수',
		'하급 수양서',
		'청수정',
		'녹수정',
		'백수정',
		'2레벨 영혼석 상자',
		'1레벨 영혼석 상자',
		'청동대정',
		'칠현고금',
		'청죽간',
		'백옥비녀',
		'비취팔찌',
		'자수정',
		'3레벨 영혼석 상자',
		'장명궁등',
		'청화자기',
		'주황수정',
		'묵옥벼루',
		'동편종',
		'벽옥반지',
		'유금은반',
		'천수관음',
		'중급수양서'

		 ]

	sangdan_item_list = [
		'토벌 증표',
		'칠현고금',
		'청죽간',
		'백옥비녀',
		'비취팔찌',

		'장명궁등',
		'청화자기',
		'묵옥벼루',
		'동편종',
		'벽옥반지',

		'유금은반',
		'천수관음',
		'청동대정',#
		'살수 증표',
		'방파 신물', # 14

		'초절봉 5레벨 영패', # 15
		'초절봉 4레벨 영패', # 16
		'초절봉 3레벨 영패', 
		'초절봉 2레벨 영패',
		'초절봉 1레벨 영패', # 19

		'보스 증표'
		 ]

	bonus_option_list = [ lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_WONBO,  lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_REWARD, 
			lybconstant.LYB_DO_BOOLEAN_BONUS_GOLD_TREE, lybconstant.LYB_DO_BOOLEAN_BONUS_OFFEXP, lybconstant.LYB_DO_BOOLEAN_BONUS_IMMEDIATE]

	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_CLANS, lybconstant.LYB_GAME_DATA_CLANS, window)

	def process(self, window_image):
		rc = super(LYBClans, self).process(window_image)
		if rc < 0:
			return rc
		elif rc == 222222:
			# 이벤트
			if self.get_scene('clans_main_scene').get_option('wait_for_next') == True:
				self.get_scene('clans_main_scene').set_option('wait_for_next', False)

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





	def process_event(self, window_pixels, event_name):
		rc = super(LYBClans, self).process_event(window_pixels, event_name)
		if rc == True:
			if (	'clans_sangdan_complete' in event_name or
					'clans_sangdan_nomore' in event_name
					):
				if self.main_scene != None:
					self.main_scene.set_option('상단 임무' + '_end_flag', True)

		return rc



	def get_screen_by_location(self, window_image):

		# 이미지 위치가 변하는 씬			
		scene_name = self.scene_nox_init_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_google_play_account_select(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_change_account(window_image)
		if len(scene_name) > 0:
			return scene_name

		return ''
		

	def scene_nox_init_screen(self, window_image):

		loc_x = -1
		loc_y = -1

		if self.player_type == 'nox':
			for each_icon in LYBClans.nox_clans_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.7,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				print('[DEBUG] NoxClansIcon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					self.loggingToGUI('녹스 클랜즈 아이콘 발견됨. 위치: '+str((loc_x, loc_y)))
					break
		elif self.player_type == 'momo':
			for each_icon in LYBClans.momo_clans_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.6,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
								)
				print('[DEBUG] NoxClansIcon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					self.loggingToGUI('모모 클랜즈 아이콘 발견됨. 위치: '+str((loc_x, loc_y)))
					break

		if loc_x == -1:
			return ''

		return 'nox_init_screen_scene'

	def scene_change_account(self, window_image):
		loc_x_list = []
		loc_y_list = []

		(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
			window_image, 
			self.resource_manager.pixel_box_dic['clans_change_account_scene_close_icon']
			)
		loc_x_list.append(loc_x)
		loc_y_list.append(loc_y)

		(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
			window_image, 
			self.resource_manager.pixel_box_dic['clans_change_account_scene_google_icon']
			)
		loc_x_list.append(loc_x)
		loc_y_list.append(loc_y)

		for i in range(2):
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				window_image, 
				self.resource_manager.pixel_box_dic['clans_change_account_scene_pb_' + str(i)]
				)

			loc_x_list.append(loc_x)
			loc_y_list.append(loc_y)

		for each_loc in loc_x_list:
			if each_loc == -1:
				return ''
			else:
				continue

		return 'clans_change_account_scene'

	def scene_google_play_account_select(self, window_image):
		loc_x_list = []
		loc_y_list = []

		(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
			window_image, 
			self.resource_manager.pixel_box_dic['clans_google_play_letter']
			)
		loc_x_list.append(loc_x)
		loc_y_list.append(loc_y)

		for i in range(6):
			(loc_x, loc_y) = lybgame.LYBGame.locationOnWindow(
				window_image, 
				self.resource_manager.pixel_box_dic['clans_google_play_letter_' + str(i)]
				)

			loc_x_list.append(loc_x)
			loc_y_list.append(loc_y)


		for each_loc in loc_x_list:
			if each_loc == -1:
				return ''
			else:
				continue

		return 'clans_google_play_account_select_scene'

	def clear_scene(self):

		last_scene = self.scene_dic
		self.scene_dic = {}
		for scene_name, scene in last_scene.items():
			if (	'google_play_account_select_scene' in scene_name or
					'clans_change_account_scene' in scene_name or
					'clans_login_scene' in scene_name
					):
				self.scene_dic[scene_name] = last_scene[scene_name]

	def add_scene(self, scene_name):
		self.scene_dic[scene_name] = lybscene.LYBClansScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBClansTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_CLANS):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBClans.work_list:
			# print(each_work)
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

	def set_option(self):

		self.inner_frame_dic['options'] = ttk.Frame(
			master 				= self.master, 
			relief 				= self.frame_relief
			)




















































		self.option_dic['option_note'] = ttk.Notebook(
			master 				= self.inner_frame_dic['options']
			)


		# 메인 탭
		self.inner_frame_dic['main_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		
		self.inner_frame_dic['main_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['main_tab_frame'], text='메인')


		# 이벤트 탭
		self.inner_frame_dic['event_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		
		self.inner_frame_dic['event_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['event_tab_frame'], text='이벤트')


		# 방파 탭
		self.inner_frame_dic['clan_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['clan_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['clan_tab_frame'], text='방파')

































































		frame = ttk.Frame(self.inner_frame_dic['main_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[자동 사냥] 작업 진행 시간:"
			)
		label.pack(side=tkinter.LEFT)

		combobox_list = []
		for i in range(0, 601):
			combobox_list.append(str(i))

		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA].trace('w', 
			lambda *args: self.callback_duration_jasa_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA))

		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA].set(combobox_list[300])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT,
			justify 			= tkinter.RIGHT
			)
		combobox.set(combobox_list[300])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "분"
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_CLANS_STRING_DURATION_JASA] = 300
		
		frame.pack(anchor=tkinter.NW)



		frame = ttk.Frame(self.inner_frame_dic['main_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[안전 지대로 이동] 작업 진행 시간:"
			)
		label.pack(side=tkinter.LEFT)

		combobox_list = []
		for i in range(1, 61):
			combobox_list.append(str(i))

		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE].trace('w', 
			lambda *args: self.callback_duration_safety_move_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE))

		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE].set(combobox_list[19])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT,
			justify 			= tkinter.RIGHT
			)
		combobox.set(combobox_list[19])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "초"
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_CLANS_STRING_DURATION_SAFETY_MOVE] = 19
		
		frame.pack(anchor=tkinter.NW)



		frame = ttk.Frame(self.inner_frame_dic['main_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[상단 임무] 작업 진행 시간:"
			)
		label.pack(side=tkinter.LEFT)

		combobox_list = []
		for i in range(1, 21):
			combobox_list.append(str(i))

		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN].trace('w', 
			lambda *args: self.callback_duration_sangdan_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN))

		self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN].set(combobox_list[19])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT,
			justify 			= tkinter.RIGHT
			)
		combobox.set(combobox_list[19])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "분"
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_CLANS_STRING_DURATION_SANGDAN] = 19
		
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(self.inner_frame_dic['main_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "메인 퀘스트를 최대"
			)
		label.pack(side=tkinter.LEFT)

		combobox_list = []
		for i in range(1, 601):
			combobox_list.append(str(i))

		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST].trace('w', 
			lambda *args: self.entry_callback(args, option_name=lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST))

		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST].set(combobox_list[60])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT,
			justify 			= tkinter.RIGHT
			)
		combobox.set(combobox_list[60])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "분 동안 진행합니다."
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST] = 60
		
		frame.pack(anchor=tkinter.NW)

		###############################################
		#              HP 낮을 경우 좌선하기          #
		###############################################

		frame = ttk.Frame(self.inner_frame_dic['main_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "전투 중 체력이 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_CHECK_HP] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_CHECK_HP].trace('w', lambda *args: self.entry_callback_2(args, option_name=lybconstant.LYB_DO_STRING_CHECK_HP))
		entry = ttk.Entry(
			master 				= frame, 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_CHECK_HP],
			justify 			= tkinter.RIGHT,
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 점프 후 수동으로 변경하고 좌선합니다."
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_STRING_CHECK_HP in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_CHECK_HP] = 20
		
		frame.pack(anchor=tkinter.NW)


		###############################################
		#                 자동 전투 설정              #
		###############################################

		frame = ttk.LabelFrame(self.inner_frame_dic['main_tab_frame'], text='자동 전투 설정')
		frame_t = ttk.Frame(frame)

		self.option_dic['combat_mode_list'] = [
			('제한 없음', 0), 
			('NPC 우선 공격', 1), 
			('협객 우선 공격', 2)
			]
		self.option_dic[lybconstant.LYB_DO_STRING_MODE_COMBAT] = tkinter.StringVar(frame_t)
		self.option_dic[lybconstant.LYB_DO_STRING_MODE_COMBAT].trace('w', self.select_combat_mode)
		for text, mode in self.option_dic['combat_mode_list']:

			combo_box = ttk.Radiobutton(
				master 				= frame_t,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MODE_COMBAT],
				value 				= mode

				)
			combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		if not lybconstant.LYB_DO_STRING_MODE_COMBAT in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MODE_COMBAT] = 0

		frame_t.pack(anchor=tkinter.W)
		frame_b = ttk.Frame(frame, relief=self.frame_relief)

		self.set_combat_skill_checkbox(frame_b, lybconstant.LYB_DO_BOOLEAN_0_COMBAT_SKILL, 0)
		self.set_combat_skill_checkbox(frame_b, lybconstant.LYB_DO_BOOLEAN_1_COMBAT_SKILL, 1)
		self.set_combat_skill_checkbox(frame_b, lybconstant.LYB_DO_BOOLEAN_2_COMBAT_SKILL, 2)
		self.set_combat_skill_checkbox(frame_b, lybconstant.LYB_DO_BOOLEAN_3_COMBAT_SKILL, 3)
		self.set_combat_skill_checkbox(frame_b, lybconstant.LYB_DO_BOOLEAN_4_COMBAT_SKILL, 4)

		frame_b.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W, pady=5)

		###############################################
		#                  보너스 설정                #
		###############################################

		frame = ttk.LabelFrame(self.inner_frame_dic['main_tab_frame'], text='보너스 받기 설정')
		frame_b = ttk.Frame(frame)
		bonus_list = [ '일일 원보', '출석 보상', '황금 나무', '오프 경험치', '즉시 완료' ]

		for each_bonus in bonus_list:

			if each_bonus == '일일 원보':
				option_name = lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_WONBO
				self.option_dic[option_name] = tkinter.BooleanVar(frame_b)
				self.option_dic[option_name].trace('w', lambda *args: self.select_daily_wonbo(args))
			elif each_bonus == '출석 보상':
				option_name = lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_REWARD
				self.option_dic[option_name] = tkinter.BooleanVar(frame_b)
				self.option_dic[option_name].trace('w', lambda *args: self.select_daily_reward(args))
			elif each_bonus == '황금 나무':
				option_name = lybconstant.LYB_DO_BOOLEAN_BONUS_GOLD_TREE
				self.option_dic[option_name] = tkinter.BooleanVar(frame_b)
				self.option_dic[option_name].trace('w', lambda *args: self.select_gold_tree(args))
			elif each_bonus == '오프 경험치':
				option_name = lybconstant.LYB_DO_BOOLEAN_BONUS_OFFEXP
				self.option_dic[option_name] = tkinter.BooleanVar(frame_b)
				self.option_dic[option_name].trace('w', lambda *args: self.select_offexp(args))
			elif each_bonus == '즉시 완료':
				option_name = lybconstant.LYB_DO_BOOLEAN_BONUS_IMMEDIATE
				self.option_dic[option_name] = tkinter.BooleanVar(frame_b)
				self.option_dic[option_name].trace('w', lambda *args: self.select_immediate(args))

			if not option_name in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][option_name] = True

			check_box = ttk.Checkbutton(

				master 				= frame_b,
				text 				= each_bonus, 
				variable 			= self.option_dic[option_name],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame_b.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(
			master 				= self.master,
			relief 				= self.frame_relief
			)
		frame.pack(pady=5)












































































































































		# -----
		frame = ttk.Frame(self.inner_frame_dic['event_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "이벤트 달력에서 이미지 검색에 실패할 경우"
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_EVENT] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_EVENT].trace('w', lambda *args: self.callback_event_duration(args, option_name=lybconstant.LYB_DO_STRING_DURATION_EVENT))
		
		entry = ttk.Entry(
			master 				= frame, 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_EVENT],
			justify 			= tkinter.RIGHT,
			width 				= 4
			)
		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 동안 추가 검색합니다"
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_STRING_DURATION_EVENT in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_EVENT] = 30
		
		frame.pack(anchor=tkinter.NW, pady=2, fill=tkinter.BOTH)
		
		# -----
		frame = ttk.Frame(self.inner_frame_dic['event_tab_frame'], relief=self.frame_relief)
		label = ttk.Label(
			master 				= frame, 
			text 				= "일일 임무 활약도 보상을 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_DAILY_REWARD] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DAILY_REWARD].trace('w', \
			lambda *args: self.callback_daily_reward(args, option_name=lybconstant.LYB_DO_STRING_DAILY_REWARD))

		entry = ttk.Entry(
			master 				= frame, 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DAILY_REWARD],
			justify 			= tkinter.RIGHT,
			width 				= 4
			)
		entry.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "분 마다 체크합니다"
			)
		label.pack(side=tkinter.LEFT)

		if not lybconstant.LYB_DO_STRING_DAILY_REWARD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DAILY_REWARD] = 30
		
		frame.pack(anchor=tkinter.NW, pady=2, fill=tkinter.BOTH)


		frame = ttk.LabelFrame(self.inner_frame_dic['event_tab_frame'], text='상단 임무 지원 요청할 아이템')
		for i in range(10):
			frame_b = ttk.Frame(frame)
			label = ttk.Label(
				master 				= frame_b, 
				text 				= "지원 요청 " + str(i) + " 순위:"
				)
			label.pack(side=tkinter.LEFT)

			combobox_list = LYBClans.sangdan_item_list

			self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)] = tkinter.StringVar(frame_b)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_0_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "0"))
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_1_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "1"))
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_2_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "2"))
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_3_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "3"))
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_4_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "4"))
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_5_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "5"))
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_6_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "6"))
			elif i == 7:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_7_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "7"))
			elif i == 8:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_8_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "8"))
			elif i == 9:
				self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_sangdan_item_9_stringvar(args, option_name=lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + "9"))

			self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)].set(combobox_list[i])

			combobox = ttk.Combobox(
				master 				= frame_b,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)], 
				state 				= "readonly",
				height				= 10,
				width 				= 20,
				font 				= lybconstant.LYB_FONT,
				justify 			= tkinter.LEFT
				)
			combobox.set(combobox_list[i])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

			if not lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_CLANS_STRING_SANGDAN_ITEM + str(i)] = combobox_list[i]

			frame_b.pack(anchor=tkinter.W)

		frame.pack(anchor=tkinter.NW, padx=5, pady=5)



























































		# TO-DO here
		

		###############################################
		#                  귀보당                     #
		###############################################

		frame = ttk.LabelFrame(self.inner_frame_dic['clan_tab_frame'], text='귀보당 구매 아이템 설정')
		frame_b = ttk.Frame(frame)

		for each_item in LYBClans.gibodang_item_list:

			i = LYBClans.gibodang_item_list.index(each_item)
			self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)] = tkinter.BooleanVar(frame_b)

			# if not lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i) in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)] = True

			if each_item == '황금상자':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_0(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(0)))
			elif each_item == '특급 경험약수':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_1(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(1)))
			elif each_item == '하급 수양서':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_2(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(2)))
			elif each_item == '청수정':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_3(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(3)))
			elif each_item == '녹수정':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_4(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(4)))
			elif each_item == '백수정':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_5(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(5)))
			elif each_item == '2레벨 영혼석 상자':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_6(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(6)))
			elif each_item == '1레벨 영혼석 상자':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_7(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(7)))
			elif each_item == '청동대정':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_8(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(8)))
			elif each_item == '칠현고금':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_9(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(9)))
			elif each_item == '청죽간':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_10(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(10)))
			elif each_item == '백옥비녀':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_11(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(11)))
			elif each_item == '비취팔찌':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_12(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(12)))
			elif each_item == '자수정':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_13(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(13)))
			elif each_item == '3레벨 영혼석 상자':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_14(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(14)))
			elif each_item == '장명궁등':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_15(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(15)))
			elif each_item == '청화자기':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_16(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(16)))
			elif each_item == '주황수정':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_17(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(17)))
			elif each_item == '묵옥벼루':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_18(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(18)))
			elif each_item == '동편종':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_19(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(19)))
			elif each_item == '벽옥반지':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_20(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(20)))
			elif each_item == '유금은반':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_21(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(21)))
			elif each_item == '천수관음':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_22(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(22)))
			elif each_item == '중급수양서':
				self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)].trace('w', 
					lambda *args: self.callback_gibodang_item_23(args, option_name=lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(23)))

			if i == 0:
				frame_checkbox = ttk.Frame(frame_b)
			elif i % 2 == 0:
				frame_checkbox.pack(anchor=tkinter.W)
				frame_checkbox = ttk.Frame(frame_b)

			check_box = ttk.Checkbutton(

				master 				= frame_checkbox,
				text 				= each_item, 
				variable 			= self.option_dic[lybconstant.LYB_DO_CLANS_BOOLEAN_GIBODANG_ITEM + str(i)],
				onvalue 			= True, 
				offvalue 			= False,
				width 				= 20
			)
			check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)
			if i == len(LYBClans.gibodang_item_list) - 1:
				frame_checkbox.pack(anchor=tkinter.W)


		frame_b.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.NW, padx=5, pady=5)


		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)

		self.set_game_option()










































	def callback_sangdan_item_0_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_1_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_2_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_3_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_4_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_5_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_6_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_7_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_8_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sangdan_item_9_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_duration_sangdan_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_duration_safety_move_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_duration_jasa_stringvar(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_0(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_1(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_2(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_3(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_4(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_5(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_6(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_7(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_8(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_9(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_10(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_11(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_12(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_13(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_14(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_15(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_16(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_17(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_18(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_19(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_20(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_21(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_22(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gibodang_item_23(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_daily_reward(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def entry_callback(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_event_duration(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def entry_callback_2(self, *args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def select_combat_mode(self, *args):
		self.set_game_config(lybconstant.LYB_DO_STRING_MODE_COMBAT, self.option_dic[lybconstant.LYB_DO_STRING_MODE_COMBAT].get())

	def select_combat_skill_1(self, *args):
		skill_name = lybconstant.LYB_DO_BOOLEAN_0_COMBAT_SKILL
		self.set_game_config(skill_name, self.option_dic[skill_name].get())

	def select_combat_skill_2(self, *args):
		skill_name = lybconstant.LYB_DO_BOOLEAN_1_COMBAT_SKILL
		self.set_game_config(skill_name, self.option_dic[skill_name].get())

	def select_combat_skill_3(self, *args):
		skill_name = lybconstant.LYB_DO_BOOLEAN_2_COMBAT_SKILL
		self.set_game_config(skill_name, self.option_dic[skill_name].get())

	def select_combat_skill_4(self, *args):
		skill_name = lybconstant.LYB_DO_BOOLEAN_3_COMBAT_SKILL
		self.set_game_config(skill_name, self.option_dic[skill_name].get())

	def select_combat_skill_5(self, *args):
		skill_name = lybconstant.LYB_DO_BOOLEAN_4_COMBAT_SKILL
		self.set_game_config(skill_name, self.option_dic[skill_name].get())

	def select_daily_wonbo(self, *args):
		bonus_name = lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_WONBO
		self.set_game_config(bonus_name, self.option_dic[bonus_name].get())

	def select_daily_reward(self, *args):
		bonus_name = lybconstant.LYB_DO_BOOLEAN_BONUS_DAILY_REWARD
		self.set_game_config(bonus_name, self.option_dic[bonus_name].get())

	def select_gold_tree(self, *args):
		bonus_name = lybconstant.LYB_DO_BOOLEAN_BONUS_GOLD_TREE
		self.set_game_config(bonus_name, self.option_dic[bonus_name].get())

	def select_offexp(self, *args):
		bonus_name = lybconstant.LYB_DO_BOOLEAN_BONUS_OFFEXP
		self.set_game_config(bonus_name, self.option_dic[bonus_name].get())

	def select_immediate(self, *args):
		bonus_name = lybconstant.LYB_DO_BOOLEAN_BONUS_IMMEDIATE
		self.set_game_config(bonus_name, self.option_dic[bonus_name].get())


	def set_combat_skill_checkbox(self, frame, option_name, i):
	
		self.option_dic[option_name] = tkinter.BooleanVar(frame)

		skill_name = '스킬 '+str(i+1)

		if i == 0:
			self.option_dic[option_name].trace('w', lambda *args: self.select_combat_skill_1(args))
		elif i == 1:
			self.option_dic[option_name].trace('w', lambda *args: self.select_combat_skill_2(args))
		elif i == 2:
			self.option_dic[option_name].trace('w', lambda *args: self.select_combat_skill_3(args))
		elif i == 3:
			self.option_dic[option_name].trace('w', lambda *args: self.select_combat_skill_4(args))
		elif i == 4:
			self.option_dic[option_name].trace('w', lambda *args: self.select_combat_skill_5(args))

		if not option_name in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= skill_name, 
			variable 			= self.option_dic[option_name],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

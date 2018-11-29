import likeyoubot_game as lybgame
import likeyoubot_icarus_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBIcarus(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'메인 퀘스트',
		'정예 퀘스트',
		'자동 사냥',
		'펠로우 탐험',
		'펠로우 세트',
		'몬스터 결정',
		'가방 정리',
		'캐릭터 선택',
		
		'알림',
		'[반복 시작]',
		'[반복 종료]',
		'[작업 대기]',
		'[작업 예약]',
		'' ]

	icarus_icon_list = [
		'icarus_icon_0',
		'icarus_icon_1',
		'icarus_icon_1109',
		]

	area_list = [
		'브라카르 숲',
		'하카나스 직할령',
		'파르나의 땅'
		]
	area_sub_list = [
		[
			'브라기 본거지',
			'잊혀진 유적지'
		],

		[
			'풍요의 언덕',
			'켈우즈 역병지대',
			'신룡의 해안가'
		],

		[
			'여신의 땅',
			'소르마 평원',
			'파를라크 얼음성채'		
		]
	]

	quest_area_sub_list = [
		[
			'엘로라의 신전',	
			'브라기 본거지',
			'잊혀진 유적지',
			'코쿤'
		],

		[
			'풍요의 언덕',
			'켈우즈 역병지대',
			'신룡의 해안가'
		],

		[
			'여신의 땅',
			'소르마 평원',
			'파를라크 얼음성채'		
		]
	]
	elite_quest_sub_dic = {
		area_list[0]: quest_area_sub_list[0],
		area_list[1]: quest_area_sub_list[1],
		area_list[2]: quest_area_sub_list[2],
	}

	elite_quest_dic = {
		quest_area_sub_list[0][0] : [
			'선택 안함',			# 0
			],
		quest_area_sub_list[0][1] : [
			'선택 안함',			# 0
			'도난당한 물건',
			'라이노 토벌',
			'렉스의 무기 조사',
			'빼앗긴 서신',
			'여왕의 날개',
			'요정의 장난',
			'튼튼한 가죽',
			],
		quest_area_sub_list[0][2] : [
			'선택 안함',			# 0	
			'거미의 덫',
			'교단의 창궐',
			'남아있는 힘',
			'박쥐 퇴치',
			'유령 퇴치',
			'유행하는 물건',
			'지팡이 개조',	
			'특별한 가면',
			'튼튼한 갑옷',
			'흑마법의 집약체',
			'힘의 근원 조사',	
			],
		quest_area_sub_list[0][3] : [
			'선택 안함',			# 0
			],

		quest_area_sub_list[1][0] : [
			'선택 안함',			# 0
			'검은 그림자',
			'낯가리는 라비니',
			'내재된 힘 1장',
			'마을을 지켜라! 1장',
			'마을을 지켜라! 2장',
			'마을의 골칫덩이',
			'민감한 라비니',
			'벌집군 붕괴 현상',
			'사라진 고문서',
			'사로잡힌 라비니',
			'영역의 폭군',
			'이상 증세',
			'이상한 뾰족귀',
			'풍요의 눈물',
			'풍요의 조각',
			'풍요의 폭군',
			],
		quest_area_sub_list[1][1] : [
			'선택 안함',			# 0
			'내재된 힘 2장',
			'론도의 주술',
			'수상한 그림자',
			'습격받은 캠프',
			'아버지의 흔적',
			'안전제일',
			'연금술 실험',
			'연금술의 비원',
			'위험 제거 1장',
			'위험 제거 2장',
			'위험 제거 3장',
			'저주받은 마물',
			'좀비 토벌',
			'좀비의 우두머리',
			'켈우즈의 눈물',
			'켈우즈의 재앙',
			'켈우즈의 조각',
			],
		quest_area_sub_list[1][2] : [
			'선택 안함',			# 0
			'내재된 힘 3장',
			'선제공격',
			'작은 악마',
			'전략적 기회',
			'절벽의 폭탄',
			'캠프 수비 1장',
			'캠프 수비 2장',
			'캠프 수비 3장',
			'캠프 수비 4장',
			'하피의 본모습',			
			'해안가의 눈물',
			'해안가의 마물',
			'해안가의 저주',
			'해안가의 조각',
			'해안가의 폭군',
			'해적소탕',
			'행운의 증표',
			],

		quest_area_sub_list[2][0] : [
			'선택 안함',			# 0
			'늑대의 가죽',
			'몸에 좋은 것',
			'보수를 해야 해 1장',
			'보수를 해야 해 2장',
			'분신 1장',
			'분신 2장',
			'야생곰의 꿀',
			'얼음 폭탄',
			'염탐꾼의 돋보기',
			'유지할 수 있는 것',
			'위험이 없도록',
			'위험한 길',
			'의지할 수 있는 것',
			'주술에 필요한 것',
			'캠프가 위험해',
			'통제 불가',
			],
		quest_area_sub_list[2][1] : [
			'선택 안함',			# 0
			'가려진 그림자',
			'가려진 슬픔',
			'가려진 진실',
			'거짓말',
			'또 다른 단서',
			'마지막 장식',
			'부정된 존재',
			'예비 수호자',
			'예비 제사장',
			'인어 알의 행방',
			'잊혀진 임무',
			'최고급 솜털',
			'최고급 무기',
			'추종자',
			'평원의 눈물 2장',
			'평원의 조각 1장',
			'평원의 폭군 3장',
			],
		quest_area_sub_list[2][2] : [
			'선택 안함',			# 0
			'결박된 자',
			'그릇된 맹세',
			'까다로운 상대 1장',
			'까다로운 상대 2장',
			'더럽히는 자',	
			'보온에 좋은 재료',
			'보초병의 애환',
			'분신의 재료',
			'성주의 장비',
			'심연의 손길',
			'심연의 어둠',
			'어둠의 힘',
			'어지럽히는 자',
			'얼음성의 병사들',
			'오염된 심장',
			'이름과 가죽',
			'일꾼의 비애',
			'적의 내통법',
			'적의 소통법',
			'파를라크 감시자',
			'혹한의 비명',
			],
	}

	# quest_scene_elite_캠프가 위험해_loc

	fellow_sort_list = [
		'전체',
		'추천 순위',
		'지역',
		'능력치',
	]

	menu_fellow_sub_list = [
		'펠로우 가방',
		'펠로우 조각',
		'펠로우 세트',
		'펠로우 탐험'
	]
	
	menu_seongjang_sub_list = [
		'영혼석',
		'교본 연구',
		'몬스터 결정',
		'축복'
	]

	fellow_set_list = [
		'설정 안함',
		'속성 저항력',
		'시공의 틈',
		'파괴자의 습격',
		'주신의 길',
		'사냥',
		'기타',
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

	item_catalog_list = [
		'무기',
		'방어구',
		'장신구'
	]
	
	item_rank_list = [
		'일반',
		'정예',
		'희귀',
		'영웅',
		'전설',
		'주신',
		'특별'
	]

	item_gakseong_list = [
		'불가',
		'1단계',
		'2단계',
		'3단계'
	]

	fellow_catalog_list = [
		'펠로우',
		'소모품',
		'재료'
	]

	fellow_level_list = [
		'D',
		'C',
		'B',
		'A',
		'S',
		'SS'
	]

	tamheom_duration_list = [
		[
			'20m',
			'40m',
			'1h',
			'1h20m'
		],
		[
			'1h',
			'2h',
			'3h',
			'4h'
		],
		[
			'3h',
			'6h',
			'12h',
			'24h'
		]
	]
	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_ICARUS, lybconstant.LYB_GAME_DATA_ICARUS, window)

	def process(self, window_image):

		rc = super(LYBIcarus, self).process(window_image)
		if rc < 0:
			return rc

		return rc

	def custom_check(self, window_image, window_pixel):

		# SKIP
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'skip_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(300, 30, 340, 360)
							)
		if loc_x != -1:
			self.logger.warn('SKIP: ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return 'skip'

		# NPC SKIP
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'npc_skip_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(590, 300, 635, 340)
							)
		if loc_x != -1:
			self.logger.warn('NPC SKIP: ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return 'skip'

		# BOSS SKIP
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'npc_skip_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(570, 30, 635, 80)
							)
		if loc_x != -1:
			self.logger.warn('BOSS SKIP: ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return 'skip'

		# 추석 팝업
		pb_name = 'popup_0920'
		(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
						window_image,
						self.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.8,
						custom_flag=1,
						custom_top_level=(70, 180, 240),
						custom_below_level=(60, 160, 210),
						custom_rect=(570, 20, 610, 70)
						)
		if loc_x != -1:
			self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return 'popup'

		# 팝업
		pb_name_list = [
			'useless_icon_0',
			'useless_icon_1',
			]
		for pb_name in pb_name_list:
			if pb_name_list.index(pb_name) == 0:
				custom_rect = (0, 40, 30, 380)
			else:
				custom_rect = (600, 40, 640, 380)

			(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
							window_image,
							self.resource_manager.pixel_box_dic[pb_name],
							custom_threshold=0.9,
							custom_flag=1,
							custom_top_level=(200, 200, 200),
							custom_below_level=(100, 100, 100),
							custom_rect=custom_rect
							)
			if loc_x != -1:
				self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
				self.window.mouse_click(self.hwnd, loc_x, loc_y)	
				return pb_name

		pb_name = 'useless_trash'
		(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
						window_image,
						self.resource_manager.pixel_box_dic[pb_name],
						custom_threshold=0.9,
						custom_flag=1,
						custom_rect=(10, 180, 640, 240)
						)
		if loc_x != -1:
			self.logger.warn(pb_name + ' ' + str((loc_x, loc_y)) + ' ' + str(match_rate))
			self.window.mouse_click(self.hwnd, loc_x, loc_y)	
			return pb_name


		# 정예 퀘스트 반복 수락
		resource_name = 'main_scene_quest_repeat_loc'
		match_rate = self.rateMatchedResource(self.window_pixels, resource_name)
		#self.logger.info(resource_name + ' ' + str(round(match_rate, 2)))
		if match_rate > 0.9:
			self.mouse_click('main_scene_quest_repeat_accept')				
			return resource_name

		# 아이템 획득 장착
		pb_name = 'main_scene_item_get'
		match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
		if match_rate > 0.9:
			pb_name = 'main_scene_equip'
			match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.mouse_click(pb_name)
				return 'item'

		# 펠로우 획득 장착
		pb_name = 'main_scene_fellow_get'
		match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
		if match_rate > 0.9:
			pb_name = 'main_scene_fellow_equip'
			match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
			if match_rate > 0.9:
				self.mouse_click(pb_name)
				return 'fellow'

		# 퀘스트 완료 OK
		pb_name = 'main_scene_quest_ok'
		match_rate = self.rateMatchedPixelBox(self.window_pixels, pb_name)
		if match_rate > 0.9:
			# self.mouse_click(pb_name)
			return 'fellow'

		return ''

	def get_screen_by_location(self, window_image):

		scene_name = self.scene_init_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		if self.get_option('search_google_account') == True:
			scene_name = self.scene_google_play_account_select(window_image)
			if len(scene_name) > 0:
				return scene_name

		# scene_name = self.jeontoo_scene(window_image)
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
			for each_icon in LYBIcarus.icarus_icon_list:
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
			for each_icon in LYBIcarus.icarus_icon_list:
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

		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
			window_image, 
			self.resource_manager.pixel_box_dic['google_play_letter'],
			custom_flag=1,
			custom_rect=(150, 50, 370, 250)
			)
		loc_x_list.append(loc_x)
		loc_y_list.append(loc_y)

		for i in range(6):
			(loc_x, loc_y), match_rate = self.locationOnWindowPart(
				window_image, 
				self.resource_manager.pixel_box_dic['google_play_letter_' + str(i)],
				custom_flag=1,
				custom_rect=(150, 50, 370, 250)
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
		self.scene_dic[scene_name] = lybscene.LYBIcarusScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBIcarusTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_ICARUS):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBIcarus.work_list:
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

		self.inner_frame_dic['work2_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['work2_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['work2_tab_frame'], text='작업2')


		self.inner_frame_dic['notify_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)
		self.inner_frame_dic['notify_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['notify_tab_frame'], text='알림')
		# ------

		# 일반 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['common_tab_frame'])

		frame_label = ttk.LabelFrame(frame_l, text='스킬')

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill'].trace(
			'w', lambda *args: self.callback_co_skill(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('연계 스킬 사용', width=14), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'co_skill'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		# frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('펠로우 스킬 쿨타임(초)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime'].trace(
			'w', lambda *args: self.callback_fellow_skill_cooltime(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime')
			)
		combobox_list = []
		for i in range(0, 301):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'fellow_skill_cooltime'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		# frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('각성 스킬 쿨타임(초)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime'].trace(
			'w', lambda *args: self.callback_gakseong_skill_cooltime(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime')
			)
		combobox_list = []
		for i in range(0, 301):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'gakseong_skill_cooltime'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('파티 스킬 쿨타임(초)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime'].trace(
			'w', lambda *args: self.callback_etc_party_skill_cooltime(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime')
			)
		combobox_list = []
		for i in range(0, 301):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'party_skill_cooltime'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_l, text='길들이기')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('길들이기 쿨타임(초)(0:안함)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming'].trace(
			'w', lambda *args: self.callback_etc_taming(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming')
			)
		combobox_list = []
		for i in range(0, 301):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('길들이기 반응 속도(ms)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response'].trace(
			'w', lambda *args: self.callback_etc_taming_response(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response')
			)
		combobox_list = []
		for i in range(1, 9001, 1):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response'] = 10

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'taming_response'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_l, text='기타')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('문자 인식 허용률(%)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold'].trace(
			'w', lambda *args: self.callback_elite_quest_threshold(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold')
			)
		combobox_list = []
		for i in range(50, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold'] = 60

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_threshold'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('퀘스트 완료 탐색 주기(초)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period'].trace(
			'w', lambda *args: self.callback_etc_quest_complete_period(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period'] = 3

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quest_complete_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('자동 전환 감지 횟수(회)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit'].trace(
			'w', lambda *args: self.callback_etc_auto_detection_limit(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit')
			)
		combobox_list = []
		for i in range(1, 61):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit'] = 2

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'auto_detection_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react'].trace(
			'w', lambda *args: self.callback_friend_react(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('친구 상호 작용', width=14), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'friend_react'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "  "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite'].trace(
			'w', lambda *args: self.callback_accept_invite(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('파티 초대 수락', width=14), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'accept_invite'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail'].trace(
			'w', lambda *args: self.callback_check_new_mail(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '우편함 확인', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_new_mail'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion'].trace(
			'w', lambda *args: self.callback_check_empty_potion(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '물약 없을 때 구매하기', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'check_empty_potion'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 일반 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['common_tab_frame'])

		frame_label = ttk.LabelFrame(frame_m, text='퀵슬롯 클릭 주기')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('퀵슬롯 1번(초)(0:안함)')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0'].trace(
			'w', lambda *args: self.callback_etc_quickslot_period_0(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_0'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('퀵슬롯 2번')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1'].trace(
			'w', lambda *args: self.callback_etc_quickslot_period_1(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_1'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('퀵슬롯 3번')
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2'].trace(
			'w', lambda *args: self.callback_etc_quickslot_period_2(args, lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_ETC + 'quickslot_period_2'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


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

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration'].trace(
			'w', lambda *args: self.callback_main_quest_duration(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration'] = 3600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('랙 체크 주기(초)(0:안함)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period'].trace(
			'w', lambda *args: self.callback_main_quest_lag_period(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period'] = 60

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_lag_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub'].trace(
			'w', lambda *args: self.callback_main_quest_sub(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub'] = True

		check_box = ttk.Checkbutton(
			master 				= frame,
			text 				= self.get_option_text('서브 퀘스트 우선 수행'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_sub'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local'].trace(
			'w', lambda *args: self.callback_main_quest_local(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local'] = True

		check_box = ttk.Checkbutton(
			master 				= frame,
			text 				= self.get_option_text('지역 퀘스트 우선 수행'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_local'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('서브 퀘스트 탐색 페이지 수', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub'].trace(
			'w', lambda *args: self.callback_main_quest_search_sub(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub')
			)
		combobox_list = []
		for i in range(0, 11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'main_quest_search_sub'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_label = ttk.LabelFrame(frame_l, text='자동 사냥')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('진행 시간(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration'].trace(
			'w', lambda *args: self.callback_auto_duration(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration'] = 3600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('퀘스트 클릭 주기(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period'].trace(
			'w', lambda *args: self.callback_auto_questclick_period(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite'].trace(
			'w', lambda *args: self.callback_auto_questclick_elite(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('정예'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'auto_questclick_elite'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_l, text='캐릭터 선택')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('선택 번호', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number'].trace(
			'w', lambda *args: self.callback_character_number(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number')
			)
		combobox_list = []
		for i in range(1, 6):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'character_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_l, text='펠로우 세트')
		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map'].trace(
			'w', lambda *args: self.callback_fellow_set_map(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('맵 열어서 이동하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_map'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('세트 효과', width=19)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name'].trace(
			'w', lambda *args: self.callback_fellow_set_name(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name')
			)
		combobox_list = LYBIcarus.fellow_set_list

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name'], 
			state 				= "readonly",
			height				= 10,
			width 				= 15,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_name'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('진행 시간(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration'].trace(
			'w', lambda *args: self.callback_fellow_set_duration(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration'] = 3600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('체크 주기(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period'].trace(
			'w', lambda *args: self.callback_fellow_set_period(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period')
			)
		combobox_list = []
		for i in range(10, 86401, 10):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period'] = 120

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_set_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work_tab_frame'])
		frame_label = ttk.LabelFrame(frame_m, text='정예 퀘스트')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('진행 시간(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration'].trace(
			'w', lambda *args: self.callback_elite_quest_duration(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration'] = 600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('반복 횟수(0:무한)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit'].trace(
			'w', lambda *args: self.callback_elite_quest_limit(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit')
			)
		combobox_list = []
		for i in range(0, 1001):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('랙 체크 주기(초)(0:안함)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag'].trace(
			'w', lambda *args: self.callback_elite_quest_lag(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag'] = 60

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_lag'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('퀘스트 체크 주기(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check'].trace(
			'w', lambda *args: self.callback_elite_quest_check(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check'] = 120

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_check'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('수행 지역(대분류)', width=19)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area'].trace(
			'w', lambda *args: self.callback_elite_quest_area(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area')
			)
		combobox_list = LYBIcarus.area_list

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area'], 
			state 				= "readonly",
			height				= 10,
			width 				= 15,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('수행 지역(소분류)', width=19)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub'].trace(
			'w', lambda *args: self.callback_elite_quest_area_sub(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub')
			)

		area_index = LYBIcarus.area_list.index(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area'])

		combobox_list = LYBIcarus.quest_area_sub_list[area_index]

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub'] = combobox_list[0]

		self.elite_quest_area_sub_combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub'], 
			state 				= "readonly",
			height				= 10,
			width 				= 15,
			font 				= lybconstant.LYB_FONT 
			)
		self.elite_quest_area_sub_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub'])
		self.elite_quest_area_sub_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		s = ttk.Style()
		s.configure('red_label.TLabel', foreground='red')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('이동할 퀘스트', width=14),
			style 				= 'red_label.TLabel'
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'].trace(
			'w', lambda *args: self.callback_elite_quest_go(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go')
			)

		combobox_list = LYBIcarus.elite_quest_dic[self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub']]

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'] = combobox_list[0]

		self.elite_quest_go_combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'], 
			state 				= "readonly",
			height				= 10,
			width 				= 20,
			font 				= lybconstant.LYB_FONT 
			)
		self.elite_quest_go_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'])
		self.elite_quest_go_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		self.elite_quest_accept_combobox = []

		for i in range(5):
			frame = ttk.Frame(frame_label)
			label = ttk.Label(
				master 				= frame, 
				text 				= self.get_option_text('수락할 퀘스트' + str(i + 1), width=14),
				)
			label.pack(side=tkinter.LEFT)

			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)] = tkinter.StringVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '0'].trace(
					'w', lambda *args: self.callback_elite_quest_accept_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '1'].trace(
					'w', lambda *args: self.callback_elite_quest_accept_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '2'].trace(
					'w', lambda *args: self.callback_elite_quest_accept_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '2')
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '3'].trace(
					'w', lambda *args: self.callback_elite_quest_accept_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '4'].trace(
					'w', lambda *args: self.callback_elite_quest_accept_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + '4')
					)

			combobox_list = LYBIcarus.elite_quest_dic[self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub']]

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)] = combobox_list[0]

			combobox = ttk.Combobox(
				master 				= frame,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)], 
				state 				= "readonly",
				height				= 10,
				width 				= 20,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
			
			self.elite_quest_accept_combobox.append(combobox)

			frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work_tab_frame'])


		frame_label = ttk.LabelFrame(frame_r, text='펠로우 탐험')


		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend'].trace(
			'w', lambda *args: self.callback_fellow_tamheom_recommend(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend'] = True

		check_box = ttk.Checkbutton(
			master 				= frame,
			text 				= self.get_option_text('추천 펠로우 사용하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom'].trace(
			'w', lambda *args: self.callback_fellow_tamheom_recommend_bottom(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom'] = False

		check_box = ttk.Checkbutton(
			master 				= frame,
			text 				= self.get_option_text('아랫쪽 추천 펠로우부터 등록하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_recommend_bottom'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('체크 주기(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check'].trace(
			'w', lambda *args: self.callback_elite_quest_fellow_check(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check')
			)
		combobox_list = []
		for i in range(0, 3601):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check'] = 600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_fellow_check'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('정렬', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort'].trace(
			'w', lambda *args: self.callback_fellow_tamheom_sort(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort')
			)
		combobox_list = LYBIcarus.fellow_sort_list

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort'] = combobox_list[1]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_sort'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		
		s = ttk.Style()
		s.configure('green_label.TLabel', foreground='green')

		tamheom_area_list = [
			'위',
			'중간',
			'아래'
		]
		for i in range(len(LYBIcarus.tamheom_duration_list)):
			frame = ttk.Frame(frame_label)
			label = ttk.Label(
				master 				= frame, 
				text 				= self.get_option_text(tamheom_area_list[i], width=5),
				style 				= 'green_label.TLabel'
				)
			label.pack(side=tkinter.LEFT)

			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i)] = tkinter.StringVar(frame)

			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_0'].trace(
					'w', lambda *args: self.callback_fellow_tamheom_duration_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_1'].trace(
					'w', lambda *args: self.callback_fellow_tamheom_duration_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_2'].trace(
					'w', lambda *args: self.callback_fellow_tamheom_duration_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_2')
					)

			if i == 0:				
				if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i) in self.configure.common_config[self.game_name]:
					self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i)] = 0
			else:
				if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i) in self.configure.common_config[self.game_name]:
					self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i)] = len(LYBIcarus.tamheom_duration_list[i]) - 1

			radio_list = []
			for j in range(len(LYBIcarus.tamheom_duration_list[i])):
				radio_list.append((LYBIcarus.tamheom_duration_list[i][j], j))

			for text, mode in radio_list:
				radioButton = ttk.Radiobutton(
					master 				= frame,
					text 				= self.get_option_text(text, width=3),
					variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_duration_' + str(i)],
					value 				= mode

					)
				radioButton.pack(anchor=tkinter.W, side=tkinter.LEFT)

			frame.pack(anchor=tkinter.W)

		# frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20'].trace(
			'w', lambda *args: self.callback_fellow_tamheom_20(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20'] = True

		# check_box = ttk.Checkbutton(

		# 	master 				= frame,
		# 	text 				= self.get_option_text('20분짜리 탐험이 인식되면 수행하기'), 
		# 	variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'fellow_tamheom_20'],
		# 	onvalue 			= True, 
		# 	offvalue 			= False
		# )
		# check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		# frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_r, text='몬스터 결정')

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now'].trace(
			'w', lambda *args: self.callback_monster_crystal_now(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('현재 지역에서만 작업하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_now'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map'].trace(
			'w', lambda *args: self.callback_monster_crystal_map(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map'] = False
			
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('맵 열어서 이동하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_map'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off'].trace(
			'w', lambda *args: self.callback_monster_crystal_auto_off(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off'] = False
			
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('체크하기 전에 항상 자동 끄기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_auto_off'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('수행 지역(대분류)', width=19)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area'].trace(
			'w', lambda *args: self.callback_monster_crystal_area(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area')
			)
		combobox_list = LYBIcarus.area_list

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area'] = combobox_list[0]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area'], 
			state 				= "readonly",
			height				= 10,
			width 				= 15,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_area'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('수행 지역(소분류)', width=19)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area'].trace(
			'w', lambda *args: self.callback_monster_crystal_sub_area(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area')
			)
		combobox_list = LYBIcarus.area_sub_list

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area'] = combobox_list[0][0]

		self.monster_area_sub_combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list[0], 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area'], 
			state 				= "readonly",
			height				= 10,
			width 				= 15,
			font 				= lybconstant.LYB_FONT 
			)
		self.monster_area_sub_combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area'])
		self.monster_area_sub_combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('진행 시간(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration'].trace(
			'w', lambda *args: self.callback_monster_crystal_duration(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration')
			)
		combobox_list = []
		for i in range(60, 86401, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration'] = 3600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_duration'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('체크 주기(초)', width=27)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period'].trace(
			'w', lambda *args: self.callback_monster_crystal_period(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period')
			)
		combobox_list = []
		for i in range(10, 86401, 10):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period'] = 120

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 좌측
		frame_l = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])

		frame_label = ttk.LabelFrame(frame_l, text='가방 정리')

		frame_label_inner = ttk.LabelFrame(frame_label, text='장비')
		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi'].trace(
			'w', lambda *args: self.callback_work_gabang_jangbi(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('장비 정리하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip'].trace(
			'w', lambda *args: self.callback_work_gabang_jangbi_auto_equip(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('자동 장착하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_auto_equip'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config'].trace(
			'w', lambda *args: self.callback_work_gabang_jangbi_sell_config(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('판매 설정 사용하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_config'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config'].trace(
			'w', lambda *args: self.callback_work_gabang_jangbi_bunhe_config(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('분해 설정 사용하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_config'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('일괄 판매 수행 횟수', width=22)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'].trace(
			'w', lambda *args: self.callback_work_gabang_jangbi_sell_count(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count')
			)
		combobox_list = []
		for i in range(0, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'] = 10

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_sell_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('일괄 분해 수행 횟수', width=22)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'].trace(
			'w', lambda *args: self.callback_work_gabang_jangbi_bunhe_count(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count')
			)
		combobox_list = []
		for i in range(0, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'] = 10

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_jangbi_bunhe_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label_inner = ttk.LabelFrame(frame_label, text='펠로우')
		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('펠로우 정리하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow_auto_equip(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('자동 장착하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_auto_equip'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow_sell_config(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('판매 설정 사용하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_config'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow_bunhe_config(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('추출 설정 사용하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_config'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_yougu'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_yougu'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow_yougu(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_yougu')
			)

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_yougu' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_yougu'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= self.get_option_text('유그라드실의 열매 제외하기'), 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_yougu'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('일괄 판매 수행 횟수', width=22)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow_sell_count(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count')
			)
		combobox_list = []
		for i in range(0, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'] = 10

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_sell_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label_inner)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('일괄 추출 수행 횟수', width=22)
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'].trace(
			'w', lambda *args: self.callback_work_gabang_fellow_bunhe_count(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count')
			)
		combobox_list = []
		for i in range(0, 101):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'] = 10

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'gabang_fellow_bunhe_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label_inner.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 중간
		frame_m = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])

		frame_label = ttk.LabelFrame(frame_m, text='장비 판매 설정')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('종류', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(3):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_catalog_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_catalog_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_catalog_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(2))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_catalog_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_catalog' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('희귀도', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text(' ', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4, 7):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(4)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(4))
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(5)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_5(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(5))
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(6)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_rank_6(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(6))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('각성', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_gakseong_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_gakseong_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_gakseong_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_config_gakseong_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_gakseong_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_config_gakseong' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)



		frame_label = ttk.LabelFrame(frame_m, text='장비 분해 설정')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('종류', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(3):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_catalog_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_catalog_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_catalog_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(2))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_catalog_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_catalog' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('희귀도', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text(' ', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4, 7):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(4)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(4))
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(5)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_5(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(5))
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(6)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_rank_6(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(6))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('각성', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_gakseong_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_gakseong_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_gakseong_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_config_gakseong_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_gakseong_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_config_gakseong' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


		frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 작업 탭 우측
		frame_r = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])


		frame_label = ttk.LabelFrame(frame_r, text='펠로우 판매 설정')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('종류', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(3):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_catalog_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_catalog_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_catalog_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(2))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.fellow_catalog_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_catalog' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('희귀도', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text(' ', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4, 7):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(4)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(4))
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(5)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_5(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(5))
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(6)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_rank_6(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(6))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('등급', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_level_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_level_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_level_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_level_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.fellow_level_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text(' ', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4, 6):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(4)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_level_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(4))
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(5)].trace(
					'w', lambda *args: self.callback_work_jangbi_sell_fellow_config_level_5(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(5))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.fellow_level_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_sell_fellow_config_level' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_r, text='펠로우 추출 설정')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('희귀도', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text(' ', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4, 7):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(4)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(4))
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(5)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_5(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(5))
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(6)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_rank_6(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(6))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.item_rank_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_rank' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text('등급', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(0)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_level_0(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(1)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_level_1(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(2)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_level_2(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(2))
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(3)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_level_3(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(3))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.fellow_level_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text(' ', width=8)
			)
		label.pack(side=tkinter.LEFT)

		for i in range(4, 6):
			self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i) ] = tkinter.BooleanVar(frame)
			if i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(4)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_level_4(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(4))
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(5)].trace(
					'w', lambda *args: self.callback_work_jangbi_bunhe_fellow_config_level_5(args, lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(5))
					)

			if not lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= LYBIcarus.fellow_level_list[i], 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_WORK + 'jangbi_bunhe_fellow_config_level' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# 알림 탭 좌
		frame_l = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])		
		frame_label = ttk.Frame(frame_l)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang'].trace(
			'w', lambda *args: self.callback_notify_elite_bosang(args, lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '정예 퀘스트 보상', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'elite_bosang'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.NW)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death'].trace(
			'w', lambda *args: self.callback_notify_character_death(args, lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death')
			)
		if not lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '캐릭터 사망', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_ICARUS_NOTIFY + 'character_death'],
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
		# frame_l = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])
		# frame_l.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# # 작업 탭 중간
		# frame_m = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])
		# frame_m.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# # 작업 탭 우측
		# frame_r = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])
		# frame_r.pack(side=tkinter.LEFT, anchor=tkinter.NW)

		# ------
		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()

	def callback_fellow_tamheom_duration_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_tamheom_duration_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_tamheom_duration_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_level_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_level_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_level_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_level_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_level_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_level_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_6(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_fellow_config_rank_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_jangbi_sell_fellow_config_level_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_level_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_level_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_level_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_level_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_level_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_6(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_rank_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_catalog_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_catalog_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_fellow_config_catalog_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_gakseong_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_gakseong_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_gakseong_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_gakseong_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_6(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_rank_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_catalog_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_catalog_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_bunhe_config_catalog_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_gakseong_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_gakseong_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_gakseong_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_gakseong_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_6(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_rank_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_catalog_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_catalog_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_jangbi_sell_config_catalog_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_fellow_sell_config(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_fellow_bunhe_config(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_fellow_yougu(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_work_gabang_fellow_bunhe_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_fellow_sell_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_fellow_auto_equip(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_fellow(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_jangbi_sell_config(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_jangbi_bunhe_config(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_jangbi_bunhe_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_jangbi_sell_count(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_jangbi_auto_equip(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_work_gabang_jangbi(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_tamheom_20(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_set_map(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_set_name(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_set_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_set_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_character_number(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_crystal_sub_area(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_crystal_auto_off(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_monster_crystal_map(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_crystal_now(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_crystal_area(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		area_index = LYBIcarus.area_list.index(self.option_dic[option_name].get())
		new_list = LYBIcarus.area_sub_list[area_index]

		self.monster_area_sub_combobox['values'] = new_list
		if not self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'monster_crystal_sub_area') in new_list:
			self.monster_area_sub_combobox.set(new_list[0])

	def callback_monster_crystal_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_crystal_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_tamheom_sort(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_tamheom_recommend_bottom(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_tamheom_recommend(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_etc_party_skill_cooltime(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gakseong_skill_cooltime(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_character_death(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_elite_bosang(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_accept_invite(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_check_empty_potion(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_quickslot_period_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_quickslot_period_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_quickslot_period_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_check_new_mail(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_taming_response(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_taming(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_auto_detection_limit(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_friend_react(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_etc_quest_complete_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_questclick_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_auto_questclick_elite(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_fellow_check(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_check(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_lag(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_accept_0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_accept_1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_accept_2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_accept_3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_accept_4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_go(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_area(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		new_list = LYBIcarus.elite_quest_sub_dic[self.option_dic[option_name].get()]

		self.elite_quest_area_sub_combobox['values'] = new_list
		if not self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_area_sub') in new_list:
			self.elite_quest_area_sub_combobox.set(new_list[0])

	def callback_elite_quest_area_sub(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		new_list = LYBIcarus.elite_quest_dic[self.option_dic[option_name].get()]
		self.elite_quest_go_combobox['values'] = new_list
		# self.logger.warn("DEBUG1: " + self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go'))
		if not self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_go') in new_list:
			self.elite_quest_go_combobox.set(new_list[0])
		# if not self.elite_quest_go_combobox.get() in new_list:
		# 	self.elite_quest_go_combobox.set(new_list[0])

		for i in range(5):
			# self.logger.warn("DEBUG2: " + self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)))
			self.elite_quest_accept_combobox[i]['values'] = new_list
			if not self.get_game_config(lybconstant.LYB_DO_STRING_ICARUS_WORK + 'elite_quest_accept' + str(i)) in new_list:
				self.elite_quest_accept_combobox[i].set(new_list[0])
			# if not self.elite_quest_accept_combobox[i].get() in new_list:
			# 	self.elite_quest_accept_combobox[i].set( new_list[0])

	def callback_elite_quest_threshold(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_limit(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fellow_skill_cooltime(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_co_skill(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_cond_skill(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_elite_quest_duration(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_lag_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_sub(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_search_sub(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_local(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())





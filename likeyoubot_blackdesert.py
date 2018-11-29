import likeyoubot_game as lybgame
import likeyoubot_blackdesert_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBBlackDesert(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'메인 퀘스트',
		'자동 사냥',
		# '이야기',
		'우편함',
		'과제',
		'길드',

		'교감',
		'말 가방에 넣기',
		'말 가방 모두 꺼내기',
		'낚시',
		'투기장',
		'인사하기',
		'영지',
		'영지로 이동',
		'영지 나가기',
		'마을로 이동',
		'가축상점',
		'교본상점',
		'토벌 게시판',
		'이벤트 보상 수령',
		'캐릭터 변경',
		'캐릭터 이동',

		'도감',
		'기술 성장',
		'월드 보스',
		'흑정령 - 흑정령 의뢰',
		'흑정령 - 검은 기운',
		'흑정령 - 잠재력 돌파',
		'흑정령 - 수정 합성',
		'흑정령 - 광원석 합성',

		'반려동물 - 먹이주기',


		'미궁 개척',
		'미궁 목록',
		'마우스 클릭',
		'알림',

		'[반복 시작]',
		'[반복 종료]',

		'[작업 대기]',
		'[작업 예약]',
		'' ]

	nox_bd_icon_list = [
		'nox_bd_icon',		
		'nox_bd_icon2',
		'bd_icon3',
		]

	momo_bd_icon_list = [
		'momo_bd_icon',
		'momo_bd_icon2',
		'bd_icon3',
	]

	potion_list = [
		'소형',
		'중형',
		'대형'
		]

	box_range_list = [
		'좁게',
		'중간'
		]

	ddolmani_skill_list = [
		"흑정령의 분노:흡수",
		"흑정령의 분노I",
		"흑정령의 분노II"
	]

	sell_pummok_list = [
		"무기",
		"방어구",
		"장신구",
		"수정",
		"물약"

		]

	item_rank_list = [
		"낡은",
		"일반",
		"고급",
		"희귀",
		"유일",
		"전설",
		"신화"

		]
	item_rank_color_list = [
		"#7d7d86",
		"#000000",
		"#759460",
		"#4880b6",
		"#433e6f",
		"#d49e4a",
		"#de5f21"

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

	sujeong_rank_list = [
		'일반',
		'고급',
		'희귀',
		'유일',
		'전설']

	geomun_rank_list = [
		'낡은',
		'일반',
		'고급',
		'희귀',
		'유일',
		'전설',
		'신화',
		'심연',
		]

	chejip_list = [
		'야생 들풀',
		'저마',
		'목화 솜',
		'누에고치',
		'통나무',
		'연한 원목',
		'가벼운 원목',
		'탄력있는 원목',
		'거친 석재',
		'구리 광석',
		'철 광석',
		'주석 광석',
		'설정 안함'
	]

	chejip_place_list = [
		'1 지역',
		'2 지역',
		'3 지역',
		'4 지역'
	]

	jamjeryeok_dolpa_rank_list = [
		'하급',
		'중급',
		'상급',
		'최상급'
	]

	jamjeryeok_dolpa_rank_order_list = [
		'낮은',
		'높은'
	]

	npc_list = [
		'잡화상점',
		'가축상점',
		'씨앗상점',
		'교본상점',
		]

	migung_rank_op_list = [
		'＝',
		'≥'
		]

	tobeol_boss_list = [
		'빨간코',
		'기아스',
		'비겁한 베그',
		'알 룬디',
		'티티움',
		'머스칸',
		'오르그',
		'켈카스',
		'검은갈기',
		'사우닐 공성대장',
		'게아쿠',
		'쿠베',
		'우라카',
		'헥세마리',
		'카부아밀레스',
		'사형 집행관',
		'일레즈라의 하수인',
		'엘릭 제사장',
	]

	tobeol_rank_list = [
		'0',
		'1',
		'2',
		'3',
		'4',
		'5',
		'6',
		'7',
		'8',
		'9',
		'10'
	]

	muge_percentage_list = [
	'70', 
	'80', 
	'90', 
	'100', 
	'110', 
	'120', 
	'130', 
	'140', 
	'150'
	]



	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_BLACKDESERT, lybconstant.LYB_GAME_DATA_BLACKDESERT, window)

	def process(self, window_image):
		rc = super(LYBBlackDesert, self).process(window_image)
		if rc < 0:
			return rc

		return rc

	def custom_check(self, window_image, window_pixel):

		# 여기서 더 있다 갈래 설정 필요
		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
				self.window_image,
				self.resource_manager.pixel_box_dic['repeat_quest'],
				custom_flag=1,
				custom_rect=(240, 300, 280, 370)
				)

		if loc_x != -1:
			c_match_rate = self.rateMatchedResource(self.window_pixels, 'migung_success_scene')	
			if c_match_rate > 0.9:
				self.logger.warn('미궁 클리어')
				return ''

			c_match_rate = self.rateMatchedResource(self.window_pixels, 'migung_success_scene_repeat_confirm_event')	
			if c_match_rate > 0.9:
				self.logger.warn('미궁 다시하기')
				return ''

			is_repeat_quest = self.get_scene('main_scene').get_game_config(lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean')
			# 보정되지 않은 클릭을 하려면 이걸 써야 한다.

			# self.telegram_send('반복 의뢰 인식됨')
			# return -1
			if is_repeat_quest == True:
				self.logger.warn('반복 의뢰 계속하기: ' + str(match_rate))
				self.window.mouse_click(self.hwnd, loc_x, loc_y)
			else:
				(n_loc_x, n_loc_y), n_match_rate = self.locationOnWindowPart(
						self.window_image,
						self.resource_manager.pixel_box_dic['next_quest'],
						custom_flag=1,
						custom_rect=(240, 300, 280, 370)
						)
				if n_loc_x != -1:
					self.logger.warn('반복 의뢰 그만하기: ' + str(n_match_rate))
					self.window.mouse_click(self.hwnd, n_loc_x, n_loc_y)
				else:
					self.logger.debug('next_quest not found: ' + str(n_match_rate))
					self.window.mouse_click(self.hwnd, loc_x, loc_y)

			return 'repeat'

		# 마을에서 부활
		# (loc_x, loc_y), match_rate = self.locationOnWindowPart(
		# 		self.window_image,
		# 		self.resource_manager.pixel_box_dic['buhwal_in_town'],
		# 		custom_flag=1,
		# 		custom_threshold=0.9,
		# 		custom_rect=(350, 200, 400, 300)
		# 		)

		# if loc_x != -1:
		# 	self.logger.warn('마을에서 부활: ' + str(match_rate))
		# 	self.window.mouse_click(self.hwnd, loc_x, loc_y)
		# 	return 'buhwal_in_town'

		# 녹색 느낌표 인식
		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
				self.window_image,
				self.resource_manager.pixel_box_dic['green_quest'],
				custom_flag=1,
				custom_threshold=0.99,
				custom_rect=(240, 300, 280, 370)
				)

		if loc_x != -1:
			self.logger.warn('녹색 느낌표 퀘스트: ' + str(match_rate))
			self.window.mouse_click(self.hwnd, loc_x, loc_y)
			return 'green_quest'


		match_rate = self.rateMatchedResource(self.window_pixels, 'world_boss_success_scene')
		if match_rate > 0.9:
			return ''

		match_rate = self.rateMatchedPixelBox(self.window_pixels, "main_scene_moving", custom_top_level=255, custom_below_level=180)
		if match_rate > 0.9:
			return ''

		if not 'skip_event' in self.event_limit:
			self.event_limit['skip_event'] = time.time()

		# skip_limit = int(self.get_game_config(lybconstant.LYB_GAME_YEOLHYUL, lybconstant.LYB_DO_STRING_SKIP_PERIOD))
		skip_limit = 0

		if self.main_scene != None and self.main_scene.current_work != None:
			if self.main_scene.current_work == '토벌 게시판':
				match_rate = self.rateMatchedResource(self.window_pixels, 'tobeol_skip_loc', custom_below_level=200,custom_top_level=255)
				if match_rate > 0.99:
					self.logger.warn('동영상 건너뛰기')
					self.mouse_click('tobeol_skip')
					return 'skip'

			elif self.main_scene.current_work == '메인 퀘스트':
				(loc_x, loc_y), skip_match_rate	= self.locationResourceOnWindowPart(
											self.window_image,
											'npc_conversation_skip_loc',
											custom_threshold=0.9,
											custom_flag=1,
											custom_top_level=(255, 255, 255),
											custom_below_level=(130, 130, 130),
											custom_rect=(570, 100, 635, 130)
											)
				# self.logger.info('npc_conversation_skip_loc' + ' ' + str((loc_x, loc_y)) + ' ' + str(skip_match_rate))
				if loc_x != -1:
					if not 'npc_conversation_skip_loc' in self.event_limit:
						self.event_limit['npc_conversation_skip_loc'] = 0

					if time.time() - self.event_limit['npc_conversation_skip_loc'] > 5:
						self.main_scene.lyb_mouse_click_location(loc_x, loc_y)
						self.event_limit['npc_conversation_skip_loc'] = time.time()
						return 'skip'
					else:
						return ''

				(loc_x, loc_y), skip_match_rate	= self.locationResourceOnWindowPart(
											self.window_image,
											'tutorial_skip_loc',
											custom_threshold=0.9,
											custom_flag=1,
											custom_rect=(570, 60, 610, 100)
											)
				if loc_x != -1:
					if not 'tutorial_skip_loc' in self.event_limit:
						self.event_limit['tutorial_skip_loc'] = 0

					if time.time() - self.event_limit['tutorial_skip_loc'] > 10:
						self.main_scene.lyb_mouse_click_location(loc_x, loc_y)
						self.event_limit['tutorial_skip_loc'] = time.time()
						return 'skip'
					else:
						return ''

				(loc_x, loc_y), skip_match_rate	= self.locationResourceOnWindowPart(
											self.window_image,
											'tutorial_skip_loc',
											custom_threshold=0.9,
											custom_flag=1,
											custom_rect=(30, 60, 70, 100)
											)
				if loc_x != -1:
					if not 'tutorial_skip_loc' in self.event_limit:
						self.event_limit['tutorial_skip_loc'] = 0

					if time.time() - self.event_limit['tutorial_skip_loc'] > 10:
						self.main_scene.lyb_mouse_click_location(loc_x, loc_y)
						self.event_limit['tutorial_skip_loc'] = time.time()
						return 'skip'
					else:
						return ''

		if time.time() - self.event_limit['skip_event'] > skip_limit:
			self.event_limit['skip_event'] = time.time()
			skip_loc_list = [
				'bottom_right_skip_loc',
				'bottom_right_skip_2_loc',
				'top_right_skip_loc',

				]

			s = time.time()
			for each_loc in skip_loc_list:
				if not each_loc in self.event_limit:
					self.event_limit[each_loc] = time.time()
				else:			
					# 건너뛰기 30초 안에 발생하는 것만 해당
					if time.time() - self.event_limit[each_loc] > 30:
						self.set_option(each_loc + '_repeat', None)

				# self.event_limit[each_loc + '_count'] += 1

				# adjust_level = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_SKIP_LEVEL_ADJUST))
				# adjust_threshold = int(self.get_game_config(lybconstant.LYB_GAME_YEOLHYUL, lybconstant.LYB_DO_STRING_YH_THRESHOLD_NEXT)) * 0.01
				adjust_threshold = int(self.get_scene('main_scene').get_game_config(lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation')) * 0.01
				# print('[DEBUG] adjust_threshold=', adjust_threshold)
				# skip_match_rate = self.rateMatchedResource(
				# 						window_pixel, 
				# 						each_loc,
				# 						custom_below_level=adjust_level
				# 									)


				if each_loc == 'top_right_skip_loc':
					each_rect = (500, 115, 535, 145)
				elif each_loc == 'bottom_right_skip_loc':
					each_rect = (580, 350, 610, 385)
				elif each_loc == 'bottom_right_skip_2_loc':
					each_rect = (380, 290, 535, 315)

				(loc_x, loc_y), skip_match_rate	= self.locationResourceOnWindowPart(
											self.window_image,
											each_loc,
											# custom_below_level=(100, 100, 100),
											# custom_top_level=(255, 255, 255),
											custom_threshold=adjust_threshold,
											custom_flag=1,
											custom_rect=each_rect
											)

				# self.logger.debug(str(skip_match_rate) + ':' + str(adjust_threshold))
				if loc_x != -1:
					self.event_limit[each_loc] = time.time()

					if each_loc != 'bottom_right_skip_loc':
						self.logger.debug('skip: ' + str(each_loc) + ':' + str((loc_x, loc_y)) +'  '+ str(int(skip_match_rate * 100)) + '%')
						if self.get_option(each_loc + '_repeat') == None:
							self.set_option(each_loc + '_repeat', (loc_x, loc_y))
							return ''
						
						(last_loc_x, last_loc_y) = self.get_option(each_loc + '_repeat')
						if last_loc_x == loc_x and last_loc_y == loc_y:
							self.set_option(each_loc + '_repeat', None)
							return ''

					self.logger.debug('Clicked SKIP: ' + str(each_loc) + ':' + str((loc_x, loc_y)) +'  '+ str(int(skip_match_rate * 100)) + '%')
					self.set_option(each_loc + '_repeat', None)
					self.mouse_click(each_loc.replace('_loc', '', 1) + '_0')

					return 'skip'
				else:
					self.set_option(each_loc + '_repeat', None)
					pass
					# print('SKIP:', each_loc + ':' + str((loc_x, loc_y)) +'  '+ str(int(skip_match_rate * 100)) + '%')

			e = time.time()
			# self.logger.debug('ElapsedTime SKIP: ' + str(round(e - s, 2)))

		resource_name = 'download_patch_loc'
		(loc_x, loc_y), match_rate	= self.locationResourceOnWindowPart(
									self.window_image,
									resource_name,
									custom_threshold=0.9,
									custom_flag=1,
									custom_rect=(230, 120, 400, 180)									
									)
		if loc_x != -1:
			pb_name = 'download_patch_ok'
			(loc_x, loc_y), match_rate = self.locationOnWindowPart(
					self.window_image,
					self.resource_manager.pixel_box_dic[pb_name],
					custom_flag=1,
					custom_threshold=0.9,
					custom_rect=(320, 250, 420, 320)
					)
			if loc_x != -1:
				self.logger.warn('패치 다운로드: ' + str(match_rate))
				self.window.mouse_click(self.hwnd, loc_x, loc_y)
				return resource_name



		return ''

	def process_terminate_applications(self):


		max_app_close_count = self.common_config[lybconstant.LYB_DO_STRING_CLOSE_APP_COUNT]
		self.logger.debug('CloseMaxCount: ' + str(max_app_close_count))
		if self.player_type == 'nox':
			if self.terminate_status == 0:
				# self.mouse_click_with_cursor(660, 350)
				if self.side_hwnd == None:
					self.logger.warn('녹스 사이드바 검색이 안되었기 때문에 종료 기능은 사용하지 못합니다.')
					self.request_terminate = False
					return
				self.window.mouse_click(self.side_hwnd, 16, 320)
				self.terminate_status += 1
			elif self.terminate_status > 0 and self.terminate_status < max_app_close_count:
				self.logger.info('녹스 앱들을 종료 중입니다.')
				self.window.mouse_drag(self.hwnd, 320, 270, 0, 270, 0.5)
				# self.window.mouse_click(self.hwnd, 630, 220, delay=2)
				# time.sleep(2)
				# self.window.mouse_click(self.hwnd, 550, 245)
				self.terminate_status += 1
			else:
				self.terminate_status = 0
				self.request_terminate = False
		elif  self.player_type == 'momo':
			if self.terminate_status == 0:
				self.window.mouse_click(self.parent_hwnd, 660, 355)
				# self.move_mouse_location(660, 355)
				self.terminate_status += 1
			elif self.terminate_status > 0 and self.terminate_status < max_app_close_count:
				self.logger.info('모모 앱들을 종료 중입니다.')
				self.window.mouse_drag(self.hwnd, 320, 270, 0, 270, 0.5)
				self.terminate_status += 1
			else:
				self.terminate_status = 0
				self.request_terminate = False	

	def get_screen_by_location(self, window_image):
		
		scene_name = self.scene_tutorial_gisul_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_init_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		# 순서 중요 !!
		# scene_name = self.scene_event_and_reward_screen(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		# 순서 중요 !!
		# scene_name = self.scene_immu_start_screen(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		# scene_name = self.scene_main_screen(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		scene_name = self.scene_death_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_urewanryo_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		# scene_name = self.scene_geomungiun_screen(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		scene_name = self.scene_jamjeryeok_jeonsu_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_nejeongbo_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_select_ure_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		# scene_name = self.scene_hukjeongryoung_soksakim_screen(window_image)
		# if len(scene_name) > 0:
		# 	return scene_name

		# return ''

		scene_name = self.scene_google_play_account_select(window_image)
		if len(scene_name) > 0:
			return scene_name

		scene_name = self.scene_jihwiso(window_image)
		if len(scene_name) > 0:
			return scene_name

		return ''

	# def scene_hukjeongryoung_soksakim_screen(self, window_image):
	# 	match_rate = self.rateMatchedResource(self.window_pixels, 
	# 		'hukjeongryoung_soksakim_scene_loc', 
	# 		custom_below_level=(150, 150, 150),
	# 		custom_top_level=(255, 255, 255),
	# 		custom_tolerance=50)	

	# 	if match_rate > 0.7:
	# 		self.logger.info('hukjeongryoung_soksakim_scene: ' + str(match_rate))
	# 		return 'hukjeongryoung_soksakim_scene'

	# 	return ''

	def scene_jihwiso(self, window_image):
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'jihwiso_scene_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(450, 40, 540, 80)
							)

		if match_rate > 0.7:
			self.logger.info('jihwiso_scene_loc: ' + str(match_rate))
			return 'jihwiso_scene'

		return ''

	def scene_tutorial_gisul_screen(self, window_image):
		match_rate = self.rateMatchedResource(self.window_pixels, 'tutorial_gisul_loc', custom_tolerance=50)	


		if match_rate > 0.7:
			self.logger.info('tutorial_gisul_scene: ' + str(match_rate))
			return 'tutorial_gisul_scene'

		return ''

	def scene_select_ure_screen(self, window_image):
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'select_ure_scene_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(280, 50, 370, 150)
							)

		if match_rate > 0.7:
			self.logger.info('select_ure_scene: ' + str(match_rate))
			return 'select_ure_scene'

		return ''

	def scene_nejeongbo_screen(self, window_image):
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'nejeongbo_scene_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(50, 35, 115, 60)
							)

		if match_rate > 0.7:
			self.logger.info('nejeongbo_scene: ' + str(match_rate))
			self.current_matched_scene['name'] = 'nejeongbo_scene_loc'
			match_rate = self.rateMatchedResource(self.window_pixels, self.current_matched_scene['name'], weight_tolerance=self.weight_tolerance)	
			self.current_matched_scene['rate'] = int(match_rate * 100)
			return 'nejeongbo_scene'

		return ''

	def scene_jamjeryeok_jeonsu_screen(self, window_image):
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'jamjeryeok_jeonsu_scene_loc',
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(50, 35, 115, 60)
							)

		if match_rate > 0.7:
			self.logger.info('jamjeryeok_jeonsu_scene: ' + str(match_rate))
			self.current_matched_scene['name'] = 'jamjeryeok_jeonsu_scene_loc'
			match_rate = self.rateMatchedResource(self.window_pixels, self.current_matched_scene['name'], weight_tolerance=self.weight_tolerance)	
			self.current_matched_scene['rate'] = int(match_rate * 100)
			return 'jamjeryeok_jeonsu_scene'

		return ''

	# def scene_geomungiun_screen(self, window_image):
	# 	(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
	# 						self.window_image,
	# 						'geomungiun_scene_loc',
	# 						custom_threshold=0.7,
	# 						custom_flag=1,
	# 						custom_rect=(50, 35, 115, 60)
	# 						)

	# 	if match_rate > 0.7:
	# 		self.logger.info('geomungiun_scene: ' + str(match_rate))
	# 		return 'geomungiun_scene'

	# 	return ''

	def scene_death_screen(self, window_image):
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'death_scene_loc',
							# custom_below_level=(130, 70, 60),
							# custom_top_level=(230, 120, 90),
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(250, 170, 380, 200)
							)

		if match_rate > 0.7:
			self.logger.info('death_scene: ' + str(match_rate))
			return 'death_scene'

		return ''

	# def scene_immu_start_screen(self, window_image):
	# 	(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
	# 						self.window_image,
	# 						'immu_start_scene_loc',
	# 						# custom_below_level=(200, 200, 200),
	# 						# custom_top_level=(255,255,255),
	# 						custom_threshold=0.7,
	# 						custom_flag=1,
	# 						custom_rect=(220, 120, 420, 145)
	# 						)

	# 	if match_rate > 0.7:
	# 		self.logger.info('immu_start_scene: ' + str(match_rate))
	# 		return 'immu_start_scene'

	# 	return ''

	# def scene_event_and_reward_screen(self, window_image):
	# 	(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
	# 						self.window_image,
	# 						'event_and_reward_scene_loc',
	# 						# custom_below_level=(200, 200, 200),
	# 						# custom_top_level=(255,255,255),
	# 						custom_threshold=0.7,
	# 						custom_flag=1,
	# 						custom_rect=(260, 70, 380, 100)
	# 						)

	# 	if match_rate > 0.7:
	# 		self.logger.info('event_and_reward_scene: ' + str(match_rate))
	# 		return 'event_and_reward_scene'

	# 	return ''

	def scene_urewanryo_screen(self, window_image):
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'urewanryo_scene_loc',
							# custom_below_level=(200, 200, 200),
							# custom_top_level=(255,255,255),
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(270, 100, 320, 200)
							)

		if match_rate > 0.7:
			self.logger.info('urewanryo_scene: ' + str(match_rate))
			return 'urewanryo_scene'

		return ''

	def scene_main_screen(self, window_image):
		s = time.time()
		(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
							self.window_image,
							'main_scene_loc',
							# custom_below_level=(200, 200, 200),
							# custom_top_level=(255,255,255),
							custom_threshold=0.7,
							custom_flag=1,
							custom_rect=(430, 30, 635, 60)
							)


		e = time.time()
		self.logger.debug('ElapsedTime main_scene_loc: ' + str(round(e - s, 5)))

		if match_rate > 0.7:
			self.logger.debug('main scene: ' + str(match_rate))
			self.current_matched_scene['name'] = 'main_scene_loc'
			match_rate = self.rateMatchedResource(self.window_pixels, self.current_matched_scene['name'], weight_tolerance=self.weight_tolerance)	
			self.current_matched_scene['rate'] = int(match_rate * 100)
			return 'main_scene'

		return ''
	
	def scene_init_screen(self, window_image):

		loc_x = -1
		loc_y = -1

		if self.player_type == 'nox':
			for each_icon in LYBBlackDesert.nox_bd_icon_list:
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
			for each_icon in LYBBlackDesert.momo_bd_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(30, 40, 610, 300)
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

		pb_name = 'google_play_letter'
		(loc_x, loc_y), match_rate = self.locationOnWindowPart(
				window_image,
				self.resource_manager.pixel_box_dic[pb_name],
				custom_flag=1,
				custom_rect=(150, 50, 490, 270)
				)
		# self.logger.warn(str((loc_x, loc_y)) + ':' + str(match_rate))
		# self.getImagePixelBox(pb_name).save(pb_name + '.png')

		loc_x_list.append(loc_x)
		loc_y_list.append(loc_y)

		for i in range(6):

			pb_name = 'google_play_letter_' + str(i)
			(loc_x, loc_y), match_rate = self.locationOnWindowPart(
					window_image,
					self.resource_manager.pixel_box_dic[pb_name],
					custom_flag=1,
					custom_rect=(150, 50, 490, 270)
					)

			# self.logger.warn(str((loc_x, loc_y)) + ':' + str(match_rate))
			# self.getImagePixelBox(pb_name).save(pb_name + '.png')

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
		self.scene_dic[scene_name] = lybscene.LYBBlackDesertScene(scene_name)
		self.scene_dic[scene_name].setLoggingQueue(self.logging_queue)
		self.scene_dic[scene_name].setGameObject(self)

class LYBBlackDesertTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_BLACKDESERT):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		lybgame.LYBGameTab.set_work_list(self)

		for each_work in LYBBlackDesert.work_list:
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


		self.inner_frame_dic['hunt_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['hunt2_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['work_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['work2_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['tobeol_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['notify_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note'], 
			relief 				= self.frame_relief
			)

		self.inner_frame_dic['common_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['common_tab_frame'], text='일반')

		self.inner_frame_dic['hunt_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['hunt_tab_frame'], text='자동 사냥')

		self.inner_frame_dic['hunt2_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['hunt2_tab_frame'], text='자동 사냥2')

		self.inner_frame_dic['work_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['work_tab_frame'], text='작업별 설정')

		self.inner_frame_dic['work2_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['work2_tab_frame'], text='작업별 설정2')

		self.inner_frame_dic['tobeol_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['tobeol_tab_frame'], text='토벌 게시판')

		self.inner_frame_dic['notify_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['notify_tab_frame'], text='알림')


















































		frame_head = ttk.Frame(self.inner_frame_dic['common_tab_frame'])

		frame_left = ttk.Frame(frame_head)
		frame_label = ttk.LabelFrame(frame_left, text='인식 허용률(%)')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("메인퀘스트 관련 이미지")
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest'].trace(
			'w', lambda *args: self.callback_threshold_mainquest_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest'] = 70

		combobox_list = []
		for i in range(50, 91):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'main_quest'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("대화 건너뛰기 이미지")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation'].trace(
			'w', lambda *args: self.callback_threshold_conversation_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation'] = 85

		combobox_list = []
		for i in range(50, 91):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'conversation'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("전흔, 채광, 채집, 벌목 이미지")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box'].trace(
			'w', lambda *args: self.callback_threshold_combat_box_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box'] = 70

		combobox_list = []
		for i in range(50, 91):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'combat_box'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_left, text='상태 체크(회)')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("자동 태세 전 수동 체크 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit'].trace(
			'w', lambda *args: self.callback_threshold_sudong_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit'] = 3

		combobox_list = []
		for i in range(2, 100):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'sudong_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("미궁 감지 체크 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit'].trace(
			'w', lambda *args: self.callback_threshold_migung_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit'] = 10

		combobox_list = []
		for i in range(5, 31):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'migung_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)
		
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("이동 중 체크 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit'].trace(
			'w', lambda *args: self.callback_threshold_moving_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit'] = 200

		combobox_list = []
		for i in range(0, 1001, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'moving_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)
	
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("물약 없음 체크 횟수")
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit'].trace(
			'w', lambda *args: self.callback_threshold_potion_empty_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit')
			)

		if not lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit'] = 30

		combobox_list = []
		for i in range(0, 1001, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_THRESHOLD + 'potion_empty_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_left.pack(side=tkinter.LEFT, anchor=tkinter.NW)




		frame_label = ttk.LabelFrame(frame_head, text='반복 주기(초)')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("무반응시 메인 퀘스트 클릭 주기")
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk'].trace(
			'w', lambda *args: self.callback_period_mainquest_afk_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk'] = 120

		combobox_list = []
		for i in range(5, 240, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest_afk'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("자동 사냥 랙 방지 움직임 주기")
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag'].trace(
			'w', lambda *args: self.callback_period_jadong_lag_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag'] = 0

		combobox_list = []
		for i in range(0, 1201, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'jadong_lag'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("토벌/미궁 랙 방지 움직임 주기")
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'].trace(
			'w', lambda *args: self.callback_period_migung_lag_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'] = 30

		combobox_list = []
		for i in range(0, 1201, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'migung_lag'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_head, text='대기 시간(초)')

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 클릭 후 다음 클릭까지")
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'].trace(
			'w', lambda *args: self.callback_period_mainquest_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'] = 120

		combobox_list = []
		for i in range(5, 30000, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'main_quest'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 클릭 후 수동 스킬 사용")
			)
		label.pack(side=tkinter.LEFT)
		self.tooltip(label, lybconstant.LYB_WAIT_ATTACK)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack'].trace(
			'w', lambda *args: self.callback_period_wait_attack_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack'] = 30

		combobox_list = []
		for i in range(5, 240, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_attack'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("퀘스트 클릭 후 자동 태세 전환")
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong'].trace(
			'w', lambda *args: self.callback_period_wait_jadong_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong'] = 10

		combobox_list = []
		for i in range(5, 300, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'wait_jadong'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("가방 경고 인식 후 클릭 대기")

			)
		label.pack(side=tkinter.LEFT)
		self.tooltip(label, lybconstant.LYB_TOOLTIP_GABANG_FULL)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full'].trace(
			'w', lambda *args: self.callback_period_gabang_full_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full'] = 30

		combobox_list = []
		for i in range(0, 86401, 60):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'gabang_full'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("절전 모드 경고 인식 후 대기")

			)
		label.pack(side=tkinter.LEFT)
		self.tooltip(label, lybconstant.LYB_TOOLTIP_GABANG_FULL)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning'].trace(
			'w', lambda *args: self.callback_period_jeoljeon_mode_warning_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning'] = 1800

		combobox_list = []
		for i in range(0, 86401, 60):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'jeoljeon_mode_warning'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("물약 상점 인식 지연 시간")
			)
		label.pack(side=tkinter.LEFT)
		self.tooltip(label, lybconstant.LYB_TOOTLIP_POTION_SHOP)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop'].trace(
			'w', lambda *args: self.callback_period_potion_shop_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop'] = 300

		combobox_list = []
		for i in range(5, 600, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'potion_shop'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= self.get_option_text("월드 보스 이동 시간")
			)
		label.pack(side=tkinter.LEFT)
		self.tooltip(label, lybconstant.LYB_TOOTLIP_POTION_SHOP)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss'].trace(
			'w', lambda *args: self.callback_period_world_boss_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss')
			)

		if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss'] = 90

		combobox_list = []
		for i in range(10, 301, 5):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'world_boss'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.W)


		# frame = ttk.Frame(frame_label)
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= self.get_option_text("반복 퀘스트 완료 대기(랜덤)")
		# 	)
		# label.pack(side=tkinter.LEFT)
		# self.tooltip(label, lybconstant.LYB_TOOTLIP_POTION_SHOP)

		# self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random'] = tkinter.StringVar(frame)
		# self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random'].trace(
		# 	'w', lambda *args: self.callback_period_reqeat_quest_random_stringvar(args, lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random')
		# 	)

		# if not lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random' in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random'] = 10

		# combobox_list = []
		# for i in range(0, 1000):
		# 	combobox_list.append(str(i))

		# combobox = ttk.Combobox(
		# 	master 				= frame,
		# 	values				= combobox_list, 
		# 	textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random'], 
		# 	state 				= "readonly",
		# 	height				= 10,
		# 	width 				= 5,
		# 	font 				= lybconstant.LYB_FONT 
		# 	)
		# combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PERIOD + 'reqeat_quest_random'])
		# combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		# frame.pack(anchor=tkinter.W)


		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_head.pack(anchor=tkinter.W)































		frame_head = ttk.Frame(self.inner_frame_dic['hunt_tab_frame'])

		frame_label = ttk.LabelFrame(frame_head, text='설정')

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean'].trace(
			'w', lambda *args: self.callback_quest_repeat_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '반복 의뢰를 수락합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'quest_repeat_boolean'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= '    '
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target'].trace(
			'w', lambda *args: self.callback_fix_target_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '타겟 고정을 해제합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'fix_target'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= '    '
			)
		label.pack(side=tkinter.LEFT)



		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean'].trace(
			'w', lambda *args: self.callback_migung_invite_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '미궁 초대 자동 수락', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_boolean'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)


		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op'].trace(
			'w', lambda *args: self.callback_migung_invite_rank_op_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op')
			)
		combobox_list = LYBBlackDesert.migung_rank_op_list

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op'] = combobox_list[1]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank_op'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'].trace(
			'w', lambda *args: self.callback_migung_invite_rank_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank')
			)
		combobox_list = []
		for i in range(1, 9):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'] = 4

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= '단계, ≤'
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2'].trace(
			'w', lambda *args: self.callback_migung_invite_rank2_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2')
			)
		combobox_list = []
		for i in range(1, 9):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2'] = 6


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'migung_invite_rank2'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= '단계'
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'period'].trace(
			'w', lambda *args: self.callback_hunt_period_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'period')
			)
		combobox_list = []
		for i in range(60, 100000, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'period'] = 3600


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 동안 자동 사냥 진행 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period'].trace(
			'w', lambda *args: self.callback_hunt_pet_period_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period')
			)
		combobox_list = []
		for i in range(0, 3601, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period'] = 3600


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'pet_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "초마다 반려 동물 체크"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence'].trace(
			'w', lambda *args: self.callback_complete_sequence_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '퀘스트 완료 무작위 대기 후 클릭(', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_sequence'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "최대"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'].trace(
			'w', lambda *args: self.callback_complete_period_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period')
			)
		combobox_list = []
		for i in range(1, 61):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'] = 2


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'complete_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "초)"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box'].trace(
			'w', lambda *args: self.callback_loot_box_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '전투의 흔적(탐색 시간 0.5초)', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_box'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "▶ 인식 범위:"
			)
		label.pack(side=tkinter.LEFT)

		self.tooltip(label, lybconstant.LYB_TOOLTIP_COMBAT_BOX_RANGE)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range'].trace(
			'w', lambda *args: self.callback_box_range_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range')
			)
		combobox_list = LYBBlackDesert.box_range_list

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range'] = combobox_list[1]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'box_range'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= " "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang'].trace(
			'w', lambda *args: self.callback_loot_chegwang_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '채광', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chegwang'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip'].trace(
			'w', lambda *args: self.callback_loot_chejip_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '채집', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_chejip'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok'].trace(
			'w', lambda *args: self.callback_loot_beolmok_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '벌목', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'loot_beolmok'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		# frame.pack(anchor=tkinter.W, side=tkinter.LEFT)

		# frame = ttk.Frame(frame_label)
		# frame.pack(anchor=tkinter.W, padx=5, side=tkinter.LEFT)

		# frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode'].trace(
			'w', lambda *args: self.callback_jeoljeon_mode_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '절전 모드', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'jeoljeon_mode'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		s = ttk.Style()
		s.configure('red_label.TLabel', foreground='red')
		label = ttk.Label(
			master 				= frame, 
			text 				= "무게 경고가 ",
			style 				= 'red_label.TLabel'
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage'].trace(
			'w', lambda *args: self.callback_muge_percentage_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage'] = 70

		combobox_list = LYBBlackDesert.muge_percentage_list

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'muge_percentage'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이상일 경우 마을 가기",
			style 				= 'red_label.TLabel'
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete'].trace(
			'w', lambda *args: self.callback_search_complete_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '퀘스트 완료 위아래로 탐색하기', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'search_complete'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_head, text='물약 구매')

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean'].trace(
			'w', lambda *args: self.callback_potion_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '물약 구매하기', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_boolean'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "횟수:"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set'].trace(
			'w', lambda *args: self.callback_potion_set_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set'] = 10

		combobox_list = [10, 50, 100]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_set'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "개씩"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number'].trace(
			'w', lambda *args: self.callback_potion_number_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number'] = 10

		combobox_list = []
		for i in range(1, 100):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "회"
			)
		label.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "물약 종류:"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing'].trace(
			'w', lambda *args: self.callback_potion_thing_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing')
			)
		combobox_list = LYBBlackDesert.potion_list

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing'] = combobox_list[1]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_thing'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= " "
			)
		label.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "무게가 "
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'].trace(
			'w', lambda *args: self.callback_potion_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'] = 70

		combobox_list = []
		for i in range(1, 100):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'potion_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이상이면 구매 중지"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_head, text='일괄 판매')

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean'].trace(
			'w', lambda *args: self.callback_sell_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '일괄 판매 하기', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_boolean'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "품목분류: "
			)
		label.pack(side=tkinter.LEFT)

		i = 0
		for each_pummok in LYBBlackDesert.sell_pummok_list:
			
			self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i)] = tkinter.BooleanVar(frame)

			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '0'].trace(
					'w', lambda *args: self.callback_sell_pummok_0_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '1'].trace(
					'w', lambda *args: self.callback_sell_pummok_1_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '2'].trace(
					'w', lambda *args: self.callback_sell_pummok_2_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '2')
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '3'].trace(
					'w', lambda *args: self.callback_sell_pummok_3_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '4'].trace(
					'w', lambda *args: self.callback_sell_pummok_4_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + '4')
					)

			if not lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i)] = False

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= self.get_item_rank_text(each_pummok), 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_pummok' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "등급분류: "
			)
		label.pack(side=tkinter.LEFT)

		i = 0
		for each_rank in LYBBlackDesert.item_rank_list:
			
			self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i)] = tkinter.BooleanVar(frame)

			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '0'].trace(
					'w', lambda *args: self.callback_sell_item_rank_0_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '1'].trace(
					'w', lambda *args: self.callback_sell_item_rank_1_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '2'].trace(
					'w', lambda *args: self.callback_sell_item_rank_2_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '2')
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '3'].trace(
					'w', lambda *args: self.callback_sell_item_rank_3_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '4'].trace(
					'w', lambda *args: self.callback_sell_item_rank_4_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '4')
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '5'].trace(
					'w', lambda *args: self.callback_sell_item_rank_5_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '5')
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '6'].trace(
					'w', lambda *args: self.callback_sell_item_rank_6_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + '6')
					)

			if not lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i)] = False

			s = ttk.Style()
			s.configure(each_rank + '.TCheckbutton', foreground=LYBBlackDesert.item_rank_color_list[i])
			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= self.get_item_rank_text(each_rank), 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'item_rank' + str(i)],
				style 				= each_rank + '.TCheckbutton',
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
			i += 1

		frame.pack(anchor=tkinter.W)
		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek'] = tkinter.BooleanVar(frame)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek'].trace(
			'w', lambda *args: self.callback_sell_jamjeryoek_booleanvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek'] = False

		s = ttk.Style()
		s.configure('sell_jamjeryoek.TCheckbutton', foreground='#0367db')
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '잠재력 돌파, 수정 장착된 장비 포함', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'sell_jamjeryoek'],
			style 				= 'sell_jamjeryoek.TCheckbutton',
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)



		frame_head.pack(anchor=tkinter.W)















































		# +-----------------------------------------+
		# |											|
		# | 				자동 사냥2				|
		# |											|
		# +-----------------------------------------+



		frame_head = ttk.Frame(self.inner_frame_dic['hunt2_tab_frame'])
		frame_row = ttk.Frame(frame_head)


		frame_label = ttk.LabelFrame(frame_row, text='자동 사냥 시작 행동 설정')



		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'].trace(
			'w', lambda *args: self.callback_hunt_quest_click_stringvar(args, lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click')
			)

		if not lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'] = 0

		frame = ttk.Frame(frame_label)

		select_quest_location_list = [

			('아무 행동도 하지 않기', 0),
			('퀘스트 슬롯 1 번 클릭', 1),
			('퀘스트 슬롯 2 번 클릭', 2),
			('퀘스트 슬롯 3 번 클릭', 3),
			('퀘스트 슬롯 4 번 클릭', 4),
			]

		for text, mode in select_quest_location_list:

			combo_box = ttk.Radiobutton(
				master 				= frame,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'],
				value 				= mode

				)
			combo_box.pack()

		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame = ttk.Frame(frame_label)
		
		select_quest_location_list = [

			('1 번 위치로 자동 이동', 5),
			('2 번 위치로 자동 이동', 6),
			('3 번 위치로 자동 이동', 7),
			]

		for text, mode in select_quest_location_list:

			combo_box = ttk.Radiobutton(
				master 				= frame,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_HUNT + 'quest_click'],
				value 				= mode

				)
			combo_box.pack()

		frame.pack(anchor=tkinter.W)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_row, text='흑정령 스킬')


		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean'].trace(
			'w', lambda *args: self.callback_jadong_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean')
			)

		if not lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '흑정령 스킬을 사용합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + 'use_boolean'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		for i in range(len(LYBBlackDesert.ddolmani_skill_list)):
			frame = ttk.Frame(frame_label)

			skill_name = "%s" % self.preformat_cjk(LYBBlackDesert.ddolmani_skill_list[i], 18)
			label = ttk.Label(
				master 				= frame, 
				text 				= skill_name + ':'
				)
			label.pack(side=tkinter.LEFT)

			self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)] = tkinter.StringVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)].trace(
					'w', lambda *args: self.callback_ddolmani_skill_0_stringvar(args, lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(0))
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)].trace(
					'w', lambda *args: self.callback_ddolmani_skill_1_stringvar(args, lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(1))
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)].trace(
					'w', lambda *args: self.callback_ddolmani_skill_2_stringvar(args, lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(2))
					)

			combobox_list = []
			for j in range(0, 300, 5):
				combobox_list.append(str(j))

			if not lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)] = 90


			combobox = ttk.Combobox(
				master 				= frame,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)], 
				state 				= "readonly",
				height				= 10,
				width 				= 3,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_DDOLMANI_SKILL + str(i)])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
			label = ttk.Label(
				master 				= frame, 
				text 				= "초"
				)
			label.pack(side=tkinter.LEFT)
			frame.pack(anchor=tkinter.W)

		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)


		frame_row.pack(anchor=tkinter.NW)

		frame_head.pack(anchor=tkinter.W)






























		# +-----------------------------------------+
		# |											|
		# | 				작업 설정				|
		# |											|
		# +-----------------------------------------+
		
		frame_head = ttk.Frame(self.inner_frame_dic['work_tab_frame'])

		frame_row = ttk.Frame(frame_head)
		frame_label = ttk.LabelFrame(frame_row, text='메인 퀘스트')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jadong_boolean'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jadong_boolean'].trace(
			'w', lambda *args: self.callback_jadong_boolean_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'jadong_boolean')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'jadong_boolean' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'jadong_boolean'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '메인 퀘스트 진행 중에 전투 태세를 [자동]으로 강제 유지합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jadong_boolean'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_row, text='캐릭터 변경')
		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "접속 캐릭터 슬롯 번호(맨 위가 1번):"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change'].trace(
			'w', lambda *args: self.callback_chracter_change_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change')
			)
		combobox_list = []
		for i in range(1, 8):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change'] = 1

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'chracter_change'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "번"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_row.pack(anchor=tkinter.W)

		frame_row = ttk.Frame(frame_head)
		frame_label = ttk.LabelFrame(frame_row, text='마우스 클릭')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "X 좌표:"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'].trace(
			'w', lambda *args: self.callback_location_x_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'location_x')
			)
		combobox_list = []
		for i in range(1, 640):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'location_x' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'] = 320


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'location_x'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= " "
			)
		label.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "Y 좌표:"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'].trace(
			'w', lambda *args: self.callback_location_y_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'location_y')
			)
		combobox_list = []
		for i in range(1, 360):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'location_y' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'] = 100


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'location_y'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= " "
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_row, text='캐릭터 이동')
		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "방향: "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'character_move'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'character_move'].trace(
			'w', lambda *args: self.callback_character_move_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'character_move')
			)
		combobox_list = LYBBlackDesert.character_move_list

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'character_move' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'character_move'] = combobox_list[0]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'character_move'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'character_move'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= " "
			)
		label.pack(side=tkinter.LEFT)	
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "이동 시간: "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'].trace(
			'w', lambda *args: self.callback_character_move_time_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time')
			)

		combobox_list = []
		for i in range(0, 361):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'] = 0


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'], 
			state 				= "readonly",
			height				= 10,
			width 				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'character_move_time'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "초"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_row, text='반려동물 - 먹이주기')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "현재 보유 중인 펫의 수: "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_PET + 'number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_PET + 'number'].trace(
			'w', lambda *args: self.callback_pet_number_stringvar(args, lybconstant.LYB_DO_STRING_BD_PET + 'number')
			)
		combobox_list = []
		for i in range(1, 21):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_PET + 'number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PET + 'number'] = 1


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_PET + 'number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_PET + 'number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		frame.pack(anchor=tkinter.W)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_row.pack(anchor=tkinter.W)
			

		frame_row = ttk.Frame(frame_head)


		frame_label = ttk.LabelFrame(frame_row, text='흑정령 - 검은 기운')
		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "무기/방어구는 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun'].trace(
			'w', lambda *args: self.callback_geomungiun_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun')
			)
		combobox_list = LYBBlackDesert.geomun_rank_list

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun'] = combobox_list[0]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "등급 이하, 장신구는 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2'].trace(
			'w', lambda *args: self.callback_geomungiun2_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2'] = combobox_list[0]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'geomungiun2'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "등급 이하 자동 선택"
			)
		label.pack(side=tkinter.LEFT)	
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_row, text='흑정령 - 수정 합성')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong'].trace(
			'w', lambda *args: self.callback_sujeong_hapseong_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong')
			)
		combobox_list = LYBBlackDesert.sujeong_rank_list

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong'] = combobox_list[0]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "등급 이하"
			)
		label.pack(side=tkinter.LEFT)	

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto'].trace(
			'w', lambda *args: self.callback_sujeong_hapseong_auto_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '자동', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'sujeong_hapseong_auto'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=5, pady=5)


		frame_label = ttk.LabelFrame(frame_row, text='흑정령 - 광원석 합성')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong'].trace(
			'w', lambda *args: self.callback_gwangwonseok_hapseong_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong')
			)
		combobox_list = LYBBlackDesert.sujeong_rank_list

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong'] = combobox_list[0]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "등급 이하"
			)
		label.pack(side=tkinter.LEFT)	

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto'].trace(
			'w', lambda *args: self.callback_gwangwonseok_hapseong_auto_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '자동', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'gwangwonseok_hapseong_auto'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_row.pack(anchor=tkinter.W)

		frame_row = ttk.Frame(frame_head)
		frame_label = ttk.LabelFrame(frame_row, text='흑정령 - 잠재력 돌파')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank'].trace(
			'w', lambda *args: self.callback_jamjeryeok_dolpa_rank_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank')
			)
		combobox_list = LYBBlackDesert.jamjeryeok_dolpa_rank_list

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank'] = combobox_list[1]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 6,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "등급 이하 "
			)
		label.pack(side=tkinter.LEFT)	

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order'].trace(
			'w', lambda *args: self.callback_jamjeryeok_dolpa_rank_order_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order')
			)
		combobox_list = LYBBlackDesert.jamjeryeok_dolpa_rank_order_list

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order'] = combobox_list[1]


		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order'], 
			# justify 			= tkinter.CENTER,
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'jamjeryeok_dolpa_rank_order'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "등급부터 사용"
			)
		label.pack(side=tkinter.LEFT)	
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)
		frame_row.pack(anchor=tkinter.W)

		frame_row = ttk.Frame(frame_head)
		frame_label = ttk.LabelFrame(frame_row, text='토벌 게시판')
		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "토벌 임무 준비할 때 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number'].trace(
			'w', lambda *args: self.callback_tobeol_degrade_number_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number'] = 0

		combobox_list = []
		for i in range(0, 11):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'tobeol_degrade_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "단계 낮춰서 시작합니다"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_row, text='투기장')
		frame = ttk.Frame(frame_label)	
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'].trace(
			'w', lambda *args: self.callback_daejeon_count_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count')
			)
		combobox_list = []
		for i in range(1, 1001):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'] = 10

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "회 진행하고 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match'].trace(
			'w', lambda *args: self.callback_daejeon_match_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match')
			)
		combobox_list = []
		for i in range(0, 60, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match'] = 30

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match'], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_match'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 후 매칭 취소하고 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'].trace(
			'w', lambda *args: self.callback_daejeon_giveup_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup')
			)
		combobox_list = []
		for i in range(0, 601, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'], 
			state 				= "readonly",
			height				= 10,
			width 				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'daejeon_giveup'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
	
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 후 항복"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_row.pack(anchor=tkinter.W)


		frame_row = ttk.Frame(frame_head)

		frame_label = ttk.LabelFrame(frame_row, text='영지')

		frame_inner = ttk.Frame(frame_label)
		frame = ttk.Frame(frame_inner)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money'].trace(
			'w', lambda *args: self.callback_youngji_money_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '영지 지원금', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_money'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame = ttk.Frame(frame_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone'].trace(
			'w', lambda *args: self.callback_youngji_blackstone_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '블랙스톤', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_blackstone'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame = ttk.Frame(frame_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa'].trace(
			'w', lambda *args: self.callback_youngji_chuksa_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '축사', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chuksa'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame = ttk.Frame(frame_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat'].trace(
			'w', lambda *args: self.callback_youngji_tukbat_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '텃밭', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'].trace(
			'w', lambda *args: self.callback_youngji_tukbat_count_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count')
			)
		combobox_list = []
		for i in range(1, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'] = 2

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'], 
			state 				= "readonly",
			height				= 10,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_tukbat_count'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "개 보유"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame_inner.pack(anchor=tkinter.W)

		frame_inner = ttk.Frame(frame_label)
		frame = ttk.Frame(frame_inner)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip'].trace(
			'w', lambda *args: self.callback_youngji_chejip_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '채집', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)
		frame = ttk.Frame(frame_inner)

		combobox_list = LYBBlackDesert.chejip_list
		place_combobox_list = LYBBlackDesert.chejip_place_list

		for i in range(8):
			self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)] = tkinter.StringVar(frame)
			self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i)] = tkinter.StringVar(frame)
			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_0'].trace(
					'w', lambda *args: self.callback_youngji_chejip_0_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_0')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_0'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_0_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_1'].trace(
					'w', lambda *args: self.callback_youngji_chejip_1_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_1')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_1'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_1_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_2'].trace(
					'w', lambda *args: self.callback_youngji_chejip_2_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_2')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_2'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_2_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_2')
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_3'].trace(
					'w', lambda *args: self.callback_youngji_chejip_3_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_3')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_3'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_3_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_3')
					)

			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_4'].trace(
					'w', lambda *args: self.callback_youngji_chejip_4_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_4')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_4'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_4_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_4')
					)
				frame.pack(anchor=tkinter.W)
				frame = ttk.Frame(frame_inner)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_5'].trace(
					'w', lambda *args: self.callback_youngji_chejip_5_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_5')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_5'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_5_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_5')
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_6'].trace(
					'w', lambda *args: self.callback_youngji_chejip_6_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_6')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_6'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_6_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_6')
					)
			elif i == 7:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_7'].trace(
					'w', lambda *args: self.callback_youngji_chejip_7_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_7')
					)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_7'].trace(
					'w', lambda *args: self.callback_youngji_chejip_place_7_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_7')
					)

			if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)] = combobox_list[-1]

			if not lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i)] = place_combobox_list[1]
				
			label = ttk.Label(
				master 				= frame, 
				text 				= str(i+1) +'. '
				)
			label.pack(side=tkinter.LEFT)

			combobox = ttk.Combobox(
				master 				= frame,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)], 
				state 				= "readonly",
				height				= 10,
				width 				= 9,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_' + str(i)])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

			combobox = ttk.Combobox(
				master 				= frame,
				values				= place_combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i)], 
				state 				= "readonly",
				height				= 10,
				width 				= 6,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK + 'youngji_chejip_place_' + str(i)])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)


		frame.pack(anchor=tkinter.W)
		frame_inner.pack(anchor=tkinter.W)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)


		frame_row.pack(anchor=tkinter.W)


		frame_head.pack(anchor=tkinter.W)









		# +-----------------------------------------+
		# |											|
		# | 				작업 설정2				|
		# |											|
		# +-----------------------------------------+
		
		frame_head = ttk.Frame(self.inner_frame_dic['work2_tab_frame'])

		frame_row = ttk.Frame(frame_head)

		frame_label = ttk.LabelFrame(frame_row, text='미궁 개척')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "난이도"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'].trace(
			'w', lambda *args: self.callback_migung_gecheok_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok')
			)
		combobox_list = []
		for i in range(1, 9):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_gecheok'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "단계 선택"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend'].trace(
			'w', lambda *args: self.callback_migung_friend_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '친구', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'].trace(
			'w', lambda *args: self.callback_migung_friend_number_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number')
			)
		combobox_list = []
		for i in range(0, 11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_friend_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild'].trace(
			'w', lambda *args: self.callback_migung_guild_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '길드', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'].trace(
			'w', lambda *args: self.callback_migung_guild_number_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number')
			)
		combobox_list = []
		for i in range(0, 11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_guild_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open'].trace(
			'w', lambda *args: self.callback_migung_open_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '공개', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_open'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)
		
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat'].trace(
			'w', lambda *args: self.callback_migung_repeat_booleanvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat')
			)
		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat'] = True
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '반복', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_repeat'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)
		frame_label = ttk.LabelFrame(frame_row, text='미궁 목록')
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "난이도"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'].trace(
			'w', lambda *args: self.callback_migung_join_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join')
			)
		combobox_list = []
		for i in range(1, 9):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'] = 5

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "단계 참여하고 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit'].trace(
			'w', lambda *args: self.callback_migung_join_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit')
			)
		combobox_list = []
		for i in range(10, 601, 5):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit'] = 30

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'migung_join_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "초 매칭 대기 후 재신청"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)
		frame_row.pack(anchor=tkinter.W)

		frame_row = ttk.Frame(frame_head)

		frame_label = ttk.LabelFrame(frame_row, text='낚시')
		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit'].trace(
			'w', lambda *args: self.callback_naksi_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit')
			)
		combobox_list = []
		for i in range(60, 7201, 60):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit'] = 600

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'naksi_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "초 동안 작업"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_row, text='말 가방에 넣기')
		frame = ttk.Frame(frame_label)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "옮길 아이템 갯수"
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'].trace(
			'w', lambda *args: self.callback_mal_bag_open_item_limit_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit')
			)
		combobox_list = []
		for i in range(1, 11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'] = 1

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'mal_bag_open_item_limit'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "개"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_row, text='가축상점')
		frame = ttk.Frame(frame_label)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "일반 사료 구매 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set'].trace(
			'w', lambda *args: self.callback_pet_set_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set'] = 100

		combobox_list = [10, 50, 100]

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_set'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame, 
			text 				= "개씩"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number'].trace(
			'w', lambda *args: self.callback_pet_number_stringvar(args, lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number')
			)

		if not lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number'] = 2

		combobox_list = []
		for i in range(1, 100):
			combobox_list.append(str(i))

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number'], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_WORK2 + 'pet_number'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "회"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.NW, padx=5, pady=5)


		frame_row.pack(anchor=tkinter.W)

		frame_head.pack(anchor=tkinter.W)












		# +-----------------------------------------+
		# |											|
		# | 				토벌 게시판				|
		# |											|
		# +-----------------------------------------+
		
		frame_head = ttk.Frame(self.inner_frame_dic['tobeol_tab_frame'])
		
		frame_row = ttk.Frame(frame_head)
		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom'].trace(
			'w', lambda *args: self.callback_tobeol_custom_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom')
			)

		if not lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom'] = False

		s = ttk.Style()
		s.configure('blue_checkbutton.TCheckbutton', foreground='blue')
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '개별 설정 사용', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'custom'],
			onvalue 			= True, 
			style 				= 'red_checkbutton.TCheckbutton',
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update'].trace(
			'w', lambda *args: self.callback_tobeol_auto_update_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update')
			)

		if not lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update'] = True

		s = ttk.Style()
		s.configure('green_checkbutton.TCheckbutton', foreground='green')
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '토벌 실패시 난이도 업데이트', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'auto_update'],
			onvalue 			= True, 
			style 				= 'green_checkbutton.TCheckbutton',
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=10)

		frame_row.pack(anchor=tkinter.W)
		frame = ttk.Frame(frame_head)
		frame.pack(pady=2)

		frame_row_top = ttk.Frame(frame_head)
		for i in range(len(LYBBlackDesert.tobeol_boss_list)):
			frame_row = ttk.Frame(frame_row_top)

			frame = ttk.Frame(frame_row)
			self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(i)] = tkinter.BooleanVar(frame)

			if not lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(i)] = True

			check_box = ttk.Checkbutton(

				master 				= frame,
				text 				= "%2d. %s" % (i+1, self.preformat_cjk(LYBBlackDesert.tobeol_boss_list[i], 18)), 
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + str(i)],
				onvalue 			= True, 
				offvalue 			= False
			)
			check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)

			combobox_list = LYBBlackDesert.tobeol_rank_list

			self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i)] = tkinter.StringVar(frame)

			if i == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '0'].trace(
					'w', lambda *args: self.callback_tobeol_process_0_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '0')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '0'].trace(
					'w', lambda *args: self.callback_tobeol_rank_0_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '0')
					)
			elif i == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '1'].trace(
					'w', lambda *args: self.callback_tobeol_process_1_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '1')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '1'].trace(
					'w', lambda *args: self.callback_tobeol_rank_1_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '1')
					)
			elif i == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '2'].trace(
					'w', lambda *args: self.callback_tobeol_process_2_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '2')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '2'].trace(
					'w', lambda *args: self.callback_tobeol_rank_2_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '2')
					)
			elif i == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '3'].trace(
					'w', lambda *args: self.callback_tobeol_process_3_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '3')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '3'].trace(
					'w', lambda *args: self.callback_tobeol_rank_3_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '3')
					)
			elif i == 4:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '4'].trace(
					'w', lambda *args: self.callback_tobeol_process_4_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '4')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '4'].trace(
					'w', lambda *args: self.callback_tobeol_rank_4_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '4')
					)
			elif i == 5:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '5'].trace(
					'w', lambda *args: self.callback_tobeol_process_5_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '5')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '5'].trace(
					'w', lambda *args: self.callback_tobeol_rank_5_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '5')
					)
			elif i == 6:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '6'].trace(
					'w', lambda *args: self.callback_tobeol_process_6_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '6')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '6'].trace(
					'w', lambda *args: self.callback_tobeol_rank_6_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '6')
					)
			elif i == 7:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '7'].trace(
					'w', lambda *args: self.callback_tobeol_process_7_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '7')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '7'].trace(
					'w', lambda *args: self.callback_tobeol_rank_7_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '7')
					)
			elif i == 8:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '8'].trace(
					'w', lambda *args: self.callback_tobeol_process_8_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '8')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '8'].trace(
					'w', lambda *args: self.callback_tobeol_rank_8_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '8')
					)
			elif i == 9:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '9'].trace(
					'w', lambda *args: self.callback_tobeol_process_9_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '9')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '9'].trace(
					'w', lambda *args: self.callback_tobeol_rank_9_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '9')
					)
				frame_row_top.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=10)
				frame_row_top = ttk.Frame(frame_head)
			elif i == 10:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '10'].trace(
					'w', lambda *args: self.callback_tobeol_process_10_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '10')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '10'].trace(
					'w', lambda *args: self.callback_tobeol_rank_10_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '10')
					)
			elif i == 11:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '11'].trace(
					'w', lambda *args: self.callback_tobeol_process_11_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '11')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '11'].trace(
					'w', lambda *args: self.callback_tobeol_rank_11_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '11')
					)
			elif i == 12:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '12'].trace(
					'w', lambda *args: self.callback_tobeol_process_12_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '12')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '12'].trace(
					'w', lambda *args: self.callback_tobeol_rank_12_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '12')
					)
			elif i == 13:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '13'].trace(
					'w', lambda *args: self.callback_tobeol_process_13_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '13')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '13'].trace(
					'w', lambda *args: self.callback_tobeol_rank_13_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '13')
					)
			elif i == 14:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '14'].trace(
					'w', lambda *args: self.callback_tobeol_process_14_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '14')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '14'].trace(
					'w', lambda *args: self.callback_tobeol_rank_14_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '14')
					)
			elif i == 15:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '15'].trace(
					'w', lambda *args: self.callback_tobeol_process_15_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '15')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '15'].trace(
					'w', lambda *args: self.callback_tobeol_rank_15_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '15')
					)
			elif i == 16:
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '16'].trace(
					'w', lambda *args: self.callback_tobeol_process_16_booleanvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'process' + '16')
				)
				self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '16'].trace(
					'w', lambda *args: self.callback_tobeol_rank_16_stringvar(args, lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + '16')
					)

			if not lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i)] = combobox_list[0]

			combobox = ttk.Combobox(
				master 				= frame,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i)], 
				state 				= "readonly",
				height				= 11,
				width 				= 4,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_TOBEOL + 'rank' + str(i)])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	

			
			label = ttk.Label(
				master 				= frame, 
				text 				= ' 단계 하락'
				)
			label.pack(side=tkinter.LEFT)
			frame.pack(side=tkinter.LEFT, anchor=tkinter.W)			
			frame_row.pack(anchor=tkinter.W)

		frame_row_top.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=10)
		frame_head.pack(anchor=tkinter.W, padx=5, pady=5)












		# +-----------------------------------------+
		# |											|
		# | 				알림 설정				|
		# |											|
		# +-----------------------------------------+
		
		frame_head = ttk.Frame(self.inner_frame_dic['notify_tab_frame'])
		frame_row = ttk.Frame(frame_head)
		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo'].trace(
			'w', lambda *args: self.callback_notify_urewanryo_stringvar(args, lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo')
			)

		if not lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '의뢰 완료', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'urewanryo'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss'].trace(
			'w', lambda *args: self.callback_notify_world_boss_stringvar(args, lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss')
			)

		if not lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '월드 보스 클리어', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'world_boss'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung'].trace(
			'w', lambda *args: self.callback_notify_migung_stringvar(args, lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung')
			)

		if not lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '미궁 클리어', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'migung'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol'].trace(
			'w', lambda *args: self.callback_notify_tobeol_stringvar(args, lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol')
			)

		if not lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '토벌 클리어', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'tobeol'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame = ttk.Frame(frame_row)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death'].trace(
			'w', lambda *args: self.callback_notify_character_death_stringvar(args, lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death')
			)

		if not lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death'] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '캐릭터 필드 사망', 
			variable 			= self.option_dic[lybconstant.LYB_DO_STRING_BD_NOTIFY + 'character_death'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame_row.pack(anchor=tkinter.W)
		frame_head.pack(anchor=tkinter.W, padx=5, pady=5)


		# ------

		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()

	def get_option_text(self, text):
		return "%s" % self.preformat_cjk(text, lybconstant.LYB_BD_OPTION_WIDTH) + ':'

	def get_item_rank_text(self, text):
		return "%s" % self.preformat_cjk(text, 6)




	def callback_tobeol_process_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_6_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_7_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_8_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_9_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_10_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_11_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_12_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_13_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_14_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_15_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_process_16_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_6_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_7_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_8_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_9_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_10_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_11_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_12_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_13_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_14_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_15_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_rank_16_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_auto_update_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_custom_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_mal_bag_open_item_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_pet_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_pet_set_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_loot_chegwang_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_loot_chejip_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_loot_beolmok_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_muge_percentage_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_search_complete_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jeoljeon_mode_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_insahagi_page_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_reqeat_quest_random_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_world_boss_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_naksi_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_gecheok_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_join_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_friend_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_guild_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_friend_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_guild_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_open_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_repeat_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_join_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_7_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_6_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_place_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_7_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_6_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_tukbat_count_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_tukbat_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chejip_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_money_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_blackstone_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_youngji_chuksa_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_daejeon_count_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_daejeon_giveup_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_daejeon_match_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tobeol_degrade_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_character_death_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_tobeol_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_migung_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_world_boss_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_notify_urewanryo_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hunt_pet_period_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_complete_sequence_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_complete_period_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_invite_rank_op_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_invite_rank2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_invite_rank_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_migung_invite_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_geomungiun2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_geomungiun_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jamjeryeok_dolpa_rank_order_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gwangwonseok_hapseong_auto_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sujeong_hapseong_auto_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jamjeryeok_dolpa_rank_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_gwangwonseok_hapseong_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sujeong_hapseong_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_character_move_time_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_character_move_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_jamjeryoek_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_6_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_item_rank_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_pummok_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_pummok_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_pummok_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_pummok_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sell_pummok_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hunt_quest_click_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_wait_jadong_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_fix_target_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_quest_repeat_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chracter_change_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_potion_shop_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_jadong_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_pet_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_ddolmani_skill_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_ddolmani_skill_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_ddolmani_skill_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_gabang_full_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_jeoljeon_mode_warning_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_location_y_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_location_x_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_potion_empty_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_moving_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_migung_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_sudong_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_combat_box_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hunt_period_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_loot_box_boolean_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_box_range_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_thing_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_limit_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_set_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_potion_number_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_wait_attack_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_migung_lag_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_jadong_lag_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_mainquest_afk_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_mainquest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_conversation_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_mainquest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	# def callback_threshold_gate_stringvar(self, args, option_name):
	# 	self.set_game_config(option_name, self.option_dic[option_name].get())

	# def callback_threshold_next_stringvar(self, args, option_name):
	# 	self.set_game_config(option_name, self.option_dic[option_name].get())



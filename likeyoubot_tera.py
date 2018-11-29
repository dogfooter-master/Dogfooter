import likeyoubot_game as lybgame
import likeyoubot_tera_scene as lybscene
from likeyoubot_configure import LYBConstant as lybconstant
import time
import datetime
import sys
import tkinter
from tkinter import ttk
from tkinter import font
import copy

class LYBTera(lybgame.LYBGame):
	
	work_list = [ 
		'게임 시작',
		'로그인',
		'알림',
		# '화면 클릭',
		'메인 퀘스트',
		'지역 퀘스트',
		'보스 퀘스트',
		'몬스터 추적',
		'채널 변경',
		# '랜덤 퀘스트',

		'설정 - 파티 초대 거절',
		'영웅 특성',
		'영웅 스킬',
		'임무 보상',
		'업적 보상',
		'이벤트 보상',
		
		'우편함',
		'보상 회수',

		'길드 출석',
		'길드 보상',
		'길드 기부',
		'길드 업적',
		'길드 마을',
		'길드 상점 - 경험치',
		'길드 상점 - 대량의 경험치',
		'길드 스킬',

		'소모품 상자 열기',
		'경험치 부스터 사용',
		'경험치 부스터 구매',
		'골드 부스터 사용',		
		'골드 부스터 구매',
		'자동 장착',
		'일괄 판매',
		
		'가슴 레벨업',
		'무기 레벨업',
		'신발 레벨업',
		'장갑 레벨업',
		'목걸이 레벨업',
		'반지 레벨업',
		'팔찌 레벨업',
		'귀걸이 레벨업',
		'장비 세트',

		'무기 레벨업 - 대장간',
		'방어구 레벨업 - 대장간',
		'장신구 레벨업 - 대장간',

		'친밀도',
		'무료 소환',
		'우정 포인트',
		'친구 관리',
		'지역 이동',
		'파티원에게 이동',

		'나가기',
		'글로리아로 이동',
		'아이샤로 이동',
		'오르단으로 이동',
		'블가메시로 이동',
		'야몽으로 이동',
		
		'영웅 변경',
		'영웅 변경 - 솔',
		'영웅 변경 - 올렌더',
		'영웅 변경 - 레인',
		'영웅 변경 - 라브랭',
		'영웅 변경 - 리벨리아',
		'영웅 변경 - 리나',
		'영웅 변경 - 카야',

		'몬스터 도감', # 중요함, 이 작업 이후는 던전으로 취급함. 이후 새로 추가되는 건 몬스터 도감을 기준으로 던전이면 뒤로, 아니면 앞으로

		'지하 결투장',

		# '카이아의 전장',
		'독립군 장비 보급',
		'무한의 탑',
		'요일 던전',
		'블가메시의 훈련',
		'황금 거인 강탈',

		'[정예]',
		'[일반]',
		'독립군 보급 기지', 
		'후카족 마을 수복전', 
		'밤피르의 저택',
		'달의 호수 쟁탈전',
		'황금의 미궁',
		'왕자의 궁전',
		'불의 제단',
		'벤튤라',
		'데미안',
		'그림자 기수',
		'굴',
		'티라누스',
		'라우라바',
		'고대 던전 입구',
		'고대 던전 1구역',
		'고대 던전 2구역',

		'[반복 시작]',
		'[반복 종료]',
		'[작업 예약]',
		'[작업 대기]',

		'',
		'',
		'',
		'',
		'' ]


	area_list = [
		'여명의 정원',
		'버려진 평야',
		'엘리누의 언덕',
		'통곡의 해안',
		'제국령 라키타니아',
		'금지된 땅'
	]

	sub_area_dic = {
		'여명의 정원': ['생명의 협곡'],
		'버려진 평야': ['리카노르 평야', '후키안 거주지', '후카족 마을'],
		'엘리누의 언덕': ['밤피르의 언덕', '언덕 위의 높은 곳', '달의 호수', '달빛 물결 숲 동쪽', '달빛 물결 숲 서쪽', '달빛 식물원'],
		'통곡의 해안': ['동부 연안', '탐욕의 계곡', '탐욕의 계곡 상류', '해적 소굴'],
		'제국령 라키타니아': ['라키타니아 하수도', '하수 처리장', '라키타니아 전망대', '도시 진입로'],
		'금지된 땅': ['라키타니아 외곽', '수도회 사막 입구', '수도회 사막', '망각의 화산']
	}

	dungeon_list = [ 
		'독립군 보급 기지', 
		'후카족 마을 수복전', 
		'밤피르의 저택',
		'달의 호수 쟁탈전',
		'황금의 미궁',
		'왕자의 궁전',
		'불의 제단'
		]

	tobul_list = [
		'벤튤라',
		'데미안',
		'그림자 기수',
		'굴',
		'티라누스',
		'라우라바'
		]

	challenge_list = [
		'독립군 장비 보급',
		'요일 던전',
		'블가메시의 훈련',
		'황금 거인 강탈',
		'왕의 던전'
		]

	chinmildo_npc_list = [
		'글로리아',
		'페라수스 관리자 아이샤',
		'벨디칸 오르단',
		'블가메시',
		'야몽'
	]

	gift_item_list = [
		'무기',
		'방어구',
		'장신구',
		'룬/크리스탈',
		'소모품'
		]

	item_rank_list = [

		'일반',
		'고급',
		'희귀',
		'영웅',
		'전설',
		'신화'

	]
	
	dogam_stance_list = [ 
		'수동', 
		'반자동', 
		'자동', 
		'추적' 
		]

	item_loc_list = [
		'가슴',
		'무기',
		'신발',
		'장갑',
		'목걸이',
		'반지',
		'팔찌',
		'귀걸이'
		]

	item_levelup_option_list = [
		'강화 등급 A 포함 선택',
		'강화 등급 S 포함 선택',
		'연마제 우선 선택'
		]

	hero_list = [
		'솔',
		'올렌더',
		'레인',
		'라브랭',
		'리벨리아',
		'리나',
		'카야'
		]


	nox_tera_icon_list = [
		'tera_icon',
		'tera_icon_6',
		'tera_icon_20171220',
		'tera_icon_20171222',
		'tera_icon_20180530'
	]

	momo_tera_icon_list = [
		'tera_icon_6',
		'tera_icon_20171222',
		'tera_icon_20180530'	
	]

	channel_favorite = [
		'쾌적',
		'혼잡'
		]

	game_config_boolean_list = [
	'비활성',
	'활성'
	]





	def __init__(self, game_name, game_data_name, window):
		lybgame.LYBGame.__init__(self, lybconstant.LYB_GAME_TERA, lybconstant.LYB_GAME_DATA_TERA, window)

		self.is_tutorial = False
		self.tutorial_checkpoint = 0
		self.friend_delete = False
		self.remove_naver_icon = False

	def process(self, window_image):
		# s = time.time()
		rc = super(LYBTera, self).process(window_image)
		if rc < 0:
			return rc
		# e = time.time()
		# print('[DEBUG] Game Process:', round(e-s, 2))
		return rc

	def custom_event(self, event_name):
		if 'repair_confirm' in event_name:
			(loc_x, loc_y), match_rate = self.locationResourceOnWindowPart(
					self.window_image,
					'tera_duplicate_login_loc',
					custom_below_level=(100, 100, 100),
					custom_top_level=(255,255,255),
					custom_threshold=0.7,
					custom_flag=1,
					custom_rect=(270, 200, 370, 220)
					)
			if loc_x != -1:
				if self.get_scene('tera_main_scene').get_checkpoint('duplicate_login') == 0:
					self.get_scene('tera_main_scene').set_checkpoint('duplicate_login')

				elapsed_time = time.time() - self.get_scene('tera_main_scene').get_checkpoint('duplicate_login')
				limit_time = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM))

				if elapsed_time - limit_time > 20:
					self.get_scene('tera_main_scene').set_checkpoint('duplicate_login')
					elapsed_time = 0

				if elapsed_time < limit_time:
					self.loggingElapsedTime('[이벤트 감지] 중복 로그인 대기 시간', elapsed_time, limit_time, period=1)
					return True

		return False

	def process_event(self, window_pixels, event_name):
		# if self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL) == True:
		# 	self.save_image('boss_kill')

		rc = super(LYBTera, self).process_event(window_pixels, event_name)
		if rc == True:
			if 'quest_do' in event_name:
				self.set_tutorial(True)
			elif 'friend_full' in event_name:
				self.set_friend_delete(True)
			elif 'boss_kill_sucess' in event_name:
				self.addStatistic('필드보스 킬 횟수')
				work_name = self.get_scene('tera_main_scene').current_work
				if work_name != None and ( work_name == '보스 퀘스트' or work_name == '몬스터 추적' ):
					self.get_scene('tera_main_scene').set_checkpoint('boss_kill_success')
					self.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)

				if (	self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL) == True or
						self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill') == True
						):
					png_name = self.save_image('boss_kill')
					if self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill') == True:
						self.telegram_send('', image=png_name)

				if self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill') == True:
					send_text = self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill')
					if len(send_text) < 1:
						send_text = '필드 보스 킬'
					self.telegram_send(send_text)

			elif 'quest_reward' in event_name:
				work_name = self.get_scene('tera_main_scene').current_work
				if work_name != None and work_name == '지역 퀘스트':
					self.get_scene('tera_main_scene').set_option(work_name + '_end_flag', True)
			elif 'service_repair' in event_name:
				self.clear_scene()
				self.terminate_application()
			elif 'dungeon_clear' in event_name:				
				self.addStatistic('던전 클리어 횟수')
				if self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear') == True:
					default_text = self.get_scene('tera_main_scene').current_work
					if default_text == None:
						default_text = ''
						default_text = '[' + default_text + '] '
					else:
						enter_count = self.get_scene('tera_main_scene').get_option(default_text + '_enter_count')
						try:
							dungeon_index = LYBTera.tobul_list.index(default_text)
							count_limit = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_LIMIT_COUNT_TOBUL + str(dungeon_index)))
							default_text = '[' + default_text +'][' + str(enter_count) +'/' + str(count_limit) + '] '
						except:
							try:
								dungeon_index = LYBTera.dungeon_list.index(default_text)
								count_limit = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_LIMIT_COUNT_DUNGEON + str(dungeon_index)))
								default_text = '[' + default_text +'][' + str(enter_count) +'/' + str(count_limit) + '] '
							except:
								return rc

					send_text = self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear')
					if len(send_text) < 1:
						send_text = '던전 클리어'
					self.telegram_send(default_text + send_text)
					png_name = self.save_image('dungeon_clear')
					if self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear') == True:
						self.telegram_send('', image=png_name)
		return rc

	def check_reserved(self):
		pass

	def custom_check(self, window_image, window_pixel):

		 # for i in range(8):
		 # 	for j in range(3):
			# print(self.item_loc_list[i], self.item_levelup_option_list[j], self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)))

			# print(self.item_loc_list[i], self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)))


		# print('::::::::::', self.get_window_config('wakeup_period_entry'), self.get_window_config(lybconstant.LYB_DO_STRING_WAIT_TIME_SCENE_CHANGE))

		# print('interval =', self.interval)

		if self.start_time == None:
			self.start_time	= time.time()

		total_elapsed_time = time.time() - self.start_time

		# if total_elapsed_time > 60:
		# 	self.remove_naver_icon = False

		if self.remove_naver_icon == False:
			pixel_box_name = 'tera_naver_icon'
			s_time = time.time()
			(loc_x, loc_y), match_rate = self.locationOnWindowPart(
									window_image,
									self.resource_manager.pixel_box_dic[pixel_box_name],
									custom_threshold=0.7,
									custom_flag=1,
									custom_rect=(0, 60, 30, 380)
									)
			e_time = time.time()
			# print('[DEBUG] -------------------------> ', pixel_box_name, (loc_x, loc_y), '[', int(match_rate*100), ']', e_time - s_time)

			if loc_x != -1:
				self.window.mouse_click(self.hwnd, loc_x, loc_y)
				self.remove_naver_icon = True
				return 'naver_icon'

			if total_elapsed_time > 30:
				self.remove_naver_icon = True

		# print(self.window_title, \
		# 	'[', \
		# 	total_elapsed_time, \
		# 	self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_BOOLEAN_RESTART_GAME), \
		# 	self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_PERIOD_RESTART_GAME), \
		# 	self.get_window_config('adjust_entry'), ']')


		restart_period = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_PERIOD_RESTART_GAME)) * 60
		self.loggingElapsedTime('[시간 체크] 주기적인 게임 종료', 	total_elapsed_time, restart_period, period=60)
		if restart_period != 0 and total_elapsed_time > restart_period:
			self.logger.info('[게임 종료] 테라M 게임을 종료합니다 - 사유: 주기적인 종료 ' + str(total_elapsed_time) + '/' + str(restart_period))
			self.clear_scene()
			self.terminate_application()
			self.start_time = time.time()
			return 'terminate_game'

		main_scene = self.get_scene('tera_main_scene')
		if (	main_scene.current_work != None and
				len(main_scene.current_work) > 0
				):
			current_work_elapsed_time = time.time() - main_scene.get_checkpoint(main_scene.current_work + '_check_start')

			
			if self.get_work_status(main_scene.current_work) > self.get_work_status('몬스터 도감'):
				duration_limit = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_DURATION_DUNGEON)) * 60
				self.loggingElapsedTime('[시간 체크] 현재 작업 - ' + main_scene.current_work + ' ',
					current_work_elapsed_time, duration_limit, period=30)

				if current_work_elapsed_time > duration_limit:
					self.logger.info('[게임 종료] 테라M 게임을 종료합니다 - 사유: 현재 작업 제한 시간 ' + 
							str(int(current_work_elapsed_time)) + '/' + str(duration_limit))
					self.clear_scene()
					self.terminate_application()
					return 'terminate_game'

				if main_scene.get_checkpoint(main_scene.current_work + '_check_start_each') != 0:
					current_dungeon_elapsed_time = time.time() - main_scene.get_checkpoint(main_scene.current_work + '_check_start_each')
					duration_limit_each = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH)) * 60
					self.loggingElapsedTime('[시간 체크] '+ main_scene.current_work + ' 던전 진입 후 경과 시간', 
						current_dungeon_elapsed_time, duration_limit_each, period=30)

					if current_dungeon_elapsed_time > duration_limit_each:
						self.logger.info('[게임 종료] 테라M 게임을 종료합니다 - 사유: 던전 제한 시간 ' + 
							str(current_dungeon_elapsed_time) + '/' + str(duration_limit_each) + '초')
						self.clear_scene()
						self.terminate_application()
						return 'terminate_game'
			else:
				# print('[시간 체크] 현재 작업:', main_scene.current_work, 'E:', current_work_elapsed_time)
				self.loggingElapsedTime('[시간 체크] 현재 작업 - ' + main_scene.current_work, 
					current_work_elapsed_time, 0, period=30)

		self.custom_check_reserved()

		if not 'skip_event' in self.event_limit:
			self.event_limit['skip_event'] = time.time()

		skip_limit = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_SKIP_PERIOD))

		# print('[DEBUG] SKIP COOLTIME:',  time.time() - self.event_limit['skip_event'], 'P:', skip_limit)
		if time.time() - self.event_limit['skip_event'] > skip_limit:
			self.event_limit['skip_event'] = time.time()
			skip_loc_list = [
				'tera_skip_loc',
				'tera_skip_touch_loc',
				'tera_skip_movie_loc',
				# 'tera_skip_tutorial_loc'
				]

			s = time.time()
			for each_loc in skip_loc_list:
				if not each_loc in self.event_limit:
					self.event_limit[each_loc] = time.time()
					self.event_limit[each_loc +'_count'] = 0
				else:			
					# 동일한 이벤트 10초마다 발생
					if time.time() - self.event_limit[each_loc] < 10:
						if self.event_limit[each_loc +'_count'] > 2:
							continue
					else:
						self.event_limit[each_loc + '_count'] = 0

				self.event_limit[each_loc + '_count'] += 1

				# adjust_level = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_SKIP_LEVEL_ADJUST))
				adjust_threshold = int(self.get_game_config(lybconstant.LYB_GAME_TERA, lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2)) * 0.01
				# print('[DEBUG] adjust_threshold=', adjust_threshold)
				# skip_match_rate = self.rateMatchedResource(
				# 						window_pixel, 
				# 						each_loc,
				# 						custom_below_level=adjust_level
				# 									)

				if each_loc == 'tera_skip_touch_loc':
					each_rect = (250, 195, 290, 220)
				else:
					each_rect = (570, 30, 620, 50)

				(loc_x, loc_y), skip_match_rate	= self.locationResourceOnWindowPart(
											self.window_image,
											each_loc,
											custom_below_level=(150, 150, 150),
											custom_top_level=(255,255,255),
											custom_threshold=adjust_threshold,
											custom_flag=1,
											custom_rect=each_rect
											)

				if loc_x != -1 and skip_match_rate >= adjust_threshold:
					self.logger.debug('Clicked SKIP:' + str(each_loc) + ':' + str((loc_x, loc_y)) +'  '+ str(int(skip_match_rate * 100)) + '%')
					self.mouse_click(each_loc.replace('_loc', '', 1) + '_0')
					self.event_limit[each_loc] = time.time()

					return 'skip'

			e = time.time()
			# print('[DEBUG] ElapsedTime SKIP:', round(e - s, 2))


		return ''

	def compare_reserved(self, reserved_hour, reserved_minute, reserved_second):
	
		now = datetime.datetime.now()
		now_time = now.strftime('%H:%M:%S')
		now_hour = int(now_time.split(':')[0])
		now_minute = int(now_time.split(':')[1])
		now_second = int(now_time.split(':')[2])

		# self.logger.debug('ReservedTimeCheck:' + str((reserved_hour, reserved_minute, reserved_second)) + ':' + str((now_hour, now_minute, now_second)))

		if reserved_hour != now_hour:
			return False

		if reserved_minute != now_minute:
			return False

		if abs(reserved_second - now_second) > 10:
			return False

		self.logger.debug('ReservedTime:' + str((reserved_hour, reserved_minute, reserved_second)) + ':' + str((now_hour, now_minute, now_second)))
		return True

	def custom_check_reserved(self):

		if self.wait_for_start_reserved_work == False:
			work_index_to_move = self.recursive_check_reserved(self.get_game_config(lybconstant.LYB_GAME_TERA, '', flag=1), [], [])
			if work_index_to_move != None:
				self.logger.debug('reserved work index='+str(work_index_to_move))
				schedule_list = self.get_game_config(lybconstant.LYB_GAME_TERA, 'schedule_list')
				self.get_scene('tera_main_scene').move_status[self.current_schedule_work] = work_index_to_move
				self.wait_for_start_reserved_work = True

			# print('[DEBUG] return_callstack:', self.get_scene('tera_main_scene').callstack, 
			# 	'work to move:', work_to_move, self.wait_for_start_reserved_work)

		return

	def recursive_check_reserved(self, config, arg_callstack, arg_callstack_status):
		schedule_list = config['schedule_list']

		if '[작업 예약]' in schedule_list:
			r_work_done_dic = self.get_scene('tera_main_scene').get_option('r_work_done_dic')
			if r_work_done_dic == None:
				r_work_done_dic = {}

			# self.logger.debug('ReservedQueue:' + str(r_work_done_dic))

			reserved_hour = int(config[lybconstant.LYB_DO_STRING_RESERVED_HOUR])
			reserved_minute = int(config[lybconstant.LYB_DO_STRING_RESERVED_MINUTE])
			reserved_second = int(config[lybconstant.LYB_DO_STRING_RESERVED_SECOND])

			queue_elem = reserved_hour*60*60 + reserved_minute*60 + reserved_second

			if queue_elem in r_work_done_dic:
				last_done_time = r_work_done_dic[queue_elem]
				# self.logger.debug('Reserved: ' + str(queue_elem) + '==>' + str(time.time()) + ':' + str(last_done_time))

				if time.time() - last_done_time > 3600:
					# 작업 예약된 애들을 보관해놓고 1시간 이상되면 꺼내서 버린다.
					# 작업 예약 한번만 실행되게 하려고.
					r_work_done_dic.pop(queue_elem)
				else:
					return None

			is_there = self.compare_reserved(reserved_hour, reserved_minute, reserved_second)
			if is_there == True:
				r_work_done_dic[queue_elem] = time.time()
				self.get_scene('tera_main_scene').set_option('r_work_done_dic', r_work_done_dic)
				call_index = 0
				if len(self.get_scene('tera_main_scene').callstack) > 0:
					for each_call in self.get_scene('tera_main_scene').callstack:
						iterator_key = self.build_iterator_key(call_index, each_call)
						self.get_scene('tera_main_scene').set_option(iterator_key, None)
						call_index += 1
					self.get_scene('tera_main_scene').callstack.clear()
				# self.get_scene('tera_main_scene').callstack.clear()
				self.get_scene('tera_main_scene').callstack = arg_callstack

				self.get_scene('tera_main_scene').callstack_status.clear()
				self.get_scene('tera_main_scene').callstack_status = arg_callstack_status

				self.logger.debug('current_schedule_work:' + str(self.current_schedule_work))
				if self.current_schedule_work != None:
					if len(self.current_schedule_work) > 0:
						self.get_scene('tera_main_scene').set_option(self.current_schedule_work + '_end_flag', True)

				if len(arg_callstack) > 0:
					# 1depth 이상
					iterator_key = self.build_iterator_key(len(arg_callstack) - 1, arg_callstack[-1])
					custom_config_dic = self.configure.window_config['custom_config_dic']

					self.get_scene('tera_main_scene').set_option(iterator_key, custom_config_dic[arg_callstack[-1]]['schedule_list'].index('[작업 예약]'))

					return custom_config_dic[arg_callstack[-1]]['schedule_list'].index('[작업 예약]')
				else:
					return schedule_list.index('[작업 예약]') + 1

		custom_config_dic = self.configure.window_config['custom_config_dic']
		i = 1
		for each_work in schedule_list:
			if each_work in custom_config_dic:
				arg_callstack.append(each_work)
				arg_callstack_status.append(i)
				work_index_to_move = self.recursive_check_reserved(custom_config_dic[each_work], arg_callstack, arg_callstack_status)
				if work_index_to_move != None:
					return work_index_to_move
				else:
					arg_callstack.pop()
					arg_callstack_status.pop()
			i += 1

		return None


	def get_screen_by_location(self, window_image):

		# print('[DEBUG] get_screen_by_location - 1')
		scene_name = self.scene_nox_init_screen(window_image)
		if len(scene_name) > 0:
			return scene_name

		# print('[DEBUG] get_screen_by_location - 2')
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

	def scene_nox_init_screen(self, window_image):

		loc_x = -1
		loc_y = -1

		if self.player_type == 'nox':
			for each_icon in LYBTera.nox_tera_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(80, 110, 570, 300)
								)
				# print('[DEBUG] NoxTeraIcon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					self.logger.info('녹스 테라 아이콘 발견됨. 위치: '+str((loc_x, loc_y)))
					break
		elif self.player_type == 'momo':
			for each_icon in LYBTera.momo_tera_icon_list:
				(loc_x, loc_y),  match_rate = self.locationOnWindowPart(
								window_image,
								self.resource_manager.pixel_box_dic[each_icon],
								custom_threshold=0.8,
								custom_flag=1,
								custom_rect=(30, 10, 610, 300)
								)
				# print('[DEBUG] MomoTeraIcon:', (loc_x, loc_y), match_rate)
				if loc_x != -1:
					self.logger.info('모모 테라 아이콘 발견됨. 위치: '+str((loc_x, loc_y)))
					break

		if loc_x == -1:
			return ''

		return 'nox_init_screen_scene'
		
	def get_work_status(self, work_name):		
		if work_name in LYBTera.work_list:
			return (LYBTera.work_list.index(work_name) + 1) * 1000
		else: 
			return 99999

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

	def get_tutorial(self):
		elapsed_time = time.time() - self.tutorial_checkpoint
		if elapsed_time > 20:
			self.set_tutorial(False)

		return self.is_tutorial

	def set_tutorial(self, flag):
		self.tutorial_checkpoint = time.time()
		self.is_tutorial = flag
		# self.get_scene('tera_manage_hero_scene').set_option('tutorial', flag)
		# self.get_scene('tera_rune_scene').set_option('tutorial', flag)
		# self.get_scene('tera_hero_talent_scene').set_option('tutorial', flag)
		# self.get_scene('tera_smithy_scene').set_option('tutorial', flag)
		# self.get_scene('tera_battle_area_scene').set_option('tutorial', flag)
		# self.get_scene('tera_injang_scene').set_option('tutorial', flag)
		# self.get_scene('tera_daily_dungeon_scene').set_option('tutorial', flag)
		# self.get_scene('tera_dungeon_scene_common').set_option('tutorial', flag)
		# self.get_scene('tera_summon_scene').set_option('tutorial', flag)

	def set_friend_delete(self, flag):
		self.friend_delete = flag

	def get_friend_delete(self):
		return self.friend_delete











































































































































# UI

class LYBTeraTab(lybgame.LYBGameTab):
	def __init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name=lybconstant.LYB_GAME_TERA):
		lybgame.LYBGameTab.__init__(self, root_frame, configure, game_options, inner_frame_dics, width, height, game_name)

	def set_work_list(self):
		# print(self.configure.common_config[self.game_name]['work_list'])
		lybgame.LYBGameTab.set_work_list(self)

		# temp_work_list = []
		# for each_work in LYBTera.work_list:
		# 	if each_work != '':
		# 		temp_work_list.append(each_work)

		# temp_work_list.sort()
		# for i in range(5):
		# 	temp_work_list.append('')

		for each_work in LYBTera.work_list:
			# print(each_work)
			self.option_dic['work_list_listbox'].insert('end', each_work)
			self.configure.common_config[self.game_name]['work_list'].append(each_work)

		# print('TEST WorkList Child')
		# print(self.configure.common_config[self.game_name]['work_list'])

	def set_option(self):


		###############################################
		#                프로그램 재시작              #
		###############################################










		# PADDING
		frame = ttk.Frame(
			master 				= self.master
			)
		frame.pack(pady=5)


		self.inner_frame_dic['options'] = ttk.Frame(
			master 				= self.master
			)

		self.option_dic['option_note'] = ttk.Notebook(
			master 				= self.inner_frame_dic['options']
			)








		self.inner_frame_dic['dungeon_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['dungeon_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['dungeon_tab_frame'], text='던전1')

	
		self.inner_frame_dic['dungeon_2_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['dungeon_2_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['dungeon_2_tab_frame'], text='던전2')

		self.inner_frame_dic['dungeon_3_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['dungeon_3_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['dungeon_3_tab_frame'], text='던전3')

	


		self.inner_frame_dic['skill_use_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['skill_use_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['skill_use_tab_frame'], text='스킬 사용')



		self.inner_frame_dic['quest_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['quest_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['quest_tab_frame'], text='메인')





		self.inner_frame_dic['hero_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['hero_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['hero_tab_frame'], text='영웅')



		self.inner_frame_dic['item_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)
		
		self.inner_frame_dic['item_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['item_tab_frame'], text='장비 레벨업')




		self.inner_frame_dic['guild_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)

		self.inner_frame_dic['guild_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['guild_tab_frame'], text='길드')





		self.inner_frame_dic['shop_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)

		self.inner_frame_dic['shop_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['shop_tab_frame'], text='상점')





		self.inner_frame_dic['monitoring_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)

		self.inner_frame_dic['monitoring_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['monitoring_tab_frame'], text='모니터링')






		self.inner_frame_dic['game_config_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)

		self.inner_frame_dic['game_config_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['game_config_tab_frame'], text='게임 설정')








		self.inner_frame_dic['move_tab_frame'] = ttk.Frame(
			master 				= self.option_dic['option_note']
			)

		self.inner_frame_dic['move_tab_frame'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.option_dic['option_note'].add(self.inner_frame_dic['move_tab_frame'], text='이동')







		###############################################
		#                몬스터 도감 진행             #
		###############################################




		# frame = ttk.Frame(self.inner_frame_dic['common_tab_frame'])
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "일반 토벌대",
		# 	anchor 				= tkinter.W,
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	)
		
		# label.pack(side=tkinter.LEFT)

		# self.option_dic[lybconstant.LYB_DO_STRING_NORMAL_TOBUL] = tkinter.StringVar(frame)
		# self.option_dic[lybconstant.LYB_DO_STRING_NORMAL_TOBUL].trace('w', 
		# 	lambda *args: self.callback_normal_tobul_stringvar(args, option_name=lybconstant.LYB_DO_STRING_NORMAL_TOBUL))

		# if not lybconstant.LYB_DO_STRING_NORMAL_TOBUL in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_NORMAL_TOBUL] = LYBTera.tobul_list[0]

		# self.option_dic[lybconstant.LYB_DO_STRING_NORMAL_TOBUL].set(LYBTera.tobul_list[0])
		# option_menu = tkinter.OptionMenu(
		# 	frame,
		# 	self.option_dic[lybconstant.LYB_DO_STRING_NORMAL_TOBUL], 
		# 	*LYBTera.tobul_list

		# 	)
		# option_menu.configure(width=20)
		# option_menu.configure(font=lybconstant.LYB_FONT)
		# option_menu.pack(side=tkinter.LEFT, anchor=tkinter.W)
		
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "를 ",
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	# fg='White' if brightness < 120 else 'Black', 
		# 	# bg=bg_colour
		# 	)
		# label.pack(side=tkinter.LEFT)
		# self.option_dic[lybconstant.LYB_DO_STRING_DURATION_NORMAL_TOBUL] = tkinter.StringVar(frame)
		# self.option_dic[lybconstant.LYB_DO_STRING_DURATION_NORMAL_TOBUL].trace('w', 
		# 	lambda *args: self.callback_normal_tobul_duration_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_NORMAL_TOBUL))

		# if not lybconstant.LYB_DO_STRING_DURATION_NORMAL_TOBUL in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_NORMAL_TOBUL] = 120
		
		# entry = ttk.Entry(
		# 	master 				= frame, 
		# 	relief 				= 'sunken', 
		# 	textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_NORMAL_TOBUL],
		# 	justify 			= tkinter.RIGHT, 
		# 	width 				= 5,
		# 	font 				= lybconstant.LYB_FONT
		# 	)

		# entry.pack(side=tkinter.LEFT)		
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "분 동안 반복해서 진행합니다.",
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	# fg='White' if brightness < 120 else 'Black', 
		# 	# bg=bg_colour
		# 	)
		# label.pack(side=tkinter.LEFT)

		# frame.pack(anchor=tkinter.W)


		




















		frame_bottom = ttk.Frame(self.inner_frame_dic['dungeon_tab_frame'])

		frame = ttk.Frame(frame_bottom)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE].trace(
			'w', lambda *args: self.callback_party_member_mode_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE)
			)

		if not lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE] = False

		s = ttk.Style()
		s.configure('checkbutton_reverse.TCheckbutton', foreground='green', background='yellow')
		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '파티원 모드', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_PARTY_MEMBER_MODE],
			style 				= 'checkbutton_reverse.TCheckbutton',
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W)
		self.tooltip(check_box, lybconstant.LYB_TOOLTIP_TERA_PARTY_MEMBER_MODE)

		frame.pack(anchor=tkinter.W, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_bottom, text='던전 작업 횟수')

		i = 0
		dungeon_d_list = []
		dungeon_e_list = []

		for each_dungeon in LYBTera.dungeon_list:

			dungeon_d_list.append(lybconstant.LYB_DO_STRING_LIMIT_COUNT_DUNGEON + str(i))
			dungeon_e_list.append(lybconstant.LYB_DO_STRING_TYPE_ENTER_DUNGEON + str(i))

			frame_dungeon = ttk.Frame(frame_label)
			label = ttk.Label(
				master 				= frame_dungeon, 
				text 				= '%s'%(self.preformat_cjk(each_dungeon, 18))
				)

			label.pack(side=tkinter.LEFT)
			self.option_dic[dungeon_d_list[i]] = tkinter.StringVar(frame_dungeon)
			self.option_dic[dungeon_e_list[i]] = tkinter.StringVar(frame_dungeon)

			# print('------------', i, )
			if i == 0:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_0_stringvar(args, option_name=dungeon_d_list[0]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_0_stringvar(args, option_name=dungeon_e_list[0]))
			elif i == 1:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_1_stringvar(args, option_name=dungeon_d_list[1]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_1_stringvar(args, option_name=dungeon_e_list[1]))
			elif i == 2:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_2_stringvar(args, option_name=dungeon_d_list[2]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_2_stringvar(args, option_name=dungeon_e_list[2]))
			elif i == 3:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_3_stringvar(args, option_name=dungeon_d_list[3]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_3_stringvar(args, option_name=dungeon_e_list[3]))
			elif i == 4:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_4_stringvar(args, option_name=dungeon_d_list[4]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_4_stringvar(args, option_name=dungeon_e_list[4]))
			elif i == 5:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_5_stringvar(args, option_name=dungeon_d_list[5]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_5_stringvar(args, option_name=dungeon_e_list[5]))
			elif i == 6:
				self.option_dic[dungeon_d_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_dungeon_6_stringvar(args, option_name=dungeon_d_list[6]))
				self.option_dic[dungeon_e_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_dungeon_6_stringvar(args, option_name=dungeon_e_list[6]))

			if not dungeon_d_list[i] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][dungeon_d_list[i]] = 10

			if not dungeon_e_list[i] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][dungeon_e_list[i]] = 1
			
			entry = ttk.Entry(
				master 				= frame_dungeon, 
				textvariable 		= self.option_dic[dungeon_d_list[i]],
				justify 			= tkinter.RIGHT, 
				width 				= 5
				)

			entry.pack(side=tkinter.LEFT)	

			dungeon_enter_style = [
				('즉시', 0),
				('매칭', 1)
				]

			for text, mode in dungeon_enter_style:
				combo_box = ttk.Radiobutton(
					master 				= frame_dungeon,
					text 				= text,
					variable 			= self.option_dic[dungeon_e_list[i]],
					value 				= mode

					)
				combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

			frame_dungeon.pack(anchor=tkinter.W)
			i += 1

		frame_label.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=5)

		frame_label = ttk.LabelFrame(frame_bottom, text='토벌대 작업 횟수')

		i = 0
		dungeon_s_list = []
		dungeon_t_list = []

		for each_dungeon in LYBTera.tobul_list:

			dungeon_s_list.append(lybconstant.LYB_DO_STRING_LIMIT_COUNT_TOBUL + str(i))
			dungeon_t_list.append(lybconstant.LYB_DO_STRING_TYPE_ENTER_TOBUL + str(i))

			frame_dungeon = ttk.Frame(frame_label)
			label = ttk.Label(
				master 				= frame_dungeon, 
				text 				= '%s'%(self.preformat_cjk(each_dungeon, 12))
				)

			label.pack(side=tkinter.LEFT)
			self.option_dic[dungeon_s_list[i]] = tkinter.StringVar(frame_dungeon)
			self.option_dic[dungeon_t_list[i]] = tkinter.StringVar(frame_dungeon)

			if i == 0:
				self.option_dic[dungeon_s_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_tobul_0_stringvar(args, option_name=dungeon_s_list[0]))
				self.option_dic[dungeon_t_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_tobul_0_stringvar(args, option_name=dungeon_t_list[0]))
			elif i == 1:
				self.option_dic[dungeon_s_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_tobul_1_stringvar(args, option_name=dungeon_s_list[1]))
				self.option_dic[dungeon_t_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_tobul_1_stringvar(args, option_name=dungeon_t_list[1]))
			elif i == 2:
				self.option_dic[dungeon_s_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_tobul_2_stringvar(args, option_name=dungeon_s_list[2]))
				self.option_dic[dungeon_t_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_tobul_2_stringvar(args, option_name=dungeon_t_list[2]))
			elif i == 3:
				self.option_dic[dungeon_s_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_tobul_3_stringvar(args, option_name=dungeon_s_list[3]))
				self.option_dic[dungeon_t_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_tobul_3_stringvar(args, option_name=dungeon_t_list[3]))
			elif i == 4:
				self.option_dic[dungeon_s_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_tobul_4_stringvar(args, option_name=dungeon_s_list[4]))
				self.option_dic[dungeon_t_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_tobul_4_stringvar(args, option_name=dungeon_t_list[4]))
			elif i == 5:
				self.option_dic[dungeon_s_list[i]].trace('w', 
					lambda *args: self.callback_limit_count_tobul_5_stringvar(args, option_name=dungeon_s_list[5]))
				self.option_dic[dungeon_t_list[i]].trace('w', 
					lambda *args: self.callback_type_enter_tobul_5_stringvar(args, option_name=dungeon_t_list[5]))

			if not dungeon_s_list[i] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][dungeon_s_list[i]] = 10
			
			if not dungeon_t_list[i] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][dungeon_t_list[i]] = 1

			entry = ttk.Entry(
				master 				= frame_dungeon, 
				textvariable 		= self.option_dic[dungeon_s_list[i]],
				justify 			= tkinter.RIGHT, 
				width 				= 5
				)

			entry.pack(side=tkinter.LEFT)	

			dungeon_enter_style = [
				('즉시', 0),
				('매칭', 1)
				]

			for text, mode in dungeon_enter_style:
				combo_box = ttk.Radiobutton(
					master 				= frame_dungeon,
					text 				= text,
					variable 			= self.option_dic[dungeon_t_list[i]],
					value 				= mode

					)
				combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
			frame_dungeon.pack(anchor=tkinter.W)
			i += 1

		frame_label.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=10, fill=tkinter.Y, expand=True)
		frame_bottom.pack(anchor=tkinter.NW, pady=5)


		frame_combat = ttk.Frame(self.inner_frame_dic['dungeon_tab_frame'])
		frame_combat_label = ttk.LabelFrame(frame_combat, text='던전 매칭시 체크한 영웅이 없으면 취소합니다')

		frame_combat_0 = ttk.Frame(frame_combat_label)
		hero_class_list = []
		for i in range(7):
			frame_s = ttk.Frame(frame_combat_0)

			hero_class_list.append(lybconstant.LYB_DO_BOOLEAN_RAID_MATCH_HERO + str(i))
			self.option_dic[hero_class_list[i]] = tkinter.BooleanVar(frame_s)

			check_box = ttk.Checkbutton(

				master 				= frame_s,
				text 				= LYBTera.hero_list[i], 
				variable 			= self.option_dic[hero_class_list[i]],
				onvalue 			= True, 
				offvalue 			= False
			)

			if i == 0:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_0_booleanvar(args, hero_class_list[0])
					)
			elif i == 1:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_1_booleanvar(args, hero_class_list[1])
					)
			elif i == 2:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_2_booleanvar(args, hero_class_list[2])
					)
			elif i == 3:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_3_booleanvar(args, hero_class_list[3])
					)
			elif i == 4:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_4_booleanvar(args, hero_class_list[4])
					)
			elif i == 5:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_5_booleanvar(args, hero_class_list[5])
					)
			elif i == 6:
				self.option_dic[hero_class_list[i]].trace(
					'w', lambda *args: self.callback_hero_class_list_6_booleanvar(args, hero_class_list[6])
					)

			if not hero_class_list[i] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][hero_class_list[i]] = False

			check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
			frame_s.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame_combat_0.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame_combat_1 = ttk.Frame(frame_combat_label)
		label = ttk.Label(
			master 				= frame_combat_1, 
			text 				= '영웅 초상화 인식 허용치(0~100): '
			)

		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD].trace( 
			'w', lambda *args: self.callback_raid_match_hero_threshold_stringvar(args, option_name=lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD)
			)

		if not lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD] = 77
		
		entry = ttk.Entry(
			master 				= frame_combat_1,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_MATCH_HERO_THRESHOLD],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(anchor=tkinter.W, side=tkinter.LEFT)	

		label = ttk.Label(
			master 				= frame_combat_1, 
			text 				= '%'
			)

		label.pack(side=tkinter.LEFT)
		frame_combat_1.pack(anchor=tkinter.W, padx=10)

		frame_combat_2 = ttk.Frame(frame_combat_label)
		label = ttk.Label(
			master 				= frame_combat_2, 
			text 				= '체크한 영웅 연산 방식'
			)

		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION].trace( 
			'w', lambda *args: self.callback_match_hero_operation_stringvar(args, option_name=lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION)
			)

		if not lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION] = 0
		
		match_operation = [
			('모두 포함', 0),
			('한 개 이상 포함', 1)
			]

		for text, mode in match_operation:
			combo_box = ttk.Radiobutton(
				master 				= frame_combat_2,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_MATCH_HERO_OPERATION],
				value 				= mode

				)
			combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		label.pack(side=tkinter.LEFT)
		frame_combat_2.pack(anchor=tkinter.W, padx=10)

		frame_combat_label.pack(anchor=tkinter.NW, fill=tkinter.X, expand=True)
		frame_combat.pack(anchor=tkinter.NW, padx=5, fill=tkinter.X, expand=True)









































		###############################################
		#                  전투 진행                  #
		###############################################
		frame_left = ttk.Frame(self.inner_frame_dic['skill_use_tab_frame'])
		frame_label = ttk.LabelFrame(frame_left, text='일반')
		frame_combat = ttk.Frame(frame_label)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '보스 [궁극기] 경고 문구 인식 허용치(0~100):', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING].trace( 
			'w', lambda *args: self.callback_threshold_boss_warning_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING] = 70
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_BOSS_WARNING],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "%"
			)
	
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '글로벌 쿨타임        :', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL].trace( 
			'w', lambda *args: self.callback_global_cool_skill_stringvar(args, option_name=lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL)
			)

		if not lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL] = 3
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_GLOBAL_COOL_SKILL],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= " × 봇 주기"
			)
	
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)





		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '궁극 스킬 쿨타임     :', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL].trace( 
			'w', lambda *args: self.callback_period_boss_skill_stringvar(args, option_name=lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL)
			)

		if not lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= " × 봇 주기"
			)
	
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '도발/평정 스킬 쿨타임:', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1].trace( 
			'w', lambda *args: self.callback_period_boss_skill_1_stringvar(args, option_name=lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1)
			)

		if not lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1] = 30
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_1],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= " × 봇 주기"
			)
	
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '회피 스킬 쿨타임     :', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2].trace( 
			'w', lambda *args: self.callback_period_boss_skill_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2)
			)

		if not lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2] = 3
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOSS_SKILL_2],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= " × 봇 주기"
			)
	
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)

		frame_combat.pack(side=tkinter.LEFT,anchor=tkinter.NW)	
		frame_label.pack(anchor=tkinter.NW, fill=tkinter.X)











		frame_label = ttk.LabelFrame(frame_left, text='궁극 스킬 발동 조건')
		frame_combat = ttk.Frame(frame_label)

		
		frame = ttk.Frame(frame_combat)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL].trace(
			'w', lambda *args: self.callback_use_boss_warning_skill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL)
			)

		if not lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '보스 [궁극기] 경고 문구가 출력될 때 궁극 스킬을 사용합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '내 영웅 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP].trace( 
			'w', lambda *args: self.callback_threshold_hero_hp_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 궁극 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)





		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '대상 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP].trace( 
			'w', lambda *args: self.callback_threshold_target_hp_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 궁극 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원1 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '0'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '0'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_1_hp_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '0')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '0' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '0'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '0'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 궁극 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원2 체력이', 
			justify 			= tkinter.LEFT
			)	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '1'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '1'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_2_hp_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '1')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '1' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '1'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '1'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 궁극 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원3 체력이', 
			justify 			= tkinter.LEFT
			)	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '2'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '2'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_3_hp_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '2')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '2' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '2'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '2'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 궁극 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원4 체력이', 
			justify 			= tkinter.LEFT
			)	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '3'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '3'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_4_hp_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '3')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '3' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '3'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP + '3'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 궁극 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '전투 진행 중 궁극 스킬을', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE].trace( 
			'w', lambda *args: self.callback_random_skill_rate_stringvar(args, option_name=lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE)
			)

		if not lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 확률로 사용하도록 설정합니다"
			)

		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame_combat.pack(side=tkinter.LEFT,anchor=tkinter.NW)		
		frame_label.pack(anchor=tkinter.NW, side=tkinter.LEFT, fill=tkinter.X, expand=True, pady=10)
		frame_left.pack(anchor=tkinter.NW, side=tkinter.LEFT, fill=tkinter.X, expand=True, padx=5, pady=5)

		# 던전 2

















		###############################################
		#                  전투 진행                  #
		###############################################

		frame_right = ttk.Frame(self.inner_frame_dic['skill_use_tab_frame'])
		frame_label = ttk.LabelFrame(frame_right, text='도발/평정 스킬 발동 조건')
		frame_combat = ttk.Frame(frame_label)

		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '내 영웅 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2].trace( 
			'w', lambda *args: self.callback_threshold_hero_hp_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_2],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 도발/평정 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '대상 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2].trace( 
			'w', lambda *args: self.callback_threshold_target_hp_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_2],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 도발/평정 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원1 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '0'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '0'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_1_hp_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '0')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '0' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '0'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '0'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 도발/평정 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원2 체력이', 
			justify 			= tkinter.LEFT
			)	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '1'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '1'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_2_hp_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '1')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '1' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '1'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '1'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 도발/평정 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원3 체력이', 
			justify 			= tkinter.LEFT
			)	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '2'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '2'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_3_hp_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '2')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '2' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '2'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '2'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 도발/평정 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '파티원4 체력이', 
			justify 			= tkinter.LEFT
			)	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '3'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '3'].trace( 
			'w', lambda *args: self.callback_threshold_party_member_4_hp_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '3')
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '3' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '3'] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_PARTY_HP_2 + '3'],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 도발/평정 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)

		label = ttk.Label(
			master 				= frame, 
			text 				= '전투 진행 중 도발/평정 스킬을', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1].trace( 
			'w', lambda *args: self.callback_random_skill_rate_1_stringvar(args, option_name=lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1)
			)

		if not lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_1],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 확률로 사용하도록 설정합니다"
			)

		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame_combat.pack(side=tkinter.LEFT,anchor=tkinter.W)		
		frame_label.pack(anchor=tkinter.NW, fill=tkinter.X)

		# 던전 2

















		###############################################
		#                  전투 진행                  #
		###############################################

		frame_label = ttk.LabelFrame(frame_right, text='회피 스킬 발동 조건')
		frame_combat = ttk.Frame(frame_label)


		frame = ttk.Frame(frame_combat)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE].trace(
			'w', lambda *args: self.callback_use_boss_warning_skill_evade_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE)
			)

		if not lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '보스 [궁극기] 경고 문구가 출력될 때 회피 스킬을 사용합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_USE_BOSS_WARNING_SKILL_EVADE],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '경고 문구 출력 후', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2].trace( 
			'w', lambda *args: self.callback_after_boss_skill_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2)
			)

		if not lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2] = 2
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_AFTER_BOSS_SKILL_2],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 후에 회피 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '내 영웅 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3].trace( 
			'w', lambda *args: self.callback_threshold_hero_hp_3_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_HERO_HP_3],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 회피 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		label = ttk.Label(
			master 				= frame, 
			text 				= '대상 체력이', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3].trace( 
			'w', lambda *args: self.callback_threshold_target_hp_3_stringvar(args, option_name=lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3)
			)

		if not lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_THRESHOLD_TARGET_HP_3],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)
		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 이하로 떨어지면 회피 스킬을 사용합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_combat)
		
		label = ttk.Label(
			master 				= frame, 
			text 				= '전투 진행 중 회피 스킬을', 
			justify 			= tkinter.LEFT
			)
	
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2].trace( 
			'w', lambda *args: self.callback_random_skill_rate_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2)
			)

		if not lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_RANDOM_SKILL_RATE_2],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% 확률로 사용하도록 설정합니다"
			)

		
		label.pack(side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame_combat.pack(side=tkinter.LEFT,anchor=tkinter.W)		
		frame_label.pack(anchor=tkinter.NW, fill=tkinter.X, pady=5)









		frame_label = ttk.LabelFrame(frame_right, text='일반 스킬 쿨타임 설정 (좌측 하단 기준 시계 방향 1 2 3 4)')
		frame_combat = ttk.Frame(frame_label)

		for nsi in range(4):
			frame = ttk.Frame(frame_combat)
			label = ttk.Label(
				master 				= frame, 
				text 				= '스킬'+str(nsi+1)+':'
				)
			label.pack(side=tkinter.LEFT)

			self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)] = tkinter.StringVar(frame)
			if nsi == 0:
				self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)].trace('w', 
					lambda *args: self.callback_normal_skill_0_stringvar(args, lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + '0'))
			elif nsi == 1:
				self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)].trace('w', 
					lambda *args: self.callback_normal_skill_1_stringvar(args, lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + '1'))
			elif nsi == 2:
				self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)].trace('w', 
					lambda *args: self.callback_normal_skill_1_stringvar(args, lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + '2'))
			elif nsi == 3:
				self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)].trace('w', 
					lambda *args: self.callback_normal_skill_1_stringvar(args, lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + '3'))

			combobox_list = []
			for i in range(5, 61):
				combobox_list.append(str(i))

			if not lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)] = combobox_list[-1]

			self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)].set(combobox_list[-1])

			combobox = ttk.Combobox(
				master 				= frame,
				values				= combobox_list, 
				textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_COOL_NORMAL_SKILL + str(nsi)], 
				state 				= "readonly",
				height				= 10,
				width 				= 3,
				font 				= lybconstant.LYB_FONT 
				)
			combobox.set(combobox_list[-1])
			combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

			label = ttk.Label(
				master 				= frame, 
				text 				= '초 '
				)
			label.pack(side=tkinter.LEFT)

			frame.pack(anchor=tkinter.W, side=tkinter.LEFT)



		frame_combat.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.W, side=tkinter.BOTTOM)


		frame_right.pack(anchor=tkinter.NW, side=tkinter.LEFT, fill=tkinter.X, padx=5, pady=5)












































































		# ------- 던전

		frame_label = ttk.LabelFrame(self.inner_frame_dic['dungeon_2_tab_frame'], text='도전')

		difficulty_list = [
			('쉬움', 0), 
			('보통', 1), 
			('어려움', 2),
			('매우 어려움', 3),
			]
		index = 0
		challenge_name_list = []
		for each_challenge in LYBTera.challenge_list:
			frame_t = ttk.Frame(frame_label)
			label = ttk.Label(
			master 				= frame_t, 
			text 				= '%s'%self.preformat_cjk(LYBTera.challenge_list[index], 16)
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
			label.pack(side=tkinter.LEFT)

			challenge_name_list.append(lybconstant.LYB_DO_STRING_MODE_DIFFICULTY + str(index))
			# print(index, 'challenge_name_list:', challenge_name_list[index])

			self.option_dic[challenge_name_list[index]] = tkinter.StringVar(frame_t)
			if index == 0:
				self.option_dic[challenge_name_list[index]].trace('w', 
					lambda *args: self.callback_challenge_difficulty_0_stringvar(args, option_name=challenge_name_list[0]))
			elif index == 1:
				self.option_dic[challenge_name_list[index]].trace('w', 
					lambda *args: self.callback_challenge_difficulty_1_stringvar(args, option_name=challenge_name_list[1]))
			elif index == 2:
				self.option_dic[challenge_name_list[index]].trace('w', 
					lambda *args: self.callback_challenge_difficulty_2_stringvar(args, option_name=challenge_name_list[2]))
			elif index == 3:
				self.option_dic[challenge_name_list[index]].trace('w', 
					lambda *args: self.callback_challenge_difficulty_3_stringvar(args, option_name=challenge_name_list[3]))
			elif index == 4:
				self.option_dic[challenge_name_list[index]].trace('w', 
					lambda *args: self.callback_challenge_difficulty_4_stringvar(args, option_name=challenge_name_list[4]))
			elif index == 5:
				self.option_dic[challenge_name_list[index]].trace('w', 
					lambda *args: self.callback_challenge_difficulty_5_stringvar(args, option_name=challenge_name_list[5]))

			for text, mode in difficulty_list:

				combo_box = ttk.Radiobutton(
					master 				= frame_t,
					text 				= text,
					variable 			= self.option_dic[challenge_name_list[index]],
					value 				= mode

					)
				combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

			if not challenge_name_list[index] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][challenge_name_list[index]] = 0

			index += 1

			frame_t.pack(anchor=tkinter.W)
		frame_label.pack(anchor=tkinter.NW, padx=5, pady=5)

		frame_label = ttk.LabelFrame(self.inner_frame_dic['dungeon_3_tab_frame'], text='기타 설정')

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG].trace(
			'w', lambda *args: self.callback_muhantap_sotang_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG)
			)

		if not lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '무한의 탑 작업은 소탕만 누르고 종료합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_MUHANTAP_SOTANG],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL].trace(
			'w', lambda *args: self.callback_full_party_cancel_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL)
			)

		if not lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '던전 파티 매칭시 풀파티가 아니면 취소합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_FULL_PARTY_CANCEL],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W)

		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "던전 입장 후"
			)
		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START].trace( 
			'w', lambda *args: self.callback_waiting_dungeon_start_stringvar(args, option_name=lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START)
			)

		if not lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_WAITING_DUNGEON_START],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "초가 경과하면 시작합니다"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "던전에서 사망 시 최대 "
			)
		
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH].trace( 
			'w', lambda *args: self.callback_count_dungeon_death_stringvar(args, option_name=lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH)
			)

		if not lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH] = 0
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_COUNT_DUNGEON_DEATH],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "회 즉시 부활하고 최대 부활 횟수를 초과하면 "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH].trace( 
			'w', lambda *args: self.callback_duration_dungeon_death_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH)
			)

		if not lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON_DEATH],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 경과 후 [나가기] 버튼을 누릅니다."
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)





		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "던전 입장 후"
			)
		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH].trace( 
			'w', lambda *args: self.callback_duration_dungeon_each_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH)
			)

		if not lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH] = 10
		
		entry = ttk.Entry(
			master 				= frame, 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON_EACH],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "분이 경과했는데도 클리어되지 않았다면 게임을 종료합니다"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "던전에 입장하면 봇의 작업 주기를"
			)
		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON].trace( 
			'w', lambda *args: self.callback_period_bot_dungeon_stringvar(args, option_name=lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON)
			)

		if not lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON] = 0.1
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_BOT_DUNGEON],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "초로 임시 변경합니다"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		###############################################
		#                  던전 매칭                  #
		###############################################

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "매칭 신청 후"
			)

		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_WAIT_MATCHING] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_WAIT_MATCHING].trace( 
			'w', lambda *args: self.callback_wati_matching_stringvar(args, option_name=lybconstant.LYB_DO_STRING_WAIT_MATCHING)
			)

		if not lybconstant.LYB_DO_STRING_WAIT_MATCHING in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_WAIT_MATCHING] = 30
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_WAIT_MATCHING],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "초가 경과했는데도 매칭이 되지 않았다면 재신청하고 "
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		# frame.pack(anchor=tkinter.W)

		# ###############################################
		# #               게임 제한 시간                #
		# ###############################################

		# frame = ttk.Frame(frame_label)
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "던전 진행 제한 시간 보다 ",
		# 	anchor 				= tkinter.W,
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	)

		
		# label.pack(side=tkinter.LEFT)
		# self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_DUNGEON] = tkinter.StringVar(frame)
		# self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_DUNGEON].trace( 
		# 	'w', lambda *args: self.callback_limit_dungeon_stringvar(args, option_name=lybconstant.LYB_DO_STRING_LIMIT_DUNGEON)
		# 	)

		# if not lybconstant.LYB_DO_STRING_LIMIT_DUNGEON in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_LIMIT_DUNGEON] = 5
		
		# entry = ttk.Entry(
		# 	master 				= frame, 
		# 	relief 				= 'sunken', 
		# 	textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_DUNGEON],
		# 	justify 			= tkinter.RIGHT, 
		# 	width 				= 2,
		# 	font 				= lybconstant.LYB_FONT
		# 	)

		# entry.pack(side=tkinter.LEFT)		
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "분 초과하거나 매칭 재시도를 ",
		# 	justify 			= tkinter.LEFT,
		# 	font 				= lybconstant.LYB_FONT
		# 	)
		# label.pack(side=tkinter.LEFT)	
		self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER].trace( 
			'w', lambda *args: self.callback_limit_dungeon_enter_stringvar(args, option_name=lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER)
			)

		if not lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER] = 5
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_DUNGEON_ENTER],
			justify 			= tkinter.RIGHT, 
			width 				= 2
			)

		entry.pack(side=tkinter.LEFT)	
		label = ttk.Label(
			master 				= frame, 
			text 				= "회 이상 재신청하면 게임을 종료합니다"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		###############################################
		#               일반 던전 진행                #
		###############################################

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "던전 스케쥴 작업 시작 후 "
			)
		
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON].trace('w', 
			lambda *args: self.callback_normal_dungeon_duration_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_DUNGEON))

		if not lybconstant.LYB_DO_STRING_DURATION_DUNGEON in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_DUNGEON] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DUNGEON],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= " 분이 경과하면 남은 횟수 상관 없이 게임을 종료합니다"
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		
		frame_label.pack(anchor=tkinter.W, fill=tkinter.BOTH, pady=5)




























































		###############################################
		#                   영웅                      #
		###############################################




		# ------
		###############################################
		#               특성 설정                     #
		###############################################

		frame_left = ttk.Frame(self.inner_frame_dic['hero_tab_frame'])
		frame = ttk.LabelFrame(frame_left, text='특성')
		select_talent_list = [
			('좌', 0), 
			('중', 1), 
			('우', 2)
			]
		hero_talent_list = []

		for index in range(16):

			frame_t = ttk.Frame(frame)
			label = ttk.Label(
			master 				= frame_t, 
			text 				= 'Lv.%3s  '%str((index+1)*5)
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
			label.pack(side=tkinter.LEFT)
			hero_talent_list.append(lybconstant.LYB_DO_STRING_HERO_TALENT_LEVEL + str(index))

			# print(index, 'challenge_name_list:', challenge_name_list[index])


			self.option_dic[hero_talent_list[index]] = tkinter.StringVar(frame_t)
			if index == 0:
				self.option_dic[hero_talent_list[0]].trace('w', 
					lambda *args: self.callback_hero_talent_0_stringvar(args, option_name=hero_talent_list[0]))
			elif index == 1:
				self.option_dic[hero_talent_list[1]].trace('w', 
					lambda *args: self.callback_hero_talent_1_stringvar(args, option_name=hero_talent_list[1]))
			elif index == 2:
				self.option_dic[hero_talent_list[2]].trace('w', 
					lambda *args: self.callback_hero_talent_2_stringvar(args, option_name=hero_talent_list[2]))
			elif index == 3:
				self.option_dic[hero_talent_list[3]].trace('w', 
					lambda *args: self.callback_hero_talent_3_stringvar(args, option_name=hero_talent_list[3]))
			elif index == 4:
				self.option_dic[hero_talent_list[4]].trace('w', 
					lambda *args: self.callback_hero_talent_4_stringvar(args, option_name=hero_talent_list[4]))
			elif index == 5:
				self.option_dic[hero_talent_list[5]].trace('w', 
					lambda *args: self.callback_hero_talent_5_stringvar(args, option_name=hero_talent_list[5]))
			elif index == 6:
				self.option_dic[hero_talent_list[6]].trace('w', 
					lambda *args: self.callback_hero_talent_6_stringvar(args, option_name=hero_talent_list[6]))
			elif index == 7:
				self.option_dic[hero_talent_list[7]].trace('w', 
					lambda *args: self.callback_hero_talent_7_stringvar(args, option_name=hero_talent_list[7]))
			elif index == 8:
				self.option_dic[hero_talent_list[8]].trace('w', 
					lambda *args: self.callback_hero_talent_8_stringvar(args, option_name=hero_talent_list[8]))
			elif index == 9:
				self.option_dic[hero_talent_list[9]].trace('w', 
					lambda *args: self.callback_hero_talent_9_stringvar(args, option_name=hero_talent_list[9]))
			elif index == 10:
				self.option_dic[hero_talent_list[10]].trace('w', 
					lambda *args: self.callback_hero_talent_10_stringvar(args, option_name=hero_talent_list[10]))
			elif index == 11:
				self.option_dic[hero_talent_list[11]].trace('w', 
					lambda *args: self.callback_hero_talent_11_stringvar(args, option_name=hero_talent_list[11]))
			elif index == 12:
				self.option_dic[hero_talent_list[12]].trace('w', 
					lambda *args: self.callback_hero_talent_12_stringvar(args, option_name=hero_talent_list[12]))
			elif index == 13:
				self.option_dic[hero_talent_list[13]].trace('w', 
					lambda *args: self.callback_hero_talent_13_stringvar(args, option_name=hero_talent_list[13]))
			elif index == 14:
				self.option_dic[hero_talent_list[14]].trace('w', 
					lambda *args: self.callback_hero_talent_14_stringvar(args, option_name=hero_talent_list[14]))
			elif index == 15:
				self.option_dic[hero_talent_list[15]].trace('w', 
					lambda *args: self.callback_hero_talent_15_stringvar(args, option_name=hero_talent_list[15]))

			for text, mode in select_talent_list:

				combo_box = ttk.Radiobutton(
					master 				= frame_t,
					text 				= text,
					variable 			= self.option_dic[hero_talent_list[index]],
					value 				= mode

					)
				combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

			if not hero_talent_list[index] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][hero_talent_list[index]] = 0

			frame_t.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)		
		frame_left.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=10, pady=5)

		# -------------------------------

		frame_left = ttk.Frame(self.inner_frame_dic['hero_tab_frame'])
		frame = ttk.LabelFrame(frame_left, text='스킬')


		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "이 기능을 사용하지 않으려면",
			foreground			= 'red',
			background			= 'yellow'
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[영웅 스킬]을 스케쥴에 넣지마세요",
			foreground			= 'red',
			background			= 'yellow'
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W, pady=10)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "아래 나열된 스킬들을 MAX 까지"
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "순서대로 올립니다"
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "체크를 해제하면 스킬 레벨을"
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "올리지 않습니다"
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W, pady=10)
		
		hero_skill_list = []
		for i in range(8):
			frame_s = ttk.Frame(frame)

			hero_skill_list.append(lybconstant.LYB_DO_BOOLEAN_HERO_SKILL + str(i))
			self.option_dic[hero_skill_list[i]] = tkinter.BooleanVar(frame_s)

			check_box = ttk.Checkbutton(

				master 				= frame_s,
				text 				= '', 
				variable 			= self.option_dic[hero_skill_list[i]],
				onvalue 			= True, 
				offvalue 			= False
			)

			if i == 0:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_0_booleanvar(args, hero_skill_list[0])
					)
				check_box.configure(text='일반 공격 (중앙)')
			elif i == 1:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_1_booleanvar(args, hero_skill_list[1])
					)
				check_box.configure(text='연계기1   (좌측 하단 첫 번째)')
			elif i == 2:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_2_booleanvar(args, hero_skill_list[2])
					)
				check_box.configure(text='액티브1   (연계기1 연결)')
			elif i == 3:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_3_booleanvar(args, hero_skill_list[3])
					)
				check_box.configure(text='액티브2   (액티브1 상단)')
			elif i == 4:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_4_booleanvar(args, hero_skill_list[4])
					)
				check_box.configure(text='액티브3   (액티브2 상단)')
			elif i == 5:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_5_booleanvar(args, hero_skill_list[5])
					)
				check_box.configure(text='액티브4   (액티브3 우측상단)')
			elif i == 6:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_6_booleanvar(args, hero_skill_list[6])
					)
				check_box.configure(text='연계기2   (액티브3 연결)')
			elif i == 7:
				self.option_dic[hero_skill_list[i]].trace(
					'w', lambda *args: self.callback_hero_skill_7_booleanvar(args, hero_skill_list[7])
					)
				check_box.configure(text='궁극기    (상단)')

			if not hero_skill_list[i] in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][hero_skill_list[i]] = True

			check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
			frame_s.pack(side=tkinter.TOP, anchor=tkinter.W)

		frame.pack(anchor=tkinter.W)		
		frame_left.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=10, pady=5)

		# -------------------------------

		frame_left = ttk.Frame(self.inner_frame_dic['hero_tab_frame'])
		frame = ttk.LabelFrame(frame_left, text='친밀도')

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "아래 체크된 친밀도 NPC 들을"
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame_s, 
			text 				= "위에서부터 아래로 순차적으로 방문하며", 
			justify 			= tkinter.LEFT
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)
		
		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame_s, 
			text 				= "아이템 등급 "
			)
		label.pack(anchor=tkinter.W, side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK] = tkinter.StringVar(frame_s)
		self.option_dic[lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK].trace('w', 
			lambda *args: self.callback_chinmildo_item_rank_stringvar(args, lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK))

		if not lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK] = LYBTera.item_rank_list[0]

		self.option_dic[lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK].set(LYBTera.item_rank_list[0])

		combobox = ttk.Combobox(
			master 				= frame_s,
			values				= LYBTera.item_rank_list, 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_CHINMILDO_ITEM_RANK],
			state 				= "readonly",
			height				= 6,
			width				= 4,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(LYBTera.item_rank_list[0])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)


		label = ttk.Label(
			master 				= frame_s, 
			text 				= " 이하 아이템을 선물합니다"
			)
		label.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame_s.pack(anchor=tkinter.NW)

		frame_s = ttk.Frame(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO].trace(
			'w', lambda *args: self.callback_debug_chinmildo_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO)
			)

		if not lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO] = True

		check_box = ttk.Checkbutton(

			master 				= frame_s,
			text 				= '친밀도 테스트 모드(선물하기 버튼을 누르지 않습니다)', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_DEBUG_CHINMILDO],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame, 
			text 				= "※ 아이템 손해에 대해 책임지지 않습니다",
			foreground			= 'red',
			background			= 'yellow'
			)
		label.pack(anchor=tkinter.W)
		frame_s.pack(anchor=tkinter.W)

		frame_s = ttk.Frame(frame)
		label = ttk.Label(
			master 				= frame_s, 
			text 				= "친밀도 아이템 탐색할 페이지 수: "
			)
		label.pack(anchor=tkinter.W, side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG].trace( 
			'w', lambda *args: self.callback_count_chinmildo_drag_stringvar(args, option_name=lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG)
			)

		if not lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG] = 2
		
		entry = ttk.Entry(
			master 				= frame_s,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_COUNT_CHINMILDO_DRAG],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame_s.pack(anchor=tkinter.W, pady=5)

		frame_s = ttk.Frame(frame)
		each_npc_gift_list = []
		i = 0
		k = 0
		for each_npc in LYBTera.chinmildo_npc_list:
			frame_npc = ttk.LabelFrame(frame_s, text=each_npc)

			j = 0
			for each_gift in LYBTera.gift_item_list:
				frame_gift = ttk.Frame(frame_npc)
				each_npc_gift_list.append(lybconstant.LYB_DO_BOOLEAN_CHINMILDO_NPC_GIFT + str(i) + str(j))
				self.option_dic[each_npc_gift_list[k]] = tkinter.BooleanVar(frame_gift)

				check_box = ttk.Checkbutton(

					master 				= frame_gift,
					text 				= LYBTera.gift_item_list[j], 
					variable 			= self.option_dic[each_npc_gift_list[k]],
					onvalue 			= True, 
					offvalue 			= False
				)

				if k == 0:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_00_booleanvar(args, each_npc_gift_list[0])
						)
				elif k == 1:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_01_booleanvar(args, each_npc_gift_list[1])
						)
				elif k == 2:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_02_booleanvar(args, each_npc_gift_list[2])
						)
				elif k == 3:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_03_booleanvar(args, each_npc_gift_list[3])
						)
				elif k == 4:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_04_booleanvar(args, each_npc_gift_list[4])
						)
				elif k == 5:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_10_booleanvar(args, each_npc_gift_list[5])
						)
				elif k == 6:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_11_booleanvar(args, each_npc_gift_list[6])
						)
				elif k == 7:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_12_booleanvar(args, each_npc_gift_list[7])
						)
				elif k == 8:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_13_booleanvar(args, each_npc_gift_list[8])
						)
				elif k == 9:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_14_booleanvar(args, each_npc_gift_list[9])
						)
				elif k == 10:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_20_booleanvar(args, each_npc_gift_list[10])
						)
				elif k == 11:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_21_booleanvar(args, each_npc_gift_list[11])
						)
				elif k == 12:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_22_booleanvar(args, each_npc_gift_list[12])
						)
				elif k == 13:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_23_booleanvar(args, each_npc_gift_list[13])
						)
				elif k == 14:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_24_booleanvar(args, each_npc_gift_list[14])
						)
				elif k == 15:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_30_booleanvar(args, each_npc_gift_list[15])
						)
				elif k == 16:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_31_booleanvar(args, each_npc_gift_list[16])
						)
				elif k == 17:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_32_booleanvar(args, each_npc_gift_list[17])
						)
				elif k == 18:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_33_booleanvar(args, each_npc_gift_list[18])
						)
				elif k == 19:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_34_booleanvar(args, each_npc_gift_list[19])
						)
				elif k == 20:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_40_booleanvar(args, each_npc_gift_list[20])
						)
				elif k == 21:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_41_booleanvar(args, each_npc_gift_list[21])
						)
				elif k == 22:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_42_booleanvar(args, each_npc_gift_list[22])
						)
				elif k == 23:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_43_booleanvar(args, each_npc_gift_list[23])
						)
				elif k == 24:					
					self.option_dic[each_npc_gift_list[k]].trace(
						'w', lambda *args: self.callback_chinmildo_npc_44_booleanvar(args, each_npc_gift_list[24])
						)


				if not each_npc_gift_list[k] in self.configure.common_config[self.game_name]:
					self.configure.common_config[self.game_name][each_npc_gift_list[k]] = False


				j += 1
				k += 1


				check_box.pack(anchor=tkinter.W)
				frame_gift.pack(side=tkinter.LEFT, anchor=tkinter.W)

			frame_npc.pack(anchor=tkinter.W)
			i += 1
		frame_s.pack(anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)
		frame_left.pack(anchor=tkinter.W)

		frame_left.pack(anchor=tkinter.NW, side=tkinter.LEFT, padx=5, pady=5)
























		#옵션
		#강화 등급 A 포함 선택
		#강화 등급 S 포함 선택
		#연마제 우선 선택
		#강화 등급 선택
		#일반 B~C
		#고급, 희귀, 영웅, 전설, 신화
		###############################################
		#                  장비                       #
		###############################################

		background_color_hex = '#3f74c6'
		s = ttk.Style()
		s.configure('inventory_bg.TFrame', background=background_color_hex)

		frame = ttk.Frame(self.inner_frame_dic['item_tab_frame'])
		label = ttk.Label(
			master 				= frame, 
			text 				= "※ 해당 기능을 사용하면서 발생하는 모든 현상에 대해 프로그램 제작자는 책임지지 않습니다. 이에 동의하는 분들만 사용하세요",
			foreground			= 'red',
			background			= 'yellow'
			)

		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, padx=5)

		frame_left = ttk.Frame(self.inner_frame_dic['item_tab_frame'])
		frame_bound = ttk.Frame(frame_left)
		for i in range(len(LYBTera.item_loc_list)):
			# l = ttk.Label(text=LYBTera.item_loc_list[i])
			frame_label = ttk.LabelFrame(frame_bound, text=LYBTera.item_loc_list[i])
			frame = ttk.Frame(frame_label)
			for j in range(len(LYBTera.item_levelup_option_list)):

				self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)] = tkinter.BooleanVar(frame)

				if i == 0:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar00(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '00')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar01(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '01')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar02(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '02')
						)						
				elif i == 1:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar10(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '10')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar11(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '11')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar12(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '12')
						)	
				elif i == 2:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar20(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '20')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar21(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '21')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar22(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '22')
						)	
				elif i == 3:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar30(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '30')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar31(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '31')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar32(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '32')
						)	
				elif i == 4:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar40(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '40')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar41(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '41')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar42(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '42')
						)	
				elif i == 5:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar50(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '50')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar51(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '51')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar52(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '52')
						)	
				elif i == 6:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar60(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '60')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar61(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '61')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar62(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '62')
						)	
				elif i == 7:
					if j == 0:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar70(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '70')
						)
					elif j == 1:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar71(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '71')
						)
					else:
						self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)].trace(
						'w', lambda *args: self.callback_item_levelup_option_booleanvar72(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + '72')
						)	

				if not lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j) in self.configure.common_config[self.game_name]:
					if j == 1:
						self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)] = False
					else:
						self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)] = True


				check_box = ttk.Checkbutton(

					master 				= frame,
					text 				= LYBTera.item_levelup_option_list[j],
					variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_OPTION + str(i) + str(j)],
					onvalue 			= True, 
					offvalue 			= False
					# bg 					= background_color_hex,
					# fg 					= 'white'
				)
				check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
				if j > 0:
					frame.pack(anchor=tkinter.W)
					frame = ttk.Frame(frame_label)

			frame.pack(anchor=tkinter.W)

			frame = ttk.Frame(frame_label)

			self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)] = tkinter.StringVar(frame)
			if not lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i) in self.configure.common_config[self.game_name]:
				self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)] = 1

			for j in range(len(LYBTera.item_rank_list)):

				if i == 0:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar0(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '0')
						)	
				elif i == 1:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar1(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '1')
						)
				elif i == 2:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar2(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '2')
						)
				elif i == 3:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar3(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '3')
						)
				elif i == 4:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar4(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '4')
						)
				elif i == 5:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar5(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '5')
						)
				elif i == 6:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar6(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '6')
						)
				elif i == 7:
					self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)].trace(
						'w', lambda *args: self.callback_item_levelup_rank_booleanvar7(args, lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + '7')
						)

				font_color = 'white'
				if j % 6 == 0:
					font_color = 'white'
				elif j % 6 == 1:
					font_color = '#9dff00'
				elif j % 6 == 2:
					font_color = '#84abe8'
				elif j % 6 == 3:
					font_color = 'purple'
				elif j % 6 == 4:
					font_color = '#fc2062'
				elif j % 6 == 5:
					font_color = '#fcd320'

				combo_box = ttk.Radiobutton(
					master 				= frame,
					text 				= LYBTera.item_rank_list[j],
					variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_LEVELUP_ITEM_RANK + str(i)],
					value 				= j

					)
				combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

			frame.pack(anchor=tkinter.W)

			frame_label.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=10, pady=1)

			if i % 2 == 1:
				frame_bound.pack(anchor=tkinter.W)
				frame_bound = ttk.Frame(frame_left)

		frame_left.pack(side=tkinter.LEFT, anchor=tkinter.NW, pady=10)

		frame_right = ttk.Frame(self.inner_frame_dic['item_tab_frame'])
		frame_inner = ttk.Frame(frame_right)


		frame_label = ttk.LabelFrame(frame_inner, text='레벨업 장비 세트')
		
		self.option_dic[lybconstant.LYB_DO_STRING_LEVELUP_EQUIP_SET] = tkinter.StringVar(frame_t)

		self.option_dic[lybconstant.LYB_DO_STRING_LEVELUP_EQUIP_SET].trace('w', 
			lambda *args: self.callback_levelup_equip_set_stringvar(args, option_name=lybconstant.LYB_DO_STRING_LEVELUP_EQUIP_SET))

		select_equip_set_list = [
			('세트 1', 0),
			('세트 2', 1),
			('세트 3', 2)
			]

		for text, mode in select_equip_set_list:

			combo_box = ttk.Radiobutton(
				master 				= frame_label,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_LEVELUP_EQUIP_SET],
				value 				= mode

				)
			combo_box.pack()

		if not lybconstant.LYB_DO_STRING_EQUIP_SET in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_LEVELUP_EQUIP_SET] = 0

		frame_label.pack(pady=5)

		frame_label = ttk.LabelFrame(frame_inner, text='장착할 장비 세트')
		
		self.option_dic[lybconstant.LYB_DO_STRING_EQUIP_SET] = tkinter.StringVar(frame_t)

		self.option_dic[lybconstant.LYB_DO_STRING_EQUIP_SET].trace('w', 
			lambda *args: self.callback_equip_set_stringvar(args, option_name=lybconstant.LYB_DO_STRING_EQUIP_SET))

		select_equip_set_list = [
			('세트 1', 0),
			('세트 2', 1),
			('세트 3', 2)
			]

		for text, mode in select_equip_set_list:

			combo_box = ttk.Radiobutton(
				master 				= frame_label,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_EQUIP_SET],
				value 				= mode

				)
			combo_box.pack()

		if not lybconstant.LYB_DO_STRING_EQUIP_SET in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_EQUIP_SET] = 0

		frame_label.pack(pady=5)

		frame_label = ttk.LabelFrame(frame_inner, text='대장간 레벨업 등급')
		frame = ttk.Frame(frame_label)
		
		self.option_dic[lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK] = tkinter.StringVar(frame)

		self.option_dic[lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK].trace('w', 
			lambda *args: self.callback_dejanggan_levelup_rank_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK))

		radiobutton_list = [
			('신화', 0),
			('전설', 1),
			('영웅', 2),
			('희귀', 3)
			]

		for text, mode in radiobutton_list:

			radiobutton = ttk.Radiobutton(
				master 				= frame,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK],
				value 				= mode

				)
			radiobutton.pack()
			self.tooltip(radiobutton, text +' 등급 이상 장비를 순차적으로 레벨업합니다.')

		if not lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DEJANGGAN_LEVELUP_RANK] = 0

		frame.pack()
		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "검색 횟수: "
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG].trace('w', 
			lambda *args: self.callback_smithy_limit_drag_stringvar(args, lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG))

		combobox_list = []
		for i in range(11):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG] = combobox_list[-1]

		self.option_dic[lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG].set(combobox_list[-1])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_SMITHY_LIMIT_DRAG], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(combobox_list[-1])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)
		frame.pack()

		frame_label.pack(pady=5)


		

		frame_inner.pack(pady=5)
		frame_right.pack()
























		###############################################
		#                퀘스트 진행                  #
		###############################################

		frame_label = ttk.LabelFrame(self.inner_frame_dic['quest_tab_frame'], text='메인')



		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "[채널 변경] 작업할 때 가장 "
			)		
		label.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic['channel_favorite'] = []
		for item in LYBTera.channel_favorite:
			self.option_dic['channel_favorite'].append(item)

		self.option_dic[lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE].trace('w', 
			lambda *args: self.callback_channel_list_stringvar(args, option_name=lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE))

		if not lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE] = self.option_dic['channel_favorite'][0]

		self.option_dic[lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE].set(self.option_dic['channel_favorite'][0])


		combobox = ttk.Combobox(
			master 				= frame,
			values				= self.option_dic['channel_favorite'], 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_CHANNEL_FAVORITE],
			state 				= "readonly",
			height				= 10,
			width				= 5,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.option_dic['channel_favorite'][0])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "한 채널로 변경하고 실패시 최대"
			)		
		label.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_RETRY_CHANNEL] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_RETRY_CHANNEL].trace('w', 
			lambda *args: self.callback_retry_channel_stringvar(args, option_name=lybconstant.LYB_DO_STRING_RETRY_CHANNEL))

		if not lybconstant.LYB_DO_STRING_RETRY_CHANNEL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_RETRY_CHANNEL] = 3
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_RETRY_CHANNEL],
			justify 			= tkinter.RIGHT, 
			width 				= 3
			)

		entry.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "회 재시도합니다"
			)		
		label.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[추적] 감지 허용 횟수:"
			)

		label.pack(side=tkinter.LEFT)
		
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_TRACKING] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_TRACKING].trace('w', 
			lambda *args: self.callback_period_tracking_stringvar(args, option_name=lybconstant.LYB_DO_STRING_PERIOD_TRACKING))

		if not lybconstant.LYB_DO_STRING_PERIOD_TRACKING in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_PERIOD_TRACKING] = 3
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_PERIOD_TRACKING],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "회"
			)

		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[메인 퀘스트]를 "
			)

		label.pack(side=tkinter.LEFT)
		option_name_mq = lybconstant.LYB_DO_STRING_DURATION_MAIN_QUEST
		self.option_dic[option_name_mq] = tkinter.StringVar(frame)
		self.option_dic[option_name_mq].trace('w', lambda *args: self.callback_main_quest_stringvar(args, option_name=option_name_mq))

		if not option_name_mq in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][option_name_mq] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[option_name_mq],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "분 동안 진행합니다"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[보스 퀘스트]를 최대"
			)

		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST].trace('w', 
			lambda *args: self.callback_boss_quest_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST))

		if not lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST] = 5
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_BOSS_QUEST],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "분 진행 후 종료하거나 최근"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS].trace('w', 
			lambda *args: self.callback_last_boss_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS))

		if not lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS] = 10
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_LAST_BOSS],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "분 안에 보스를 잡은 적이 있다면 종료합니다."
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W)





		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[몬스터 추적]을 최대"
			)

		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE].trace('w', 
			lambda *args: self.callback_duration_monster_chase_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE))

		if not lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE] = 3
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MONSTER_CHASE],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "분 동안 진행합니다"
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		###############################################
		#                  건너뛰기                   #
		###############################################

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[건너 뛰기][그만 보기] 체크 주기: "
			)

		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_SKIP_PERIOD] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_SKIP_PERIOD].trace( 
			'w', lambda *args: self.callback_skip_period_stringvar(args, option_name=lybconstant.LYB_DO_STRING_SKIP_PERIOD)
			)

		if not lybconstant.LYB_DO_STRING_SKIP_PERIOD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_SKIP_PERIOD] = 2
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_SKIP_PERIOD],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "초"
			)

		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[건너 뛰기][그만 보기] 인식 허용치(0~100): "
			)

		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2].trace( 
			'w', lambda *args: self.callback_skip_threshold_2_stringvar(args, option_name=lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2)
			)

		if not lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_SKIP_THRESHOLD_2],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "% (100보다 큰 값을 설정하면 동영상을 끝까지 다 봅니다)"
			)

		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[메인][서브][던전][토벌대][완료][도전][지역] 인식 허용치(0~100): "
			)		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD].trace( 
			'w', lambda *args: self.callback_mainscene_quest_threshold_stringvar(args, option_name=lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD)
			)

		if not lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD] = 70
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_MAINSCENE_QUEST_THRESHOLD],
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




		###############################################
		#                  부활 진행                  #
		###############################################

		frame = ttk.Frame(frame_label)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_STOP_WORKING] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_STOP_WORKING].trace(
			'w', lambda *args: self.callback_stop_working_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_STOP_WORKING)
			)

		if not lybconstant.LYB_DO_BOOLEAN_STOP_WORKING in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_STOP_WORKING] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '[메인 퀘스트] 작업 중 캐릭터가 사망하게 되면 부활 후 다음 작업을 수행합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_STOP_WORKING],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU].trace(
			'w', lambda *args: self.callback_eliminate_buhyu_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU)
			)

		if not lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '부활 후유증을 제거합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_ELIMINATE_BUHYU],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)




		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "중복 로그인 이벤트가 감지되면 "
			)		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM].trace( 
			'w', lambda *args: self.callback_delay_duplicate_confirm_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM)
			)

		if not lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM] = 300
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DELAY_DUPLICATE_CONFIRM],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 동안 대기했다가 클릭합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)



		#-------------------------------------------
		#
		# 가방 풀
		#
		#-------------------------------------------

		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL].trace(
			'w', lambda *args: self.callback_stop_inventory_full_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL)
			)

		if not lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '가방이 가득차면 등록된 [일괄 판매][친밀도][장비 레벨업] 작업을 수행합니다', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_STOP_INVENTORY_FULL],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)
		frame.pack(anchor=tkinter.W)


		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "이벤트 보상 체크 주기(초)"
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period'].trace(
			'w', lambda *args: self.callback_etc_event_check_period(args, lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period')
			)
		combobox_list = []
		for i in range(0, 86401, 600):
			combobox_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period'] = 0

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period'], 
			state 				= "readonly",
			height				= 10,
			width 				= 7,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TERA_ETC + 'event_check_period'])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)	
		frame.pack(anchor=tkinter.NW)


		frame_label.pack(anchor=tkinter.NW, fill=tkinter.X, padx=5, pady=5)















































































































		frame_label = ttk.LabelFrame(self.inner_frame_dic['guild_tab_frame'], text='길드 기부')
		
		frame = ttk.Frame(frame_label)

		select_guild_donate_list = [
			('초급 기부', 0), 
			('중급 기부', 1), 
			('고급 기부', 2)
			]

		frame_t = ttk.Frame(frame)

		self.option_dic[lybconstant.LYB_DO_STRING_GUILD_DONATE] = tkinter.StringVar(frame_t)

		self.option_dic[lybconstant.LYB_DO_STRING_GUILD_DONATE].trace('w', 
			lambda *args: self.callback_guild_donate_stringvar(args, option_name=lybconstant.LYB_DO_STRING_GUILD_DONATE))

		for text, mode in select_guild_donate_list:

			combo_box = ttk.Radiobutton(
				master 				= frame_t,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_GUILD_DONATE],
				value 				= mode

				)
			combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		if not lybconstant.LYB_DO_STRING_GUILD_DONATE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_GUILD_DONATE] = 0

		frame_t.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(anchor=tkinter.W, fill=tkinter.X, pady=5)


		frame_label = ttk.LabelFrame(self.inner_frame_dic['guild_tab_frame'], text='티아란의 나무')
		
		frame = ttk.Frame(frame_label)

		select_tiaran_gift_list = [
			('성수 뿌려주기', 0), 
			('고급 비료주기', 1), 
			('물 뿌려주기', 2), 
			('일반 비료주기', 3), 
			('잡초 뽑기', 4)
			]

		frame_t = ttk.Frame(frame)

		self.option_dic[lybconstant.LYB_DO_STRING_TIARAN_GIVE] = tkinter.StringVar(frame_t)

		self.option_dic[lybconstant.LYB_DO_STRING_TIARAN_GIVE].trace('w', 
			lambda *args: self.callback_tiaran_give_stringvar(args, option_name=lybconstant.LYB_DO_STRING_TIARAN_GIVE))

		for text, mode in select_tiaran_gift_list:

			combo_box = ttk.Radiobutton(
				master 				= frame_t,
				text 				= text,
				variable 			= self.option_dic[lybconstant.LYB_DO_STRING_TIARAN_GIVE],
				value 				= mode

				)
			combo_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		if not lybconstant.LYB_DO_STRING_TIARAN_GIVE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TIARAN_GIVE] = 3

		frame_t.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(anchor=tkinter.W,  fill=tkinter.X, pady=5)




		frame_label = ttk.LabelFrame(self.inner_frame_dic['guild_tab_frame'], text='길드 상점')
		
		frame = ttk.Frame(frame_label)

		label = ttk.Label(
			master 				= frame, 
			text 				= "경험치 물약 구매 갯수:"
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_GUILD_EXP_POTION] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_GUILD_EXP_POTION].trace('w', 
			lambda *args: self.callback_guild_exp_potion_stringvar(args, lybconstant.LYB_DO_STRING_GUILD_EXP_POTION))

		potion_list = []
		for i in range(10):
			potion_list.append(str(i + 1))

		if not lybconstant.LYB_DO_STRING_GUILD_EXP_POTION in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_GUILD_EXP_POTION] = potion_list[-1]

		self.option_dic[lybconstant.LYB_DO_STRING_GUILD_EXP_POTION].set(potion_list[-1])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= potion_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_GUILD_EXP_POTION], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(potion_list[-1])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(anchor=tkinter.W,  fill=tkinter.X, pady=5)




		frame_label = ttk.LabelFrame(self.inner_frame_dic['guild_tab_frame'], text='길드 스킬')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0].trace(
			'w', lambda *args: self.callback_guild_skill_0_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0)
			)

		if not lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '공격력', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_0],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)


		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1].trace(
			'w', lambda *args: self.callback_guild_skill_1_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1)
			)

		if not lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '방어력', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_1],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)



		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2].trace(
			'w', lambda *args: self.callback_guild_skill_2_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2)
			)

		if not lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= 'HP', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_2],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)



		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3].trace(
			'w', lambda *args: self.callback_guild_skill_3_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3)
			)

		if not lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '저항', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_GUILD_SKILL_3],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)


		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(anchor=tkinter.W,  fill=tkinter.X, pady=5)

























		frame_booster = ttk.Frame(self.inner_frame_dic['shop_tab_frame'])

		frame_label = ttk.LabelFrame(frame_booster, text='경험치 부스터 구매 설정')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1].trace(
			'w', lambda *args: self.callback_shop_exp_booster_1_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '1시간', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_1],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2].trace(
			'w', lambda *args: self.callback_shop_exp_booster_2_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '2시간', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_2],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5].trace(
			'w', lambda *args: self.callback_shop_exp_booster_5_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '5시간', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_EXP_BOOSTER_5],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(side=tkinter.LEFT, anchor=tkinter.W, pady=5, padx=5)







		frame = ttk.Frame(frame_booster)
		frame.pack(side=tkinter.LEFT, anchor=tkinter.W, pady=5, padx=10)







		frame_label = ttk.LabelFrame(frame_booster, text='골드 부스터 구매 설정')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1].trace(
			'w', lambda *args: self.callback_shop_gold_booster_1_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '1시간', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_1],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2].trace(
			'w', lambda *args: self.callback_shop_gold_booster_1_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '2시간', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_2],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5].trace(
			'w', lambda *args: self.callback_shop_gold_booster_1_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5 in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5] = True

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '5시간', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SHOP_GOLD_BOOSTER_5],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W, padx=5)

		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(anchor=tkinter.W, pady=5)

		frame_booster.pack(anchor=tkinter.W,  fill=tkinter.X, pady=5)

		frame = ttk.Frame(self.inner_frame_dic['shop_tab_frame'])

		label = ttk.Label(
			master 				= frame, 
			text 				= "부스터 아이템을 찾지 못 했을 경우 인벤토리 드래그 횟수:"
			)		
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT].trace('w', 
			lambda *args: self.callback_exp_drag_count_stringvar(args, lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT))

		drag_list = []
		for i in range(1,30):
			drag_list.append(str(i))

		if not lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT] = drag_list[1]

		self.option_dic[lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT].set(drag_list[1])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= drag_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_EXP_DRAG_COUNT], 
			state 				= "readonly",
			height				= 10,
			width 				= 3,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(drag_list[1])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "회"
			)
		label.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, pady=5)

















































		frame_screenshot = ttk.Frame(self.inner_frame_dic['monitoring_tab_frame'])

		frame_label = ttk.LabelFrame(frame_screenshot, text='스크린 샷')
		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL].trace(
			'w', lambda *args: self.callback_use_screenshot_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL)
			)

		if not lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '필드 보스 결과 화면', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_SCREENSHOT_BOSS_KILL],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(anchor=tkinter.W)

		frame.pack(anchor=tkinter.W, pady=5)
		frame_label.pack(anchor=tkinter.W, padx=5, pady=5)

		frame_label = ttk.LabelFrame(frame_screenshot, text='텔레그램 알림')








		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work')
			)

		if not lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '작업이 시작했을 경우 보낼 메세지 : ', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'start_work'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work')
			)

		if not lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work'] = '작업 시작'

		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'start_work'],
			width 				= 50,
			font 				= lybconstant.LYB_FONT 
			)

		entry.pack(side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, pady=5)







		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill')
			)

		if not lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '필드 보스 킬했을 경우 보낼 메세지: ',
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'bosskill'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill')
			)

		if not lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill'] = '필드 보스를 잡았습니다'

		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'bosskill'],
			width 				= 50,
			font 				= lybconstant.LYB_FONT 
			)

		entry.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill')
			)

		if not lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '스크린샷 보내기',
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'bosskill'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)	

		frame.pack(anchor=tkinter.W, pady=5)
		







		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear')
			)

		if not lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '던전 클리어했을 경우 보낼 메세지 : ', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'dungeon_clear'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear')
			)

		if not lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear'] = '던전을 클리어했습니다'

		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'dungeon_clear'],
			width 				= 50,
			font 				= lybconstant.LYB_FONT 
			)

		entry.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear')
			)

		if not lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '스크린샷 보내기',
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_IMAGE + 'dungeon_clear'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)	

		frame.pack(anchor=tkinter.W, pady=5)













		frame = ttk.Frame(frame_label)

		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full'] = tkinter.BooleanVar(frame)
		self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full')
			)

		if not lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full'] = False

		check_box = ttk.Checkbutton(

			master 				= frame,
			text 				= '가방이 가득 찼을 경우 보낼 메세지: ', 
			variable 			= self.option_dic[lybconstant.LYB_DO_BOOLEAN_TELEGRAM_NOTIFY + 'inventory_full'],
			onvalue 			= True, 
			offvalue 			= False
		)
		check_box.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full'] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full'].trace(
			'w', lambda *args: self.callback_telegram_boss_kill_booleanvar(args, lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full')
			)

		if not lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full' in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full'] = '가방이 가득 찼습니다'

		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_TELEGRAM_ENTRY + 'inventory_full'],
			width 				= 50,
			font 				= lybconstant.LYB_FONT 
			)

		entry.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W, pady=5)







		frame_label.pack(anchor=tkinter.W, padx=5, pady=5)

		frame_screenshot.pack(anchor=tkinter.W)







































		frame_game_config = ttk.Frame(self.inner_frame_dic['game_config_tab_frame'])

		frame = ttk.Frame(frame_game_config)

		label = ttk.Label(
			master 				= frame, 
			text 				= "파티 초대 거절:"
			)		
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY].trace('w', 
			lambda *args: self.callback_game_config_invite_party_stringvar(args, lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY))

		combobox_list = LYBTera.game_config_boolean_list

		if not lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY] = combobox_list[-1]

		self.option_dic[lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY].set(combobox_list[-1])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_GAME_CONFIG_INVITE_PARTY], 
			state 				= "readonly",
			height				= 10,
			width 				= 10,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(combobox_list[-1])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		frame.pack(anchor=tkinter.W, pady=5)
		frame_game_config.pack(anchor=tkinter.W)

















































































		frame_local_move = ttk.Frame(self.inner_frame_dic['move_tab_frame'])

		frame = ttk.Frame(frame_local_move)

		label = ttk.Label(
			master 				= frame, 
			text 				= "[파티원에게 이동] 작업할 때 "
			)

		
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_PARTY_LOC] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_PARTY_LOC].trace('w', 
			lambda *args: self.callback_party_loc_stringvar(args, lybconstant.LYB_DO_STRING_PARTY_LOC))

		combobox_list = []
		for i in range(1,5):
			combobox_list.append(i)

		if not lybconstant.LYB_DO_STRING_PARTY_LOC in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_PARTY_LOC] = combobox_list[0]

		self.option_dic[lybconstant.LYB_DO_STRING_PARTY_LOC].set(combobox_list[0])

		combobox = ttk.Combobox(
			master 				= frame,
			values				= combobox_list, 
			textvariable		= self.option_dic[lybconstant.LYB_DO_STRING_PARTY_LOC], 
			state 				= "readonly",
			height				= 5,
			width 				= 2,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(combobox_list[0])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "번 파티원에게로 이동합니다"
			)		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_local_move)
		label = ttk.Label(
			master 				= frame, 
			text 				= "지역 인식 허용치(0~100) : "
			)

		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_AREA_THRESHOLD] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_AREA_THRESHOLD].trace( 
			'w', lambda *args: self.callback_area_threshold_stringvar(args, option_name=lybconstant.LYB_DO_STRING_AREA_THRESHOLD)
			)

		if not lybconstant.LYB_DO_STRING_AREA_THRESHOLD in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_AREA_THRESHOLD] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_AREA_THRESHOLD],
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




		frame = ttk.Frame(frame_local_move)
		label = ttk.Label(
			master 				= frame, 
			text 				= "분쟁 지역이 감지되면 최대 "
			)

		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_BATTLE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_BATTLE].trace( 
			'w', lambda *args: self.callback_duration_battle_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_BATTLE)
			)

		if not lybconstant.LYB_DO_STRING_DURATION_BATTLE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_BATTLE] = 160
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_BATTLE],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 동안 머무르고 [나가기] 클릭 합니다"
			)

		
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)



		frame = ttk.Frame(frame_local_move)

		label = ttk.Label(
			master 				= frame, 
			text 				= "[지역 이동] 작업할 때 이동할 지역 선택: "
			)		
		label.pack(side=tkinter.LEFT, anchor=tkinter.W)

		self.option_dic['sub_area_list'] = []
		for area, sub_area_list in LYBTera.sub_area_dic.items():
			for sub_area in sub_area_list:
				self.option_dic['sub_area_list'].append(sub_area)

		self.option_dic[lybconstant.LYB_DO_STRING_SUB_AREA] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_SUB_AREA].trace('w', 
			lambda *args: self.callback_sub_area_stringvar(args, option_name=lybconstant.LYB_DO_STRING_SUB_AREA))

		if not lybconstant.LYB_DO_STRING_SUB_AREA in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_SUB_AREA] = self.option_dic['sub_area_list'][0]

		self.option_dic[lybconstant.LYB_DO_STRING_SUB_AREA].set(self.option_dic['sub_area_list'][0])


		combobox = ttk.Combobox(
			master 				= frame,
			values				= self.option_dic['sub_area_list'], 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_SUB_AREA],
			state 				= "readonly",
			height				= 10,
			width				= 16,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.option_dic['sub_area_list'][0])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		# option_menu = ttk.OptionMenu(
		# 	frame,
		# 	self.option_dic[lybconstant.LYB_DO_STRING_SUB_AREA], 
		# 	''
		# 	)
		# option_menu.configure(width=20)
		# for each_menu in self.option_dic['sub_area_list']:
		# 	option_menu['menu'].add_command(
		# 		label 				= each_menu, 
		# 		command 			= tkinter._setit(self.option_dic[lybconstant.LYB_DO_STRING_SUB_AREA], each_menu)
		# 		)
		# combobox.pack(side=tkinter.LEFT, anchor=tkinter.W)

		frame.pack(side=tkinter.LEFT, anchor=tkinter.W)


		frame = ttk.Frame(frame_local_move)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[지역 이동] 작업 최대 지속 시간: "
			)

		
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA].trace( 
			'w', lambda *args: self.callback_limit_move_area_stringvar(args, option_name=lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA)
			)

		if not lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA] = 300
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_LIMIT_MOVE_AREA],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)
		label = ttk.Label(
			master 				= frame, 
			text 				= "초"
			)

		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)
		frame_local_move.pack(anchor=tkinter.W, padx=5, pady=5)


		frame_label = ttk.LabelFrame(self.inner_frame_dic['move_tab_frame'], text='몬스터 도감')
		
		frame = ttk.Frame(frame_label)
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "몬스터 도감 지역 "
		# 	)

		# label.pack(side=tkinter.LEFT)

		# self.option_dic['dogam_area_list'] = []
		# for area, sub_area_list in LYBTera.sub_area_dic.items():
		# 	for sub_area in sub_area_list:
		# 		self.option_dic['dogam_area_list'].append(sub_area)

		# self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_AREA] = tkinter.StringVar(frame)
		# self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_AREA].trace('w', 
		# 	lambda *args: self.callback_dogam_area_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DOGAM_AREA))

		# if not lybconstant.LYB_DO_STRING_DOGAM_AREA in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DOGAM_AREA] = self.option_dic['dogam_area_list'][0]

		# self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_AREA].set(self.option_dic['dogam_area_list'][0])

		# combobox = ttk.Combobox(
		# 	master 				= frame,
		# 	values				= self.option_dic['dogam_area_list'], 
		# 	textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_AREA],
		# 	state 				= "readonly",
		# 	height				= 10,
		# 	width				= 16,
		# 	font 				= lybconstant.LYB_FONT 
		# 	)
		# combobox.set(self.option_dic['dogam_area_list'][0])
		# combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "에서 "
		# 	# fg='White' if brightness < 120 else 'Black', 
		# 	# bg=bg_colour
		# 	)
		# label.pack(side=tkinter.LEFT)
		
		s = ttk.Style()
		s.configure('help.TLabel', foreground='white', background='green')
		label = ttk.Label(
			master 				= frame, 
			text 				= "？",
			style 				= 'help.TLabel'
			)
		label.pack(side=tkinter.LEFT)
		self.tooltip(label, lybconstant.LYB_TOOLTIP_MONSTER_DOGAM)
		label = ttk.Label(
			master 				= frame, 
			text 				= "[몬스터 도감] 작업을"
			)
		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM].trace('w', 
			lambda *args: self.callback_monster_dogam_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM))

		if not lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_MONSTER_DOGAM],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "분 동안 진행하고 "
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK].trace('w', 
			lambda *args: self.callback_monster_dogam_check_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK))

		if not lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK] = 300
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DURATION_DOGAM_CHECK],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)		
		label = ttk.Label(
			master 				= frame, 
			text 				= "초 마다 주기적으로 [추적]/[받기]를 체크합니다."
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(anchor=tkinter.W)

		###############################################
		#                  건너뛰기                   #
		###############################################

		# frame = ttk.Frame(frame_label)
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "몬스터 도감 인식 허용 매칭률(0~100): "
		# 	)

		
		# label.pack(side=tkinter.LEFT)
		# self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD] = tkinter.StringVar(frame)
		# self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD].trace( 
		# 	'w', lambda *args: self.callback_dogam_threshold_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD)
		# 	)

		# if not lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD in self.configure.common_config[self.game_name]:
		# 	self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD] = 75
		
		# entry = ttk.Entry(
		# 	master 				= frame,
		# 	textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_THRESHOLD],
		# 	justify 			= tkinter.RIGHT, 
		# 	width 				= 5
		# 	)

		# entry.pack(side=tkinter.LEFT)
		# label = ttk.Label(
		# 	master 				= frame, 
		# 	text 				= "%"
		# 	)

		
		# label.pack(side=tkinter.LEFT)
		# frame.pack(anchor=tkinter.W)

		frame = ttk.Frame(frame_label)
		label = ttk.Label(
			master 				= frame, 
			text 				= "몬스터 도감 추적 시작 누르고"
			)

		label.pack(side=tkinter.LEFT)

		self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_INTERVAL] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_INTERVAL].trace( 
			'w', lambda *args: self.callback_dogam_interval_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DOGAM_INTERVAL)
			)

		if not lybconstant.LYB_DO_STRING_DOGAM_INTERVAL in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DOGAM_INTERVAL] = 60
		
		entry = ttk.Entry(
			master 				= frame,
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_INTERVAL],
			justify 			= tkinter.RIGHT, 
			width 				= 5
			)

		entry.pack(side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= "초 경과 후 전투 태세 "
			)

		label.pack(side=tkinter.LEFT)

		self.option_dic['dogam_stance_list'] = LYBTera.dogam_stance_list

		self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_STANCE] = tkinter.StringVar(frame)
		self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_STANCE].trace('w', 
			lambda *args: self.callback_dogam_stance_stringvar(args, option_name=lybconstant.LYB_DO_STRING_DOGAM_STANCE))

		if not lybconstant.LYB_DO_STRING_DOGAM_STANCE in self.configure.common_config[self.game_name]:
			self.configure.common_config[self.game_name][lybconstant.LYB_DO_STRING_DOGAM_STANCE] = self.option_dic['dogam_stance_list'][1]

		self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_STANCE].set(self.option_dic['dogam_stance_list'][1])
		
		combobox = ttk.Combobox(
			master 				= frame,
			values				= self.option_dic['dogam_stance_list'], 
			textvariable 		= self.option_dic[lybconstant.LYB_DO_STRING_DOGAM_STANCE],
			state 				= "readonly",
			height				= 5,
			width 				= 6,
			font 				= lybconstant.LYB_FONT 
			)
		combobox.set(self.option_dic['dogam_stance_list'][1])
		combobox.pack(anchor=tkinter.W, side=tkinter.LEFT)

		label = ttk.Label(
			master 				= frame, 
			text 				= " 상태를 유지합니다. "
			# fg='White' if brightness < 120 else 'Black', 
			# bg=bg_colour
			)
		label.pack(side=tkinter.LEFT)
		frame.pack(side=tkinter.LEFT)

		frame_label.pack(anchor=tkinter.W, pady=5, padx=5)













		self.option_dic['option_note'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)
		self.inner_frame_dic['options'].pack(anchor=tkinter.NW, fill=tkinter.BOTH, expand=True)


		self.set_game_option()

	def callback_etc_event_check_period(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_telegram_boss_kill_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_party_member_mode_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_party_loc_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_game_config_invite_party_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_use_screenshot_boss_kill_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_smithy_limit_drag_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_dejanggan_levelup_rank_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_skill_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_skill_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_skill_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_skill_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_exp_drag_count_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_shop_gold_booster_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_shop_gold_booster_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_shop_gold_booster_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_shop_exp_booster_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_shop_exp_booster_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_shop_exp_booster_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_last_boss_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_retry_channel_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_guild_skill_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_guild_skill_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_guild_skill_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_guild_skill_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_target_hp_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_target_hp_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_target_hp_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_channel_list_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_skip_threshold_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_skip_period_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_guild_exp_potion_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_tracking_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
	def callback_duration_monster_chase_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_delay_duplicate_confirm_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_move_area_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_sub_area_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_boss_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_after_boss_skill_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_global_cool_skill_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_boss_skill_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_boss_skill_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_boss_skill_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_use_boss_warning_skill_evade_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_hero_hp_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_hero_hp_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_party_member_1_hp_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_party_member_2_hp_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_threshold_party_member_3_hp_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_party_member_4_hp_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_hero_hp_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_party_member_1_hp_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_party_member_2_hp_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_threshold_party_member_3_hp_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_party_member_4_hp_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_eliminate_buhyu_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_mainscene_quest_threshold_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_use_boss_warning_skill_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_count_dungeon_death_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_duration_dungeon_death_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_match_hero_operation_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_threshold_boss_warning_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_full_party_cancel_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_raid_match_hero_threshold_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_class_list_6_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_levelup_equip_set_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_period_bot_dungeon_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_equip_set_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_waiting_dungeon_start_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar00(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar01(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar02(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar10(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar11(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar12(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar20(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar21(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar22(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar30(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar31(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar32(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar40(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar41(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar42(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar50(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar51(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar52(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar60(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar61(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar62(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar70(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar71(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_option_booleanvar72(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar0(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar1(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar2(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar3(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar4(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar5(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar6(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_item_levelup_rank_booleanvar7(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_stop_inventory_full_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_area_threshold_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_guild_donate_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_tiaran_give_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_count_chinmildo_drag_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_muhantap_sotang_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_dogam_interval_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_dogam_stance_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_duration_battle_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_dungeon_6_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_tobul_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_tobul_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_tobul_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_tobul_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_tobul_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_type_enter_tobul_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())


	def callback_limit_count_dungeon_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_dungeon_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_dungeon_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_dungeon_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_dungeon_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_dungeon_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_dungeon_6_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_tobul_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_tobul_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_tobul_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_tobul_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_tobul_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_count_tobul_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_debug_chinmildo_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_threshold_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_duration_dungeon_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_item_rank_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_00_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_01_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_02_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_03_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_04_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_10_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_11_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_12_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_13_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_14_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_20_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_21_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_22_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_23_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_24_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_30_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_31_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_32_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_33_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_34_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_40_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_41_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_42_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_43_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_chinmildo_npc_44_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_dungeon_enter_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_limit_dungeon_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_random_skill_rate_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_random_skill_rate_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_random_skill_rate_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_skill_0_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_skill_1_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_hero_skill_2_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_hero_skill_3_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_hero_skill_4_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_hero_skill_5_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_hero_skill_6_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())
		
	def callback_hero_skill_7_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())


	def callback_hero_talent_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_6_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_7_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_8_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_9_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_10_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_11_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_12_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_13_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_14_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_hero_talent_15_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_skip_threshold_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_dogam_threshold_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_dogam_area_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_challenge_difficulty_0_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_challenge_difficulty_1_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_challenge_difficulty_2_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_challenge_difficulty_3_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_challenge_difficulty_4_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_challenge_difficulty_5_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_skip_level_adjust_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_wati_matching_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_tobul_duration_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_tobul_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_dungeon_duration_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_normal_dungeon_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_dogam_check_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_monster_dogam_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_stop_working_booleanvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())

	def callback_main_quest_each_stringvar(self, args, option_name):
		self.set_game_config(option_name, self.option_dic[option_name].get())



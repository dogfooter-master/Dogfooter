import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
import likeyoubot_license
import likeyoubot_win
import time

def mouseOverOnLink(web, url):
	print('mouse over: ', url)
	if ( 
		('adclick' in url) or
		('googleads' in url) or
		('clickmon' in url) or
		('doubleclick' in url)
		):
		web.ads_url = url
	else:
		web.ads_url = ''
	# if web != None and len(url) > 0:
	#     web.page().acceptNavigationRequest(url, 1000, False)

class WebEnginePage(QWebEnginePage):
	def __init__(self, parent=None):
		super().__init__(parent)

	def acceptNavigationRequest(self, url,  _type, isMainFrame):
		print('acceptNavigationRequest: ', url, _type, isMainFrame)
		if _type == QWebEnginePage.NavigationTypeLinkClicked:
			return True

			if "https://googleads.g.doubleclick.net/pagead" in str(url):
				return True
			elif "https://pagead2.googlesyndication.com/pagead/s/cookie_push.html" in str(url):
				return True
			else:
				QDesktopServices.openUrl(QUrl(url))
		elif _type == 1000:
			QDesktopServices.openUrl(QUrl(url))
			return False
		else:
			return True

		return True

class AdsView(QWebEngineView):
	def __init__(self, *args, **kwargs):
		QWebEngineView.__init__(self, *args, **kwargs)
		self.ads_url = ''
		self.setPage(WebEnginePage(self))
		self.monitorTimer = QTimer()
		self.monitorTimer.timeout.connect(self.updateAdsWindow)
		self.monitorTimer2 = QTimer()
		self.monitorTimer2.timeout.connect(self.updateAdsWindow2)
		self.adsHwnd = None
		self.beforeWindowList = None
		self.afterWindowList = None
		self.myTitle = "클릭하면 오늘 하루 동안 보이지 않습니다. 광고 클릭 후 약 10초 동안 창을 닫지 말아주세요. "
		self.elapsedTime = 0
		self.adsHwndList = None
		self.timeClicked = None
		self.elapsedTimeTotal = 0
		self.timePopup = None

	def event(self, e):
		# print('EVENT: ', e.type(), len(self.ads_url), QEvent.ChildAdded)
		if e.type() == QEvent.ChildAdded and len(self.ads_url) > 0:

			win = likeyoubot_win.LYBWin("ads")
			self.beforeWindowList = win.getCurrentWindowList()
			self.page().acceptNavigationRequest(self.ads_url, 1000, False)
			self.timeClicked = time.time()
			self.adsHwndList = None
			self.monitorTimer.start(500)

		return super().event(e)

	def updateAdsWindow(self):
		print("updateAdsWindow")
		self.setWindowTitle(str(15 - int(self.elapsedTime)) + " 초 후에 자동으로 사라집니다." )
		win = likeyoubot_win.LYBWin("ads")
		self.afterWindowList = win.getCurrentWindowList()

		adsHwndList = []
		for each_hwnd in self.afterWindowList:
			if not each_hwnd in self.beforeWindowList:
				adsHwndList.append(each_hwnd)

		if len(adsHwndList) > 0:
			if self.adsHwnd == None:
				self.adsHwnd = adsHwndList[0]
			else:
				print('OK -- [', win.get_title(adsHwndList[0]), ']')
		else:
			if self.adsHwnd != None:
				print('Not OK. Closed')
				self.close()

		self.elapsedTime = time.time() - self.timeClicked
		if self.elapsedTime > 15:
			print('Ads successfully completed')
			likeyoubot_license.LYBLicense().update_ads_info()

			self.close()

	def updateAdsWindow2(self):
		self.elapsedTimeTotal = time.time() - self.timePopup
		if self.elapsedTimeTotal > 1200:
			self.close()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit()

	if sys.argv[1] != 'dogfooter':
		sys.exit()

	app = QApplication(sys.argv)

	screen_resolution = app.desktop().screenGeometry()
	width, height = screen_resolution.width(), screen_resolution.height()

	web = AdsView()
	# web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
	web.settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
	# web.settings().setAttribute(QWebEngineSettings.FocusOnNavigationEnabled, True)
	# web.setPage(WebEnginePage(web))
	web.page().fullScreenRequested.connect(lambda request: request.accept())
	web.page().linkHovered.connect(lambda url: mouseOverOnLink(web, url=url))
	# web.page().loadFinished.connect(lambda ok: debug_action(ok=ok, web=web))
	# web.urlChanged.connect(lambda: debug_change())

	baseUrl = "https://www.dogfooter.com"
	web.page().load(QUrl(baseUrl))
	web.setWindowTitle(web.myTitle)
	web.setFixedSize(1020, 260)
	web.setGeometry(width - 1020, height - 260 - 30, 1020, 260)
	web.show()
	web.timePopup = time.time()
	web.monitorTimer2.start(2000)
	sys.exit(app.exec_())
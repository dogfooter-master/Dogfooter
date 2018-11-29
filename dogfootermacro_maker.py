import os
import sys
import cv2
import numpy as np
import traceback
import time
import threading
import pickle
import math

from PIL import ImageGrab
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

import likeyoubot_win
import likeyoubot_resource
import likeyoubot_configure

form_class = uic.loadUiType('./dogfootermaker/DogFooterMaker/dogfootermaker.ui')[0]
dogfootermaker_title = 'DogFooter Maker'

def resource_path(relative):
    return os.path.join(
    os.environ.get(
        "_MEIPASS2",
        os.path.abspath(".")
    ),
    relative
    )

class DFMConst():
    def __init__(self):
        pass

    SCREEN_W = likeyoubot_win.LYBWin.WIDTH
    SCREEN_H = likeyoubot_win.LYBWin.HEIGHT
    PREVIEW_W = 256
    PREVIEW_H = 256



class PlayThread(QThread):
    def __init__(self, ui):
        QThread.__init__(self)
        self.ui = ui
        self.win = self.ui.win

    def __del__(self):
        self.wait()

    def run(self):
        while True:            
            appPlayer_name = self.ui.playerComboBox.currentText()
            if len(appPlayer_name) > 0:
                self.hwnd = self.ui.hwnd_dic[appPlayer_name]
                (anchor_x, anchor_y, end_x, end_y) = self.win.get_window_location(self.hwnd)
                adj_x, adj_y = self.win.get_player_adjust(self.hwnd)

                img = self.win.get_window_screenshot(self.hwnd, 2)
                crop_area = (adj_x + 2, adj_y + 30, adj_x + 2 + DFMConst.SCREEN_W, adj_y + 30 + DFMConst.SCREEN_H)
                self.ui.mainImg = img.crop(crop_area)
                img = self.ui.mainImg.convert("RGB")
                data = img.tobytes("raw", "RGB")
                qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qim)

                self.ui.screenLabel.setPixmap(pixmap)  

                # img = img.convert("RGB")
                # data = img.tobytes("raw", "RGB")
                # qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGB888)
                # pixmap = QPixmap.fromImage(qim)
                # self.ui.screenLabel.setPixmap(pixmap)
            
                # self.ui.mainImg = Image.open(imagePath)
                # pixmap = QPixmap(imagePath)
                # # img = img.convert("RGB")
                # # data = img.tobytes("raw", "RGB")
                # # qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGB888)
                # # pixmap = QPixmap.fromImage(qim)
                # self.screenLabel.setPixmap(pixmap)

                if self.ui.current_pixelbox_label != None:
                    x = self.ui.current_pixelbox_label.x()
                    y = self.ui.current_pixelbox_label.y()
                    w = self.ui.current_pixelbox_label.width()
                    h = self.ui.current_pixelbox_label.height()
                    
                    loc_x = x + int(w*0.5)
                    loc_y = y + int(w*0.5)

                    self.ui.screenLabel.mouseMove(loc_x, loc_y, init=True)

                time.sleep(0.01)

class PixelBoxLabel(QLabel):
    def __init__(self, parent=None):
        super(PixelBoxLabel, self).__init__(parent)
        self.ui = None
        self.pb_name = None
        self.size = None
        self.setMouseTracking(True)

    def setupPixelBox(self, ui, pb_name, size):
        self.ui = ui
        self.pb_name = pb_name
        self.size = size
        self.is_pressed = False
        self.setGeometry(0, 0, size, size)
        self.setMinimumWidth(size)
        self.setMinimumHeight(size)
        # self.setCursor(QCursor(Qt.BlankCursor))
        self.setCurrentFocus(False)
        self.hide()

    def setCurrentFocus(self, focus):
        self.ui.resourceLineEdit.clearFocus()
        if focus == True:
            self.setStyleSheet('PixelBoxLabel { background-color: rgb(255, 255, 255, 50%); }')
        else:
            self.setStyleSheet('PixelBoxLabel { background-color: rgb(255, 0, 0, 50%); }')

    def mouseMove(self, x, y, init=False):
        # print(self.x(), self.y(), self.width(), self.height())

        if init == True or ( self.ui.current_pixelbox_label == self and self.is_pressed == True and self.ui.controlKeyPressed == True):
            self.setGeometry(x - int(self.width()*0.5), y - int(self.height()*0.5), self.width(), self.height())
            return (self.x() + int(self.width()*0.5), self.y() + int(self.height()*0.5))

        return (-1, -1)

    def mouseMoveEvent (self, e):
        if self.ui.mainImg == None:
            return

        self.ui.screenLabel.mouseMove(e.x() + self.x(), e.y() + self.y())

    def mousePressEvent(self, e):
        self.is_pressed = True

        if self.ui.mainImg == None:
            return

        if e.buttons() & Qt.LeftButton:
            print('mousePressEvent LEFT Button')
            if self.ui.current_pixelbox_label != None:
                self.ui.current_pixelbox_label.setCurrentFocus(False)
            self.ui.current_pixelbox_label = self
            self.ui.current_pixelbox_label.setCurrentFocus(True)

            self.ui.screenLabel.mouseMove(e.x() + self.x(), e.y() + self.y())

        elif e.buttons() & Qt.RightButton:
            print('mousePressEvent RIGHT Button')
            if self.ui.current_pixelbox_label == self:
                self.ui.current_pixelbox_label = None

            self.setParent(None)
        else:
            print('mousePressEvent Else Button')

        self.ui.focusCurrentPixelBoxLabel()

    def mouseReleaseEvent(self, e):
        self.is_pressed = False
        if self.ui.mainImg == None:
            return


class MainScreenShotLabel(QLabel):
    def __init__(self, parent=None):
        super(MainScreenShotLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.ui = None
        self.is_pressed = False
        self.last_x = 0
        self.last_y = 0

    def setUI(self, ui):
        self.ui = ui

    def mouseMoveEvent (self, e):
        if self.ui.mainImg == None:
            return

        # 드래그 전송            
        # if self.is_pressed == True:
        #     appPlayer_name = self.ui.playerComboBox.currentText()
        #     if len(appPlayer_name) > 0 and appPlayer_name in self.ui.hwnd_dic:
        #         hwnd = self.ui.hwnd_dic[appPlayer_name]
        #         (x, y, w, h) = self.ui.win.get_player_screen_rect(hwnd)
        #         self.ui.win.mouse_drag(hwnd, self.last_x + x, self.last_y + y, e.x() + x, e.y() + y)

        # print(e.x(), e.y())
        self.mouseMove(e.x(), e.y())

        # QWidget.mouseMoveEvent(self, eventQMouseEvent)

    def mouseMove(self, anchor_x, anchor_y, init=False):
        if self.ui.mainImg == None:
            return

        if self.ui.current_pixelbox_label == None:
            return

        (loc_x, loc_y) = self.ui.current_pixelbox_label.mouseMove(self.x() + anchor_x, self.y() + anchor_y, init=init)
        if loc_x == -1:
            return

        crop_area = self.getCropArea(loc_x - self.x(), loc_y - self.y(), 15)

        img = self.ui.mainImg.crop(crop_area)
        # img.save('test_maker.png')
        # img = img.convert("RGB")
        # data = img.tobytes("raw", "RGB")
        # print(img.size)
        qim = ImageQt(img)
        # qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGB888)
        # qim = QImage(data, 14, 14, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qim)
        pixmap = pixmap.scaled(DFMConst.PREVIEW_W * 0.75, DFMConst.PREVIEW_H * 0.75, Qt.KeepAspectRatio)
        self.ui.pixelBoxPreviewLabel.setPixmap(pixmap)

    def getCropArea(self, x, y, size):

        distance = int((size - 1) / 2)

        anchor_x = x
        anchor_y = y

        if anchor_x < distance:
            anchor_x = distance
        elif anchor_x + distance > DFMConst.SCREEN_W:
            anchor_x = DFMConst.SCREEN_W - distance

        if anchor_y < distance:
            anchor_y = distance
        elif anchor_y + distance > DFMConst.SCREEN_H:
            anchor_y = DFMConst.SCREEN_H - distance

        # print((anchor_x - distance, anchor_y - distance, anchor_x + distance, anchor_y + distance + 1))

        return (anchor_x - distance, anchor_y - distance, anchor_x + distance, anchor_y + distance)
        # return (x, y, x + size, y + size)
        # return (x, y, x + 15, y + 15)


    def mousePressEvent(self, e):
        self.is_pressed = True
        self.last_x = e.x()
        self.last_y = e.y()

        if self.ui.mainImg == None:
            return

        if e.buttons() & Qt.LeftButton:
            print('Left mouse button pressed ', e.x(), e.y())        
            pb = self.ui.addPixelBoxLabel(e, 'pixel_box_label_' + str(e.x()), 15)
            self.mouseMove(e.x(), e.y(), init=True)
            # self.dragstart = event.pos()
            # self.clicked.emit()

            appPlayer_name = self.ui.playerComboBox.currentText()
            if len(appPlayer_name) > 0 and appPlayer_name in self.ui.hwnd_dic:
                hwnd = self.ui.hwnd_dic[appPlayer_name]
                # (x, y, w, h) = self.ui.win.get_player_screen_rect(hwnd)
                # self.ui.win.mouse_click(hwnd, e.x() + x, e.y() + y)

        elif e.buttons() & Qt.RightButton:
            print('Right mouse button pressed ', e.x(), e.y())

    def mouseReleaseEvent(self, e):
        self.is_pressed = False

        if self.ui.mainImg == None:
            return
        print('mouse released ', e.x(), e.y())
        # self.dragstart = None

    # def mouseMoveEvent(self, e):
    #     if self.ui.mainImg == None:
    #         return
    #     print('mouse move ', e.x(), e.y())
    #     if (self.dragstart is not None and
    # event.buttons() & QtCore.Qt.LeftButton and
    # (event.pos() - self.dragstart).manhattanLength() >
    # QtWidgets.qApp.startDragDistance()):
    # self.dragstart = None
    # drag = QtGui.QDrag(self)
    # drag.setMimeData(QtCore.QMimeData())
    # drag.exec_(QtCore.Qt.LinkAction)

    def dragEnterEvent(self, e):
        if self.ui.mainImg == None:
            return
        e.acceptProposedAction()
        if e.source() is not self:
            print('dragEnterEvent source is not self')
        else:                
            print('dragEnterEvent source is self')

    # if event.source() is not self:
    # self.clicked.emit()


class PixelImageLabel(QLabel):
    def __init__(self, parent=None):
        super(PixelImageLabel, self).__init__(parent)
        self.setMouseTracking(True)
        self.ui = None

    def setUI(self, ui):
        self.ui = ui

    def mouseMoveEvent (self, eventQMouseEvent):
        if self.ui.mainImg == None:
            return

        # QWidget.mouseMoveEvent(self, eventQMouseEvent)

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(dogfootermaker_title)
        self.setFixedSize(QSize(DFMConst.SCREEN_W + 335, DFMConst.SCREEN_H + 250))
        self.statusBar.setSizeGripEnabled(False) 
        self.win = likeyoubot_win.LYBWin(dogfootermaker_title)
        self.hwnd_dic = {}
        self.play_thread = None
        self.controlKeyPressed = False
        self.mainImg = None

        self.connectAction = QAction('Connect', self)
        self.connectAction.triggered.connect(self.connectPlayer)
        self.menuBar.addAction(self.connectAction)

        openAction = QAction('Open Image', self)  
        openAction.triggered.connect(self.openImage) 
        self.menuBar.addAction(openAction)

        self.screenLabel = MainScreenShotLabel(self.mainImageWidget)
        self.screenLabel.setUI(self)
        self.screenLabel.setGeometry(0, 0, DFMConst.SCREEN_W, DFMConst.SCREEN_H)
        self.screenLabel.setMinimumWidth(DFMConst.SCREEN_W)
        self.screenLabel.setMinimumHeight(DFMConst.SCREEN_H)
        self.screenLabel.setStyleSheet('MainScreenShotLabel { background-color: white; }')
        self.screenLabel.setAlignment(Qt.AlignLeft|Qt.AlignTop)

        self.pixelBoxPreviewLabel = PixelImageLabel(self.pixelImageWidget)
        self.pixelBoxPreviewLabel.setUI(self)
        self.pixelBoxPreviewLabel.setGeometry(0, 0, DFMConst.PREVIEW_W, DFMConst.PREVIEW_H)
        self.pixelBoxPreviewLabel.setMinimumWidth(DFMConst.PREVIEW_W)
        self.pixelBoxPreviewLabel.setMinimumHeight(DFMConst.PREVIEW_H)
        self.pixelBoxPreviewLabel.setStyleSheet('PixelImageLabel { background-color: white; border: 1px solid black; }')
        self.pixelBoxPreviewLabel.setAlignment(Qt.AlignCenter)

        self.pixelbox_label_dic = {}
        self.current_pixelbox_label = None
        self.playerComboBox.setFocusPolicy(Qt.NoFocus)
        self.playerComboBox.currentIndexChanged.connect(self.callbackPlayerComboBox)

        self.resource_manager_dic = {}

        for each_game, each_game_data in likeyoubot_configure.LYBConstant.LYB_GAMES.items():
            self.gameComboBox.addItem(each_game)
            try:
                with open(resource_path(each_game_data + '.lyb'), 'rb') as resource_file:
                    print('resource_file', resource_file)
                    self.resource_manager_dic[each_game] = pickle.load(resource_file)
            except:
                print(traceback.format_exc())
                self.resource_manager_dic[each_game] = likeyoubot_resource.LYBResourceManager(likeyoubot_resource.LYBPixelBoxDic(), likeyoubot_resource.LYBResourceDic())

        self.callbackGameComboBox()
        self.gameComboBox.currentIndexChanged.connect(self.callbackGameComboBox)        
        self.gameComboBox.setFocusPolicy(Qt.NoFocus)

        self.callbackResourceComboBox()
        self.resourceComboBox.currentIndexChanged.connect(self.callbackResourceComboBox)      
        self.resourceComboBox.setFocusPolicy(Qt.NoFocus)

        # self.pixelBoxListWidget.indexesMoved.connect(self.callbackPixelBoxListWidget)
        self.pixelBoxListWidget.clicked.connect(self.callbackPixelBoxListWidget)

        self.allCheckBox.stateChanged.connect(self.callbackAllCheckBox)
        self.eventCheckBox.stateChanged.connect(self.callbackEventCheckBox)
        self.sceneCheckBox.stateChanged.connect(self.callbackSceneCheckBox)
        self.locCheckBox.stateChanged.connect(self.callbackLocCheckBox)

        self.eventTableWidget.setRowCount(self.getResourceCount('event'))        
        self.sceneTableWidget.setRowCount(self.getResourceCount('scene'))
        self.locTableWidget.setRowCount(self.getResourceCount('loc'))

        self.resourceLineEdit.textChanged.connect(self.callbackResourceLineEdit)

        self.updateResourceTable()


        # self.win.find_window_wildcard('')
        # for each_hwnd in self.win.handle_list:
        #     if each_hwnd in self.win.parent_handle_dic:
        #         title = self.win.get_title(self.win.parent_handle_dic[each_hwnd])
        #     else:
        #         title = self.win.get_title(each_hwnd)

        #     self.hwnd_dic[title] = each_hwnd

    def callbackResourceLineEdit(self):
        print('callbackResourceLineEdit')
        self.updateResourceComboBox()
        self.resourceLineEdit.setFocus()

    def getResourceCount(self, postfix):

        count = 0
        for each in self.resource_manager_dic[self.gameComboBox.currentText()].resource_dic.sortedResourceListByName():
            if postfix in each.resource_name[-5:]:
                count += 1

        return count

    def setResourceTableRow(self, widget, postfix):
        widget.setColumnCount(2)
        widget.setHorizontalHeaderLabels([postfix, '%'])
        widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        widget.horizontalHeader().setStyleSheet('::section{Background-color:#c2b6b6}')
        # widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        widget.setColumnWidth(1, 10)
        widget.setSelectionBehavior(QTableView.SelectRows);
        widget.clicked.connect(self.callbackTableWidget)
        widget.setFocusPolicy(Qt.NoFocus)

        row = 0
        for each in self.resource_manager_dic[self.gameComboBox.currentText()].resource_dic.sortedResourceListByName():
            if postfix in each.resource_name[-5:]:
                item = QTableWidgetItem(each.resource_name)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
                widget.setItem(row, 0, item)
                item = QTableWidgetItem(99)
                item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                widget.setItem(row, 1, item)
                row += 1

        widget.resizeColumnsToContents()
        widget.resizeRowsToContents()

    def callbackTableWidget(self, QPos=None):
        print(QPos.column(), QPos.row(), QPos.data())
        self.resourceComboBox.setCurrentIndex(self.resourceComboBox.findText(str(QPos.data())))

    def addPixelBoxLabel(self, e, name, size):
        if name in self.pixelbox_label_dic:
            name += '_' + str(len(self.pixelbox_label_dic) - 1)

        self.pixelbox_label_dic[name] = PixelBoxLabel(self.mainImageWidget)
        self.pixelbox_label_dic[name].setupPixelBox(self, name, size)
        self.pixelbox_label_dic[name].mouseMove(e.x(), e.y(), init=True)
        self.pixelbox_label_dic[name].show()
        self.current_pixelbox_label = self.pixelbox_label_dic[name]  
        self.focusCurrentPixelBoxLabel()

        return self.pixelbox_label_dic[name]

    def focusCurrentPixelBoxLabel(self):
        if self.current_pixelbox_label == None:
            self.pixelBoxPreviewLabel.clear()
            return

        for key, value in self.pixelbox_label_dic.items():
            print('-- name: ', self.current_pixelbox_label.pb_name, key)
            if self.current_pixelbox_label.pb_name == key:
                self.pixelbox_label_dic[key].setCurrentFocus(True)
            else:
                self.pixelbox_label_dic[key].setCurrentFocus(False)


    def connectPlayer(self):
        # self.play_thread =  PlayThread(self)
        # self.play_thread.start()
        # try:
        #     with open(resource_path('lyb.cfg'), 'rb') as dat_file:
        #         self.configure = pickle.load(dat_file)

        #     self.configure.path = resource_path('lyb.cfg')
        #     dogfootermacro_logger.debug('configure.path [' + self.configure.path + ']')

        # except FileNotFoundError:       
        #     exitMessage = QMessageBox.warning(self, ' ', resource_path('lyb2.cfg') + ' 파일이 없습니다.')
        #     sys.exit(1)

        if self.connectAction.text() == 'Connect':
            self.connectAction.setText('Disconnect')
            self.playerComboBox.clear()
            self.hwnd_dic = {}

            try:
                hwnd_dic = {}
                self.win.find_window_wildcard('')
                for each_hwnd in self.win.handle_list:
                    print(str(each_hwnd) + ' ' + self.win.get_title(each_hwnd))
                    if each_hwnd in self.win.parent_handle_dic:
                        title = self.win.get_title(self.win.parent_handle_dic[each_hwnd])
                    else:
                        title = self.win.get_title(each_hwnd)

                    self.playerComboBox.addItem(title)
                    hwnd_dic[title] = each_hwnd

                self.hwnd_dic = hwnd_dic
                print(self.playerComboBox.count())

                self.callbackPlayerComboBox()

            except:
                self.win = likeyoubot_win.LYBWin(dogfootermaker_title)
                self.hwnd_dic = {}
                print(traceback.format_exc())

        else:
            self.connectAction.setText('Connect')
            self.playerComboBox.clear()
            self.hwnd_dic = {}
            self.play_thread.terminate()
            self.play_thread = None
            print('Thread count ', threading.activeCount())
            self.screenLabel.clear()
       

    def openImage(self):
        print("openImage")
        option = QFileDialog.Options()
        option |= QFileDialog.DontUseNativeDialog
        imagePath, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files(*);;Image Files (*.png)", options=option)
        if len(imagePath) > 0:
            self.mainImg = Image.open(imagePath)
            pixmap = QPixmap(imagePath)
            # img = img.convert("RGB")
            # data = img.tobytes("raw", "RGB")
            # qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGB888)
            # pixmap = QPixmap.fromImage(qim)
            self.screenLabel.setPixmap(pixmap)            
            self.clearPixelBoxOnScreen()


        # self.screenLabel.setStyleSheet("QLabel { background-color : red; color:blue;}")
        # pixmap = QPixmap('d:/Workspace/dogfooter/screenshot/elite_quest_reward_180901_145709.png')
        # dogfootermacro_logger.debug(pixmap)
        # dogfootermacro_logger.debug(self.mainImageLabel)
        # self.mainImageLabel.setPixmap(pixmap)  

    def keyReleaseEvent(self, e):
        if self.controlKeyPressed == True:
            if e.key() == Qt.Key_Control:
                self.controlKeyPressed = False 

    def keyPressEvent(self, e):
        def isPrintable(key): 
            printable = [ Qt.Key_Space, Qt.Key_Exclam, Qt.Key_QuoteDbl, Qt.Key_NumberSign, 
            Qt.Key_Dollar, Qt.Key_Percent, Qt.Key_Ampersand, Qt.Key_Apostrophe, Qt.Key_ParenLeft, 
            Qt.Key_ParenRight, Qt.Key_Asterisk, Qt.Key_Plus, Qt.Key_Comma, Qt.Key_Minus, Qt.Key_Period, 
            Qt.Key_Slash, Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9, 
            Qt.Key_Colon, Qt.Key_Semicolon, Qt.Key_Less, Qt.Key_Equal, Qt.Key_Greater, Qt.Key_Question, Qt.Key_At, 
            Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_G, Qt.Key_H, Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, 
            Qt.Key_M, Qt.Key_N, Qt.Key_O, Qt.Key_P, Qt.Key_Q, Qt.Key_R, Qt.Key_S, Qt.Key_T, Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, 
            Qt.Key_Y, Qt.Key_Z, Qt.Key_BracketLeft, Qt.Key_Backslash, Qt.Key_BracketRight, Qt.Key_AsciiCircum, Qt.Key_Underscore, 
            Qt.Key_QuoteLeft, Qt.Key_BraceLeft, Qt.Key_Bar, Qt.Key_BraceRight, Qt.Key_AsciiTilde, ] 

            if key in printable: 
                return True 
            else: 
                return False 

        if e.modifiers() & Qt.ControlModifier: 
            print('Control') 
            self.controlKeyPressed = True 

        if e.modifiers() & Qt.ShiftModifier: 
            print('Shift') 

        if e.modifiers() & Qt.AltModifier: 
            print('Alt') 

        if e.key() == Qt.Key_Delete: 
            print('Delete') 
        elif e.key() == Qt.Key_Backspace: 
            print('Backspace') 
        elif e.key() in [Qt.Key_Return, Qt.Key_Enter]: 
            print('Enter') 
        elif e.key() == Qt.Key_Escape: 
            print('Escape')
        elif e.key() == Qt.Key_Q and self.controlKeyPressed == True:
            print('Exit')
            sys.exit(1)
        elif (  e.key() == Qt.Key_Right or
                e.key() == Qt.Key_Left or
                e.key() == Qt.Key_Up or
                e.key() == Qt.Key_Down ):
            if self.current_pixelbox_label == None:
                return

            x = self.current_pixelbox_label.x()
            y = self.current_pixelbox_label.y()
            w = self.current_pixelbox_label.width()
            h = self.current_pixelbox_label.height()
            print(x, y, w, h)
            if e.key() == Qt.Key_Right:
                print('Right')
                loc_x = x + int(w*0.5) + 1
                loc_y = y + int(w*0.5) 
            elif e.key() == Qt.Key_Left: 
                print('Left') 
                loc_x = x + int(w*0.5) - 1
                loc_y = y + int(w*0.5)
            elif e.key() == Qt.Key_Up: 
                print('Up') 
                loc_x = x + int(w*0.5)
                loc_y = y + int(w*0.5) - 1
            elif e.key() == Qt.Key_Down: 
                print('Down') 
                loc_x = x + int(w*0.5)
                loc_y = y + int(w*0.5) + 1

            if loc_x < int(w*0.5):
                loc_x = int(w*0.5)
            elif loc_x + w - int(w*0.5) > DFMConst.SCREEN_W:
                loc_x = DFMConst.SCREEN_W - w + int(w*0.5)

            if loc_y < int(h*0.5):
                loc_y = int(h*0.5)
            elif loc_y + h - int(h*0.5) > DFMConst.SCREEN_H:
                loc_y = DFMConst.SCREEN_H - h + int(h*0.5)           

            self.screenLabel.mouseMove(loc_x, loc_y, init=True)
            
        if not self.controlKeyPressed and isPrintable(e.key()): 
            print(e.text()) 

    def callbackPlayerComboBox(self):

        if len(self.hwnd_dic) == 0:
            return

        self.clearPixelBoxOnScreen()

        if self.play_thread == None:
            self.play_thread = PlayThread(self)
            self.play_thread.start()

    def callbackGameComboBox(self):
        self.updateResourceTable()
        self.allCheckBox.setChecked(True)
        self.callbackAllCheckBox()    
        self.updateResourceComboBox()

    def updateResourceTable(self):
        self.setResourceTableRow(self.eventTableWidget, 'event')
        self.setResourceTableRow(self.sceneTableWidget, 'scene')
        self.setResourceTableRow(self.locTableWidget, 'loc')

    def updateResourceComboBox(self): 
        self.resourceComboBox.clear()   
        for each in self.resource_manager_dic[self.gameComboBox.currentText()].resource_dic.sortedResourceListByName():
            if len(self.resourceLineEdit.text()) > 0 and self.resourceLineEdit.text() not in each.resource_name:
                continue

            if self.allCheckBox.isChecked() == True:
                self.resourceComboBox.addItem(each.resource_name)
            else:
                if self.eventCheckBox.isChecked() == True and 'event' in each.resource_name[-5:]:
                    self.resourceComboBox.addItem(each.resource_name)
                elif self.sceneCheckBox.isChecked() == True and 'scene' in each.resource_name[-5:]:
                    self.resourceComboBox.addItem(each.resource_name)
                elif self.locCheckBox.isChecked() == True and 'loc' in each.resource_name[-5:]:
                    self.resourceComboBox.addItem(each.resource_name)
                else:
                    if (    'event' not in each.resource_name[-5:] and
                            'scene' not in each.resource_name[-5:] and
                            'loc' not in each.resource_name[-5:] 
                            ):
                        self.resourceComboBox.addItem(each.resource_name)

        self.totalCountLabel.setText(str(len(self.resourceComboBox)))

    # 리소스를 선택할 때마다 호출

    def callbackResourceComboBox(self):
        print('+', self.resourceComboBox.currentText())
        self.pixelBoxListWidget.clear()
        self.clearPixelBoxOnScreen()   
        if len(self.resourceComboBox.currentText()) > 0:
            for each in self.resource_manager_dic[self.gameComboBox.currentText()].resource_dic[self.resourceComboBox.currentText()]:                
                self.pixelBoxListWidget.addItem(each)

        for i in range(self.pixelBoxListWidget.count()):
            print('-', self.pixelBoxListWidget.item(i).text())
            try:
                print('--', self.get_center_pixel_info(self.pixelBoxListWidget.item(i).text()))
            except:
                print(traceback.format_exc())

        if self.pixelBoxListWidget.count() > 0:
            self.pixelBoxListWidget.item(0).setSelected(True)
            self.pixelBoxListWidget.setFocus()
            self.pixelBoxListWidget.setCurrentRow(0)
            self.callbackPixelBoxListWidget()

    # 픽셀 박스 선택할때마다 호출
    # 1. 개별적인 픽셀박스 보여주기

    def callbackPixelBoxListWidget(self):
        print('DEBUG: PixelBox clicked')
        print('DEBUG: -->', self.pixelBoxListWidget.currentRow())
        if self.pixelBoxListWidget.currentRow() < 0:
            return

        print('DEBUG: --->', self.pixelBoxListWidget.currentItem().text(), self.gameComboBox.currentText())
        img = self.getImagePixelBox(self.pixelBoxListWidget.currentItem().text())
        qim = ImageQt(img)
        pixmap = QPixmap.fromImage(qim)
        pixmap = pixmap.scaled(DFMConst.PREVIEW_W * 0.75, DFMConst.PREVIEW_H * 0.75, Qt.KeepAspectRatio)
        self.pixelBoxPreviewLabel.setPixmap(pixmap)

    def callbackAllCheckBox(self):
        self.eventCheckBox.setChecked(self.allCheckBox.isChecked())
        self.sceneCheckBox.setChecked(self.allCheckBox.isChecked())
        self.locCheckBox.setChecked(self.allCheckBox.isChecked())
        self.updateResourceComboBox()

    def callbackEventCheckBox(self):
        self.updateResourceComboBox()

    def callbackSceneCheckBox(self):
        self.updateResourceComboBox()

    def callbackLocCheckBox(self):
        self.updateResourceComboBox()

    def clearPixelBoxOnScreen(self):
        for key, value in self.pixelbox_label_dic.items():
            self.pixelbox_label_dic[key].setParent(None)

        self.pixelbox_label_dic.clear()
        self.current_pixelbox_label = None 

    def getImagePixelBox(self, pixel_box_name):

        try:
            pixel_box = self.resource_manager_dic[self.gameComboBox.currentText()].pixel_box_dic[pixel_box_name]
        except:
            print('Not found pixel box data:' + str(pixel_box_name))
            return None

        template_image = np.ndarray(shape=(pixel_box.height, pixel_box.width, 3), dtype='uint8')

        i = 0
        j = 0
        k = 0

        for elem in np.nditer(template_image, op_flags=['readwrite']):
            elem[...] = pixel_box[i + j][1][k]

            k += 1
            if k >= 3:

                i += pixel_box.height
                k = 0
                if i >= pixel_box.height * pixel_box.width:
                    j += 1
                    i = 0
                    rgb, w, h = template_image.shape[::-1]

        return Image.fromarray(template_image, 'RGB')

    def get_center_pixel_info(self, object_name):               
        pixel_box = self.resource_manager_dic[self.gameComboBox.currentText()].pixel_box_dic[object_name]
    
        width = int(math.sqrt(len(pixel_box)))
        height = int(math.sqrt(len(pixel_box)))
        half = int(width * 0.5)

        middle_index = width * half + half

        return pixel_box[middle_index]

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
# coding: utf-8

import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except:
    pass

import ctypes
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from myqt import *
from gui import MainWindow
from common_utils import CURRENT_DIR
from log_utils import logger

#app start
if __name__ == '__main__':
    logger.info('Application starts.')
    
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("MakesenseAwesomeDialog")
    except:
        pass
    
    os.environ['QT_MAC_WANTS_LAYER'] = '1'

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(CURRENT_DIR + "/res/logo.png"))

    app.processEvents()

    mainWin = MainWindow()
    mainWin.showNormal()

    sys.exit(app.exec_())
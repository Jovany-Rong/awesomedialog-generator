# coding: utf-8

from myqt import *
from ui import Ui_MainWindow
from log_utils import logger
from common_utils import CURRENT_DIR

from gui import DbDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        
        self.logger.info('Application main window started.')
        
        self.logger.debug('Connecting signals and slots of main window.')
        self.__connect()
        
        
    def __connect(self):
        self.actionConnection.triggered.connect(self.__db_config)
    
    
    def __db_config(self):
        self.logger.info('Opening database connection window.')
        self.dbConnWindow = DbDialog()
        self.dbConnWindow.showNormal()
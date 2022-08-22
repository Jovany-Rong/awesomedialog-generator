# coding: utf-8

from myqt import *
from ui import Ui_MainWindow
from log_utils import logger
from common_utils import CURRENT_DIR, gen_time_based_uuid
from db_utils import Connection
from gui import DbDialog, DialogEditor

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        
        self.logger.info('Application main window started.')
        
        self.connector = Connection()
        
        self.logger.debug('Connecting signals and slots of main window.')
        self.__connect()
        
        self.__show_conn_string()
        
        
        
        
    def __connect(self):
        self.actionConnection.triggered.connect(self.__db_config)
        self.actionNew.triggered.connect(self.__new_dialog)
    
    
    def __db_config(self):
        self.logger.info('Opening database connection window.')
        self.dbConnWindow = DbDialog()
        self.dbConnWindow.sigSave.connect(self.__show_conn_string)
        self.dbConnWindow.showNormal()
        
    
    def __new_dialog(self):
        self.logger.info('Opening dialog editor window to create a new dialog.')
        uuid = gen_time_based_uuid()
        self.logger.info('Using uuid: %s' % uuid)
        self.dialogEditorWindow = DialogEditor(uuid)
        self.dialogEditorWindow.sigSave.connect(self.__slot_save_dialog)
        self.dialogEditorWindow.showNormal()
        
        
    def __show_conn_string(self):
        res = self.connector.get_connection_string()
        self.statusBar().showMessage(res)
        
    
    def __slot_save_dialog(self, dialogMetaInfo):
        self.logger.info('Sending saving dialog signal.')
        res = self.connector.new_dialog(dialogMetaInfo)
        if res:
            QMessageBox.information(self, 'Info', 'Success.')
        else:
            QMessageBox.critical(self, 'Error', 'Failed.')
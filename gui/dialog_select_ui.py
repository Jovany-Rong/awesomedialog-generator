# coding: utf-8

from myqt import *
from ui import Ui_DialogSelectDialog
from log_utils import logger
from common_utils import CURRENT_DIR
from db_utils import Connection

class DialogSelector(QDialog, Ui_DialogSelectDialog):
    sigOpen = pyqtSignal(str)
    def __init__(self):
        super(DialogSelector, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        self.connector = Connection()
        self.logger.info('Dialog selector window started.')
        
        self.btnOpen.clicked.connect(self.open_dialog)
        
        self.dialogs = self.get_dialogs()
        
        self.init_table_dialogs()
        self.fill_table_dialogs()
        
        
        
    def init_table_dialogs(self):
        self.tableDialogs.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableDialogs.horizontalHeader().setStretchLastSection(True)
        self.tableDialogs.model = QStandardItemModel(0, 0, self.tableDialogs)
        self.tableDialogs.setModel(self.tableDialogs.model)
        self.tableDialogs.headers = ["ID", "对话标题", "作者"]
        self.tableDialogs.model.setHorizontalHeaderLabels(self.tableDialogs.headers)
        self.tableDialogs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        
    def fill_table_dialogs(self):
        ctRow = 0
        for dialog in self.dialogs:
            itemId = QStandardItem(dialog[0])
            itemTitle = QStandardItem(dialog[2])
            itemAuthor = QStandardItem(dialog[5])
            
            self.tableDialogs.model.setItem(ctRow, 0, itemId)
            self.tableDialogs.model.setItem(ctRow, 1, itemTitle)
            self.tableDialogs.model.setItem(ctRow, 2, itemAuthor)
        
            ctRow += 1
        
        
    def get_dialogs(self):
        result = self.connector.search_owned_dialogs()
        
        return result
    
    
    def open_dialog(self):
        try:
            index = self.tableDialogs.currentIndex()
            rowNum = index.row()
            dialogId = self.tableDialogs.model.item(rowNum, 0).text()
        except:
            self.logger.warning('Failed to get dialog ID.')
            dialogId = ''
            
        self.logger.info('Selected dialog ID is "%s".' % (dialogId))
        self.sigOpen.emit(dialogId)
        
        
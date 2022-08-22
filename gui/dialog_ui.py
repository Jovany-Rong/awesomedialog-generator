# coding: utf-8

from myqt import *
from ui import Ui_DialogDialog
from log_utils import logger
from common_utils import CURRENT_DIR
from db_utils import Connection

class DialogEditor(QDialog, Ui_DialogDialog):
    sigSave = pyqtSignal(dict)
    def __init__(self, uuid):
        super(DialogEditor, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        self.id = uuid
        
        self.logger.info('Dialog editor window started.')
        self.logger.info('Dialog ID is %s.' % (self.id))
        self.lbId.setText(self.id)
        
        self.btnSave.clicked.connect(self.save)
        
    
    def check_valid(self):
        self.logger.info('Checking dialog meta info validity.')
        if self.cbDialogType.currentText().strip() == '':
            QMessageBox.warning(self, 'Warning', '对话类型不能为空！')
            self.logger.warning('Checking result: failed.')
            return False
        
        if self.editDialogTitle.text().strip() == '':
            QMessageBox.warning(self, 'Warning', '对话标题不能为空！')
            self.logger.warning('Checking result: failed.')
            return False
        
        self.logger.info('Checking result: success.')
        return True
    
    
    def save(self):
        if self.check_valid():
            di = dict()
            di["id"] = self.lbId.text().strip()
            if self.cbDialogType.currentText().strip() == "旁白式对话":
                dialogType = 0
            else:
                dialogType = 1
            di["dialogType"] = dialogType
            di["dialogTitle"] = self.editDialogTitle.text().strip()
            self.logger.info('Saving meta info of dialog %s.' % (di["id"]))
            self.sigSave.emit(di)
            self.close()
        
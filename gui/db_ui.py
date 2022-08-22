# coding: utf-8

from myqt import *
from ui import Ui_DbDialog
from log_utils import logger
from common_utils import CURRENT_DIR
from db_utils import Connection
from crypt_utils import encrypt_str

class DbDialog(QDialog, Ui_DbDialog):
    sigSave = pyqtSignal(str)
    def __init__(self):
        super(DbDialog, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        
        self.logger.info('Database connection window started.')
        
        self.connector = Connection()
        
        self.btnTest.clicked.connect(self.test_connection)
        self.btnSave.clicked.connect(self.save_connection)
        
        self.show_connection()
        
    
    def show_connection(self):
        conf = self.connector.export_config()
        self.logger.debug('Database connection config: %s' % (conf))
        self.editHost.setText(conf["host"])
        self.spinPort.setValue(conf["port"])
        self.editDatabase.setText(conf["database"])
        self.editUsername.setText(conf["user"])
        

    def test_connection(self):
        if self.check_valid():
            conf = {
                "host": self.editHost.text().strip(),
                "port": self.spinPort.value(),
                "database": self.editDatabase.text().strip(),
                "user": self.editUsername.text().strip(),
                "password": self.editPassword.text().strip()
            }
            if self.connector.test_conn_from_params(conf):
                QMessageBox.information(self, 'Info', 'Success.')
            else:
                QMessageBox.critical(self, 'Error', 'Failed.')
                
        
    def save_connection(self):
        if self.check_valid():
            conf = {
                "host": self.editHost.text().strip(),
                "port": str(self.spinPort.value()),
                "database": self.editDatabase.text().strip(),
                "user": self.editUsername.text().strip(),
                "password": self.editPassword.text().strip()
            }
            flag = True
            if not self.connector.set_config('db.host', conf["host"]):
                flag = False
            if not self.connector.set_config('db.port', conf["port"]):
                flag = False
            if not self.connector.set_config('db.database', conf["database"]):
                flag = False
            if not self.connector.set_config('db.username', conf["user"]):
                flag = False
            if not self.connector.set_config('db.password', encrypt_str(conf["password"])):
                flag = False
            
            if flag:
                QMessageBox.information(self, 'Info', 'Success.')
                self.sigSave.emit('success')
            else:
                QMessageBox.critical(self, 'Error', 'Failed.')
        
    
    def check_valid(self):
        self.logger.info('Checking database connection validity.')
        if self.editPassword.text().strip() == '':
            QMessageBox.warning(self, 'Warning', '密码不能为空！')
            self.logger.warning('Checking result: failed.')
            return False
        
        if self.editHost.text().strip() == '':
            QMessageBox.warning(self, 'Warning', '服务器不能为空！')
            self.logger.warning('Checking result: failed.')
            return False
        
        if self.editUsername.text().strip() == '':
            QMessageBox.warning(self, 'Warning', '用户名不能为空！')
            self.logger.warning('Checking result: failed.')
            return False
        
        self.logger.info('Checking result: success.')
        return True
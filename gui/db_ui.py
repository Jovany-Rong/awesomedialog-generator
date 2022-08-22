# coding: utf-8

from myqt import *
from ui import Ui_DbDialog
from log_utils import logger
from common_utils import CURRENT_DIR
from db_utils import Connection

class DbDialog(QDialog, Ui_DbDialog):
    def __init__(self):
        super(DbDialog, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        
        self.logger.info('Database connection window started.')
        
        self.connector = Connection()
        
        self.btnTest.clicked.connect(self.test_connection)
        
        self.show_connection()
        
    
    def show_connection(self):
        conf = self.connector.export_config()
        print(conf)
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
        
        self.logger.warning('Checking result: success.')
        return True
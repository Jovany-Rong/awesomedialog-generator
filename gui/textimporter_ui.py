# coding: utf-8

from myqt import *
from ui import Ui_ImportFromTextDialog
from log_utils import logger
from common_utils import CURRENT_DIR
from db_utils import Connection
import os

class TextImporter(QDialog, Ui_ImportFromTextDialog):
    #sigOpen = pyqtSignal(str)
    def __init__(self):
        super(TextImporter, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        self.connector = Connection()
        self.logger.info('Text importer window started.')
        
        self.fname = None
        
        self.btnSelect.clicked.connect(self.select_file)
        
        
    def select_file(self):
        self.logger.info('Selecting text file.')
        cwd = os.getcwd()
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', cwd, "ALL Files (*.*)")
        
        if fname == '':
            self.lbFilePath.setText('null')
            self.logger.warning('No file selected.')
            self.fname = None
        else:
            self.lbFilePath.setText(fname)
            self.logger.info('Selected file: %s.' % (fname))
            self.fname = fname
            
        self.show_info()
        
    
    def show_info(self):
        coding = self.cbCoding.currentText()
        text = ''
        
        if self.fname == None:
            pass
        else:
        
            try:
                with open(self.fname, 'r+', encoding=coding) as f:
                    text = f.read()
            except Exception as e:
                self.logger.error('An error occurred when opening file %s.\n%s' % (self.fname, e))
                QMessageBox.critical(self, 'Error', '文件打开失败！')
        
        self.textBrowser.setPlainText(text)
    
    
    def gen_interacts(self):
        self.logger.info('Generating interacts.')
        fullText = self.textBrowser.toPlainText()
        textList = fullText.split('')
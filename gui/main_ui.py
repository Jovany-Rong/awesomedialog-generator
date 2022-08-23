# coding: utf-8

from myqt import *
from ui import Ui_MainWindow
from log_utils import logger
from common_utils import CURRENT_DIR, gen_time_based_uuid
from db_utils import Connection
from gui import DbDialog, DialogEditor, DialogSelector

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
        
        self.currentDialog = None
        self.currentInteracts = []
        
        self.__show_interact_detail()
        
        
        
        
    def __connect(self):
        self.actionConnection.triggered.connect(self.__db_config)
        self.actionNew.triggered.connect(self.__new_dialog)
        self.actionOpen.triggered.connect(self.__select_dialog)
        self.btnAdd.clicked.connect(self.__add_interact)
    
    
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
        
        
    def __select_dialog(self):
        self.logger.info('Opening dialog selector window to open a dialog.')
        
        self.dialogSelectorWindow = DialogSelector()
        self.dialogSelectorWindow.sigOpen.connect(self.__slot_open_dialog)
        self.dialogSelectorWindow.showNormal()
        
        
    def __show_conn_string(self):
        res = self.connector.get_connection_string()
        self.statusBar().showMessage(res)
        
    
    def __slot_save_dialog(self, dialogMetaInfo):
        self.logger.info('Sending saving dialog signal.')
        res = self.connector.new_dialog(dialogMetaInfo)
        if res:
            QMessageBox.information(self, 'Info', 'Success.')
            # open immediately
            self.__slot_open_dialog(dialogMetaInfo["id"])
        else:
            QMessageBox.critical(self, 'Error', 'Failed.')
            
            
    def __slot_open_dialog(self, dialogId):
        self.logger.info('Sending opening dialog %s signal.' % (dialogId))
        if dialogId == '':
            self.logger.warning('No dialog selected.')
            QMessageBox.warning(self, 'Warning', 'No dialog selected.')
        
            return
        
        dia = self.connector.get_dialog(dialogId)
        if dia == None:
            QMessageBox.critical(self, 'error', 'No such dialog found.')
        else:
            self.logger.info('Current dialog is set to %s.' % (dialogId))
            self.currentDialog = dia
            self.currentInteracts = self.connector.get_existed_interacts(dialogId)
            self.__init_table_dialog_index()
            self.__fill_table_dialog_index()
            self.__show_interact_detail()
            
            
    def __add_interact(self):
        if self.currentDialog == None:
            self.logger.warning("You have to open a dialog before you add any interact.")
            QMessageBox.warning(self, 'Warning', 'No dialog opened.')
            return
        
        self.logger.info('Sending adding interact signal.')
        i = self.connector.new_blank_interact(self.currentDialog.dialogId)
        idx = self.__max_interact_index() + 1
        self.logger.info('Setting index %s.' % (idx))
        i.interactIndex = idx
        self.currentInteracts.append(i)
        self.__init_table_dialog_index()
        self.__fill_table_dialog_index()
        row = len(self.currentInteracts) - 1
        self.tableDialogIndex.setCurrentIndex(self.tableDialogIndex.model.index(row, 0))
        self.__show_interact_detail()
            
    
            
    def __init_table_dialog_index(self):
        self.tableDialogIndex.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableDialogIndex.horizontalHeader().setStretchLastSection(True)
        self.tableDialogIndex.model = QStandardItemModel(0, 0, self.tableDialogIndex)
        #self.tableDialogIndex.model.selectionChanged.connect(self.__show_interact_detail)
        self.tableDialogIndex.setModel(self.tableDialogIndex.model)
        self.tableDialogIndex.headers = ["序号", "ID"]
        self.tableDialogIndex.model.setHorizontalHeaderLabels(self.tableDialogIndex.headers)
        self.tableDialogIndex.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.tableDialogIndex.sModel = self.tableDialogIndex.selectionModel()
        self.tableDialogIndex.sModel.selectionChanged.connect(self.__show_interact_detail)
        
        
    def __fill_table_dialog_index(self):
        ctRow = 0
        for interact in self.currentInteracts:
            
            itemIndex = QStandardItem(str(interact.interactIndex))
            itemId = QStandardItem(interact.interactId)
            
            self.tableDialogIndex.model.setItem(ctRow, 0, itemIndex)
            self.tableDialogIndex.model.setItem(ctRow, 1, itemId)
        
            ctRow += 1
            
    
    def __max_interact_index(self):
        if self.currentInteracts == []:
            return -1
        else:
            return self.currentInteracts[-1].interactIndex
        
        
    
    def __show_interact_detail(self):
        if self.currentDialog == None:
            self.spinInteractIndex.setEnabled(False)
            self.spinInteractBefore.setEnabled(False)
            self.cbInteractType.setEnabled(False)
            self.editSpeakerName.setEnabled(False)
            self.editSpeakerAvatarId.setEnabled(False)
            self.cbSpeakerAvatarPosition.setEnabled(False)
            self.textContent.setEnabled(False)
            
            return
        
        row = self.tableDialogIndex.currentIndex().row()
        if (row >= len(self.currentInteracts)) or (row < 0):
            self.spinInteractIndex.setEnabled(False)
            self.spinInteractBefore.setEnabled(False)
            self.cbInteractType.setEnabled(False)
            self.editSpeakerName.setEnabled(False)
            self.editSpeakerAvatarId.setEnabled(False)
            self.cbSpeakerAvatarPosition.setEnabled(False)
            self.textContent.setEnabled(False)
            
            return
        
        t = self.currentInteracts[row]
        self.spinInteractIndex.setEnabled(True)
        self.spinInteractBefore.setEnabled(True)
        self.cbInteractType.setEnabled(True)
        self.editSpeakerName.setEnabled(True)
        self.editSpeakerAvatarId.setEnabled(True)
        self.cbSpeakerAvatarPosition.setEnabled(True)
        self.textContent.setEnabled(True)
        
        self.lbInteractId.setText(t.interactId)
        self.spinInteractIndex.setValue(t.interactIndex)
        
        if t.interactBefore != None:
            self.spinInteractBefore.setValue(t.interactBefore)
        else:
            self.spinInteractBefore.setValue(t.interactIndex - 1)
            
        if t.interactType != None:
            self.cbInteractType.setCurrentIndex(t.interactType)
        else:
            self.cbInteractType.setCurrentIndex(0)
            
        if t.speakerName != None:
            self.editSpeakerName.setText(t.speakerName)
        else:
            self.editSpeakerName.setText('')
            
        if t.speakerAvatarId != None:
            self.editSpeakerAvatarId.setText(t.speakerAvatarId)
        else:
            self.editSpeakerAvatarId.setText('')
            
        if t.speakerAvatarPosition != None:
            self.cbSpeakerAvatarPosition.setCurrentIndex(t.speakerAvatarPosition)
        else:
            self.cbSpeakerAvatarPosition.setCurrentIndex(0)
            
        if t.content != None:
            self.textContent.setPlainText(t.content)
        else:
            self.textContent.setPlainText('')
        
        
        if self.currentDialog.dialogType == 0:
            self.cbInteractType.setCurrentIndex(0)
            self.cbInteractType.setEnabled(False)
            
        if self.spinInteractIndex.value() == 0:
            self.spinInteractBefore.setValue(-1)
            self.spinInteractBefore.setEnabled(False)
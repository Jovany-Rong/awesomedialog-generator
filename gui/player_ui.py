# coding: utf-8

from myqt import *
from ui import Ui_PlayerWindow
from log_utils import logger
from common_utils import CURRENT_DIR, deleteItemsOfLayout
from functools import partial

class PlayerWindow(QMainWindow, Ui_PlayerWindow):
    def __init__(self, dialog, interacts, startFrom=0):
        super(PlayerWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(CURRENT_DIR + '/res/logo.png'))
        self.logger = logger
        
        self.logger.info('Player window started.')
        
        self.dialog = dialog
        self.interacts = interacts
        
        self.logger.info('Playing dialog %s - %s.' % (self.dialog.dialogId, self.dialog.dialogTitle))
        
        self.selectionsLayout = QHBoxLayout(self.widgetSelections)
        
        self.load_interact(startFrom)
        
    
    def find_next_index(self, interactIndex):
        interact = None
        for t in self.interacts:
            if t.interactBefore == interactIndex:
                interact = t
                break
            
        if interact == None:
            self.logger.info('No next index found.')
            return None
        else:
            self.logger.info('Next index %s found.' % (interact.interactIndex))
            return interact.interactIndex
        
        
    def find_parallel_interacts(self, interact):
        result = []
        indexBefore = interact.interactBefore 
        for t in self.interacts:
            if t.interactBefore == indexBefore:
                if t.interactType == 1:
                    result.append(t)
                else:
                    self.logger.error('Not all parallel interacts are selections!')
                    QMessageBox.critical(self, 'Error', '并列互动并非都是选项！请检查！')
                    return []
                
        return result
                
            
    
    def load_interact(self, interactIndex):
        deleteItemsOfLayout(self.selectionsLayout)
        
        interact = None
        for t in self.interacts:
            if t.interactIndex == interactIndex:
                interact = t
                break
            
        if interact == None:
            self.logger.error('No such interact index %s.' % (interactIndex))
            QMessageBox.critical(self, 'Error', 'Interact index %s not found.' % (interactIndex))
            return
        
        interactType = interact.interactType
        
        if interactType == 0:
            self.logger.info('Loading non-selection interact %s.' % (interactIndex))
            
            speakerName = interact.speakerName
            content = interact.content 
            
            if speakerName != '':
                self.lbSpeakerName.setText(speakerName)
                self.lbSpeakerName.show()
                
                txt = '【%s】 %s\n\n' % (speakerName, content)
            else:
                self.lbSpeakerName.hide()
                
                txt = '%s\n\n' % (content)
             
            self.labelContent.setText(content)
            self.labelContent.show()
            
            originTxt = self.textBrowser.toPlainText()
            txt = originTxt + txt
            self.textBrowser.setPlainText(txt)
            
            nextIndex = self.find_next_index(interactIndex)
            
            if nextIndex != None:
                button = QPushButton('继续')
                button.clicked.connect(partial(self.load_interact, nextIndex))
                spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                self.selectionsLayout.addWidget(button)
                self.selectionsLayout.addItem(spacer)
                
        elif interactType == 1:
            parallelInteracts = self.find_parallel_interacts(interact)
            self.logger.info('Loading selection interacts.')
            
            self.lbSpeakerName.hide()
            self.labelContent.hide()
            
            for pt in parallelInteracts:
                nextIndex = self.find_next_index(pt.interactIndex)
                if nextIndex != None:
                    button = QPushButton(pt.content)
                    button.clicked.connect(partial(self.__slot_add_text_and_load_interact, pt.content, nextIndex))
                    spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
                    self.selectionsLayout.addWidget(button)
                    self.selectionsLayout.addItem(spacer)
            
        else:
            self.logger.error('Unsupported interact type %s.' % interactType)
            
            
    def __slot_add_text_and_load_interact(self, newTxt, interactIndex):
        newTxt = '%s\n\n' % (newTxt)
        originTxt = self.textBrowser.toPlainText()
        txt = originTxt + newTxt
        self.textBrowser.setPlainText(txt)
            
        self.load_interact(interactIndex)
            
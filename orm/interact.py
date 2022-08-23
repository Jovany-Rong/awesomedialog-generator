# coding: utf-8

class Interact(object):
    
    def __init__(self, id, dialogId, interactType=None, speakerName=None, speakerAvatarId=None, speakerAvatarPosition=0, interactIndex=None, interactBefore=None, content=None):
        self.interactId = id
        self.dialogId = dialogId
        self.interactType = interactType
        self.speakerName = speakerName
        self.speakerAvatarId = speakerAvatarId
        self.speakerAvatarPosition = speakerAvatarPosition
        self.interactIndex = interactIndex
        self.interactBefore = interactBefore
        self.content = content
        
    
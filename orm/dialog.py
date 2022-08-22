# coding: utf-8

class Dialog(object):
    
    def __init__(self, id, dialogType, dialogTitle, createUser, *args, **kwargs):
        self.dialogId = id
        self.dialogType = dialogType
        self.dialogTitle = dialogTitle
        self.createUser = createUser
        
    
    def insert_sql(self):
        sqlTemplate = '''insert into t_dialog_meta (dialog_id, dialog_type, dialog_title, create_user)
values ('<dialogId>', <dialogType>, '<dialogTitle>', '<createUser>')
        '''
        sql = sqlTemplate.replace('<dialogId>', self.dialogId).replace('<dialogType>', str(self.dialogType)).replace('<dialogTitle>', self.dialogTitle).replace('<createUser>', self.createUser)
        
        return sql
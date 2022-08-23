# coding: utf-8

import pymysql
from log_utils import logger
from config_utils import get_conf, set_conf, DB_ADMINISTRATORS
from crypt_utils import decrypt_str
from orm import Dialog, Interact
from common_utils import gen_time_based_uuid


class Connection(object):
    
    def __init__(self):
        self.logger = logger
        self.logger.debug('Database connection initialized.')
    
    
    def test_conn(self):
        self.logger.info('Testing connecion.')
        try:
            self.__connect_from_config()
            self.__close_connection()
            self.logger.info('Testing result: success.')
            return True
        except:
            self.logger.error('Testing result: failed.')
            return False
        
        
    def test_conn_from_params(self, conf):
        self.logger.info('Testing connecion from given parameters.')
        if self.__connect_from_params(conf):
            self.__close_connection()
            self.logger.info('Testing result: success.')
            return True
        else:
            self.logger.error('Testing result: failed.')
            return False
        
    
    def export_config(self):
        di = dict()
        self.logger.info('Exporting database config.')
        
        host = ''
        port = 3306
        database = ''
        user = ''
        
        try:
            host = get_conf('DB', 'db.host')
            portStr = get_conf('DB', 'db.port')
            port = int(portStr)
            database = get_conf('DB', 'db.database')
            user = get_conf('DB', 'db.username')
        except Exception as e:
            self.logger.error('An error occurred when getting connection information from config.\n%s' % (e))
        
        di["host"] = host
        di["port"] = port
        di["database"] = database
        di["user"] = user
        
        return di
    
    
    def set_config(self, opt, val):
        sec = 'DB'
        self.logger.info('Setting database config: %s' % (opt))
        try:
            set_conf(sec, opt, val)
            return True
        except Exception as e:
            self.logger.error('An error occurred when setting database connection config %s.\n%s' % (opt, e))
            return False
        
        
    def get_connection_string(self):
        conf = self.export_config()
        if (conf["host"] == '') or (conf["user"] == ''):
            res = '未连接'
        else:
            res = '%s@%s:%s/%s' % (conf["user"], conf["host"], conf["port"], conf["database"])
        self.logger.info('Getting current connection string: %s' % (res))
        return res
        
        
    def new_dialog(self, dialogMetaInfo):
        self.logger.info('Creating new dialog: %s' % (dialogMetaInfo))
        creator = self.export_config()["user"]
        dia = Dialog(dialogMetaInfo["id"], dialogMetaInfo["dialogType"], dialogMetaInfo["dialogTitle"], creator)
        sql = dia.insert_sql()
        res = self.__exec_sql_without_result(sql)
        if res:
            return True
        else:
            return False
        
        
    def new_blank_interact(self, dialogId):
        self.logger.info('Creating new blank interact of dialog %s.' % (dialogId))
        uuid = gen_time_based_uuid()
        t = Interact(uuid, dialogId)
        self.logger.info('Using uuid: %s' % (uuid))
        return t
        
        
    def get_existed_interacts(self, dialogId):
        self.logger.info('Getting existing interacts of dialog %s.' % (dialogId))
        sql = """
        select * from t_dialog_data where dialog_id = '%s' order by interact_index asc
        """
        result = self.__exec_sql_with_all_result(sql)
        if result == []:
            self.logger.warning('No interact found.')
            return []
        t = list()
        for row in result:
            i = Interact(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            t.append(i)
        self.logger.info('%s interact(s) found.' % (len(t)))
        return t
        
    
    def search_owned_dialogs(self):
        creator = self.export_config()["user"]
        if creator in DB_ADMINISTRATORS:
            self.logger.info('Searching all dialogs because you are an administrator.')
            filterCondition = ' where 1 = 1'
        else:
            self.logger.info('Searching dialogs created by user %s.' % (creator))
            filterCondition = " where create_user = '%s'" % (creator)
            
        sql = "select * from t_dialog_meta" + filterCondition
        
        result = self.__exec_sql_with_all_result(sql)
        self.logger.info('%s result(s) found.' % (len(result)))
        
        return result
        
        
    def get_dialog(self, dialogId):
        result = self.__search_table_with_pk('t_dialog_meta', 'dialog_id', dialogId)
        if result == []:
            self.logger.error('No such dialog ID: %s' % (dialogId))
            return None
        dia = Dialog(dialogId, result[0][1], result[0][2], result[0][5])
        self.logger.info('Dialog found.')
        return dia
        
    
    ### basic methods
    
    def __connect_from_config(self):
        try:
            host = get_conf('DB', 'db.host')
            portStr = get_conf('DB', 'db.port')
            port = int(portStr)
            database = get_conf('DB', 'db.database')
            user = get_conf('DB', 'db.username')
            passwordEnc = get_conf('DB', 'db.password')
            password = decrypt_str(passwordEnc)
        except Exception as e:
            self.logger.error('An error occurred when getting connection information from config.\n%s' % (e))
            raise e
        
        self.logger.debug('Connecting to database: %s@%s:%s/%s .' % (user, host, port, database))
        
        try:
            self.conn = pymysql.connect(host=host, port=port, database=database, user=user, password=password)
            self.logger.info('Database connection created.')
        except Exception as e:
            self.logger.error('Failed to connect to database.\n%s' % (e))
            raise e
        
        try:
            self.cursor = self.conn.cursor()
            self.logger.info('Cursor created.')
        except Exception as e:
            self.logger.error('Failed to create cursor.\n%s' % (e))
            raise e
        
    
    def __connect_from_params(self, conf):
        try:
            host = conf["host"]
            port = conf["port"]
            database = conf["database"]
            user = conf['user']
            password = conf["password"]
        except Exception as e:
            self.logger.error('An error occurred when getting connection information from config.\n%s' % (e))
            raise e
        
        self.logger.debug('Connecting to database: %s@%s:%s/%s .' % (user, host, port, database))
        
        try:
            self.conn = pymysql.connect(host=host, port=port, database=database, user=user, password=password)
            self.logger.info('Database connection created.')
        except Exception as e:
            self.logger.error('Failed to connect to database.\n%s' % (e))
            return False
        
        try:
            self.cursor = self.conn.cursor()
            self.logger.info('Cursor created.')
        except Exception as e:
            self.logger.error('Failed to create cursor.\n%s' % (e))
            return False
        
        return True
        
    
    def __close_connection(self):
        try:
            self.cursor.close()
            self.logger.info('Cursor closed.')
        except:
            self.logger.warning('Failed to close cursor.')
            
        try:
            self.conn.close()
            self.logger.info('Database connection closed.')
        except:
            self.logger.warning('Failed to close database connection.')
            
    
    def __exec_sql_without_result(self, sql):
        self.logger.debug('Executing sql: %s' % (sql))
        try:
            self.__connect_from_config()
            self.cursor.execute(sql)
            self.conn.commit()
            self.__close_connection()
            return True
        except Exception as e:
            self.logger.error('SQL exception occured: %s.\nSQL is: %s' % (e, sql))
            return False
        
        
    def __exec_sql_with_all_result(self, sql):
        self.logger.debug('Executing sql and getting result: %s' % (sql))
        try:
            self.__connect_from_config()
            self.cursor.execute(sql)
            result = list(self.cursor.fetchall())
            self.__close_connection()
            self.logger.debug('Result: %s' % (result))
            return result
        except Exception as e:
            self.logger.error('SQL exception occured: %s.\nSQL is: %s' % (e, sql))
            return []
        
        
    def __search_table_with_pk(self, tableName, pkColumn, pkVal):
        sql = '''
select * from %s where %s = '%s' limit 1
        ''' % (tableName, pkColumn, pkVal)
        result = self.__exec_sql_with_all_result(sql)
        return result
            

if __name__ == "__main__":
    c = Connection()
    c.test_conn()
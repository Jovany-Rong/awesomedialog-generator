# coding: utf-8

import pymysql
from log_utils import logger
from config_utils import get_conf
from crypt_utils import decrypt_str


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
            
            

if __name__ == "__main__":
    c = Connection()
    c.test_conn()
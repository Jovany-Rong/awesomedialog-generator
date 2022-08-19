# coding: utf-8

import pymysql
from log_utils import logger
from config_utils import get_conf
from crypt_utils import decrypt_str


class Connection(object):
    
    def __init__(self):
        self.logger = logger
        self.logger.debug('Database connection initialized.')
    
    
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
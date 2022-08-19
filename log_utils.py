# coding: utf-8

import logging
from logging.handlers import RotatingFileHandler
import random
from common_utils import CURRENT_DIR
from config_utils import get_conf
from version import VERSION

def __create_logger(debug=False):
    '''
    Create the logger.
    '''
    sid = random.randint(10000000, 99999999)
    loggerName = 'AwesomeDialog-%s' % sid
    logger = logging.getLogger(loggerName)
    
    debugStr = get_conf('LOGGING', 'logging.debug')
    if debugStr.lower().strip() == 'true':
        debug = True
    
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    
    filePath = get_conf('LOGGING', 'logging.file')
    if filePath == '':
        filePath = CURRENT_DIR + '/adg.log'
        
    rHandler = RotatingFileHandler(filePath, maxBytes=1024 * 1024 * 32, backupCount=10)
    if debug:
        rHandler.setLevel(logging.DEBUG)
    else:
        rHandler.setLevel(logging.INFO)
        
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(name)s - %(message)s')
    rHandler.setFormatter(formatter)
    logger.addHandler(rHandler)
    logger.info('AwesomeDialog (version %s) logger starts.' % VERSION)
    
    return logger
    
logger = __create_logger()
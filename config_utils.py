# coding: utf-8

import configparser as cp 
from common_utils import CURRENT_DIR

def __create_conf():
    config = cp.ConfigParser()
    config.read(CURRENT_DIR + '/adg.conf', encoding='utf-8')
    return config


configObj = __create_conf()


def save_conf():
    with open(CURRENT_DIR + '/adg.conf', 'w+', encoding='utf-8') as f:
        configObj.write(f)
        
        
def get_conf(sec, opt):
    try:
        tmp = configObj.get(sec, opt)
    except:
        tmp = ''
        
    tmp = tmp.replace('<<currentDir>>', CURRENT_DIR)
    
    return tmp


if __name__ == "__main__":
    val = get_conf('LOGGING', 'logging.file')
    print(val)
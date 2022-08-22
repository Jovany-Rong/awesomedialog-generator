# coding: utf-8

import os
import sys
from datetime import datetime
import string
import random

def getDirPath():
    if getattr(sys, 'frozen', False):
        return os.path.abspath(os.path.dirname(sys.executable)).replace('\\', '/')
    elif __file__:
        return os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
    

def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())
    

CURRENT_DIR = getDirPath()


def gen_time_based_uuid(strlen=6):
    nowStr = datetime.now().strftime('%Y%m%d%H%M%S')
    
    samp = string.ascii_letters + string.digits
    suffix = ''.join(random.sample(samp, strlen))
    
    return '%s-%s' % (nowStr, suffix)


if __name__ == "__main__":
    #print(CURRENT_DIR)
    print(gen_time_based_uuid())
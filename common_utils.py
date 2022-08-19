# coding: utf-8

import os
import sys

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


if __name__ == "__main__":
    print(CURRENT_DIR)
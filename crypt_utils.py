# coding: utf-8

import base64
from version import VERSION_SALT

def encrypt_str(text):
    salt = ('YouCanNeverGuessIt!!' + VERSION_SALT).replace(' ', '').strip()
    textByte = text.encode(encoding='utf-8')
    temp1 = base64.b64encode(textByte)
    print(temp1)
    temp2 = temp1.decode(encoding='utf-8').strip()
    temp3 = temp2 + salt
    temp4 = temp3.encode(encoding='utf-8')
    temp5 = base64.b64encode(temp4)
    temp6 = temp5.decode(encoding='utf-8').strip()
    
    return temp6

def decrypt_str(text):
    salt = ('YouCanNeverGuessIt!!' + VERSION_SALT).replace(' ', '').strip()
    lenSalt = len(salt)
    temp6 = text.strip()
    temp5 = temp6.encode(encoding='utf-8')
    temp4 = base64.b64decode(temp5).strip()
    temp3 = temp4.decode(encoding='utf-8').strip()
    temp2 = temp3[:-lenSalt].strip()
    temp1 = temp2.encode(encoding='utf-8')
    textByte = base64.b64decode(temp1)
    res = textByte.decode(encoding='utf-8').strip()
    
    return res


if __name__ == "__main__":
    print(encrypt_str('abcd1234'))    
    
    print(decrypt_str('WVdKalpERXlNelE9WW91Q2FuTmV2ZXJHdWVzc0l0ISEwMDE='))
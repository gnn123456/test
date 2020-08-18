import time
import datetime
import hashlib
from pyDes import des, CBC, PAD_PKCS5
import binascii
""" 10位时间戳"""
def time_sj():
    a = int(time.time())
    return a

""" MD5加密"""
def MD5Test(s):
    m = hashlib.md5()
    m.update(s.encode('UTF-8'))
    return m.hexdigest()


















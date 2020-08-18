from pyDes import *
import base64
# Des_Key = b"CF8D1911" # 相当于加密钥
# Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7" # 自定IV向量（官网例子就是这么写的）
#加密id算法
def encrypt_str(s):
    Des_Key = b"CF8D1911"
    Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7"
    k = des(Des_Key, ECB, Des_IV, pad=None, padmode=PAD_PKCS5)
    encrystr = k.encrypt(s)
    print(base64.b64encode(encrystr))
    return base64.b64encode(encrystr)

#解密id算法
def decrypt_str(s):
     Des_Key = b"CF8D1911"
     Des_IV = b"\x22\x33\x35\x81\xBC\x38\x5A\xE7"
     k = des(Des_Key, ECB, Des_IV, pad=None, padmode=PAD_PKCS5)
     decrystr = k.decrypt(base64.b64decode(s))
     decrystr = decrystr.decode('utf8')
     # print(decrystr)
     # return decrypt_str
     return decrystr

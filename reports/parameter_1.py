from reports.methods import time_sj
from reports.methods import MD5Test
from midd.ll import login,token_1
import requests
from reports.jm import decrypt_str
class data_1:
    Version = "1.0"
    TimeStamp = str(time_sj())
    versionQD = "1234567890"
    RequestId = "10000000000000000"
    ChannelNo = "HY"
    Token = "TOKEN_337298514abaa358298845cf5bcebab6"
    Hmac = MD5Test(
        "ChannelNo=HY&RequestId=10000000000000000&TimeStamp=" + TimeStamp + "&Token=" + Token + "&Version=1.0" + versionQD).upper()
    data1 = {"Version": "1.0", "TimeStamp": str(time_sj()),
             "RequestId": "10000000000000000", "ChannelNo": "HY", "Hmac":Hmac , "Token": Token}
    dat = {"Password":MD5Test("123123gnn").upper()}
    data1["data"] = dat
    url = "https://t-bjbus.tuspass.net/member/checkPassword"

    res = requests.request(method="post", url=url, json=data1)
    # print(login())
    print(decrypt_str(res.json()))
    # print(Token)
q
"""  未使用token前的请求体"""
from reports.methods import time_sj
from reports.methods import MD5Test
class data_1:
    Version = "1.0"
    TimeStamp = str(time_sj())
    versionQD = "1234567890"
    RequestId = "10000000000000000"
    ChannelNo = "HY"
    Hmac = MD5Test(
        "ChannelNo=HY&RequestId=10000000000000000&TimeStamp=" + TimeStamp + "&Version=1.0" + versionQD).upper()
    data1 = {"Version": "1.0", "TimeStamp": str(time_sj()),
                "RequestId": "10000000000000000", "ChannelNo": "HY", "Hmac": Hmac}



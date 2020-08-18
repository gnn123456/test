
import requests
from common.confin import confing
from reports.jm import decrypt_str
from reports.methods import MD5Test
from reports.parameter import data_1

class Request:
    def request(self,method,url,json):
        """ 把方法转换为大写"""
        method=method.upper()
        """ 地址路径进行拼接"""
        confin=confing()
        url_1=confin.get("api","pre_url")
        url=url_1+url
        """参数str强转为dict"""
        if type(json) == str:
            json=eval(json)
        """公共参数与参数进行拼接请求接口"""
        if method=="GET":
            return requests.request(method,url=url,json=json)
        if method=="POST":
            return requests.request(method,url=url,json=json)
        else:
            print("接口错误")
if __name__=="__main__":
    url="/member/login"
    method="post"
    data={"Mobile":"18735571533","Password":MD5Test("123123gnn").upper(),"deviceid":"123"}
    data_2 = data_1.data1
    data_2["data"] = data
    res=Request().request(method=method,url=url,json=data_2)
    print(decrypt_str(res.json()))
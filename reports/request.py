# 用session来保存cookise，
import requests
from common.confin import confing

# data = {"mobilephone": "", "pwd": "123123"}
class Request:
    def __init__(self):
        self.session=requests.session()           #放在初始化函数里，可以存放登陆过的cookis
    def request(self,method,url,data=None):      #可以给她赋值一个变量，获取响应信息，然后和excel表里的期望信息进行判断
        method=method.upper()                       #把方法转换为大写
        confin=confing()
        url_1=confin.get("api","pre_url")
        url=url_1+url
        if data is not None and type(data)==str:    #如果参数为None或者为字符串类型。就把她转换成join格式
            data=eval(data)                           #eval转换
        if method=="GET":
            return self.session.request(method,url=url,params=data)
        if method=="POST":
            return self.session.request(method,url=url,data=data)
        else:
            print("cuowu")
# if __name__=="__main__":
#     ww= Request().request("post","http://test.lemonban.com/futureloan/mvc/api/member/register",data=data)
#     print(ww.text)
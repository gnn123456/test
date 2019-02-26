# import requests
# # # 注册接口调用
# data={"mobilephone":15003556788,"pwd":123456}
# res=requests.get("http://test.lemonban.com/futureloan/mvc/api/member/login",params=data)
# print(res.json())
# data={"memberId":13593299566,"title":"大哥大姐们啊,可怜可怜",
#       "amount":20000,"loanRate":"12.0",
#       "loanTerm":3 ,"loanDateType":0,"repaymemtWay":11,"biddingDays":5}
#
# resp=requests.get("http://test.lemonban.com/futureloan/mvc/api/loan/add",params=data,cookies=res.cookies)
# print(resp.json())

#
# import re
# data={"admin_user":"15234567583","admin_pwd":"123456gnn"}
# s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
# p="\$\{(.*?)}"
# a=re.search(p,s)            #在s里面查找p
# print(a)                    #
# g=a.group()                 #查找第一个admin——user
# print(g)
# g1=a.group(1)               #取出来他的值
# print(g1)
# value=data[g1]               #取出来替换的值
# print(value)
# s=re.sub(p,value,s,count=1)
# print(s)
#
import re
from common.confin import confing
class dey:
    admin_user=confing().get("data","admin_user")
    admin_pwd=confing().get("data","admin_pwd")
    add_user=confing().get("data","add_user")
    tzr_user=confing().get("data","tzr_user")
    tzr_pwd=confing().get("data","tzr_pwd")
    tzr_userid=confing().get("data","tzr_userid")
def replance(s):
    p="\$\{(.*?)}"
    while  re.search(p, s):      #在s里面查找p
        m=re.search(p,s)         #
        key=m.group(1)
       #获取的是元组，然后取出来，
        if hasattr(dey,key):
            value=getattr(dey,key)
            s=re.sub(p,value,s,count=1)
        else:
            return None
    return s
s = '{"mobilephone":"${tzr_user}","pwd":"${tzr_pwd}"}'
s=replance(s)
print(s)






# 反射
# class boy:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def shuaiqi(self):
#         print(self.name,"往后余生，风雪是你，陪伴是你，暴富也是你")
# if __name__=="__main__":
#     gnn=boy("郭牛牛",23)
#     setattr(boy,"ny","zy")   #  给类或者实列对象动态参加属性和方法
#
#     print(getattr(boy,"ny"))      #获取这个属性的值
#     print(hasattr(boy,"main"))    #比较
import logging
import logging.handlers
def get_logger(logger_name):
    logger=logging.getLogger(logger_name)  #创建一个自己得容器
    logger.setLevel("DEBUG")         #给自己得容器设置级别

    formatter=logging.Formatter("%(asctime)s-"      #当前时间          #设置输出渠道
                                 "[%(levelname)s]-"   #当前级别
                                 "%(filename)s-"    #当前日志执行的模块名
                                 "%(name)s-"        #当前日志名
                                 "日志信息:%(message)s")  #日志信息
    #1设置一个输出到控制台得输出渠道，指定输出
    sc=logging.StreamHandler()
    sc.setLevel("DEBUG")
    sc.setFormatter(formatter)

    #输出指定得级别到一个文件内
    file=logging.handlers.RotatingFileHandler("thyon13.log",encoding="UTF-8")
    file.setLevel("INFO")
    file.setFormatter(formatter)
    # sc.setFormatter(formatter)


    logger.addHandler(sc)
    logger.addHandler(file)
    return logger
# logging=get_logger(logger_name="郭牛牛")
# logging.error("this.is error")

# wologer.debug("这是debug的报错信息")
# wologer.info("这是轻微错误")
# wologer.warning("这是差不多的错误")
# wologer.error("这是严重的错误")
# wologer.critical("这是致命的错误")
#
















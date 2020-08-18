# 环境的来回切换（线上，和测试）给配置文件写成一个类，如果是Ture就执行这个；
import configparser
from common import splicing
import configparser     #默认需要导入的
from common import splicing
class confing:
    def __init__(self):
        self.s=configparser.ConfigParser()
        self.s.read(splicing.conf2_dir,encoding="utf-8")#读取那个配置文件
        open=self.s.getboolean("swich","open")
        if open:
            self.s.read(splicing.conf_dir,encoding="utf-8")
        else:
            self.s.read(splicing.conf1_dir,encoding="utf-8")
    def get(self,section,option):
        return self.s.get(section,option)
if __name__=="__main__":
    # print(confing.get(api,"pre_url"))
    #
    # url_1 = confing().get("api", "pre_url")
    # print(url_1)
    admin_user = confing().get("data", "data1")
    # admin_pwd = confing().get("data","admin_pwd")

    print(admin_user)
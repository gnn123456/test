
#设置绝对路径的使用
import os
dirpat=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  #上上级目录 的绝对路径
data_dir=os.path.join(dirpat,"datas")      #路径拼接
file_os=os.path.join(data_dir,"dyl.xlsx")
file_os1=os.path.join(data_dir,"casas.xlsx")
print(file_os1)

test_dir=os.path.join(dirpat,"test_case")
conf=os.path.join(dirpat,"conf")
conf_dir=os.path.join(conf,"test_conf")
conf1_dir=os.path.join(conf,"test2_conf")
conf2_dir=os.path.join(conf,"glob")
print(test_dir)
ceyl=os.path.join(dirpat,"datas")
cey_html=os.path.join(ceyl,"cey.html")
test_d=os.path.join(dirpat,"test_cake1")

# 测试报告的路径
from datetime import datetime
ts=datetime.now().strftime("%y-%m-%d-%H-%M-%S")
reports_filename="reports-{}.html".format(ts)
reports=os.path.join(ceyl,reports_filename)

# 保存token的yaml
# conf_dir=os.path.join(conf,"token.yaml")


# 执行日志的路径
reports_log=os.path.join(ceyl,"柠檬班.log")








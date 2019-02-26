
#设置绝对路径的使用
import os
dirpat=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))   #绝对路径
data_dir=os.path.join(dirpat,"datas")      #路径拼接
file_os=os.path.join(data_dir,"dyl.xlsx")
test_dir=os.path.join(dirpat,"test_case")
conf=os.path.join(dirpat,"conf")
conf_dir=os.path.join(conf,"test_conf")
conf1_dir=os.path.join(conf,"test2_conf")
conf2_dir=os.path.join(conf,"glob")
print(test_dir)
ceyl=os.path.join(dirpat,"datas")
cey_html=os.path.join(ceyl,"cey.html")



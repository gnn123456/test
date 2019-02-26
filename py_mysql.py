import pymysql#先自行安装pip install pymysql
#1.建立连接数据库
host="test.lemonban.com"
user="test"
password="test"
mysql=pymysql.connect(host=host, user=user, password=password, port=3306)
# 2.新建一个查询页面
cursor=mysql.cursor()
# 3.编写sql----***
sql="SELECT mobilephone FROM future.member ORDER BY MobilePhone DESC LIMIT 1"
# 4.执行sql
cursor.execute(sql)
# 5查看结果(查看最近的一条）
result=cursor.fetchone()
print(result[0])
# 6.关闭查询
cursor.close()
# 7.数据库关闭
mysql.close()
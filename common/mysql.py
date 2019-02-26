# 首先安装pip  install pymysql；链接数据库，用里给excel表里的注册实现最大手机号加1/
import pymysql
class mysqlni:
    def __init__(self,retu_dict):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        #建立链接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
        #新建一个查询
        if retu_dict:
            self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)#指定每行数据字典形式返回
        else:
            self.cursor = self.mysql.cursor()
    def fet(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result
    def fet_all(self,sql):
        self.cursor.execute(sql)
        #获取结果
        result=self.cursor.fetchall()
        return result
    def close(self):
        self.cursor.close()
        self.mysql.close()
if __name__=="__main__":
    # mysql=mysqlni(retu_dict=False)
    # ww=mysql.fet("SELECT mobilephone FROM future.member ORDER BY MobilePhone DESC LIMIT 1")
    # print(ww[0])
    mysql = mysqlni(retu_dict=True)
    ww=mysql.fet_all("select * from future.member limit 1")
    print(ww[0])
    for w in  ww:
        print(w)
    mysql.close()

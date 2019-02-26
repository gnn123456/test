import unittest
from common.do_excel import Do_excel
from common.cl import file_os
from reports.request import Request
from libext.ddtnew import ddt,data
from common.mysql import mysqlni


@ddt
class register(unittest.TestCase):
    do_excel = Do_excel(file_os, "register")
    cases = do_excel.excel()


    @classmethod
    def setUpClass(cls):  # 整个类的开始准备工作
        cls.request = Request()

    def setUp(self):
        print("------------------开始执行测试用例----------------------")

        self.mysql = mysqlni(retu_dict=True)     #创建数据库链接
        red = "SELECT max(mobilephone) as max_phone FROM future.member ORDER BY MobilePhone DESC LIMIT 1"
        self.max = self.mysql.fet(red)["max_phone"]#执行sql，并返回最近的一条数据
    # print(max[0])

    @data(*cases)
    def test_login(self, case):
        print("开始执行         第几个条测试用例{}".format(case.case_id))
        import json
        data_dice = json.loads(case.data)
        if data_dice["mobilephone"] == "${r_b}":
            data_dice["mobilephone"] = int(self.max) + 1

        res = self.request.request(case.method, case.url, data_dice)
        # ss = case.expected
        # print(type(ss))
        # aa=int(type(res.json()["code"]))
        # print(type(aa))
        try:
            self.assertEqual(str(case.expected), res.json()["code"])
            if res.json()["msg"]=="注册成功":
                sql="select * from future.member where mobilephone={}" .format(data_dice["mobilephone"])
                ress=self.mysql.fet_all(sql)
                #首先判断是否成功插入数据；
                self.assertEquals(1,len(ress))
                meber=ress[0]
                self.assertEquals(0,meber["LeaveAmount"])#判断注册成功余额应该为0            self.do_excel.write_data(case.case_id + 1, res.text, "pass")
            print("第{}条的结果为：pass".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_data(case.case_id + 1, res.text, "Flas")
            print("第{}条的结果为：Flas".format(case.case_id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()

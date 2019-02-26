import unittest
from common.do_excel import Do_excel
from common.cl import file_os
from reports.request import Request
from libext.ddtnew import ddt,data
from test_case import vvvv
import re
@ddt
class recharge(    unittest.TestCase):
    do_excel = Do_excel(file_os, "recharge")
    cases = do_excel.excel()
    request = Request()

    @classmethod
    def setUpClass(cls):  # 整个类的开始准备工作
     cls.request = Request()
    def setUp(self):
        print("------------------开始执行测试用例----------------------")

    @data(*cases)
    def test_login(self,case):
            print("开始执行第几个条测试用例{}".format(case.case_id))
            data=vvvv.replance(case.data)
            res = self.request.request(case.method, case.url, data)
            # ss = case.expected
            # print(type(ss))
            # aa=int(type(res.json()["code"]))
            # print(type(aa))
            try:
                self.assertEqual(str(case.expected),res.json()["code"])
                self.do_excel.write_data(case.case_id + 1, res.text, "pass")
                print("第{}条的结果为：pass".format(case.case_id))
            except AssertionError as e:
                self.do_excel.write_data(case.case_id + 1, res.text, "Flas")
                print("第{}条的结果为：Flas".format(case.case_id))
                raise e
    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()


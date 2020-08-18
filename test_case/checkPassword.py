import json
import unittest
from reports.jm import decrypt_str
from common.do_excel import Do_excel
from common.splicing import file_os1
from libext.ddtnew import ddt, data
from logs.log import get_logger
from reports.request import Request
from reports.parameter_1 import data_1
logging=get_logger(logger_name="校验密码断言处理")
@ddt
class Check(unittest.TestCase):
    do_excel = Do_excel(file_os1, "checkPassword")
    cases = do_excel.excel()
    def setUp(self):
        print("------------------开始执行校验密码测试用例----------------------")
    @data(*cases)
    def test_login(self,case):
        logging.info("开始执行第{}个条测试用例".format(case.case_id))
        data_2=data_1.data1
        data_2["data"]=json.loads(case.data)
        res = Request().request(case.method,case.url,data_2)
        test_api=json.loads(decrypt_str(res.json()))
        try:
            excepted = eval(case.expected)
            for key, value in excepted.items():
                self.assertEqual(value, test_api[key])
            self.do_excel.write_data(case.case_id + 1, res.text, "pass")
            logging.error("第{}条的结果为：pass".format(case.case_id))

        except AssertionError as e:
            self.do_excel.write_data(case.case_id + 1, res.text, "flas")
            logging.error("第{}条的结果为：flas".format(case.case_id))
            raise e
#
import json
import unittest
from reports.jm import decrypt_str
from common.do_excel import Do_excel
from common.mysql import mysqlni
from common.register import gen_mobile
from common.splicing import file_os1
from libext.ddtnew import ddt, data
from logs.log import get_logger
from reports.request import Request
from reports.parameter import data_1

logging=get_logger(logger_name="注册断言处理")
@ddt
class Register(unittest.TestCase):
    do_excel = Do_excel(file_os1, "register")
    cases = do_excel.excel()


    def setUp(self):
        print("------------------开始执行注册测试用例----------------------")
        self.mysql = mysqlni(retu_dict=True)


    @data(*cases)
    def test_login(self,case):
        if "#phone#" in case.data:
            phone=gen_mobile()
            case.data=case.data.replace("#phone#",phone)
        logging.info("开始执行第{}个条测试用例".format(case.case_id))
        data_2=data_1.data1
        data_2["data"]=json.loads(case.data)
        res = Request().request(case.method,case.url,data_2)
        test_api=json.loads(decrypt_str(res.json()))
        # print(test_api)
        try:
            excepted=eval(case.expected)
            for key , value in excepted.items():
                self.assertEqual(value,test_api[key])
            if test_api["Status"] == 000000:
                data_dice = json.loads(case.data)
                sql="select * from ab_member where mobile=to_base64(AES_ENCRYPT('{}','19549303ghdyoscc'))".format(data_dice["Mobile"])
                sql = "select * from futureloan.member where mobile_phone={};".format(data_dice["mobile_phone"])
                ress = self.mysql.fet_all(sql)
                self.assertTrue(ress)

            self.do_excel.write_data(case.case_id + 1, res.text, "pass")
            logging.error("第{}条的结果为：pass".format(case.case_id))

        except AssertionError as e:
            self.do_excel.write_data(case.case_id + 1, res.text, "flas")
            logging.error("第{}条的结果为：flas".format(case.case_id))
            raise e
    #
    def tearDown(self):
        self.mysql.close()



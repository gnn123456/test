# import unittest
# from libext import HTML
# from common import cl
# s=unittest.defaultTestLoader.discover(cl.test_dir,pattern="test_*.py",top_level_dir=None)
# with open(cl.cey_html,"wb+")as file:
#     runner=HTML.HTMLTestRunner(stream=file,
#                                             title="excel测试报告",
#                                             description="测试我们得类",
#                                             tester="niu")
#
#     runner.run(s)


import unittest
"""这是导入的绝对路径"""
from common import splicing
from libext import HTML
from common.splicing import reports
# 初始化一个加载器 test_loader
loader=unittest.TestLoader()
# 使用loader收集 所有测试用例,
"""cl.test_d,我用路径拼接到test测试模块"""
suit=loader.discover(splicing.test_dir)
# from datetime import datetime
# ts=datetime.now().strftime("%y-%m-%d-%H-%M-%S")
# reports_filename="reports-{}.html".format(ts)
# 执行测试用例
# runner=unittest.TextTestRunner()
# runner.run(suit)

with open(reports,"wb") as f:
    runner=HTML.HTMLTestRunner(stream=f,
                                title="柠檬班接口测试报告",
                                description="接口测试",
                                tester="郭牛牛")

    runner.run(suit)


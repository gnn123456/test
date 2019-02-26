import unittest
from libext import HTML
from common import cl
s=unittest.defaultTestLoader.discover(cl.test_dir,pattern="test_*.py",top_level_dir=None)
with open(cl.cey_html,"wb+")as file:
    runner=HTML.HTMLTestRunner(stream=file,
                                            title="excel测试报告",
                                            description="测试我们得类",
                                            tester="niu")

    runner.run(s)

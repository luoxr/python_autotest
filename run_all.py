__author__ = "luo"

import sys
import unittest
from BeautifulReport import BeautifulReport
from demo_test.create_clear_report import *
from demo_test.testCase.test_faxian import FaXianTest

path = os.getcwd() + "/run_all.py"
sys.path.append(path)

test_cases = (FaXianTest,)


def whole_suite():

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 遍历所有测试类
    for test_class in test_cases:
        # 从测试类中加载测试用例
        tests = loader.loadTestsFromTestCase(test_class)
        # 将测试类添加到测试包中
        suite.addTests(tests)

    return suite


if __name__ == '__main__': 
    # 创建测试运行器（verbosity=2可以生成更详细的测试信息）
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(whole_suite())

    create_report_dirs()
    # clear_report_files()

    report_name = "/report/" + "测试报告"
    runner = BeautifulReport(whole_suite())
    runner.report(filename=report_name, description='python+requests+unittest+excel+ddt测试')



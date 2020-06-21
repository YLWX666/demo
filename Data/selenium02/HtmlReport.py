import HTMLTestRunner
import unittest
from time import strftime, localtime, time

from selenium02.TestCase import SearchTestCase


suite = unittest.TestSuite()
# 获取TestSuite的实例对象
suite.addTest(SearchTestCase("test_searchChina"))
# 把测试用例添加到测试容器中

now = strftime("%Y-%m-%M-%H_%M_%S", localtime(time()))
# 获取当前时间
filename = now + "test.html"
# 文件名

fp = open(filename, "wb")
# 以二进制的方式打开文件并写入结果
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title="测试报告的标题",
    description="测试报告的详情")

runner.run(suite)

fp.close()
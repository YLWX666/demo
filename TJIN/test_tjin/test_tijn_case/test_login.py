import unittest
from element_step.step import StepElement

class TestTijn(unittest.TestCase):


    def setUp(self):
        self.driver = StepElement()
        self.driver.open_url('https://tj.uat.heywind.cn/')

    def tearDown(self):
        self.driver.close_web()
#首页转盘登录
    def test_login(self):
        success_log = self.driver.login(0)
        self.assertEquals(success_log,'MY ACCOUNT',"不匹配，登录失败")

#SIGN IN登录
    def test_sign_login(self):
        success_log = self.driver.sign_login(1)
        self.assertEquals(success_log, 'MY ACCOUNT', "不匹配，登录失败")










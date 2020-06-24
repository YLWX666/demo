import unittest
import ddt
import time
from test_tjin.datas import get_datas
from element_step.step import StepElement
from BeautifulReport import BeautifulReport as Be
from HTMLTestRunner import HTMLTestRunner

data = get_datas.json_data(get_datas.get_path_file('email'))

@ddt.ddt()
class TestCheckOut(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn/')
    def tearDown(self) -> None:
        self.driver.close_web()


    def judge_element(self,element):
        try:
            time.sleep(1)
            error = self.driver.by_xpath(element).get_attribute('textContent')
            return error
        except:
            return ""

#新用户合法与非法登录
    @ddt.data(*data)
    def test_visitors(self,datas):
        '''新用户合法与非法登录'''
        self.driver.delete_pan(1)
        time.sleep(2)
        self.driver.add_cart()
        time.sleep(2)
        self.driver.enter_checkout()
        self.driver.checkout_visitor(datas['email'])
        self.driver.click_arb()
        infor = self.judge_element('//p[@class="hint error_text"]')
        self.assertEqual(infor,datas['errorinformation'])





# if __name__ == "__main__":
#     unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(TestCheckOut))
#     f = open('报告.html','wb')
#     b = HTMLTestRunner(f,title='测试报告标题',description='测试报告描述')
#     b.run(suite)
























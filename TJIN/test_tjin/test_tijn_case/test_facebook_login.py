import time
import unittest
from element_step.step import StepElement
from ele_common.common import Get_data


class TestFacebookLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn')

    def tearDown(self) -> None:
        self.driver.close_web()

    def test_facebook_login(self):
        '''测试首页转盘facebook登录'''
        datas = Get_data('element_yaml')
        self.driver.facebook_login(6)
        test = self.driver.judge_element(datas.data(6,4))
        self.assertEqual(test,'GO SHOPPING',msg='登录不成功')

    def test_checkout_facebook_login(self):
        '''checkout FACEBOOK登录'''
        self.driver.delete_pan(1)
        self.driver.add_cart()
        self.driver.enter_checkout()
        self.driver.facebook_click()
        self.driver.facebook_login_info(6)
        test = self.driver.judge_element('//p[@class="emainAdd"]')
        self.assertEqual(test,'steckoklqo_1591429998@tfbnw.net',msg='登录失败')


# if __name__ == "__main__":
#     unittest.main()






















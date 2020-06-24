import time
import unittest
from element_step.step import StepElement


class TestCardPay(unittest.TestCase):
    '''测试游客信用卡支付'''

    #已注册，无购买用户
    lists = ['789764645@qq.com','464864481@qq.com','161846489@qq.com','6484641831@qq.com']

    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn')

    def tearDown(self) -> None:
        self.driver.close_web()

    def dele_list(self):
        self.lists.pop()


    def test_card_pay(self):
        '''游客信用卡支付流程'''
        email = self.driver.email_address()
        time.sleep(2)
        self.driver.delete_pan(1)
        time.sleep(2)
        self.driver.add_cart()
        time.sleep(2)
        self.driver.enter_checkout()
        time.sleep(2)
        self.driver.checkout_visitor(email)
        self.driver.checkout(5, email)
        time.sleep(2)
        test = self.driver.card_pay()
        self.assertEqual(test, 'Your order payment successful')
        time.sleep(2)

    def test_no_password_visitor(self):
        """测试已注册无密码，没有保存地址的顾客下单"""
        self.driver.delete_pan(1)
        time.sleep(2)
        self.driver.add_cart()
        time.sleep(1)
        self.driver.enter_checkout()
        time.sleep(2)
        self.driver.checkout_visitor(self.lists[-1])
        time.sleep(1)
        self.driver.click_arb()
        time.sleep(4)
        self.driver.checkout(5, self.lists[-1])
        time.sleep(2)
        test = self.driver.card_pay()
        self.assertEqual(test, 'Your order payment successful')
        self.dele_list()

    def test_have_password_user(self):
        """测试有密码用户购买"""
        self.driver.delete_pan(1)
        time.sleep(2)
        self.driver.add_cart()
        time.sleep(1)
        self.driver.enter_checkout()
        time.sleep(2)
        self.driver.checkout_visitor('xiong.chen@x.heywind.com')
        time.sleep(1)
        self.driver.click_arb()
        time.sleep(2)
        test = self.driver.card_pay()
        self.assertEqual(test, 'Your order payment successful')





# if __name__ == "__main__":
#     unittest.main()











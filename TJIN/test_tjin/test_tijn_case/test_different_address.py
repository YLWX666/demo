import unittest,time
from element_step.step import StepElement

class TestCardPay(unittest.TestCase):
    '''测试游客不同地址支付'''
    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn')

    def tearDown(self) -> None:
        self.driver.close_web()

    def test_card_pay(self):
        '''游客地址不同，信用卡支付流程'''

        email = self.driver.email_address()
        time.sleep(1)
        self.driver.delete_pan(1)
        time.sleep(2)
        self.driver.add_cart()
        time.sleep(2)
        self.driver.enter_checkout()
        time.sleep(2)
        self.driver.checkout_visitor(email)
        self.driver.checkout(5,email)
        time.sleep(2)
        self.driver.attick_address()
        self.driver.billing_address(8)
        time.sleep(3)
        test = self.driver.card_pay()
        self.assertEqual(test,'Your order payment successful')

# if __name__ == "__main__":
#     unittest.main()

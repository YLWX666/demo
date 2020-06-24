import unittest
from element_step.step import StepElement


class TestCardPay(unittest.TestCase):
    '''测试游客信用卡支付'''
    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn')

    def tearDown(self) -> None:
        self.driver.close_web()

    def test_card_pay(self):
        '''游客信用卡支付流程'''
        self.driver.delete_pan(1)
        self.driver.add_cart()
        self.driver.enter_checkout()
        self.driver.checkout(5)
        test = self.driver.card_pay()
        self.assertEqual(test,'Your order payment successful')

# if __name__ == "__main__":
#     unittest.main()











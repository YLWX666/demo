import time
# from element import Element
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class TestPay(unittest.TestCase):

    def setUp(self):
        self.driver = Element('https://tj.qa.heywind.cn/')


    def test_buy(self):
        self.driver.maxsize()
        self.driver.by_xpath('//*[@class="cm_close"]').click()
        self.driver.excute_js("window.scrollTo(0,1400)")
        shop_now = self.driver.by_xpath('//*[@class="product_price_button "][1]')
        shop_now.click()
        time.sleep(4)
        self.driver.excute_js("window.scrollTo(0,400)")
        buy = self.driver.waite_element(10,'//*[@class="buyFrom js_buy"]')
        buy.click()
        time.sleep(5)
        self.driver.switchToframe(1)
        pay = self.driver.waite_element(10,'//*[@id="paypal-animation-container"]')
        pay.click()
        time.sleep(4)
        self.driver.quite_frame()
        self.driver.handle()
        self.driver.maxsize()
        time.sleep(10)
        self.driver.switchToframe('injectedUl')
        time.sleep(4)
        self.driver.by_xpath('//*[@name="login_email"]').send_keys('tijneyewear.test@gmail.com')
        self.driver.by_xpath('//*[@name="login_password"]').send_keys('heywind@2019')
        self.driver.by_xpath('//*[@name="btnLogin"]').click()
        # self.driver.quite_frame()
        time.sleep(10)
        self.driver.by_xpath('//*[@value="Pay Now"]').click()

    def tearDown(self):
        self.driver.quite()


# if __name__ == "__main__":
#     unittest.main()
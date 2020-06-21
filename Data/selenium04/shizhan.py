from selenium05 import webdriver
import unittest
import time
class Login(unittest.TestCase):
    def setUp(self):
        self.db = webdriver.Firefox()
        self.db.get('http://www.renren.com/')
        self.db.maximize_window()



    def test_case(self):
        id = self.db.find_element_by_id('email')
        id.send_keys('18279188010')
        pass_word = self.db.find_element_by_id('password')
        pass_word.send_keys('1111111')
        login = self.db.find_element_by_id('login')
        login.click()
        self.db.find_element_by_link_text()
    def tearDown(self):
        time.sleep(10)
        self.db.quit()


if __name__ == '__main__':
    unittest.main()
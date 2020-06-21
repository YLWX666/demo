import unittest
import HTMLTestRunner
import os

from selenium05 import webdriver
class Case01(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        print('开始测试')

    def tearDown(self):
        self.driver.quit()
        print('测试结束')

    def test_first(self):
        '''
        u格式报告
        :return:
        '''
        b = self.driver
        b.get('http://www.maiziedu.com/')
        b.maximize_window()
        b.find_element_by_link_text('登录').click()
        b.find_element_by_id('id_account_l').clear()
        b.find_element_by_id('id_account_l').send_keys('111')
        b.find_element_by_id('id_password_l').send_keys('111')
        b.find_element_by_id('login_btn').click()
        a = b.find_element_by_id('login-form-tips').text
        self.assertEqual(a,'该账格式不正确')


if __name__ =='__main__':
    # unittest.main()
    # a = unittest.TextTestRunner()
    # a.run(suite)
    # file_path = 'a.html'
    f = open('a.html','wb')
    suite = unittest.TestSuite()
    suite.addTest(Case01('test_first'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='报告',description='爱你哦')
    runner.run(suite)
    f.close()


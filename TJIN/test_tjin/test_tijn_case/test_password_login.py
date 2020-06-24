import ddt
import unittest

import time
from selenium import webdriver
from test_tjin.datas import get_datas
#获取json文件
datas = get_datas.json_data(get_datas.get_path_file('password'))

@ddt.ddt
class TestLoginPassword(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get('https://tj.qa.heywind.cn/')
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()


    def judge_element(self,element):
        try:
            error = self.driver.find_element_by_xpath(element).get_attribute('textContent')
            return error
        except:
            return ""
    @ddt.data(*datas)
    def test_password(self,data):
        self.driver.find_element_by_xpath('//*[@class="cm_close"]').click()
        self.driver.find_element_by_xpath('//*[@id="pc_account"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="email"][1]').send_keys(data["email"])
        self.driver.find_element_by_xpath('//*[@value="CONTINUE"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="password"]').send_keys(data["password"])
        self.driver.find_element_by_xpath('//*[@value="LOG IN"]').click()
        time.sleep(2)
        error_informations = self.judge_element('//*[@class="validation-summary-errors"]')
        self.assertEqual(error_informations,data["error"],"没通过")

# if __name__ == "__main__":
#     unittest.main()
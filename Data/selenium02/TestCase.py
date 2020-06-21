import unittest
from selenium05 import webdriver
from selenium05.webdriver.support.wait import WebDriverWait


class SearchTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(15)

    def test_searchChina(self):
        """百度搜索中国的测试用例"""
        self.driver.find_element_by_xpath(".//*[@id='kw']").send_keys("中国")
        self.driver.find_element_by_xpath(".//*[@id='su']").click()

        # WebDriverWait(self.driver, 15).until(lambda x: x.find_element_by_xpath(".//*[@id='1']/h3/a"))
        result = self.driver.find_element_by_xpath(".//*[@id='1']/h3/a").text

        self.assertEqual(result, "中国_百度百科")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
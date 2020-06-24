
import os
import ddt
import unittest
import time
from test_tjin.datas import get_datas
from element_step.step import StepElement

#获取json文件
datas = get_datas.json_data(get_datas.get_path_file('search_data'))

@ddt.ddt()
class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = StepElement('element_yaml','Firefox')
        self.driver.open_url('https://tj.qa.heywind.cn/')

    def tearDown(self) -> None:
        self.driver.close_web()

    def judge_element(self,element):
        try:
            time.sleep(3)
            error = self.driver.by_xpath(element).get_attribute('textContent')
            return error
        except:
            return ""

    @ddt.data(*datas)
    def test_search(self,datas):
        self.driver.search(3,datas)
        self.assertEqual(self.judge_element('//*[@class="most_search"]'),datas['error'])


if __name__ =="__main__":
    unittest.main()





















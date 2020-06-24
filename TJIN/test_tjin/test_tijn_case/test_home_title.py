import time
import unittest
from selenium import webdriver
from ele_common.common import Get_data





class TestHomeTitle(unittest.TestCase):
    '''测试首页正副标题'''


    def setUp(self):
        self.lists = [
            'This is how we look like in Real life',
            'Powered by Real people on Instagram worldwide.',
            'Extra-light Titanium meets ECO-acetate, extra-thin alloy meets understated design.Ready for your summer.',
            "Look what surprises we've brought.",
            '//*[@class="module_title_small"]'
        ]
        self.driver = webdriver.Chrome()
        self.driver.get('https://tj.qa.heywind.cn')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@class="cm_close"]').click()


    def tearDown(self):
        self.driver.quit()

    def delete_blank(self,text):
        '''去首尾空格'''
        text = text.strip()
        text = text.lstrip()
        return text


    def test_ins_title(self):
        '''测试ins正标题'''
        self.driver.execute_script('window.scrollTo(0,700)')
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath('//*[@class="module_title"]')[0]
        test = ele.get_attribute('textContent')
        test = self.delete_blank(test)
        self.assertEqual(test,self.lists[0],msg='正标题不相同')

    def test_ins_assistant_title(self):
        '''测试ins副标题'''
        self.driver.execute_script('window.scrollTo(0,700)')
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath(self.lists[4])[0]
        test = ele.get_attribute('textContent')
        test = self.delete_blank(test)
        self.assertEqual(test,self.lists[1],msg='副标题不相同')

    def test_new_title(self):
        '''测试new arrivals副标题'''
        self.driver.execute_script('window.scrollTo(0,1000)')
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath(self.lists[4])[1]
        test = ele.get_attribute('textContent')
        test = self.delete_blank(test)
        self.assertEqual(test,self.lists[2])

    def test_summer_title(self):
        '''测试summer perfection副标题'''

        self.driver.execute_script('window.scrollTo(0,1850)')
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath(self.lists[4])[2]
        test = ele.get_attribute('textContent')
        test = self.delete_blank(test)
        self.assertEqual(test,self.lists[3],msg="副标题不相等")

# if __name__ == '__main__':
#     unittest.main()















if __name__ == "__main__":
    unittest.main()













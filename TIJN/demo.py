import time
from selenium import webdriver


# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# test = driver.find_element_by_xpath('//span[@id="pc_account"]/a').get_attribute('textContent')
# print(test)
# s = {'sfs':'fs','sfef':1,'ee':5}
# for i in s:
#     print(i)

import unittest
import ddt

# 测试数据
# datas = [ {"user": "admin", "psw": "123", "result": "true"},
#         {"user": "admin1", "psw": "1234", "result": "true"},
#         {"user": "admin2", "psw": "1234", "result": "true"},
#         {"user": "admin3", "psw": "1234", "result": "true"},
#         {"user": "admin4", "psw": "1234", "result": "true"},
#         {"user": "admin5", "psw": "1234", "result": "true"},
#         {"user": "admin6", "psw": "1234", "result": "true"},
#         {"user": "admin7", "psw": "1234", "result": "true"},
#         {"user": "admin8", "psw": "1234", "result": "true"},
#         {"user": "admin9", "psw": "1234", "result": "true"},
#         {"user": "admin10", "psw": "1234", "result": "true"},
#         {"user": "admin11", "psw": "1234", "result": "true"}]

# datas = ["1","2","3"]
# datas = (['老胡','老胡_百度搜索'],['图片','图片_百度搜索'],['laohu','laohu_百度搜索'])
# @ddt.ddt
# class Test(unittest.TestCase):
#
#     @ddt.data(*datas)
#     def test_(self, d,c):
#         """上海-悠悠：{0}"""
#         print("测试数据：%s" % d)
        # print("用户:%s"%c)
# import ddt  #导入ddt模块
# import unittest,time
# from selenium import webdriver
# @ddt.ddt  #在测试类前声明使用ddt
# class DoubanTest(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get('https://baidu.com')
#         self.driver.implicitly_wait(3)
#     def tearDown(self):
#         self.driver.quit()
#      #在测试方法前使用ddt传入数据
#     @ddt.data(['老胡','老胡_百度搜索'],['图片','图片_百度搜索'],['laohu','laohu_百度搜索'])
#     @ddt.unpack   #起连接作用，将测试数据传给参数，与@ddt.data()成对出现
#     def test_add(self,can,yu):
#         self.driver.find_element_by_id('kw').send_keys(can)
#         time.sleep(2)
#         self.driver.find_element_by_id('su').click()
#         time.sleep(2)
#         self.assertEqual(self.driver.title, yu)

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# driver.find_element_by_xpath('//*[@id="pc_account"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="email"][1]').send_keys("xiong.chen@x.heywind.com")
# driver.find_element_by_xpath('//*[@value="CONTINUE"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="password"]').send_keys('heywind2020')
# driver.find_element_by_xpath('//*[@value="LOG IN"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="validation-summary-errors"]').get_attribute('textContent')

#？？》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(2)
# driver.execute_script("window.scrollTo(0,900)")
# time.sleep(5)
# js = "document.getElementsByClassName('instagram_img')[1].click()"
# driver.execute_script(js)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(4)
# js = "document.getElementsByClassName('pc_tj_search')[0].click()"
# driver.execute_script(js)
# time.sleep(2)
# driver.find_element_by_xpath('//*[@type="text"]').send_keys('6485846')
# driver.find_element_by_xpath('//span[@class="pc_input_search"]/img').click()
#
# error = driver.find_element_by_xpath('//span[@class="most_search"]').get_attribute('textContent')
# print(error)

import ddt
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# element = WebDriverWait(driver,10,2).until(lambda a:a.find_element_by_xpath('//*[text()="SIGN IN"]'))
# element.click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="email"]').send_keys('xiong.chen@x.heywind.com')
# driver.find_element_by_xpath('//*[text()="CONTINUE"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="Password"]').send_keys('heywind2020')
# driver.find_element_by_xpath('//*[@id="loginSubmitNew"]').click()

# driver.execute_script('window.scrollTo(0,1250)')
# a = driver.find_element_by_xpath('//*[@class="product_price_button "][1]')
# a.click()
# time.sleep(2)
# # driver.find_element_by_xpath('//*[text()="CHECKOUT"]').click()

# element = WebDriverWait(driver,10,2).until(lambda a:a.find_element_by_xpath('//*[text()="CHECKOUT"]'))
# element.click()
# element = WebDriverWait(driver,10,2).until(lambda a:a.find_element_by_xpath('//*[@id="tijn-paypal-button"]'))
# element.click()

#》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》

driver = webdriver.Chrome()
driver.get('https://tj.qa.heywind.cn/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@class="cm_close"]').click()
#加购


















































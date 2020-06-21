# # from selenium import webdrive
#
# # b = webdriver.Firefox()
# # b.get('http://www.maiziedu.com/')
# # b.maximize_window()
# # ele1 = b.find_element_by_css_selector('html body.YaHei.index div.main div.side-bar div.side-menu.w1920 div.w1920-scroll div.side-nav ul li.icon-6 a')
# #
# # ele1.click()
#
# # b = webdriver.Firefox()
# # b.get('http://www.maiziedu.com/')
# # b.maximize_window()
# #
# # ele1 = b.find_element_by_link_text('软件测试')
# # ele1.click()
#
# # from selenium04.webdriver.common.action_chains import ActionChains
# #
# # ele = b.find_element_by_link_text('企业直通车')
# # ActionChains(b).move_to_element(ele).perform()
# # ele1 = b.find_element_by_link_text('软件测试')
#
# # from selenium04 import webdriver
# # import time
# # b = webdriver.Firefox()
# # b.get('http://www.baidu.com')
# #
# # ele1 = b.find_element_by_id('kw').clear()
# # b.find_element_by_id('kw').send_keys('麦子学院')
# #
# # ele2 = b.find_element_by_id('su')
# # ele2.click()
# # b.maximize_window()
# # b.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/div[1]/h3/a[1]').click()
# #
# # b.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/div[1]/h3/a[1]').click()
# # print(b.window_handles)
# # print(b.current_window_handle)
#
# import requests
#
# url = 'http://httpbin.org/get'
# # proxies = {'http': 'http://309435365:szayclhp@122.114.67.136:16819','https':'https://309435365:szayclhp@122.114.67.136:16819'}
#
# headers = {'User-Agent' : 'Mozilla/5.0'}
#
# html = requests.get(url,headers=headers).text
# print(html)
# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
from selenium05 import webdriver
from selenium05.webdriver.support.wait import WebDriverWait
from selenium05.webdriver.support import expected_conditions as EC
from selenium05.webdriver.common.by import By
from selenium05.webdriver.support.select import Select
import time


# 创建一个Chrome对象
driver = webdriver.Firefox()
# 访问百度
driver.get('http://baidu.com')
# 非select下拉框操作
# 找到百度首页的设置按钮
driver.find_element_by_xpath("//*[contains(@text(),'设'])").click()
# 等待下拉框的出现

driver_x = WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_xpath('//a[text()="高级搜索"]'))
driver_x.click()

# //div[@id='ul']//span[8]/a[@class='mnav']



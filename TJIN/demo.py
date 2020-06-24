import os

from selenium import webdriver
import time
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# driver.find_element_by_xpath('//*[@id="pc_account"]').click()
# # driver.find_element_by_link_text('SIGN IN').click()
# time.sleep(2)
# # driver.find_element_by_xpath('//*[@class="email"][1]').clear()
# driver.find_element_by_xpath('//*[@class="email"][1]').send_keys('4684648@qq.com')
# driver.find_element_by_xpath('//*[@value="CONTINUE"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="closeSet"]').click()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# def panduan():
#     try:
#         driver.find_element_by_xpath('//*[@class="validation-summary-errors"]').get_attribute('textContent')
#         return True
#     except:
#         return False
#
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
# panduan()
# print(panduan())


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait

# def sun(e,ele):
#     actions = ActionChains(e)
#     sunglasses = e.find_element_by_xpath(ele)
#     actions.move_to_element(sunglasses).perform()
#
#
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# driver.find_element_by_link_text('OPTICAL').click()
# # opt = WebDriverWait(driver,5).until(e.title_contains("Optical Eyeglasses"))
# time.sleep(3)
# driver.find_element_by_link_text('BLUE LIGHT FILTER').click()
# time.sleep(3)
#
# sun(driver,'//*[@id="summer"]')
# driver.find_element_by_xpath('//*[@class="tj_pc_menu_list"][1]/li[1]').click()
# time.sleep(3)
#
# sun(driver,'//*[@id="summer"]')
# driver.find_element_by_xpath('//*[@class="tj_pc_menu_list"][1]/li[2]').click()
# time.sleep(3)
#
#
# sun(driver,'//*[@id="collection"]')
# driver.find_element_by_xpath('//*[@id="collection"]/ul/li[1]').click()
# time.sleep(3)
# sun(driver,'//*[@id="collection"]')
# driver.find_element_by_xpath('//*[@id="collection"]/ul/li[2]').click()
# time.sleep(3)
# sun(driver,'//*[@id="collection"]')
# driver.find_element_by_xpath('//*[@id="collection"]/ul/li[3]').click()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#ins图
import random
from selenium.webdriver.common.touch_actions import TouchActions
# driver = webdriver.Firefox()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0,900)")
# time.sleep(10)
# js = "document.getElementsByClassName('instagram_img')[3].click()"
# driver.execute_script(js)
# a = driver.find_element_by_xpath('//*[@data-index="3"]/div[1]').size
# b = driver.find_element_by_xpath('//*[@data-index="0"]/div[1]').size
# print(a)
# print(b)
# actions = ActionChains(driver)
# actions.drag_and_drop(a,b).perform()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# driver.find_element_by_link_text('OPTICAL').click()
# time.sleep(3)
# driver.execute_script('window.scrollTo(0,700)')
# time.sleep(5)
# js = "document.getElementsByClassName('swiper-lazy')[1].click()"
# driver.execute_script(js)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#tj首页-new arrivals购买

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# driver = webdriver.Firefox()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(3)
# js = "document.getElementsByClassName('pc_tj_search')[0].click()"
# driver.execute_script(js)
# driver.find_element_by_xpath('//*[@class="search_msg_top"]/div/p/input').send_keys('sljf')
# driver.find_element_by_xpath('//*[@class="pc_input_search"]').click()
# time.sleep(4)
# test = driver.find_element_by_xpath('//*[@class="most_search"]').get_attribute('textContent')
# print(test)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(2)
# #首页加购一件商品(游客)
# driver.execute_script('window.scrollTo(0,1100)')
# driver.find_element_by_xpath('//a[@class="pc_product_item"]/img').click()
# time.sleep(2)
# driver.find_element_by_xpath('//div[@class="pc_out_box"]/a').click()
# time.sleep(2)
#
# checkout = WebDriverWait(driver,5).until(lambda a:a.find_element_by_xpath('//a[@class="pay checkoutPayNow"]'))
# checkout.click()
# time.sleep(2)
# email = driver.find_element_by_xpath('//input[@class="input_item"]')
# email.send_keys('54648464')
# driver.find_element_by_xpath('//*[text()="Checkout"]').click()
# time.sleep(2)
# error = driver.find_element_by_xpath('//p[@class="hint error_text"]').get_attribute('textContent')
# print(error)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import yagmail
#发送邮件
# yag = yagmail.SMTP(user="xiong.chen@x.heywind.com",password="CHExio0911",host="smtp.exmail.qq.com")
# subject = "6666666"
# contents = "7777777777"
# yag.send('yesheng.su@x.heywind.com',subject,contents)
# print('email send ok')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# #进入checkout页面
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# driver.execute_script('window.scrollTo(0,1700)')
# time.sleep(2)
# ele = driver.find_elements_by_xpath('//*[@class="product_price_button "]')[5]
# ele.click()
# time.sleep(3)
# ele = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[text()="CHECKOUT"]'))
# ele.click()
# #checkout游客登录
# email_info = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[@id="Customer_Email"]'))
# email_info.send_keys('301262357@qq.com')
# name = driver.find_element_by_xpath('//*[@class="address_first_name"][1]')
# name.click()
# driver.implicitly_wait(3)
# name.send_keys('111111')
# last_name = driver.find_element_by_xpath('//*[@class="address_last_name"][1]').send_keys('2222')
# driver.find_element_by_xpath('//*[@class="address_email"]').send_keys('646464687@qq.com')
# time.sleep(2)
# se = driver.find_element_by_xpath('//*[@class="edit_country_select"][1]')
# Select(se).select_by_index(1)
# city = driver.find_element_by_xpath('//*[@class="edit_state_select"][1]')
# time.sleep(2)
# Select(city).select_by_value("3")
# #地址
# driver.find_element_by_xpath('//*[@class="address1 "][1]').send_keys('jgpdjhgdjglsjg')
# driver.find_element_by_xpath('//*[@class="adderss_city"][1]').send_keys('pjgpja')
# #code
# driver.find_element_by_xpath('//*[@class="address_code"][1]').send_keys("16468")
# driver.find_element_by_xpath('//*[@class="address_phone"][1]').send_keys('094646465')
# time.sleep(2)
# #信用卡支付
# driver.execute_script('window.scrollTo(0,900)')
# driver.find_element_by_xpath('//*[text()="Pay with Credit Card"]').click()
# #切换frame
# time.sleep(4)
# fra = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_tag_name('iframe'))
# driver.switch_to.frame(fra)
# time.sleep(4)
# datas = driver.find_elements_by_class_name('Textbox-control')[0]
# datas.send_keys('4242424242424242')
# data = driver.find_elements_by_class_name('Textbox-control')[1]
# data.send_keys('0425')
# dat = driver.find_elements_by_class_name('Textbox-control')[2]
# dat.send_keys('464')
# time.sleep(2)
# # driver.find_element_by_xpath('//*[@class="Button"]').click()
# driver.find_element_by_class_name('Button').click()
# driver.switch_to.default_content()
# time.sleep(5)
# a = driver.find_element_by_xpath('//*[@class="successful_text"][1]').get_attribute('textContent')
# print(a)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# #进入checkout页面
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# driver.execute_script('window.scrollTo(0,1800)')
# ele = WebDriverWait(driver,20,2).until(lambda a:a.find_elements_by_xpath('//*[@class="product_price_button "]')[3])
# ele.click()
#第三方快捷支付无法定位
# element = WebDriverWait(driver,20,2).until(lambda a:a.find_elements_by_tag_name('iframe')[0])
# driver.switch_to.frame(element)
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="paypal-animation-content"]/div[1]/div').click()

# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》

#模糊code
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# #进入checkout页面
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# #加购
# driver.execute_script('window.scrollTo(0,1800)')
# try:
#     ele = WebDriverWait(driver,20,2).until(lambda a:a.find_elements_by_xpath('//*[@class="product_price_button "]')[3])
#     ele.click()
# except:
#     ele = WebDriverWait(driver, 20, 2).until(lambda a: a.find_elements_by_xpath('//*[@class="product_price_button "]')[4])
#     ele.click()
# #填code
# WebDriverWait(driver,15,2).until(lambda a:a.find_element_by_xpath('//*[@id="code"]')).send_keys('  5free  ')
# driver.find_element_by_class_name('js_apply').click()
# time.sleep(1)
# test = driver.find_element_by_class_name('js_apply').get_attribute('textContent')
# print(test)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# option = webdriver.ChromeOptions()
# option.add_argument(r'--user-data-dir=C:\Users\chexi\AppData\Local\Google\Chrome\User Data-副本\Default')
# driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# #判断TJ首页ins正副标题
# driver.execute_script('window.scrollTo(0,700)')
# ele = driver.find_elements_by_xpath('//*[@class="module_title"]')[0]
# ele2 = driver.find_elements_by_xpath('//*[@class="module_title_small"]')[0]
# test = ele.get_attribute('textContent')
# test2 = ele2.get_attribute('textContent')
# test = test.lstrip()
# test = test.rstrip()
# test2 =test2.lstrip()
# test2 = test2.rstrip()
# print(test)
# print(test2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(5)
# # driver.find_element_by_xpath('//*[@class="vjs-poster"]').click()
# js = 'document.getElementsByClassName("vjs-poster")[0].click()'
# driver.execute_script(js)
# time.sleep(2)
# # driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# url = driver.current_url
# print(url)
# print(type(url))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#fackbook登录
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# time.sleep(2)
# handle = driver.current_window_handle
# driver.find_element_by_xpath('//*[@class="dailg_login_facebook"]').click()
# time.sleep(3)
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# driver.find_element_by_xpath('//*[@id="email_container"]/div/input').send_keys('steckoklqo_1591429998@tfbnw.net')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys('login@123456')
# time.sleep(2)
# driver.find_element_by_xpath('//*[@name="login"]').click()
# time.sleep(1)
# driver.switch_to.window(handles[0])
# time.sleep(2)
# driver.find_element_by_xpath('//*[text()="GO SHOPPING"]').click()

# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
#发送报告
# import yagmail
# path = os.getcwd()
# report_file = os.path.join(path,'report')
# file = report_file+'\测试用例报告.html'
# yag = yagmail.SMTP(user="xiong.chen@x.heywind.com", password="CHExio0911", host="smtp.exmail.qq.com")
# subject = "测试"
# contents = "自动化测试报告"
# yag.send('yesheng.su@x.heywind.com', subject, contents, file)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#谷歌无法做自动化
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="abcRioButtonContentWrapper"]').click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
#
# driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('syszhenxin@gmail.com')
# time.sleep(1)
# js = 'document.getElementsByClassName("CeoRYc")[0].click()'
# driver.execute_script(js)
# ele = driver.find_elements_by_class_name('CeoRYc')[0]
# ele.click()

#》》》》》》》》》》》》》》》》》》》》》>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#ins

# driver = webdriver.Firefox()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(2)
# driver.execute_script("window.scrollTo(0,900)")
# time.sleep(10)
# js = "document.getElementsByClassName('instagram_img')[3].click()"
# driver.execute_script(js)
#
# test = driver.find_element_by_xpath('//*[text()="TAP TO VIEW PRODUCTS"]').get_attribute('textContent')
# print(test)
# driver.find_element_by_xpath('//*[text()="TAP TO VIEW PRODUCTS"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@class="ins_pic"]/ul/li').click()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# driver = webdriver.Chrome()
# driver.get('https://tj.qa.heywind.cn/')
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@class="cm_close"]').click()
# time.sleep(2)
# #加入购物车
# driver.execute_script('window.scrollTo(0,1700)')
# time.sleep(2)
# ele = driver.find_elements_by_xpath('//*[@class="product_price_button "]')[5]
# ele.click()
# time.sleep(3)
# #进入checkout页面
# ele = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[text()="CHECKOUT"]'))
# ele.click()
# # #填入游客email地址
# email_info = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[@id="Customer_Email"]'))
# email_info.send_keys('xiong.chen@x.heywind.com')
# name = driver.find_element_by_xpath('//*[@class="address_first_name"][1]')
# name.click()
# driver.implicitly_wait(3)
# name.send_keys('111111')
# last_name = driver.find_element_by_xpath('//*[@class="address_last_name"][1]').send_keys('2222')
# driver.find_element_by_xpath('//*[@class="address_email"][1]').send_keys('646464687@qq.com')
# time.sleep(2)
# se = driver.find_element_by_xpath('//*[@class="edit_country_select"][1]')
# Select(se).select_by_index(1)
# city = driver.find_element_by_xpath('//*[@class="edit_state_select"][1]')
# time.sleep(2)
# Select(city).select_by_value("3")
# # #地址
# driver.find_element_by_xpath('//*[@class="address1 "][1]').send_keys('jgpdjhgdjglsjg')
# driver.find_element_by_xpath('//*[@class="adderss_city"][1]').send_keys('pjgpja')
# #code
# driver.find_element_by_xpath('//*[@class="address_code"][1]').send_keys("16468")
# driver.find_element_by_xpath('//*[@class="address_phone"][1]').send_keys('094646465')
#
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="use_billing"]/span[1]').click()
# driver.execute_script('window.scrollTo(0,500)')
# time.sleep(2)
# names = driver.find_elements_by_xpath('//*[@class="address_first_name"]')
# name = names[1]
# name.send_keys('33333')
# time.sleep(1)
# names = driver.find_elements_by_xpath('//*[@class="address_last_name"]')
# name = names[1]
# name.send_keys('44444444')
# time.sleep(1)
# names = driver.find_elements_by_xpath('//*[@class="address_email"]')
# name = names[1]
# name.send_keys('646464687@qq.com')
# time.sleep(2)
# se = driver.find_elements_by_xpath('//*[@class="edit_country_select"]')[1]
# Select(se).select_by_index(1)
# city = driver.find_elements_by_xpath('//*[@class="edit_state_select"]')[1]
# time.sleep(2)
# Select(city).select_by_value("7")
# # #地址
# name = driver.find_elements_by_xpath('//*[@class="address1 "]')[1]
# name.send_keys('fhjyyufjfjfj')
# time.sleep(1)
# name = driver.find_elements_by_xpath('//*[@class="adderss_city"]')[1]
# name.send_keys('yjuytityjd')
# #code
# driver.find_elements_by_xpath('//*[@class="address_code"]')[1].send_keys("16468")
# driver.find_elements_by_xpath('//*[@class="address_phone"]')[1].send_keys('094646465')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

driver = webdriver.Chrome()
driver.get('https://tj.qa.heywind.cn/')
driver.maximize_window()
driver.find_element_by_xpath('//*[@class="cm_close"]').click()
time.sleep(4)
#加入购物车
driver.execute_script('window.scrollTo(0,1700)')
time.sleep(4)
ele = driver.find_elements_by_class_name('product_price_button')
ele = ele[4]
ele.click()
time.sleep(2)
#进入checkout页面
ele = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[text()="CHECKOUT"]'))
ele.click()
time.sleep(2)
driver.find_element_by_xpath('//*[@class="left"]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[text()="LEAVE"]').click()
# email_info = WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[@id="Customer_Email"]'))
# email_info.send_keys('xiong.chen@x.heywind.com')
# time.sleep(1)
# driver.find_element_by_xpath('//*[text()="Checkout"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="Customer_Password"]').send_keys('heywind2020')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="login_button"]').click()
# time.sleep(2)
# WebDriverWait(driver,20,2).until(lambda a:a.find_element_by_xpath('//*[@class="edit_shipping_address_wrap"][1]/div/p[1]/img')).click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@class="shipping_address_save"]').click()

























































































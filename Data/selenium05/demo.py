from selenium import webdriver
# #修改浏览器的User-Agent来伪装你的浏览器访问手机m站，并不能模仿手机
# option = webdriver.ChromeOptions()
# option.add_argument('--user-agent=iphone')
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('https://www.baidu.com')
# driver.find_element_by_id('word').send_keys('刘亦菲')
# driver.find_element_by_xpath('//*[@class="bn"]').click()

# #启动时安装crx扩展
# option = webdriver.ChromeOptions()
# option.add_extension('xxxx')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
driver = webdriver.Chrome()
driver.get(r'C:\Users\Admin\PycharmProjects\Data\selenium05\内嵌滚动条.html')
js = 'document.getElementById("yoyoketang").scrollTop=10000'
driver.execute_script(js)

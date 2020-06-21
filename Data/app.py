from appium import webdriver
from selenium05.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "5.1.1"
desired_caps['deviceName'] = "127.0.0.1:62001"
desired_caps['appPackage'] = "com.android.settings"
desired_caps['appActivity'] = ".Settings"
# 允许输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.close_app()
# driver.open_notifications()  打开通知
# print(driver.network_connection)
# driver.set_network_connection()设置网络
# resolution = driver.get_window_size()
# w = resolution.get("width")
# h = resolution.get("height")
# driver.swipe(w*0.9,h*0.5,w*0.1,h*0.5,2000)
# print(resolution)













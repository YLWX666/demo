import os
from appium import webdriver
from selenium05.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = "5.1.1"
desired_caps['deviceName'] = "127.0.0.1:62001"
desired_caps['appPackage'] = "com.tal.kaoyan"
desired_caps['appActivity'] = ".ui.activity.ucenter.LoginActivity t12"


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# driver.quit()
# driver.install_app("/storage/emulated/legacy/Pictures/kaoyan3.1.0.apk")
# os.system(r"adb install C:\Users\Admin\Nox_share\ImageShare\kaoyan3.1.0.apk")
# 该台电脑安装apk文件只能用adb命令+电脑文件路径；
# ............................................
# driver.remove_app("com.tencent.mobileqq")
import base64
#
# data = str(base64.b64encode('123456 cc'.encode('utf-8')),'utf-8')
#
# driver.push_file("/sdcard/Pictures/app12.txt",data)
# iphone = driver.pull_file("/sdcard/Pictures/app12.txt")
# print(iphone)

# print(driver.page_source)
# ele_list = driver.find_elements_by_id("com.android.settings:id/title")
# print(ele_list)
# driver.close_app()
# driver.quit()
# try:
    # class_list = driver.find_elements_by_class_name("android.widget.LinearLayout")
    # for i in class_list:
    #     if i.text == "WLAN":
    #         i.click()
    #         break
# WebDriverWait(driver,timeout=5,poll_frequency=0.5)\
#     .until(lambda x:x.find_element_by_id("1"))
# except Exception as error:
#    print(error)
# finally:driver.quit()
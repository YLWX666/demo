import time
from selenium import webdriver
from get_file_data.common import Get_data

#打开url
class StepElement:

    def __init__(self,file,browser=None):
        self.data = Get_data(file)
        if browser == 'Chrome' or browser == None:
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            print("输入正确浏览器")

#打开浏览器并最大化
    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

#xpath定位
    def by_xpath(self,element):
        page_element = self.driver.find_element_by_xpath(element)
        return page_element

#上下滑动pc
    def swipe(self,js):
        self.driver.execute_script(js)

#加入购物车
    def add_cart(self,product):
        pass


#支付
    def pay(self):
        pass

#关闭浏览器
    def close_web(self):
        self.driver.quit()

#首页转盘登录
    def login(self,n):

        get_login = self.data.login_data(n)
        self.driver.implicitly_wait(3)
        self.by_xpath(get_login[0]).send_keys(get_login[1])
        time.sleep(3)
        self.by_xpath(get_login[2]).click()
        time.sleep(3)
        self.by_xpath(get_login[3]).click()
        log = self.by_xpath(get_login[4]).get_attribute('textContent')
        log = log.lstrip()
        log = log.rstrip()
        return log
#页面内登陆，新号
    def sign_login(self,n):
        """
        :param n: yaml文件里列表序数
        :return:
        """
        get_login = self.data.login_data(n)
        self.by_xpath(get_login[0]).click()
        time.sleep(2)
        self.by_xpath(get_login[1]).click()
        time.sleep(2)
        self.by_xpath(get_login[2]).send_keys(get_login[3])
        self.by_xpath(get_login[4]).click()
        time.sleep(3)
        self.by_xpath(get_login[6]).click()
        time.sleep(2)
        log = self.by_xpath(get_login[5]).get_attribute('textContent')
        log = log.lstrip()
        log = log.rstrip()
        return log

#搜索
    def search(self):
        pass



#checkout
    def checkout(self):
        pass

#进入类目页
    def types(self):
        pass




# if __name__ == "__main__":
#     step = StepElement('element_yaml')
#     step.open_url('https://tj.qa.heywind.cn/')
#     step.login()




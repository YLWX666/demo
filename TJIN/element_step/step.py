import time
import random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as e
from ele_common.common import Get_data
from test_tjin.datas.get_datas import *


class StepElement:

    def __init__(self, file=None, browser=None):
        if not file and browser == None:
            self.data = Get_data('element_yaml')
            self.driver = webdriver.Chrome()
        elif browser == 'Chrome' or browser == None:
            self.data = Get_data('element_yaml')
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox' and file == 'element_yaml':
            self.data = Get_data('element_yaml')
            self.driver = webdriver.Firefox()
        elif browser == 'IE' and file == None:
            self.driver = webdriver.Ie()
            self.data = Get_data('element_yaml')
        elif file == "element_yaml" and browser == "Firefox":
            self.driver = webdriver.Firefox()
            self.data = Get_data('element_yaml')

        else:
            print("输入正确浏览器")

    def open_url(self, url):
        """
        打开浏览器并最大化
        :param url: 路由
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def by_xpath(self, element):
        """
        xpath定位
        :param element: 页面元素属性
        :return: 页面元素
        """
        page_element = self.driver.find_element_by_xpath(element)
        return page_element

    def by_xpathes(self, element, n):
        """
        复数xpath定位
        :param element: 元素属性
        :param n: 序数
        :return: 元素
        """
        page_element = self.driver.find_elements_by_xpath(element)
        page = page_element[n]
        return page

    def by_link_test(self, element):
        """
        link_text定位
        :param element:元素属性
        :return:
        """
        page_element = self.driver.find_element_by_link_text(element)
        return page_element

    def by_classes(self, element, n):
        """
        class复数定位
        :param element: 元素属性
        :param n: 序数
        :return:
        """
        page_element = self.driver.find_elements_by_class_name(element)
        page = page_element[n]
        return page

    def by_class(self, element):
        """
        class定位
        :param element: 元素属性
        :return:
        """
        page_element = self.driver.find_element_by_class_name(element)
        return page_element

    def web_xpath_wait(self, element):
        """
        WebDriverWait_xpath
        :param element: 元素属性
        :return:
        """
        ele = WebDriverWait(self.driver, 15, 2).until(lambda a: a.find_element_by_xpath(element))
        return ele

    def web_class_wait(self, element):
        """
        WebDriverWait_class_name
        :param element: 元素属性
        :return:
        """
        ele = WebDriverWait(self.driver, 15, 2).until(lambda a: a.find_element_by_class_name(element))
        return ele

    def web_tag_wait(self, element):
        """
        WebDriverWait_tag_name
        :param element: 元素属性
        :return:
        """
        ele = WebDriverWait(self.driver, 20, 2).until(lambda a: a.find_element_by_tag_name(element))
        return ele

    def action_js(self, js):
        """
        执行js
        :param js: 原生javascript
        :return:
        """
        self.driver.execute_script(js)

    def add_cart(self):
        """
        new arrivals加入购物车
        :return:
        """
        self.action_js('window.scrollTo(0,1700)')
        time.sleep(2)
        num = random.randint(0, 5)
        ele = self.by_xpathes('//*[@class="product_price_button "]', num)
        ele.click()
        time.sleep(3)

    def code(self, code):
        """
        模糊code
        :param code: code值
        :return:
        """
        time.sleep(2)
        input_code = self.web_xpath_wait('//*[@id="code"]')
        input_code.send_keys(code)
        time.sleep(2)
        self.by_class('js_apply').click()
        time.sleep(2)
        test = self.by_class('js_apply').get_attribute('textContent')
        return test

    def enter_checkout(self):
        """
        进入checkout
        :return:
        """
        try:
            time.sleep(2)
            ele = self.web_xpath_wait('//*[text()="CHECKOUT"]')
            ele.click()
        except :
            print('超时')

    def card_pay(self):
        """
        信用卡支付
        :return:
        """
        time.sleep(3)
        self.action_js('window.scrollTo(0,900)')
        time.sleep(3)
        js = 'document.getElementById("card_pay").click()'
        self.action_js(js)
        # 切换frame
        time.sleep(5)
        fra = self.web_tag_wait('iframe')
        self.driver.switch_to.frame(fra)
        time.sleep(3)
        for i in range(0, 3):
            data = self.by_classes('Textbox-control', i)
            time.sleep(2)
            if i == 0:
                data.send_keys('4242424242424242')
            elif i == 1:
                data.send_keys('0426')
            else:
                data.send_keys('465')
        time.sleep(4)
        self.driver.find_element_by_class_name('Button').click()
        self.driver.switch_to.default_content()
        time.sleep(10)
        test = self.by_xpath('//*[@class="successful_text"][1]').get_attribute('textContent')
        return test

    def view_order(self):
        """
        VIEW ORDER
        :return:
        """
        self.by_xpath('//*[@text()="VIEW ORDER"]').click()

    def continue_shopping(self):
        """
        CONTINUE SHOPPING
        :return:
        """
        self.by_xpath('//*[@text()="CONTINUE SHOPPING"]').click()

    def close_web(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def login(self, n):
        """
        首页转盘登录,新号
        :param n: yaml文件里列表序数
        :return:
        """
        get_login = self.data.get_data(n)
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

    def currenturl(self):
        """
        当前页面url
        :return:
        """
        urls = self.driver.current_url
        return urls

    def delete_blank(self, text):
        """
        去首尾空格
        :param text:
        :return:
        """
        text = text.strip()
        text = text.lstrip()
        return text

    def sign_login(self, n):
        """
        页面内登录，新号
        :param n: yaml文件里列表序数
        :return:
        """
        get_login = self.data.get_data(n)
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
        log = self.delete_blank(log)
        return log

    def facebook_login(self,n):
        """
        facebook登录
        :param n:列表序数
        :return:
        """
        datas = self.data.get_data(n)
        time.sleep(2)
        self.by_xpath(datas[0]).click()
        time.sleep(3)
        self.facebook_login_info(n)
        time.sleep(2)

    def facebook_login_info(self, n):
        """
        facebook登录账号
        :param handle: 句柄
        :param ele: 元素
        :param eles: 元素
        :return:
        """
        file = get_path_file('facebook_login_info')
        data = json_data(file)
        datas = self.data.get_data(n)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.by_xpath(datas[1]).send_keys(data['user'])
        time.sleep(2)
        self.by_xpath(datas[2]).send_keys(data['password'])
        time.sleep(2)
        self.by_xpath(datas[3]).click()
        time.sleep(10)
        self.driver.switch_to.window(handles[0])

    def facebook_click(self):
        """
        在checkout里点击FACEBOOK
        """
        time.sleep(3)
        self.by_xpath('//*[@class="checkout_third_party"][1]/button').click()
        time.sleep(5)

    def judge_element(self, element):
        """
        判断某个元素是否存在
        :param element:xpath定位
        :return: 错误提示文档；空
        """
        try:
            time.sleep(2)
            informations = self.by_xpath(element).get_attribute('textContent')
            return informations
        except:
            return ""

    def email_address(self):
        """
        产生随机QQ
        :return:
        """
        email = ""
        QQ = '@qq.com'
        for i in range(10):
            letter = random.randint(0, 10)
            email += str(letter)
        qq_address = email + QQ
        return qq_address

    def checkout(self,n,data):
        """
        checkout_shipping address
        :param n: 列表序数
        :param data: 随机QQ
        :return:
        """
        datas = self.data.get_data(n)
        name = self.by_xpath(datas[1])
        name.click()
        self.driver.implicitly_wait(3)
        name.send_keys('111111')
        self.by_xpath(datas[2]).send_keys('2222')
        self.by_xpath(datas[3]).send_keys(data)
        time.sleep(2)
        se = self.by_xpath(datas[4])
        Select(se).select_by_index(1)
        city = self.by_xpath(datas[5])
        time.sleep(2)
        Select(city).select_by_value("3")
        # 地址
        dicts = {datas[6]: 'jgpdjhgdjglsjg', datas[7]: 'pjgpja', datas[8]: "16468", datas[9]: '094646465'}
        for k, v in zip(dicts.keys(), dicts.values()):
            time.sleep(1)
            self.by_xpath(k).send_keys(v)
        time.sleep(2)

    def attick_address(self):
        """
        点击不使用Use this shipping
        :return:
        """
        data = self.data.get_data(9)
        self.by_xpath(data[0]).click()
        time.sleep(1)

    def billing_address(self, n):
        """
        checkout_billing address
        :param n: 列表序数
        :return:
        """
        datas = self.data.get_data(n)
        self.action_js('window.scrollTo(0,500)')
        time.sleep(2)
        self.by_xpathes(datas[0], 1).send_keys('33333')
        time.sleep(1)
        self.by_xpathes(datas[1], 1).send_keys('4444')
        time.sleep(1)
        self.by_xpathes(datas[2], 1).send_keys('646464687@qq.com')
        time.sleep(2)
        se = self.by_xpathes(datas[3], 1)
        Select(se).select_by_index(1)
        time.sleep(2)
        city = self.by_xpathes(datas[4], 1)
        Select(city).select_by_value("7")
        time.sleep(1)
        self.by_xpathes(datas[5], 1).send_keys('oojhgjfe')
        time.sleep(1)
        self.by_xpathes(datas[6], 1).send_keys('epgfjogjero')
        time.sleep(1)
        self.by_xpathes(datas[7], 1).send_keys('16486')
        self.by_xpathes(datas[8], 1).send_keys('468648465')

    def delete_pan(self, n):
        """
        删除转盘页
        :param n: element_yaml列表序数
        :return: 列表
        """
        get_datas = self.data.get_data(n)
        self.by_xpath(get_datas[0]).click()
        return get_datas

    def types_optical(self, n):
        """
        光学类目页
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.by_link_test(get_datas[1]).click()
        optical = WebDriverWait(self.driver, 10).until(e.title_contains("Optical Eyeglasses"))
        return optical

    def types_blue(self, n):
        """
        蓝光类目页
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.by_link_test(get_datas[2]).click()
        blue = WebDriverWait(self.driver,5).until(e.title_contains('Blue Light Filter'))
        return blue

    def type_story(self, n):
        """
        故事类目页
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.by_link_test(get_datas[5]).click()
        story = WebDriverWait(self.driver, 5).until(e.title_contains('Our Story'))
        return story

    def move_element(self, ele):
        """
        鼠标移至sunglasses或collection
        :param ele: 元素属性
        :return: True
        """
        actions = ActionChains(self.driver)
        sunglasses = self.by_xpath(ele)
        actions.move_to_element(sunglasses).perform()

    def type_sunwear(self, n):
        """
        sunwear类目页
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.move_element(get_datas[3])
        self.by_xpath('//*[@class="tj_pc_menu_list"][1]/li[1]').click()
        sunwear = WebDriverWait(self.driver, 5).until(e.title_contains('Sunwear'))
        return sunwear

    def type_prescription(self, n):
        """
        prescription sunnies
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.move_element(get_datas[3])
        self.by_xpath('//*[@class="tj_pc_menu_list"][1]/li[2]').click()
        prescription = WebDriverWait(self.driver, 5).until(e.title_contains('Prescription Sunnies'))
        return prescription

    def type_life(self,n):
        """
        life is art
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.move_element(get_datas[4])
        self.by_xpath('//*[@id="collection"]/ul/li[1]').click()
        life = WebDriverWait(self.driver,5).until(e.title_contains('Life is Art'))
        return life

    def type_eco(self, n):
        """
        ECO
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.move_element(get_datas[4])
        self.by_xpath('//*[@id="collection"]/ul/li[2]').click()
        eco = WebDriverWait(self.driver,5).until(e.title_contains('Eco-Friendly'))
        return eco

    def type_pets(self, n):
        """
        TIJN X PETS
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.move_element(get_datas[4])
        self.by_xpath('//*[@id="collection"]/ul/li[3]').click()
        pets = WebDriverWait(self.driver,5).until(e.title_contains('Pets Eyeglasses'))
        return pets

    def type_search(self, n):
        """
        SEARCH页
        :param n: element_yaml列表序数
        :return: True
        """
        get_datas = self.delete_pan(n)
        self.by_xpath(get_datas[6]).click()
        time.sleep(2)
        search = self.by_xpath(get_datas[7]).get_attribute('textContent')
        return search

    def search(self, n, data):
        """
        搜索功能
        :param n: 列表序数
        :param data: 数据
        :return:
        """
        get_datas = self.delete_pan(n)
        time.sleep(2)
        js = "document.getElementsByClassName('pc_tj_search')[0].click()"
        self.action_js(js)
        time.sleep(2)
        self.by_xpath(get_datas[1]).send_keys(data['datas'])
        self.by_xpath(get_datas[2]).click()

    def checkout_visitor(self, data):
        """
        游客登录checkout
        :param data: 数据参数
        :return:
        """
        time.sleep(2)
        self.by_xpath('//input[@class="input_item"]').send_keys(data)

    def click_arb(self):
        """
        任意点击
        :return:
        """
        self.by_xpath('//*[text()="Checkout"]').click()

    def checkout_password(self, data):
        """
        checkout_password
        :param data:
        :return:
        """
        self.by_xpath('//*[@id="Customer_Password"]').send_keys(data)
        time.sleep(2)
        self.by_xpath('//*[@id="login_button"]').click()

    def save_checkout_address(self):
        """
        已保存地址
        :return:
        """
        self.by_xpath('//*[@class="edit_shipping_address_wrap"][1]/div/p[1]/img').click()

    def shipping(self):
        """
        运费加急
        :return:
        """
        self.by_xpath('//*[@class="change"][2]').click()

    def save_address(self):
        """
        保存地址
        :return:
        """
        self.by_xpath('//*[@class="shipping_address_save"]').click()


    def ins_tag(self, n):
        """
        ins中tag
        :param n:列表序数
        :return:
        """
        get_datas = self.data.get_data(n)
        time.sleep(2)
        self.action_js(get_datas[0])
        time.sleep(5)
        self.action_js(get_datas[1])
        self.by_xpath(get_datas[2]).click()
        time.sleep(1)
        self.by_xpath(get_datas[3]).click()

    def home_index(self):
        """
        点击TIJN，回到首页
        :return:
        """
        self.by_xpath('//*[@class="left"]/a').click()

    def live_cart(self):
        """
        离开购物车
        :return:
        """
        self.by_xpath('//*[text()="LEAVE"]').click()
























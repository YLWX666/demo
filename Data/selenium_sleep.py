from selenium04 import webdriver
import time
from selenium04.webdriver.common.action_chains import ActionChains
from selenium04.webdriver.support.ui import WebDriverWait



# web = webdriver.Firefox()
# web.get('http://www.baidu.com')
# web.find_element_by_id('kw').send_keys('麦子学院')
# web.find_element_by_id('su').click()
# web.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[3]/div[1]/h3/a[1]/em').click()
# web.switch_to_window()
# print(web.window_handles)
# print(web.current_window_handle)



url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc123456'


def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def login_test():
    d = webdriver.Firefox()
    d.get(url)

    d.maximize_window()
    ele_login = get_ele_times(d,10,lambda d:d.find_element_by_link_text(login_text))
    # d.find_element_by_link_text(login_test()).click()
    ele_login.click()
    account_ele = d.find_element_by_id('id_account_l')
    # account_ele.send_keys('')
    account_ele.clear()
    account_ele.send_keys(account)

    pwd_ele = d.find_element_by_id('id_password_l')
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
    d.find_element_by_id('login_btn').click()

    try:
        d.find_element_by_link_text('该账号格式不正确')
        print("Account And Pwd Error")
    except:
        print("Account And Pwd Right")
    # d.quit()
if __name__ == '__main__':
    login_test()





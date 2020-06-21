from selenium05 import webdriver

from selenium05.webdriver.support.ui import WebDriverWait


#
url = 'http://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = 'abc123456'
text = '该账号格式不正确'
#
#
# def get_ele_times(driver,times,func):
#     return WebDriverWait(driver,times).until(func)
#
# def openBrowser():
#     web = webdriver.Firefox()
#     return web
#
# def poenUrl(url):
#     d = openBrowser()
#     d.get(url)
#     d.maximize_window()
#     return d
#
#
# def findElement():
#     d = poenUrl(url)
#     ele_login = get_ele_times(d, 10, lambda d: d.find_element_by_link_text(login_text))
#     ele_login.click()
#     account_ele = d.find_element_by_id('id_account_l')
#     account_ele.clear()
#     pwd_ele = d.find_element_by_id('id_password_l')
#     pwd_ele.clear()
#     return account_ele,pwd_ele
# def sendKeys():
#     b,d = findElement()
#     b.send_keys(account)
#     d.send_keys(pwd)
#
#
# def login_test():
#     # d = poenUrl(url)
#     sendKeys()
#
#     # account_ele = d.find_element_by_id('login_text')
#     # # account_ele.send_keys('')
#     # account_ele.clear()
#     # account_ele.send_keys(account)
#     #
#     # pwd_ele = d.find_element_by_id('id_password_l')
#     # pwd_ele.clear()
#     # pwd_ele.send_keys(pwd)
#     # d.find_element_by_id('login_btn').click()
#
#     # try:
#     #     d.find_element_by_link_text('该账号格式不正确')
#     #     print("Account And Pwd Error")
#     # except:
#     #     print("Account And Pwd Right")
#     # d.quit()
# if __name__ == '__main__':
#     login_test()




def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():
    webdriver_handle = webdriver.Firefox()
    return  webdriver_handle

def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()

def findElement(d,arg):

    if 'text_id' in arg:
        ele_login = get_ele_times(d, 10, lambda d: d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
        useEle = d.find_element_by_id(arg['userid'])
        pwdEle = d.find_element_by_id(arg['pwdid'])
        loginEle = d.find_element_by_id(arg['loginid'])

        return useEle,pwdEle,loginEle
def sendVals(eletuple,arg):
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i +=1
    eletuple[2].click()

def checkRusult(d,text):
    try:
        d.find_element_by_link_text(text)
        print("Account And Pwd Error")
    except:
        print("Account And Pwd Right")

def login_test():
    d = openBrower()
    openUrl(d,url)
    ele_dict = {'text_id':login_text,'userid':'id_account_l','pwdid':'id_password_l','loginid':'login_btn'}
    account_dict = {'uname':account,'pwd':pwd}

    ele_tuple = findElement(d,ele_dict)
    sendVals(ele_tuple, account_dict)

    checkRusult(d,text)

if __name__ =='__main__':
    login_test()

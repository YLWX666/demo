
from selenium05 import webdriver

from selenium05.webdriver.support.ui import WebDriverWait




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
    # listkey = {'uname':account,'pwd':pwd}
    i = 0
    for key in arg:
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

def login_test(ele_dict,user_list):
    d = openBrower()
    openUrl(d,ele_dict['url'])
    ele_tuple = findElement(d,ele_dict)
    for arg in user_list:
        sendVals(ele_tuple, arg)
        checkRusult(d,ele_dict['error'])

if __name__ =='__main__':

    url = 'http://www.maiziedu.com/'
    login_text = '登录'
    account = 'maizi_test@139.com'
    pwd = 'abc123456'
    text = '该账号格式不正确'
    ele_dict = {'url':url,'text_id':login_text,'userid':'id_account_l','pwdid':'id_password_l','loginid':'login_btn','uname':account,'pwd':pwd,'error':text}
    user_list = [{'uname':account,'pwd':pwd}]
    login_test(ele_dict,user_list)
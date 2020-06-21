from selenium04.webdriver.common.action_chains import ActionChains
import time
import xlsxwriter
from selenium04 import webdriver
#
# db = webdriver.Firefox()
# db.get('http://www.baidu.com')
# time.sleep(2)
# iput = db.find_element_by_id('kw')
# iput.send_keys('爱奇艺')
# db.find_element_by_id('su').click()
# db.maximize_window()
# db.find_element_by_link_text('爱奇艺-在线视频网站-海量正版高清视频在线观看').click()
# # print(db.window_handles)

xl = xlsxwriter.Workbook(r'C:\Users\Admin\Desktop\t.xls')
sheet1 = xl.add_worksheet('aaa')
sheet1.write_string(1,0,'name')
sheet1.write_string(1,1,'mima')
sheet1.set_column('A:B',30)
xl.close()
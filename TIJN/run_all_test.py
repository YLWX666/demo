
import unittest,os
from BeautifulReport import BeautifulReport as Be
import yagmail
def send_mail(report):
    yag =yagmail.SMTP(user="xiong.chen@x.heywind.com",
                      password="CHExio0911",
                      host="smtp.exmail.qq.com")
    subject = "主题，自动化测试报告"
    contents = "正文，请看附件"
    yag.send("yesheng.su@x.heywind.com",subject,contents,report)

def run_test():
    path = os.getcwd()
    file_path = os.path.join(path,'test_case')
    all_test = unittest.defaultTestLoader.discover(file_path,pattern='test*.py',top_level_dir=None)
    report = Be(all_test)
    report.report('所有用例','测试用例报告',report_dir=r'C:\Users\Admin\PycharmProjects\TIJN\report')

if __name__ == '__main__':
    run = unittest.TextTestRunner()
    run.run(run_test())
report = r'C:\Users\Admin\PycharmProjects\TIJN\report\测试用例报告.html'
send_mail(report)






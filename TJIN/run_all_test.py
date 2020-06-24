
import unittest,os
from BeautifulReport import BeautifulReport as Be
import yagmail


# 发送邮件
def send_email(report):
    yag = yagmail.SMTP(user="xiong.chen@x.heywind.com",password="CHExio0911",host="smtp.exmail.qq.com")
    subject = "测试"
    contents = "自动化测试报告"
    yag.send(['yesheng.su@x.heywind.com','yuping.chen@x.heywind.com'],subject,contents,report)

def run_test():
    path = os.getcwd()
    file_path = os.path.join(path,'test_tjin')
    report_path = os.path.join(path,'report')
    all_test = unittest.defaultTestLoader.discover(file_path,pattern='test*.py',top_level_dir=None)
    report = Be(all_test)
    report.report('所有用例','测试用例报告',report_dir=report_path)
    reports = report_path+'\测试用例报告.html'
    send_email(reports)

if __name__ == '__main__':
    run = unittest.TextTestRunner()
    run.run(run_test())
    # run_test()














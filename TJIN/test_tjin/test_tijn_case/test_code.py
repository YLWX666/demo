import unittest,ddt
from BeautifulReport import BeautifulReport as Be
from element_step.step import StepElement

@ddt.ddt()
class TestCode(unittest.TestCase):
    '''测试模糊code'''

    def setUp(self) -> None:
        self.driver = StepElement()
        self.driver.open_url('https://tj.qa.heywind.cn')

    def tearDown(self) -> None:
        self.driver.close_web()
    @ddt.data(*[' 5free',' 5free ','5free  ','ksfle'])
    def test_code(self,data):
        '''测试游客模糊code及无效code'''
        self.driver.delete_pan(1)
        self.driver.add_cart()
        test = self.driver.code(data)
        self.assertEqual(test,'REMOVE')

# if __name__ == "__main__":
#     unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(TestCode))
#     re = Be(suite)
#     re.report(filename='测试报告',description='测试报告',report_dir=r'C:\Users\chexi\PycharmProjects\TJIN\report\测试报告.html')


















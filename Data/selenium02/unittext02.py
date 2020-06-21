import unittest

class Case02(unittest.TestCase):



    def setUp(self):
        print('测试开始')

    def test_03(self):
        print('第3条用例')

    def test_04(self):
        print('第4条用例')
    def tearDown(self):
        print('测试结束')
if __name__ =='__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Case02('test_03'))
    # suite.addTest(Case02('test_04'))
    # unittest.TextTestRunner().run(suite)
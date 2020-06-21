import unittest
import os

class Case(unittest.TestCase):

    # def setUp(self):
    #     print('开始测试')
    #
    def test_start(self):
        case_path = os.getcwd()
        suite = unittest.defaultTestLoader.discover(case_path,'unittext*.py')
        unittest.TextTestRunner().run(suite)
if __name__ == '__main__':
    unittest.main()
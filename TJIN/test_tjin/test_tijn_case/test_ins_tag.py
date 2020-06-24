import unittest

from element_step.step import StepElement



class TestInsTag(unittest.TestCase):
    '''测试首页ins中的tag'''

    def setUp(self) -> None:
        self.driver = StepElement('element_yaml','Firefox')
        self.driver.open_url('https://tj.qa.heywind.cn')

    def test_ins_tag(self):
        '''测试首页ins中的tag'''
        self.driver.delete_pan(1)
        self.driver.ins_tag(7)

# if __name__ == "__main__":
#     unittest.main()





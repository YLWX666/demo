# import pytest
#
# def test_hello():
#     print("hello world!")
#     assert 1
#
# @pytest.mark.xfail()
# def test_yoyo1():
#     a = "hello"
#     b = "hello world"
#     assert a == b
#
# @pytest.mark.xfail()
# def test_yoyo2():
#     a = "hello"
#     b = "hello world"
#     assert a != b
#
# if __name__ == "__main__":
#     pytest.main(["-v", "a.py"])
import unittest
from ddt import ddt,data,unpack

#需要测试的代码
def add(a):
    return (a+1)

#设置值
data1=[{'a':1,'b':2},{'a':1,'b':2},{'a':1,'b':2},{'a':1,'b':2}]

#使用ddt对被测试代码进行批量测试
@ddt
class TestDDT(unittest.TestCase):

    @data(*data1)
    def test_add(self,data1):
        res=add(data1["a"])
        print(data1['a'])
        assert res==data1["b"]

if __name__=='__main__':
    unittest.main()



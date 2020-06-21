# class Test02:
#
#     def __init__(self):
import pytest
@pytest.fixture(scope="class")
def first():
    print("\n获取用户名，scope为class级别只运行一次")
    a="nuo"
    return a

class TestCase():
    @pytest.mark.fixtures("first")
    def test_1(self):
        '用例传fixture'
        print("测试账号：%s")


    def test_2(self,first):
        '用例传fixture'
        print("测试账号：%s"%first)
        assert first == "nuo"

if __name__ == '__main__':
    pytest.main()





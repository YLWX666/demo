import pytest

class Test_st:
    def setup_class(self):
        print("1")
    def teardown_class(self):
        print("2")

    def test_001(self):
        assert True



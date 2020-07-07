import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("test_fixtureDemo2 lépések")

    def test_fixtureDemo2(self):
        print("test_fixtureDemo2 lépések")

    def test_fixtureDemo3(self):
        print("test_fixtureDemo3 lépések")

    def test_fixtureDemo4(self):
        print("test_fixtureDemo4 lépések")
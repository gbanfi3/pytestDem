import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad):
        assert dataLoad.upper() == "ALMAg"
        print("kkkkkkk ez már utólag van?")
        print(dataLoad.upper())

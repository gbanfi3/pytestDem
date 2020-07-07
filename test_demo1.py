import pytest

@pytest.mark.smoke
def test_firstProgramCreditCard():
    print('helloka')

def test_greetings(setup):
    print('jó reggelt')

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "hi", "test failed mert ..."

@pytest.mark.xfail
def test_2ndProgramCreditCard():
    a = 4
    b = 6
    assert a + 2 == b, "nem találta el a számolást"

def test_fixtureDemo(setup):
    print("test_fixtureDemo lépések")
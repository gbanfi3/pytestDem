import pytest

@pytest.fixture(scope="class")
def setup():
    print("executed first")
    yield
    print("last executed")

@pytest.fixture()
def dataLoad():
    print("user profile is being created")
    return ['aa', 'bb', 'cc']
    # return "alma"

@pytest.fixture(params=[("chrome","aa", "bb"), ("Firefox","cc"), "IE"])
def crossBrowser(request):
    return request.param
# https://www.youtube.com/watch?v=xNo4G-njtJk
from selenium import webdriver
import pytest
class TestOrange():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homPageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title=="OrangeHRM"

    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("divLoginButton").click()
        assert self.driver.title=="OrangeHRM"
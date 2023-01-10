import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from testing.base import Base


class Testfrom(Base):
    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()
    #
    # def teardown(self):
    #     self.driver.quit()
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")

if __name__ == '__main__':

    pytest.main(['-v','-s','test_From.py'])


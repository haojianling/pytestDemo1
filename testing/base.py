import os

from selenium import webdriver


class Base():
    def setup(self):
        key = 'JAVA_HOME'
        value = os.getenv(key)
        print("Value of 'HOME' environment variable :", value)
        # if browse=="filfox":
        #     self.driver=webdriver.firefox()
       # if value=="Chrome":
        self.driver=webdriver.Chrome()
        # else:
        #     self.driver=webdriver.edge()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()


    def teardown(self):
        self.driver.quit()


    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
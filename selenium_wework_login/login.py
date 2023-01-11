import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_wework_login.register import Register

class Login:
    def __init__(self,driver:WebDriver): #语法的注释，添加标签可有可无
        self._driver=driver
    def scanf(self):#扫码
        pass
    def goto_register(self):
        # time.sleep(2)
        self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register(self._driver)
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def register(self):
        self.driver.find_element(By.ID,'corp_name').send_keys("haollllll")
        self.driver.find_element(By.ID, 'manager_name').send_keys('ffff')
        # time.sleep(3)
        self.driver.quit()
        return True


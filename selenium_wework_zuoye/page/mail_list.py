import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_zuoye.page.addmember import AddMember
from selenium_wework_zuoye.page.basepage import BasePage


class Maillist(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver
    def goto_add_member(self):
        time.sleep(3)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        # self._driver.find_element(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        # print(ele)
        # ele[1].click()
        return AddMember(self._driver)
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_zuoye.page.basepage import BasePage


class AddMember(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver
    def add_member(self):
        self.find(By.ID, 'username').send_keys("999")
        self.find(By.ID, 'memberAdd_acctid').send_keys("999")
        self.find(By.ID, 'memberAdd_biz_mail').send_keys("9939")
        self.find(By.ID, 'memberAdd_phone').send_keys("15678909606")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # self._driver.find_element(By.ID, 'username').send_keys("999")
        # self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("999")
        # self._driver.find_element(By.ID, 'memberAdd_biz_mail').send_keys("9939")
        # self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("15678909606")
        # self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()


    def get_member(self):
        time.sleep(3)
        # self.wait_for_click(By.CSS_SELECTOR, '.ww_checkbox')
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr>td:nth-child(2)')
        # elements=self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_tr>td:nth-child(2)')
        list=[ele.get_attribute("title") for ele in elements]
        return list

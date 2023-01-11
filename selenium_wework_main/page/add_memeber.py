import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:
    def __init__(self,driver:WebDriver):
        self._driver=driver
    def add_member(self):
        time.sleep(3)
        self._driver.find_element(By.ID,'username').send_keys("321321321")
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys("123456")
        self._driver.find_element(By.ID, 'memberAdd_biz_mail').send_keys("444444444444")
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys("15678909876")
        self._driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        time.sleep(2)
        # self._driver.quit()
        # return True

    def get_member(self):
        elements=self._driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_tr>td:nth-child(2)")
        list=[element.get_attribute("title") for element in elements]
        return list
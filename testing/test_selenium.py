import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_selenium():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://testerhome.com/")
    driver.find_element(By.LINK_TEXT,"社团").click()
    driver.find_element(By.LINK_TEXT,"测试开发方舟号").click()
    el=driver.find_element(By.CSS_SELECTOR,".topic-34995 .title > a")
    print(el.text)
    time.sleep(2)


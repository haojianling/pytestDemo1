from appium import webdriver
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='12.0'
# desired_caps['deviceName']='vivo iQOO Neo3'
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# driver.quit()

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'
desired_caps['deviceName']='vivo iQOO Neo3'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.quit()
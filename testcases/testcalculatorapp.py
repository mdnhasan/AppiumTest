import time

from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='.activities.PeopleActivity',
)

# appium_service = AppiumService()
# appium_service.start()


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(1)

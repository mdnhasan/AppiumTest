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
    appPackage='com.android.dialer',
    appActivity='.main.impl.MainActivity',
)

# appium_service = AppiumService()
# appium_service.start()


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(1)

driver.find_element(By.ID, 'com.android.dialer:id/fab').click()
time.sleep(3)
driver.find_element(By.XPATH, "//android.widget.TextView[@text='1']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='2']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='3']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='4']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='5']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='6']").click()
driver.find_element(By.XPATH, "//android.widget.TextView[@text='0']").click()

driver.find_element(By.ID, "com.android.dialer:id/dialpad_floating_action_button").click()

time.sleep(2)
driver.quit()

# appium_service.stop()

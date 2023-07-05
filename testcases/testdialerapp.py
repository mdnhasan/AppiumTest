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
    appPackage='com.samsung.android.dialer',
    appActivity='.DialtactsActivity',
)

# appium_service = AppiumService()
# appium_service.start()


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(1)

# driver.find_element(By.ID, 'com.android.dialer:id/fab').click()
# time.sleep(3)
driver.find_element(By.ID, 'com.samsung.android.dialer:id/one').click()
driver.find_element(By.ID, "com.samsung.android.dialer:id/two").click()
driver.find_element(By.ID, "com.samsung.android.dialer:id/three").click()
driver.find_element(By.ID, "com.samsung.android.dialer:id/four").click()
driver.find_element(By.ID, "com.samsung.android.dialer:id/one").click()
driver.find_element(By.ID, "com.samsung.android.dialer:id/one").click()

driver.find_element(By.ID, "com.samsung.android.dialer:id/callButtonContainer").click()

time.sleep(2)
driver.quit()

# appium_service.stop()

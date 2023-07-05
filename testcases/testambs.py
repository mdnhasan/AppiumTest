import time

from appium import webdriver
from pathlib import Path
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.ambs.mobile',
    appActivity='.LoginActivity'
)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)


driver.find_element(By.ID, 'com.ambs.mobile:id/etLogin_MainActivity').send_keys("00453")
time.sleep(3)
driver.find_element(By.ID, 'com.ambs.mobile:id/etPassword_MainActivity').send_keys("Test@12345")
time.sleep(3)

driver.find_element(By.ID, 'com.ambs.mobile:id/rbOnlineMode_Login').click()
time.sleep(3)

driver.find_element(By.ID, 'com.ambs.mobile:id/btnLogin_MainActivity').click()

driver.quit()
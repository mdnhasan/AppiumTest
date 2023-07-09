import time

from appium import webdriver
from pathlib import Path
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from scrollUtility import ScrollUtility

from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select

from appium import webdriver
from pathlib import Path
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from appium.webdriver.common.touch_action import TouchAction


desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='flipboard.app',
    appActivity='flipboard.activities.LaunchActivity',
    noReset= True
)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
"""Android App Switching to another App"""
# time.sleep(5)
#
#
# driver.start_activity('com.android.dialer', '.main.impl.MainActivity')
# time.sleep(10)
#
# driver.start_activity('com.google.android.apps.messaging', '.home.HomeActivity')
#
# time.sleep(10)
#
# driver.start_activity('com.mobeta.android.demodslv', '.Launcher')

"""Not Reset Option true """
driver.implicitly_wait(5)

try:
    a = driver.find_element(By.ID, "flipboard.app:id/icon_button_text")
    if a.is_displayed():
        a.click()
        time.sleep(2)

except NoSuchElementException:
    print("Get Started Not found")

try:
    b = driver.find_element(By.XPATH, "//android.widget.TextView[@text='WHAT INTERESTS YOU?']")
    if b.is_displayed():
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='# NEWS']").click()
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='# SCIENCE']").click()
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='# TECHNOLOGY']").click()
        time.sleep(2)
        driver.find_element(By.ID, "flipboard.app:id/icon_button_text").click()


except NoSuchElementException:
    print("Selection not found")

time.sleep(2)
try:
    c = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Skip for Now']")
    if c.is_displayed():
        c.click()
except NoSuchElementException:
    print("Skip Page not found")

time.sleep(5)
"""Its working till now """
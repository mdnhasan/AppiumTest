import time

from appium import webdriver
from pathlib import Path
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.amazon.mShop.android.shopping',
    appActivity='com.amazon.mShop.splashscreen.StartupActivity'
)
# desired_caps = {}
# desired_caps['deviceName'] = 'Android'
# desired_caps['platformName'] = 'Android'
# desired_caps['appPackage'] = 'com.amazon.mShop.android.shopping'
# desired_caps['appActivity'] = 'com.amazon.mShop.splashscreen.StartupActivity'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)

try:
    a = driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_deny_button")
    if a.is_displayed():
        driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_deny_button").click()
        time.sleep(5)
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Done']")))
        # driver.find_element(By.XPATH, "//android.widget.Button[@text='Done']").click()
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')))
        # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()

except NoSuchElementException:
    print("Permission page not found")

try:
    b = driver.find_element(By.XPATH, "//android.widget.Button[@text='Done']")

    if b.is_displayed():
        driver.find_element(By.XPATH, "//android.widget.Button[@text='Done']").click()
        time.sleep(5)
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')))
        # driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()
        # time.sleep(1)

except NoSuchElementException:
    print("Language Page Not Found")

try:
    c = driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button')
    if c.is_displayed():
        driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/skip_sign_in_button').click()

except NoSuchElementException:
    print("Skip Sign not found")


time.sleep(2)

driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text')))

driver.find_element(By.ID, 'com.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys("Jeans")
driver.press_keycode(66)
time.sleep(5)

print("Code Run Successfully")
driver.quit()

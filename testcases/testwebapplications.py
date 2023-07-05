import time

from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get('https://www.google.com/')
print(driver.title)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@name='q']").send_keys("abc")


time.sleep(5)
driver.quit()

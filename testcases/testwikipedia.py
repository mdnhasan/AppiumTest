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
    browserName='Chrome'
)

# appium_service = AppiumService()
# appium_service.start()


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get('https://www.wikipedia.org/')
print(driver.title)
dropdown = driver.find_element(By.ID, "searchLanguage")
select = Select(dropdown)
select.select_by_index(1)

options = driver.find_elements(By.TAG_NAME, "option")
print(len(options))

for option in options:
    print("Text Is: ", option.text, "Lang Is: ", option.get_attribute("Lang"))
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@name='q']").send_keys("abc")


time.sleep(5)
driver.quit()

# appium_service.stop()

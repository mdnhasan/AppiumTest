import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


"""Global Setup"""

"""For Single Device"""
# @pytest.fixture(scope="function")
# def appium_driver():
#     global driver
#     desired_caps = {}
#     desired_caps['deviceName'] = 'Android'
#     desired_caps['platformName'] = 'Android'
#     desired_caps['appPackage'] = 'com.goibibo'
#     desired_caps['appActivity'] = '.common.HomeActivity'
#     desired_caps['noReset'] = True
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

"""For Multiple Devices parallel """
@pytest.fixture(params=["device1","device2"],scope="function")
def appium_driver(request):
    if request.param=="device1":
        desired_caps = {}
        desired_caps['deviceName'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['browserName'] = 'chrome'
        desired_caps['udid'] = 'emulator-5554'
        # desired_caps['noReset'] = True
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    if request.param == "device2":
        desired_caps = {}
        desired_caps['deviceName'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['browserName'] = 'chrome'
        desired_caps['udid'] = 'emulator-5556'
        # desired_caps['noReset'] = True
        driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_caps)

    driver.implicitly_wait(15)
    yield driver
    driver.quit()



@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=AttachmentType.PNG)  ###Success Sceenshot

import time

import pytest
from selenium import webdriver

from pageObjects.Frames import Frame
from pageObjects.Homepage import HomePage
from Utilities.BaseClass import BaseClass
from Utilities.Screenshot import Screenshot


def pytest_addoption(parser):
    parser.addoption(
       "--browser_name", action="store", default="chrome"
   )



@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")  # to get the browser name during runtime
    ss_path = "/conftest/"

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe",chrome_options=options)

    elif browser_name == "firefox":  # firefox gecko driver
        # driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Documents\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Downloads\\geckodriver-v0.26.0-win32\\geckodriver.exe")

    driver.get("https://c6.avaamo.com/web_channels/444588bc-92fe-477f-87c1-88a92946346a/demo.html?theme=avm-messenger&banner=true&demo=true&banner_text=%20&banner_title=This%20is%20how%20the%20chat%20agent%20shows%20up")

    baseclass = BaseClass()
    logs = baseclass.getLogger()
    ss = Screenshot(driver)

    expected_title = "Test agent - IRA"

    try:
        assert driver.title == expected_title
        logs.info("Webpage loaded successfully")

    except Exception as e:
        logs.info("Webpage failed to load",e)
        ss.screenShot(ss_path+"webpage_load_fail.png")

    driver.maximize_window()
    driver.implicitly_wait(4)

    home_page = HomePage(driver)

    try:
        if home_page.IraIcon().is_displayed():
            home_page.notificationButton().click()

    except Exception as e:
        logs.critical("IraIcon is not displayed in the webpage",e)
        ss.screenShot(ss_path+"IraIcon_Unavailable.png")

    request.cls.driver = driver
    yield
    driver.close()
import time

import pytest
from selenium import webdriver

from pageObjects.Frames import Frame
from pageObjects.Homepage import HomePage


def pytest_addoption(parser):
    parser.addoption(
       "--browser_name", action="store", default="chrome"
   )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")  # to get the browser name during runtime
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe",chrome_options=options)

    elif browser_name == "firefox":  # firefox gecko driver
        # driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Documents\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver = webdriver.Firefox(executable_path="C:\\Users\\indrasen\\Downloads\\geckodriver-v0.26.0-win32\\geckodriver.exe")

    driver.get("https://c6.avaamo.com/web_channels/444588bc-92fe-477f-87c1-88a92946346a/demo.html?theme=avm-messenger&banner=true&demo=true&banner_text=%20&banner_title=This%20is%20how%20the%20chat%20agent%20shows%20up")
    driver.maximize_window()
    driver.implicitly_wait(4)
    home_page = HomePage(driver)
    home_page.notificationButton().click()
    request.cls.driver = driver
    yield
    driver.close()
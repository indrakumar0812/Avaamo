import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup")
class BaseClass:

    def windowHandles(self):
        windows = self.driver.window_handles
        return windows

    def switchWindow(self,index):
        self.driver.switch_to.window(index)


    def ElementFound(self,timesec,locator):
        wait = WebDriverWait(self.driver,timesec)
        wait.until(expected_conditions.presence_of_element_located((locator)))

    def ImplicitWait(self,time):
        self.driver.implicitly_wait(time)

    def ScreenShot(self,filename):
        self.driver.get_screenshot_as_file(filename)

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger




import inspect
import logging
import time

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:

#Window handle method

    def windowHandles(self):
        windows = self.driver.window_handles
        return windows

    def switchWindow(self,index):
        self.driver.switch_to.window(index)

#Capture Logs method
    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger




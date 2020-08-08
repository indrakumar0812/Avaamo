import time

class Screenshot:

    def __init__(self,driver):
        self.driver = driver

    def screenShot(self,path):
        directory = "C:/Users/indrasen/PycharmProjects/avaamo/ScreenShots"
        filename = directory+path
        self.driver.get_screenshot_as_file(filename)



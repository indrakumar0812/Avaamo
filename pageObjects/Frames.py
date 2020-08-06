
class Frame:

    def __init__(self,driver):
        self.driver=driver


    def switchFrame(self):
        self.driver.switch_to.frame("avaamoIframe")

    
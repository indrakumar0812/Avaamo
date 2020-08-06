from selenium.webdriver.common.by import By
from pageObjects.Frames import Frame


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    notification=(By.XPATH,"//small[text()='Hello and welcome to IRA agent']")
    welcomemsg = (By.CLASS_NAME,"welcome-message")
    getstarted = (By.CLASS_NAME,"get-started-link")

    def notificationButton(self):
        return self.driver.find_element(*HomePage.notification)

    def welcomeMsg(self):
        return self.driver.find_element(*HomePage.welcomemsg)

    def getStarted(self):
        self.driver.find_element(*HomePage.getstarted).click()
        frame_switch = Frame(self.driver)
        frame_switch.switchFrame()

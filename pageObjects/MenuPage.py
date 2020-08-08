from selenium.webdriver.common.by import By

#Menu page locators

class MenuPage:

    def __init__(self,driver):
        self.driver=driver

    menubutton = (By.XPATH,"//div[@class='botMenu dflex ptr']/div[3]")
    searchbox = (By.XPATH,"//div[contains(@class,'textarea-wrap')]/textarea")
    sendbutton = (By.CSS_SELECTOR,"div[class*='send']")
    responsemsg =(By.XPATH,"//div[contains(@class,'message-wrap')]")

    def menuButton(self):
        return self.driver.find_element(*MenuPage.menubutton)

    def searchBox(self):
        return self.driver.find_element(*MenuPage.searchbox)

    def sendButton(self):
        return self.driver.find_element(*MenuPage.sendbutton)

    def responseMsg(self):
        return self.driver.find_elements(*MenuPage.responsemsg)
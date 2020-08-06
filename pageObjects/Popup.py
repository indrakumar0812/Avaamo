from selenium.webdriver.common.by import By

class Popup:

    def __init__(self,driver):
        self.driver=driver

    google = (By.LINK_TEXT,"Google")
    closeicon = (By.XPATH,"//div[contains(@class,'modal-dialog tall')]/div/div/button")
    call = (By.LINK_TEXT,"Call")

    def googleLink(self):
        return self.driver.find_element(*Popup.google)

    def closeIcon(self):
        return self.driver.find_element(*Popup.closeicon)

    def callLink(self):
        return self.driver.find_element(*Popup.call)

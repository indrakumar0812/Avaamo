from selenium.webdriver.common.by import By

#Policy Page locators

class PolicyPage:

    def __init__(self,driver):
        self.driver = driver

    startover = (By.CSS_SELECTOR,"a[actionname='Start Over']")
    motorpolicy = (By.LINK_TEXT,"Download Motor Policy")
    downloadbutton = (By.LINK_TEXT,"Download")
    policyno = (By.CSS_SELECTOR,"input[formcontrolname='policyNumber']")
    vechileno = (By.CSS_SELECTOR,"input[formcontrolname='vehRegNumber']")
    engineno = (By.CSS_SELECTOR,"input[formcontrolname='engineNo']")
    downloadpolicybutton = (By.XPATH,"//button[text()='Download Policy']")

    def startOver(self):
        return self.driver.find_element(*PolicyPage.startover)

    def motorPolicy(self):
        return self.driver.find_element(*PolicyPage.motorpolicy)

    def downloadButton(self):
        return self.driver.find_element(*PolicyPage.downloadbutton)

    def policyNo(self):
        return self.driver.find_element(*PolicyPage.policyno)

    def vechileNo(self):
        return self.driver.find_element(*PolicyPage.vechileno)

    def engineNo(self):
        return self.driver.find_element(*PolicyPage.engineno)

    def downloadPolicyButton(self):
        return self.driver.find_element(*PolicyPage.downloadpolicybutton)

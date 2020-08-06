from selenium.webdriver.common.by import By


class UserDetailPage:

    def __init__(self,driver):
        self.driver = driver

    #namefeild = (By.XPATH,"//input[contains(@id,'single_line_text')]")
    namefeild = (By.CSS_SELECTOR, "input[type='text']")
    addressfeild = (By.XPATH,"//div[contains(@class,'composer__container')]/textarea")
    genderradio = (By.XPATH,"//span[text()='Male']")
    optionbox = (By.XPATH,"//input[contains(@class,'picklist-textbox')]")
    selectoption =(By.XPATH,"//li[text()='Very Often']")
    ratings = (By.XPATH,"//span[@class='star-cb-group']/label")
    submit = (By.CSS_SELECTOR,"button[class*='btn default_card_submit']")

    def nameField(self):
        return self.driver.find_element(*UserDetailPage.namefeild)

    def addressField(self):
        return self.driver.find_element(*UserDetailPage.addressfeild)

    def genderRadio(self):
        return self.driver.find_element(*UserDetailPage.genderradio)

    def selectBox(self):
        return self.driver.find_element(*UserDetailPage.optionbox)

    def selectOption(self):
        return self.driver.find_element(*UserDetailPage.selectoption)

    def ratingSelection(self):
        return self.driver.find_elements(*UserDetailPage.ratings)

    def submitButton(self):
        return self.driver.find_element(*UserDetailPage.submit)
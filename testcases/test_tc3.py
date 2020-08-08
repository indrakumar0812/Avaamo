import time

import pytest

from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.MenuPage import MenuPage
from pageObjects.UserPage import UserDetailPage
from testData.formPage import UserPageData
from Utilities.Screenshot import Screenshot


class TestUserForm(BaseClass):

    def test_tc3(self,getData):

        ss_path="/test_tc3.py/"
        logs=self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getStarted()
        menu_page=MenuPage(self.driver)
        ss=Screenshot(self.driver)

#Checking for menu option availability

        if menu_page.menuButton().is_displayed():
            menu_page.menuButton().click()

        else:
            logs.info("Menu button not found")
            ss.screenShot(ss_path+"menu_button_locate_fail.png")

#Entering the command "Test bot" and validation
        try:
            if menu_page.searchBox().is_displayed():
                logs.info("sending the command", getData["command"])
                menu_page.searchBox().send_keys(getData["command"])

            else:
                logs.info("searchbox not found")

            if menu_page.searchBox().get_attribute("value") == getData["command"]:
                menu_page.sendButton().click()

            else:
                logs.info("command doesn't match")

        except Exception as e:
            logs.info("exception has occurred",e)
            ss.screenShot(ss_path+"send_command_fail.png")

        user_page = UserDetailPage(self.driver)

#Enter details only when submit button is seen
        try:
            if user_page.submitButton().is_displayed():
                logs.info("form page is displayed")
                user_page.nameField().send_keys(getData["fullname"])
                user_page.addressField().send_keys(getData["useraddress"])
                gender = user_page.genderRadio()

                for i in gender:
                    if i.text == getData["gender"][1]:
                        logs.info(getData["gender"][1])
                        i.click()

                user_page.selectBox().click()

                options = user_page.selectOption()

                logs.info("selecting option")
                for i in options:
                    if i.text == getData["choice"][1]:
                        logs.info(getData["choice"][1])
                        i.click()
                        break

                logs.info("selecting ratings")
                feedback = user_page.ratingSelection()
                for i in feedback:
                    if int(i.text) == getData["stars"][2]:
                        logs.info(getData["stars"][2])
                        i.click()

                user_page.submitButton().click()

        except Exception as e:
            logs.info("Exception occured while filling the form",e)
            ss.screenShot(ss_path+"form_fill_fail.png")

#validing the form submission

        try:
           assert user_page.submittedText().text == "Submitted Successfully"
           logs.info("Test Passed")

        except Exception as e:
            logs.info("Exception occured",e)
            ss.screenShot(ss_path+"Assertion_Fail.png")

#Clearing the chat history

        menu_page.searchBox().send_keys(getData["Clear"])

    @pytest.fixture(params=UserPageData.test_data)
    def getData(self, request):
        return request.param
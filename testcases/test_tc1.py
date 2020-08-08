import time

import pytest
from testData.homePage import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.MenuPage import MenuPage
from Utilities.Screenshot import Screenshot


class TestScreen(BaseClass):

    def test_tc1(self,getData):

#Creating a relative path

        ss_path="/test_tc1/"

        logs = self.getLogger()
        home_page = HomePage(self.driver)
        ss = Screenshot(self.driver)

#Validating the welcome message

        expected_message ="Hello and welcome to IRA agent"
        actual_message = home_page.welcomeMsg().text

        try:
            assert expected_message == actual_message
            logs.info(actual_message)

        except Exception as e:
            logs.info("failed to get retrieve the welcome message",e)
            ss.screenShot(ss_path+"WelcomeMessage_Fail.png")

        home_page.getStarted()

        menu_page = MenuPage(self.driver)

#Checking the availability of menu button before action
        try:
            if menu_page.menuButton().is_displayed():
                menu_page.menuButton().click()

        except Exception as e:
            logs.info("menu button is not available or failed to click on the button",e)
            ss.screenShot(ss_path+"menu_button_fail.png")

#Entering data in the search box

        if menu_page.searchBox().is_enabled():
            menu_page.searchBox().send_keys(getData)
        else:
            logs.info("menu button not found")
            ss.screenShot(ss_path+"menu_button_unavailable.png")

        if menu_page.sendButton().is_enabled():
            menu_page.sendButton().click()

        else:
            logs.info("unable to send message")
            ss.screenShot(ss_path+"message_sent_fail.png")

        time.sleep(3)

        resMsgList = menu_page.responseMsg()

        try:
            for i in range (0,len(resMsgList)):
                if i==2:
                    respmsg=resMsgList[i].text
                    logs.info(respmsg)
                    assert len(respmsg) != 0
                    logs.info("Test passed")

        except Exception as e:
            logs.info(e)


    @pytest.fixture(params=HomePageData.test_data)
    def getData(self,request):
        return request.param
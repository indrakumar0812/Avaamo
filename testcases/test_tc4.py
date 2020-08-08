import time

import pytest
from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.MenuPage import MenuPage
from testData.PopupData import PopUpData
from pageObjects.Popup import Popup
from Utilities.Screenshot import Screenshot


class TestPopup(BaseClass):

    def test_tc4(self,getData):

#Creating a relative path
        ss_path="/tesr_tc4/"

        home_page = HomePage(self.driver)
        home_page.getStarted()

        menu_page = MenuPage(self.driver)

        popup = Popup(self.driver)

        logs=self.getLogger()

        ss=Screenshot(self.driver)

        menu_page.menuButton().click()

        if menu_page.searchBox().is_displayed():
            logs.info(getData)
            menu_page.searchBox().send_keys(getData)
        else:
            logs.info("Menu box is not displayed")

        menu_page.sendButton().click()

        self.driver.implicitly_wait(4)

        target_url = "https://www.google.com/"

#Validating the hyperlinks before action
        try:
            if popup.googleLink().get_attribute("href")==target_url:
                popup.googleLink().click()
            else:
                logs.info("unable to navigate")
                ss.screenShot(ss_path+"google_navigate_fail.png")

            if popup.closeIcon().is_displayed():
                popup.closeIcon().click()
            else:
                logs.info("element not found")
                ss.screenShot(ss_path + "close_icon_fail.png")

            expected_link="tel:1234567890"
            if popup.callLink().get_attribute("href")==expected_link:
                popup.callLink().click()
            else:
                logs.info("unable to navigate")
                ss.screenShot(ss_path+"call_link_fail.png")

        except Exception as e:
            logs.info(e)

#Handling the pop-up window

        window = self.windowHandles()
        actual_url = self.driver.current_url
        try:
            for i in window[1:]:
                self.switchWindow(i)
                self.driver.close()
            self.switchWindow(window[0])
        except Exception as e:
            logs.info("exception occured while handling pop-up",e)

        recent_url = self.driver.current_url

#assertion home page and the navigated url

        assert actual_url == recent_url
        logs.info("Test passed")

    @pytest.fixture(params=PopUpData.test_data)
    def getData(self, request):
        return request.param
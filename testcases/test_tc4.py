import time

import pytest
from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.MenuPage import MenuPage
from testData.PopupData import PopUpData
from pageObjects.Popup import Popup


class TestPopup(BaseClass):

    def test_tc4(self,getData):

        home_page = HomePage(self.driver)
        home_page.getStarted()
        menu_page = MenuPage(self.driver)
        menu_page.menuButton().click()
        menu_page.searchBox().send_keys(getData)
        menu_page.sendButton().click()
        popup = Popup(self.driver)
        self.ImplicitWait(4)
        popup.googleLink().click()
        popup.closeIcon().click()
        popup.callLink().click()

        window = self.windowHandles()

        for i in window[1:]:
            self.switchWindow(i)
            self.driver.close()
        self.switchWindow(window[0])

    @pytest.fixture(params=PopUpData.test_data)
    def getData(self, request):
        return request.param
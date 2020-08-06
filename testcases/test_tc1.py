import time

import pytest
from testData.homePage import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.MenuPage import MenuPage


class TestScreen(BaseClass):

    def test_tc1(self,getData):

        logs = self.getLogger()
        home_page = HomePage(self.driver)
        msg = home_page.welcomeMsg().text
        logs.info(msg)
        home_page.getStarted()
        menu_page = MenuPage(self.driver)
        menu_page.menuButton().click()
        menu_page.searchBox().send_keys(getData)
        menu_page.sendButton().click()
        time.sleep(3)
        resMsgList = menu_page.responseMsg()

        for i in range (0,len(resMsgList)):
            if i==2:
                respmsg=resMsgList[i].text
                logs.info(respmsg)

    @pytest.fixture(params=HomePageData.test_data)
    def getData(self,request):
        return request.param
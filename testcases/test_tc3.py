import pytest

from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage
from pageObjects.MenuPage import MenuPage
from pageObjects.UserPage import UserDetailPage
from testData.formPage import UserPageData


class TestUserForm(BaseClass):

    def test_tc3(self,getData):
        home_page = HomePage(self.driver)
        home_page.getStarted()
        menu_page=MenuPage(self.driver)
        menu_page.menuButton().click()
        menu_page.searchBox().send_keys(getData["command"])
        menu_page.sendButton().click()
        try:
            user_page = UserDetailPage(self.driver)
            user_page.nameField().send_keys(getData["fullname"])
            user_page.addressField().send_keys(getData["useraddress"])
            user_page.genderRadio().click()
            user_page.selectBox().click()
            user_page.selectOption().click()
            ratings = user_page.ratingSelection()
            for i in range(0, len(ratings)):
                if i == 2:
                    ratings[i].click()

            user_page.submitButton().click()
        except AttributeError:
            self.ScreenShot("tc3.png")
            print("there's no such attribute")
        menu_page.searchBox().send_keys(getData["Clear"])
        menu_page.sendButton().click()

    @pytest.fixture(params=UserPageData.test_data)
    def getData(self, request):
        return request.param
import time

import pytest
from selenium.webdriver.support import expected_conditions

from Utilities.BaseClass import BaseClass
from pageObjects.PolicyPage import PolicyPage
from testData.policyDetails import PolicyPageData
from pageObjects.Frames import Frame
from pageObjects.Homepage import HomePage
from Utilities.Screenshot import Screenshot


class TestPolicyScreen(BaseClass):

    def test_tc2(self, getData):

#Creating a relative path

        ss_path="/test_tc2/"

        logs=self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getStarted()

        policy_page = PolicyPage(self.driver)

        ss=Screenshot(self.driver)

#Validating the button availability befrore action
        try:
            if policy_page.startOver().is_displayed():
                policy_page.startOver().click()

        except Exception as e:
            logs.info("Failed to locate the button",e)
            ss.screenShot(ss_path +"StartOver_button_fail.png")

#Validating the different options

        if policy_page.motorPolicy().text == "Download Motor Policy":
            policy_page.motorPolicy().click()
        else:
            logs.info("invalid link")

        if policy_page.downloadButton().is_displayed():
            policy_page.downloadButton().click()

        else:
            logs.info("download button is not available")
            ss.screenShot(ss_path+"DownloadButton_Fail.png")

        policy_download_url = policy_page.downloadButton().get_attribute("href")

#Handling the window switch

        try:
            childwindow=self.windowHandles()[1]
            assert self.driver.current_url != policy_download_url

            self.switchWindow(childwindow)

        except Exception as e:
            logs.info("failed to switch",e)
            ss.screenShot(ss_path+"Navigation_error.png")

#Filling the form
        try:
            logs.info(getData["policyNumber"])
            policy_page.policyNo().send_keys(getData["policyNumber"])
            logs.info(getData["vechileNumber"])
            policy_page.vechileNo().send_keys(getData["vechileNumber"])
            logs.info(getData["engineNumber"])
            policy_page.engineNo().send_keys(getData["engineNumber"])
            policy_page.downloadPolicyButton().click()

        except Exception as e:
            logs.info("failed to get the userdata",e)
            ss.screenShot(ss_path+"userdata_retrieve_fail.png")

        self.driver.close()

        self.switchWindow(self.windowHandles()[0])

#Asserting with home page
        assert self.driver.current_url != policy_download_url
        logs.info("Test passed")

    @pytest.fixture(params= PolicyPageData.test_data)
    def getData(self,request):
        return request.param
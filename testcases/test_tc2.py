
import pytest
from Utilities.BaseClass import BaseClass
from pageObjects.PolicyPage import PolicyPage
from testData.policyDetails import PolicyPageData
from pageObjects.Frames import Frame
from pageObjects.Homepage import HomePage


class TestPolicyScreen(BaseClass):

    def test_tc2(self, getData):
        logs=self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getStarted()
        policy_page = PolicyPage(self.driver)
        policy_page.startOver().click()
        policy_page.motorPolicy().click()
        policy_page.downloadButton().click()
        childwindow=self.windowHandles()[1]
        self.switchWindow(childwindow)
        logs.info(getData["policyNumber"])
        policy_page.policyNo().send_keys(getData["policyNumber"])
        logs.info(getData["vechileNumber"])
        policy_page.vechileNo().send_keys(getData["vechileNumber"])
        logs.info(getData["engineNumber"])
        policy_page.engineNo().send_keys(getData["engineNumber"])
        policy_page.downloadPolicyButton().click()
        self.driver.close()
        self.switchWindow(self.windowHandles()[0])

    @pytest.fixture(params= PolicyPageData.test_data)
    def getData(self,request):
        return request.param
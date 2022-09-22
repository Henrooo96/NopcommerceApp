from asyncio.log import logger
import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearcCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("******* SearchingCustomerByEmail_004 ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login successful **********")

        self.logger.info("********** Starting Search Customer By Email ***********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("******* searching customer by emailID *******")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("billy_ross@nopcommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("billy_ross@nopcommerce.com")
        assert True == status
        self.logger.info("*********** TC_SearchCustomerByEmail_004 Finished  ***********")
        self.driver.close();


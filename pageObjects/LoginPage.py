class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = "logout"

    def __int__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self,login):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
        self.driver.find_element_by_xpath(login.ENTER).click()
    


    def clickLogout(self,logout):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        self.driver.find_element_by_link_text(logout, "//link_logout_linktext[@id='logout']").text

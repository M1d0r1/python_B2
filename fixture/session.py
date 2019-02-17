from selenium import webdriver

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, admin, password):
        self.app.open_start_page()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(admin)
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(password)
        self.app.wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

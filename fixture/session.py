class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, admin, password):
        self.app.open_start_page()
        wd = self.app.wd
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(admin)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

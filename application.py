from selenium import webdriver

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def login(self, admin, password):
        self.open_start_page()
        self.wd.find_element_by_name("user").clear()
        self.wd.find_element_by_name("user").send_keys(admin)
        self.wd.find_element_by_name("pass").clear()
        self.wd.find_element_by_name("pass").send_keys(password)
        self.wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_group(self, group):
        # Init group creation
        self.navigate_to_groups()
        self.wd.find_element_by_name("new").click()
        # Fill in the form
        self.wd.find_element_by_name("group_name").click()
        self.wd.find_element_by_name("group_name").clear()
        self.wd.find_element_by_name("group_name").send_keys(group.name)
        self.wd.find_element_by_name("group_header").click()
        self.wd.find_element_by_name("group_header").clear()
        self.wd.find_element_by_name("group_header").send_keys(group.header)
        self.wd.find_element_by_name("group_footer").click()
        self.wd.find_element_by_name("group_footer").clear()
        self.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation and navigate to groups
        self.wd.find_element_by_name("submit").click()
        self.navigate_to_groups()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def open_start_page(self):
        self.wd.get("http://localhost/addressbook/")


    def navigate_to_groups(self):
        self.wd.find_element_by_link_text("groups").click()

    def destroy(self):
        self.wd.quit()
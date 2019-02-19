class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        # Init group creation
        self.app.navigate_to_groups()
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        # Fill in the form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation and navigate to groups
        wd.find_element_by_name("submit").click()
        self.app.navigate_to_groups()

    def delete_first(self):
        self.app.navigate_to_groups()
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.app.navigate_to_groups()

    def modify_first(self):
        self.app.navigate_to_groups()
        # Init group modification
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # Update group parameters
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("Upd")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Upd")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("Upd")
        # Submit group creation and navigate to groups
        wd.find_element_by_name("update").click()
        self.app.navigate_to_groups()


        self.app.navigate_to_groups()
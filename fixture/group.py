class GroupHelper:
    def __init__(self, app):
        self.app = app


    def create(self, group):
        # Init group creation
        self.app.navigate_to_groups()
        self.app.wd.find_element_by_name("new").click()
        # Fill in the form
        self.app.wd.find_element_by_name("group_name").click()
        self.app.wd.find_element_by_name("group_name").clear()
        self.app.wd.find_element_by_name("group_name").send_keys(group.name)
        self.app.wd.find_element_by_name("group_header").click()
        self.app.wd.find_element_by_name("group_header").clear()
        self.app.wd.find_element_by_name("group_header").send_keys(group.header)
        self.app.wd.find_element_by_name("group_footer").click()
        self.app.wd.find_element_by_name("group_footer").clear()
        self.app.wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation and navigate to groups
        self.app.wd.find_element_by_name("submit").click()
        self.app.navigate_to_groups()

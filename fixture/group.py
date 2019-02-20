from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self,group):
        # Init group creation
        self.app.navigate_to_groups()
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        # Fill in the form
        self.fill_form(group)
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
        old_group = self.app.group.get_data()
        new_group = Group(name=old_group.name + " upd", header=old_group.header + " upd", footer=old_group.footer + " upd")
        self.fill_form(new_group)
        # Submit group modification and navigate to groups
        wd.find_element_by_name("update").click()
        self.app.navigate_to_groups()

    def fill_form(self,group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def get_data(self):
        wd = self.app.wd
        name = wd.find_element_by_name("group_name").get_attribute('value')
        header = wd.find_element_by_name("group_header").get_attribute('value')
        footer = wd.find_element_by_name("group_footer").get_attribute('value')
        group = Group(name, header, footer)
        return group
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        # Init group creation
        self.app.navigate_to_groups()
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        # Fill in the form
        self.fill_form(group)
        # Submit group creation and navigate to groups
        wd.find_element_by_name("submit").click()
        self.app.navigate_to_groups()
        self.group_cache = None

    def delete_first(self):
        self.app.navigate_to_groups()
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.app.navigate_to_groups()
        self.group_cache = None

    def modify_first(self, new_group_data):
        self.app.navigate_to_groups()
        # Init group modification
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_form(new_group_data)
        # Submit group modification and navigate to groups
        wd.find_element_by_name("update").click()
        self.app.navigate_to_groups()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_form(self, group):
        self.app.fill_text_field("group_name", group.name)
        self.app.fill_text_field("group_header", group.header)
        self.app.fill_text_field("group_footer", group.footer)

    def get_data_first(self):
        wd = self.app.wd
        self.app.navigate_to_groups()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        name = wd.find_element_by_name("group_name").get_attribute('value')
        header = wd.find_element_by_name("group_header").get_attribute('value')
        footer = wd.find_element_by_name("group_footer").get_attribute('value')
        group = Group(name, header, footer)
        self.app.navigate_to_groups()
        return group

    def count(self):
        wd = self.app.wd
        self.app.navigate_to_groups()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigate_to_groups()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_start_page(self):
        self.wd.get("http://localhost/addressbook/")

    def navigate_to_groups(self):
        self.wd.find_element_by_link_text("groups").click()

    def fill_text_field(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_file_field(self, field_name, path):
        wd = self.wd
        if path is not None:
            wd.find_element_by_name(field_name).send_keys(path)

    def fill_date_field(self, day_field, month_field, year_field, date):
        wd = self.wd
        if date is not None:
            Select(wd.find_element_by_name(day_field)).select_by_visible_text(str(date.day))
            Select(wd.find_element_by_name(month_field)).select_by_index(date.month)
            wd.find_element_by_name(year_field).clear()
            wd.find_element_by_name(year_field).send_keys(str(date.year))

    def destroy(self):
        self.wd.quit()
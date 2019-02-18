from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


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

    def destroy(self):
        self.wd.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
import os

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

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


    def create_contact(self, contact):
        # Init contact creation
        self.navigate_to_contacts()
        # Fill in the form
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.first_name)
        self.wd.find_element_by_name("middlename").click()
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        self.wd.find_element_by_name("lastname").click()
        self.wd.find_element_by_name("lastname").clear()
        self.wd.find_element_by_name("lastname").send_keys(contact.last_name)
        self.wd.find_element_by_name("nickname").click()
        self.wd.find_element_by_name("nickname").clear()
        self.wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.wd.find_element_by_name("photo").send_keys(os.getcwd() + r'\Resource\photo.jpg')
        self.wd.find_element_by_name("title").click()
        self.wd.find_element_by_name("title").clear()
        self.wd.find_element_by_name("title").send_keys(contact.title)
        self.wd.find_element_by_name("company").click()
        self.wd.find_element_by_name("company").clear()
        self.wd.find_element_by_name("company").send_keys(contact.company)
        self.wd.find_element_by_name("address").click()
        self.wd.find_element_by_name("address").clear()
        self.wd.find_element_by_name("address").send_keys(contact.primary_address)
        self.wd.find_element_by_name("home").click()
        self.wd.find_element_by_name("home").clear()
        self.wd.find_element_by_name("home").send_keys(contact.primary_home_phone)
        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        self.wd.find_element_by_name("work").click()
        self.wd.find_element_by_name("work").clear()
        self.wd.find_element_by_name("work").send_keys(contact.work_phone)
        self.wd.find_element_by_name("fax").click()
        self.wd.find_element_by_name("fax").clear()
        self.wd.find_element_by_name("fax").send_keys(contact.fax)
        self.wd.find_element_by_name("email").click()
        self.wd.find_element_by_name("email").clear()
        self.wd.find_element_by_name("email").send_keys(contact.email1)
        self.wd.find_element_by_name("email2").click()
        self.wd.find_element_by_name("email2").clear()
        self.wd.find_element_by_name("email2").send_keys(contact.email2)
        self.wd.find_element_by_name("email3").click()
        self.wd.find_element_by_name("email3").clear()
        self.wd.find_element_by_name("email3").send_keys(contact.email3)
        self.wd.find_element_by_name("homepage").click()
        self.wd.find_element_by_name("homepage").clear()
        self.wd.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(self.wd.find_element_by_name("bday")).select_by_visible_text(str(contact.birthdate.day))
        Select(self.wd.find_element_by_name("bmonth")).select_by_index(contact.birthdate.month)
        self.wd.find_element_by_name("byear").clear()
        self.wd.find_element_by_name("byear").send_keys(contact.birthdate.year)
        Select(self.wd.find_element_by_name("aday")).select_by_visible_text(str(contact.anniversary_date.day))
        Select(self.wd.find_element_by_name("amonth")).select_by_index(contact.anniversary_date.month)
        self.wd.find_element_by_name("ayear").clear()
        self.wd.find_element_by_name("ayear").send_keys(contact.anniversary_date.year)
        self.wd.find_element_by_name("address2").click()
        self.wd.find_element_by_name("address2").clear()
        self.wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        self.wd.find_element_by_name("phone2").click()
        self.wd.find_element_by_name("phone2").clear()
        self.wd.find_element_by_name("phone2").send_keys(contact.secondary_home_phone)
        Select(self.wd.find_element_by_name("new_group")).select_by_visible_text(contact.group.name)
        self.wd.find_element_by_name("notes").click()
        self.wd.find_element_by_name("notes").clear()
        self.wd.find_element_by_name("notes").send_keys(contact.notes)
        # Submit contact creation
        self.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_start_page()


    def open_start_page(self):
        self.wd.get("http://localhost/addressbook/")


    def navigate_to_groups(self):
        self.wd.find_element_by_link_text("groups").click()

    def navigate_to_contacts(self):
        self.wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()
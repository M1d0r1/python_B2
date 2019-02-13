# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
from contact import Contact, Address
import navigation
import unittest
import time


class AddGroupsAndContactsTest(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    # def test_add_group(self):
    #     wd = self.wd
    #     self.open_start_page(wd)
    #     self.login(wd, "admin", "secret")
    #     self.create_group(wd, Group(name="Group"+str(time.time()), header="Header"+str(time.time()), footer="Footer"+str(time.time())))
    #     self.navigate_to_groups(wd)
    #     self.logout(wd)
    #
    # def test_add_empty_group(self):
    #     wd = self.wd
    #     self.open_start_page(wd)
    #     self.login(wd, "admin", "secret")
    #     self.create_group(wd, Group(name="", header="", footer=""))
    #     self.navigate_to_groups(wd)
    #     self.logout(wd)

    def test_add_contact(self):
        wd = self.wd
        self.open_start_page(wd)
        self.login(wd, "admin", "secret")
        self.create_contact(wd, Contact(first_name="Contact"+str(time.time())))
        self.navigate_to_contacts(wd)
        self.logout(wd)


    def login(self, wd, admin, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(admin)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_start_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def navigate_to_groups(self, wd):
        wd.find_element_by_link_text("groups").click()

    def navigate_to_contacts(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_group(self, wd, group):
        # Init group creation
        self.navigate_to_groups(wd)
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
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def create_contact(self, wd, contact):
        # Init contact creation
        self.navigate_to_contacts(wd)
        # Fill in the form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        # wd.find_element_by_name("group_header").click()
        # wd.find_element_by_name("group_header").clear()
        # wd.find_element_by_name("group_header").send_keys(group.header)
        # wd.find_element_by_name("group_footer").click()
        # wd.find_element_by_name("group_footer").clear()
        # wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

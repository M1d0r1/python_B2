# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
from contact import Contact, Address
from selenium.webdriver.support.ui import Select
import unittest
import time
import datetime
import os

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
        tmstp = str(time.time())
        birthdate = datetime.date(1980, 11, 20)
        anniversary_date = datetime.date(2005, 3, 14)
        primary_address = Address(geo_address = "Country\nCity\nStreet,"+tmstp[13], home_phone = tmstp[4:7]+tmstp[13:16])
        secondary_address = Address(geo_address="Country\nCity\nStreet,"+tmstp[15], home_phone=tmstp[3:6] + tmstp[14:17])
        group = Group(name="Group" + tmstp[14:17], header="Header" + tmstp[14:17],footer="Footer" + tmstp[14:17])
        contact = Contact(first_name="Name"+tmstp,middle_name="Middle name"+tmstp,last_name="Last name"+tmstp,nickname="Nickname"+tmstp,title = "Title"+tmstp, company = "Company"+tmstp, primary_address=primary_address, secondary_address=secondary_address, mobile_phone = tmstp[0:8], work_phone = tmstp[1:9],fax = tmstp[2:10],email1=tmstp[0:5]+"@gmail.com", email2=tmstp[6:10]+"@mail.ru", email3=tmstp[8:11]+"@myjob.com",homepage = "https://"+tmstp[13:20]+".com", birthdate = birthdate, anniversary_date = anniversary_date, group = group, notes="here is my note")
        self.create_group(wd, group)
        self.create_contact(wd, contact)
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
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("photo").send_keys(os.getcwd() + "\Resource\photo.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.primary_address.geo_address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.primary_address.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(str(contact.birthdate.day))
        Select(wd.find_element_by_name("bmonth")).select_by_index(contact.birthdate.month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthdate.year)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(str(contact.anniversary_date.day))
        Select(wd.find_element_by_name("amonth")).select_by_index(contact.anniversary_date.month)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_date.year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address.geo_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_address.home_phone)
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group.name)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

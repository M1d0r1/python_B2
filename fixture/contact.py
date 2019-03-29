from model.contact import Contact
from selenium.webdriver.support.ui import Select
import datetime
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_start_page()
        wd.find_element_by_link_text("add new").click()
        # Fill everything but the group
        self.fill_form(contact)
        # Fill in the group
        if contact.group is not None:
            Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group.name)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_start_page()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_start_page()
        self.select_by_index(index)
        wd.find_element_by_xpath("// input[ @ value = 'Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        wd.find_element_by_link_text("add new")
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.open_start_page()
        self.select_by_id(id)
        wd.find_element_by_xpath("// input[ @ value = 'Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        wd.find_element_by_link_text("add new")
        self.contact_cache = None

    # def delete_first(self):
    #    self.delete_by_index(0)

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()

    # def select_first(self):
    #   self.select_by_index(0)

    def modify_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_start_page()
        # Init modification
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # Fill the form
        self.fill_form(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.app.open_start_page()
        self.contact_cache = None

    def modify_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_start_page()
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        self.fill_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    # def modify_first(self, contact):
    #   self.modify_by_index(0, contact)

    # The method fills in the form for contact creation/modification except for the group (as group is absent in the Edit screen)
    def fill_form(self, contact):
        self.app.fill_text_field("firstname", contact.first_name)
        self.app.fill_text_field("middlename", contact.middle_name)
        self.app.fill_text_field("lastname", contact.last_name)
        self.app.fill_text_field("nickname", contact.nickname)
        self.app.fill_text_field("title", contact.title)
        self.app.fill_text_field("company", contact.company)
        self.app.fill_text_field("address", contact.primary_address)
        self.app.fill_text_field("home", contact.primary_home_phone)
        self.app.fill_text_field("mobile", contact.mobile_phone)
        self.app.fill_text_field("work", contact.work_phone)
        self.app.fill_text_field("fax", contact.fax)
        self.app.fill_text_field("email", contact.email1)
        self.app.fill_text_field("email2", contact.email2)
        self.app.fill_text_field("email3", contact.email3)
        self.app.fill_text_field("homepage", contact.homepage)
        self.app.fill_date_field("bday", "bmonth", "byear", contact.birthdate)
        self.app.fill_date_field("aday", "amonth", "ayear", contact.anniversary_date)
        self.app.fill_text_field("address2", contact.secondary_address)
        self.app.fill_text_field("phone2", contact.secondary_home_phone)
        self.app.fill_text_field("notes", contact.notes)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_start_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def get_data_from_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute('value')
        middlename = wd.find_element_by_name("middlename").get_attribute('value')
        lastname = wd.find_element_by_name("lastname").get_attribute('value')
        nickname = wd.find_element_by_name("nickname").get_attribute('value')
        title = wd.find_element_by_name("title").get_attribute('value')
        company = wd.find_element_by_name("company").get_attribute('value')
        primary_address = wd.find_element_by_name("address").get_attribute('value')
        primary_home_phone = wd.find_element_by_name("home").get_attribute('value')
        mobile_phone = wd.find_element_by_name("mobile").get_attribute('value')
        work_phone = wd.find_element_by_name("work").get_attribute('value')
        fax = wd.find_element_by_name("fax").get_attribute('value')
        email1 = wd.find_element_by_name("email").get_attribute('value')
        email2 = wd.find_element_by_name("email2").get_attribute('value')
        email3 = wd.find_element_by_name("email3").get_attribute('value')
        homepage = wd.find_element_by_name("homepage").get_attribute('value')
        id = wd.find_element_by_name("id").get_attribute('value')
        # Dirty trick: set default dates
        if (wd.find_element_by_name("byear").get_attribute('value') is not "") and (
                wd.find_element_by_name("bday").get_attribute('value') is not "0"):
            birthdate = datetime.date(int(wd.find_element_by_name("byear").get_attribute('value')), 5,
                                      int(wd.find_element_by_name("bday").get_attribute('value')))
        else:
            birthdate = datetime.date(1982, 5, 4)
        if (wd.find_element_by_name("ayear").get_attribute('value') is not "") and (
                wd.find_element_by_name("aday").get_attribute('value') is not "0"):
            anniversary_date = datetime.date(int(wd.find_element_by_name("ayear").get_attribute('value')), 10,
                                             int(wd.find_element_by_name("aday").get_attribute('value')))
        else:
            anniversary_date = datetime.date(2009, 10, 10)
        secondary_address = wd.find_element_by_name("address2").get_attribute('value')
        secondary_home_phone = wd.find_element_by_name("phone2").get_attribute('value')
        notes = wd.find_element_by_name("notes").get_attribute('value')
        # birthdate.month and anniversary.month, photo_keys and group are hardcoded
        contact = Contact(first_name=firstname, middle_name=middlename, last_name=lastname, nickname=nickname,
                          photo_keys="", title=title, company=company, primary_address=primary_address,
                          primary_home_phone=primary_home_phone, secondary_address=secondary_address,
                          secondary_home_phone=secondary_home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                          fax=fax, email1=email1, email2=email2, email3=email3, homepage=homepage, birthdate=birthdate,
                          anniversary_date=anniversary_date, group="", notes=notes)
        self.app.open_start_page()
        return contact

    def count(self):
        wd = self.app.wd
        self.app.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_start_page()
            self.contact_cache = []
            for i in range(0,len(wd.find_elements_by_name("entry"))):
                contact = self.get_data_from_home_page_by_index(i)
                self.contact_cache.append(contact)
        return list(self.contact_cache)

    def get_data_from_home_page_by_index(self, index):
        wd = self.app.wd
        element = wd.find_elements_by_name("entry")[index]
        cells = element.find_elements_by_tag_name("td")
        firstname = cells[2].text
        lastname = cells[1].text
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        id = element.find_element_by_name("selected[]").get_attribute("value")
        contact = Contact(first_name=firstname, last_name=lastname, primary_address=address, all_phones=all_phones, all_emails=all_emails,id=id)
        return contact

    def get_data_from_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is not None:
            homephone = re.search("H: (.*)", text).group(1)
        else:
            homephone = ""
        if re.search("M: (.*)", text) is not None:
            mobilephone = re.search("M: (.*)", text).group(1)
        else:
            mobilephone = ""
        if re.search("W: (.*)", text) is not None:
            workphone = re.search("W: (.*)", text).group(1)
        else:
            workphone = ""
       # all_phones = homephone + mobilephone + workphone
        if re.search("P: (.*)", text) is not None:
            secondaryphone = re.search("P: (.*)", text).group(1)
        else:
            secondaryphone = ""
        #email1 = re.search("(.*)@(.*).(.*)",text).group(1)+re.search("(.*)@(.*).(.*)",text).group(2)+re.search("(.*)@(.*).(.*)",text).group(3)
       # email2 = re.search("(.*)@(.*).(.*)", text).grou
        #email3 = re.search("(.*)@(.*).(.*)", text).group(3)
        return Contact(primary_home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone, secondary_home_phone=secondaryphone)

    def get_data_from_view_page_by_id(self, id):
        wd = self.app.wd
        self.open_contact_to_view_by_id(id)
        text = wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is not None:
            homephone = re.search("H: (.*)", text).group(1)
        else:
            homephone = ""
        if re.search("M: (.*)", text) is not None:
            mobilephone = re.search("M: (.*)", text).group(1)
        else:
            mobilephone = ""
        if re.search("W: (.*)", text) is not None:
            workphone = re.search("W: (.*)", text).group(1)
        else:
            workphone = ""
       # all_phones = homephone + mobilephone + workphone
        if re.search("P: (.*)", text) is not None:
            secondaryphone = re.search("P: (.*)", text).group(1)
        else:
            secondaryphone = ""
        #email1 = re.search("(.*)@(.*).(.*)",text).group(1)+re.search("(.*)@(.*).(.*)",text).group(2)+re.search("(.*)@(.*).(.*)",text).group(3)
       # email2 = re.search("(.*)@(.*).(.*)", text).grou
        #email3 = re.search("(.*)@(.*).(.*)", text).group(3)
        return Contact(primary_home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone, secondary_home_phone=secondaryphone)


    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_start_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def open_contact_to_view_by_id(self, id):
        wd = self.app.wd
        self.app.open_start_page()
        wd.find_element_by_xpath("//a[@href='view.php?id=%s']" % id).click()
from model.contact import Contact
from selenium.webdriver.support.ui import Select
import datetime

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

    def delete_first(self):
        wd = self.app.wd
        self.app.open_start_page()
        self.select_first_contact()
        wd.find_element_by_xpath("// input[ @ value = 'Delete']").click()
        alert=wd.switch_to.alert
        alert.accept()
        self.app.open_start_page()
       # wd.find_element_by_name("add new")


    def select_first_contact(self):
        wd=self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first(self,contact):
        wd = self.app.wd
        self.app.open_start_page()
        #Init modification
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #Fill the form
        self.fill_form(contact)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.app.open_start_page()

    # The method fills in the form for contact creation/modification except for the group (as group is absent in the Edit screen)
    def fill_form(self, contact):
        wd = self.app.wd
        self.app.fill_text_field("firstname", contact.first_name)
        self.app.fill_text_field("middlename", contact.middle_name)
        self.app.fill_text_field("lastname", contact.last_name)
        self.app.fill_text_field("nickname", contact.nickname)
        self.app.fill_file_field("photo", contact.photo_keys)
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

    def get_data_first(self):
        wd = self.app.wd
        self.app.open_start_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
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
        #Dirty trick: set default dates
        if (wd.find_element_by_name("byear").get_attribute('value') is not "") and (wd.find_element_by_name("bday").get_attribute('value') is not "0"):
            birthdate  = datetime.date(int(wd.find_element_by_name("byear").get_attribute('value')), 5, int(wd.find_element_by_name("bday").get_attribute('value')))
        else:
            birthdate = datetime.date(1982, 5, 4)
        if (wd.find_element_by_name("ayear").get_attribute('value') is not "") and (
                wd.find_element_by_name("aday").get_attribute('value') is not "0"):
             anniversary_date = datetime.date(int(wd.find_element_by_name("ayear").get_attribute('value')), 10, int(wd.find_element_by_name("aday").get_attribute('value')))
        else:
            anniversary_date= datetime.date(2009, 10, 10)
        secondary_address = wd.find_element_by_name("address2").get_attribute('value')
        secondary_home_phone = wd.find_element_by_name("phone2").get_attribute('value')
        notes = wd.find_element_by_name("notes").get_attribute('value')
        # birthdate.month and anniversary.month, photo_keys and group are hardcoded
        contact = Contact(first_name=firstname,middle_name=middlename, last_name=lastname,nickname=nickname,photo_keys="",title=title,company=company,primary_address=primary_address, primary_home_phone=primary_home_phone, secondary_address=secondary_address, secondary_home_phone=secondary_home_phone, mobile_phone=mobile_phone,work_phone=work_phone,fax=fax, email1=email1,email2=email2, email3=email3,homepage=homepage,birthdate=birthdate,anniversary_date=anniversary_date,group="",notes=notes )
        self.app.open_start_page()
        return contact

    def count(self):
        wd = self.app.wd
        self.app.open_start_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_start_page()
        contact_list = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            firstname = cells[2].text
            lastname = cells[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contact_list.append(Contact(first_name = firstname, last_name = lastname, id = id))
        return contact_list
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
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group.name)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_start_page()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_start_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("// input[ @ value = 'Delete']").click()
        alert=wd.switch_to.alert
        alert.accept()
        self.app.open_start_page()

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
        wd.find_element_by_name("photo").send_keys(contact.photo_keys)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.primary_address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.primary_home_phone)
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
        wd.find_element_by_name("byear").send_keys(str(contact.birthdate.year))
        Select(wd.find_element_by_name("aday")).select_by_visible_text(str(contact.anniversary_date.day))
        Select(wd.find_element_by_name("amonth")).select_by_index(contact.anniversary_date.month)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(str(contact.anniversary_date.year))
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_home_phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

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
        birthdate  = datetime.date(int(wd.find_element_by_name("byear").get_attribute('value')), 5, int(wd.find_element_by_name("bday").get_attribute('value')))
        anniversary_date = datetime.date(int(wd.find_element_by_name("ayear").get_attribute('value')), 10, int(wd.find_element_by_name("aday").get_attribute('value')))
        secondary_address = wd.find_element_by_name("address2").get_attribute('value')
        secondary_home_phone = wd.find_element_by_name("phone2").get_attribute('value')
        notes = wd.find_element_by_name("notes").get_attribute('value')
        # birthdate.month and anniversary.month, photo_keys and group are hardcoded
        contact = Contact(first_name=firstname,middle_name=middlename, last_name=lastname,nickname=nickname,photo_keys="",title=title,company=company,primary_address=primary_address, primary_home_phone=primary_home_phone, secondary_address=secondary_address, secondary_home_phone=secondary_home_phone, mobile_phone=mobile_phone,work_phone=work_phone,fax=fax, email1=email1,email2=email2, email3=email3,homepage=homepage,birthdate=birthdate,anniversary_date=anniversary_date,group="",notes=notes )
        self.app.open_start_page()
        return contact
import pymysql.cursors
from model.group import Group
from model.contact import Contact
import datetime
from utils.formatstrings import FormatStrings

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database = name, user = user, password = password, autocommit = True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id = str(id), name = name, header = header, footer = footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes from addressbook where deprecated='0000-00-00 00:00:00'")

            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes) = row
                try:
                    birthdate = datetime.date(int(byear), FormatStrings.month_number(bmonth), int(bday))
                except:
                    birthdate = None
                try:
                    anniversary_date = datetime.date(int(ayear), FormatStrings.month_number(amonth), int(aday))
                except:
                    anniversary_date = None
                contact_list.append(Contact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname, nickname=nickname,
                                            company=company, title=title, primary_address=address, primary_home_phone=home, mobile_phone=mobile,
                                            work_phone=work, fax=fax, email1=email, email2=email2, email3=email3, homepage=homepage,
                                            birthdate=birthdate, anniversary_date=anniversary_date,
                                            secondary_address=address2, secondary_home_phone=phone2, notes=notes))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
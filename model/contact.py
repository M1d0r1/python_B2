from sys import maxsize
from utils.formatstrings import FormatStrings


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, photo_keys=None, title=None,
                 company=None, primary_address=None, primary_home_phone=None, secondary_address=None,
                 secondary_home_phone=None, mobile_phone=None, work_phone=None, all_phones = None, fax=None, email1=None, email2=None,
                 email3=None, all_emails = None, homepage=None, birthdate=None, anniversary_date=None, group=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo_keys = photo_keys
        self.title = title
        self.company = company
        self.primary_address = primary_address
        self.primary_home_phone = primary_home_phone
        self.secondary_address = secondary_address
        self.secondary_home_phone = secondary_home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.all_phones = all_phones
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails = all_emails
        self.homepage = homepage
        self.birthdate = birthdate
        self.anniversary_date = anniversary_date
        self.group = group
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "Contact:id=%s,first_name=%s,middle_name = %s, last_name=%s, primary_address=%s, primary_home_phone=%s" % (self.id, self.first_name, self.middle_name, self.last_name, self.primary_address, self.primary_home_phone)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and (self.first_name == other.first_name or self.first_name == None and other.first_name == "" or self.first_name == "" and other.first_name == None) and (self.last_name == other.last_name or self.last_name == "" and other.last_name == None or self.last_name == None and other.last_name == "")

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def clear(self):
        return Contact(id = self.id, first_name= FormatStrings.clear_spaces(self.first_name),  last_name = FormatStrings.clear_spaces(self.last_name))
from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, photo_keys=None, title=None,
                 company=None, primary_address=None, primary_home_phone=None, secondary_address=None,
                 secondary_home_phone=None, mobile_phone=None, work_phone=None, fax=None, email1=None, email2=None,
                 email3=None, homepage=None, birthdate=None, anniversary_date=None, group=None, notes=None, id=None):
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
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthdate = birthdate
        self.anniversary_date = anniversary_date
        self.group = group
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "Contact:id=%s,first_name=%s,last_name=%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (
                       self.id == other.id or self.id is None or other.id is None) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

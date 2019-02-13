class Contact:
    def __init__(self, first_name, middle_name, last_name, nickname, title, company, mobile_phone, work_phone, fax, email1, email2, email3, notes):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        # self.primary_address = primary_address
        # self.secondary_address = secondary_address
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        # self.birthday = birthday
        # self.anniversary = anniversary
        self.notes = notes

class Address:
    def __init__(self, geo_address, home_phone):
        self.geo_address = geo_address
        self.home_phone = home_phone
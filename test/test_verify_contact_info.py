import random
import re
from model.contact import Contact

def test_verify_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    ind = random.randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_data_from_edit_page_by_index(ind)
    contact_from_home_page = app.contact.get_data_from_home_page_by_index(ind)
    assert contact_from_edit_page.first_name == contact_from_home_page.first_name
    assert contact_from_edit_page.last_name == contact_from_home_page.last_name
    assert contact_from_edit_page.primary_address == contact_from_home_page.primary_address
    assert clear(contact_from_edit_page.primary_home_phone) == contact_from_home_page.primary_home_phone
    assert clear(contact_from_edit_page.work_phone) == contact_from_home_page.work_phone
    assert clear(contact_from_edit_page.mobile_phone) == contact_from_home_page.mobile_phone
    assert clear(contact_from_edit_page.secondary_home_phone) == contact_from_home_page.secondary_home_phone
    assert contact_from_edit_page.email1 == contact_from_home_page.email1
    assert contact_from_edit_page.email2 == contact_from_home_page.email2
    assert contact_from_edit_page.email3 == contact_from_home_page.email3

def clear(s):
    return re.sub("[- ()] ","",s)
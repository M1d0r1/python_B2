import random
import re
from model.contact import Contact

def test_verify_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    ind = random.randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_data_from_edit_page_by_index(ind)
    contact_from_home_page = app.contact.get_data_from_home_page_by_index(ind)
    assert clear_spaces(contact_from_edit_page.first_name) == contact_from_home_page.first_name
    assert clear_spaces(contact_from_edit_page.last_name) == contact_from_home_page.last_name
    assert clear_spaces(contact_from_edit_page.primary_address) == contact_from_home_page.primary_address
    assert contact_from_home_page.all_phones == merge_phones_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_home_page(contact_from_edit_page)


def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.primary_home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_home_phone]))))

def merge_emails_like_home_page(contact):
    return clear_spaces("\n".join(filter(lambda x: x is not None and clear(x) !="",[contact.email1, contact.email2, contact.email3])))

def merge_contact_primary_phones_like_view_page(contact):
    return merge_phones_like_view_page(contact.primary_home_phone, contact.mobile_phone, contact.work_phone)

def merge_primary_info_like_view_page(contact):
    return " ".join(filter(lambda x: x is not None and x != "", [contact.first_name, contact.middle_name, contact.last_name]))

def merge_phones_like_view_page(home, mobile, work):
    s = ""
    if (home is not None) and (clear(home) is not ""):
        s = "H: %s\n" % home
    if (mobile is not None) and (clear(mobile) is not ""):
        s = s + "M: %s\n" % mobile
    if (work is not None) and (clear(work) is not ""):
        s = s + "W: %s\n" % work
    return s

def clear(s):
    return re.sub("[- )(]","",s)

def clear_spaces(s):
    return re.sub(" \n","\n",re.sub(" +"," ",s))

def test_verify_phones_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    ind = random.randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_data_from_edit_page_by_index(ind)
    contact_from_view_page = app.contact.get_data_from_view_page_by_index(ind)
    assert merge_contact_primary_phones_like_view_page(contact_from_view_page) == merge_contact_primary_phones_like_view_page(contact_from_edit_page)

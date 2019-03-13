import random
from utils.formatstrings import FormatStrings
from model.contact import Contact


def test_verify_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    ind = random.randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_data_from_edit_page_by_index(ind)
    contact_from_home_page = app.contact.get_data_from_home_page_by_index(ind)
    assert FormatStrings.clear_spaces(contact_from_edit_page.first_name) == contact_from_home_page.first_name
    assert FormatStrings.clear_spaces(contact_from_edit_page.last_name) == contact_from_home_page.last_name
    assert FormatStrings.clear_spaces(contact_from_edit_page.primary_address) == contact_from_home_page.primary_address
    assert contact_from_home_page.all_phones == FormatStrings.merge_phones_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == FormatStrings.merge_emails_like_home_page(contact_from_edit_page)


def test_verify_phones_on_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    ind = random.randrange(app.contact.count())
    contact_from_edit_page = app.contact.get_data_from_edit_page_by_index(ind)
    contact_from_view_page = app.contact.get_data_from_view_page_by_index(ind)
    assert FormatStrings.merge_contact_primary_phones_like_view_page(
        contact_from_view_page) == FormatStrings.merge_contact_primary_phones_like_view_page(contact_from_edit_page)

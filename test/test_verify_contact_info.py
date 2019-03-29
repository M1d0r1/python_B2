from utils.formatstrings import FormatStrings
from model.contact import Contact


def test_verify_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact for verification"))
    db_list = sorted(db.get_contact_list(), key=Contact.id_or_max)
    home_page_list = []
    for ind in range(0, app.contact.count()):
        contact_from_home_page = app.contact.get_data_from_home_page_by_index(ind)
        home_page_list.append(contact_from_home_page)
    sorted_home_page_list = sorted(home_page_list, key=Contact.id_or_max)
    for ind in range(0, app.contact.count()):
        assert FormatStrings.clear_spaces(db_list[ind].first_name) == sorted_home_page_list[ind].first_name
        assert FormatStrings.clear_spaces(db_list[ind].last_name) == sorted_home_page_list[ind].last_name
        assert FormatStrings.clear_spaces(
            FormatStrings.clear_breaks(db_list[ind].primary_address)) == FormatStrings.clear_spaces(
            FormatStrings.clear_breaks(sorted_home_page_list[ind].primary_address))
        assert sorted_home_page_list[ind].all_phones == FormatStrings.merge_phones_like_home_page(db_list[ind])
        assert sorted_home_page_list[ind].all_emails == FormatStrings.merge_emails_like_home_page(db_list[ind])


def test_verify_phones_on_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact for verification"))
    db_list = sorted(db.get_contact_list(), key=Contact.id_or_max)
    view_page_list = []
    for contact in db_list:
        contact_from_view_page = app.contact.get_data_from_view_page_by_id(contact.id)
        view_page_list.append(contact_from_view_page)
    for ind in range(0, app.contact.count()):
        assert FormatStrings.merge_contact_primary_phones_like_view_page(
            db_list[ind]) == FormatStrings.merge_contact_primary_phones_like_view_page(view_page_list[ind])

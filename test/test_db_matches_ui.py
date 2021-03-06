from model.group import Group
from utils.formatstrings import FormatStrings
from model.contact import Contact
import allure

def test_verify_group_list(app, db):
    with allure.step("Given list of groups got from home page and list of groups got from db"):
        ui_list = app.group.get_group_list()
        db_list = db.get_group_list()
    with allure.step("Then the info in the lists is equal"):
        for i in range(0, len(db_list)):
            db_list[i] = db_list[i].clear()
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_verify_contact_info_on_home_page(app, db):
    with allure.step("Given list of contacts got from home page and list of contacts got from db"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="Contact for verification"))
        db_list = sorted(db.get_contact_list(), key=Contact.id_or_max)
        home_page_list = []
        for ind in range(0, app.contact.count()):
            contact_from_home_page = app.contact.get_data_from_home_page_by_index(ind)
            home_page_list.append(contact_from_home_page)
        sorted_home_page_list = sorted(home_page_list, key=Contact.id_or_max)
    with allure.step("Then the info in the lists is equal"):
        for ind in range(0, app.contact.count()):
            assert FormatStrings.clear_spaces(db_list[ind].first_name) == sorted_home_page_list[ind].first_name
            assert FormatStrings.clear_spaces(db_list[ind].last_name) == sorted_home_page_list[ind].last_name
            assert FormatStrings.clear_spaces(
                FormatStrings.clear_breaks(db_list[ind].primary_address)) == FormatStrings.clear_spaces(
                FormatStrings.clear_breaks(sorted_home_page_list[ind].primary_address))
            assert sorted_home_page_list[ind].all_phones == FormatStrings.merge_phones_like_home_page(db_list[ind])
            assert sorted_home_page_list[ind].all_emails == FormatStrings.merge_emails_like_home_page(db_list[ind])


def test_verify_contact_phones_on_view_page(app, db):
    with allure.step("Given list of groups got from view page and list of groups got from db"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="Contact for verification"))
        db_list = sorted(db.get_contact_list(), key=Contact.id_or_max)
        view_page_list = []
        for contact in db_list:
            contact_from_view_page = app.contact.get_data_from_view_page_by_id(contact.id)
            view_page_list.append(contact_from_view_page)
    with allure.step("Then the info in the lists is equal"):
        for ind in range(0, app.contact.count()):
            assert FormatStrings.merge_contact_primary_phones_like_view_page(
                db_list[ind]) == FormatStrings.merge_contact_primary_phones_like_view_page(view_page_list[ind])

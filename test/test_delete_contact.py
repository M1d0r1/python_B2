from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for deletion"))
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    app.open_start_page()
    app.wd.find_element_by_link_text("add new")
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

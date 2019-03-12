from model.contact import Contact
from random import randrange


def test_delete_contact(app):
  #for i in range (0,200):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for deletion"))
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    app.open_start_page()
    app.wd.find_element_by_link_text("add new")
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts

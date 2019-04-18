import random
from model.contact import Contact
from model.group import Group
import allure

def test_add_contact_in_group(app, db, orm, check_ui):
    with allure.step("If there are no groups create a group"):
        if len(orm.get_group_list()) == 0:
            app.group.create(Group(name="Group for adding contacts"))
    with allure.step("Given a list of contacts in a group"):
        groups = orm.get_group_list()
        group = random.choice(groups)
        old_contacts_in_group = orm.get_contacts_in_group(group)
    with allure.step("When adding a contact to group"):
        if len(orm.get_contacts_not_in_group(group)) == 0:
            app.contact.create(Contact(first_name="Contact for adding to group"))
        contact= random.choice(orm.get_contacts_not_in_group(group))
        app.contact.add_to_group(contact, group)
    with allure.step("Then new list of contacts in a group is equal to the old list with the added contact"):
        old_contacts_in_group.append(contact)
        new_contacts_in_group = orm.get_contacts_in_group(group)
        assert sorted(old_contacts_in_group, key = Contact.id_or_max) == sorted(new_contacts_in_group, key = Contact.id_or_max)


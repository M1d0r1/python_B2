import random
from model.contact import Contact
from model.group import Group
import allure


def test_remove_contact_from_group(app, db, orm, check_ui):
    with allure.step("If there are no groups create one"):
        if app.group.count() == 0:
            new_group = Group(name="Group for removing contacts")
            app.group.create(new_group)
    with allure.step("If there are no contacts create one"):
        if app.contact.count() == 0:
            new_contact = Contact(first_name="Contact for removing")
            app.contact.create(new_contact)
    with allure.step("If there are no groups with contacts add a contact to a group"):
        groups = orm.get_not_empty_group_list()
        if len(groups)== 0:
            group = random.choice(orm.get_group_list())
            contact = random.choice(orm.get_contacts_not_in_group(group))
            app.contact.add_to_group(contact, group)
            groups = orm.get_not_empty_group_list()
    with allure.step("Given a non-empty list of contacts in the group"):
        group = random.choice(groups)
        old_contacts_in_group = orm.get_contacts_in_group(group)
    with allure.step("When removing a contact from a group"):
        contact_to_remove = random.choice(old_contacts_in_group)
        app.contact.remove_from_group(contact_to_remove, group)
    with allure.step("Then the new list of contacts in the group is equal to the old one without the deleted contact"):
        old_contacts_in_group.remove(contact_to_remove)
        new_contacts_in_group = orm.get_contacts_in_group(group)
        assert sorted(old_contacts_in_group, key = Contact.id_or_max) == sorted(new_contacts_in_group, key = Contact.id_or_max)


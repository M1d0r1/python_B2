import random
from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(app, db, orm, check_ui):
    print("GROUPS: ", orm.get_group_list(), len(orm.get_group_list()))
    print("EMPTY GROUPS: ", orm.get_empty_group_list(), len(orm.get_empty_group_list()))
    print("NOT EMPTY GROUPS: ", orm.get_not_empty_group_list(), len(orm.get_not_empty_group_list()))
    if len(orm.get_group_list()) == len(orm.get_empty_group_list()):
        new_group = Group(name="Group for removing contacts")
        app.group.create(new_group)
        contact = random.choice(orm.get_contacts_not_in_group(new_group))
        app.contact.add_to_group(contact, new_group)
    groups = orm.get_not_empty_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    contact= random.choice(old_contacts_in_group)
    app.contact.remove_from_group(contact, group)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key = Contact.id_or_max) == sorted(new_contacts_in_group, key = Contact.id_or_max)


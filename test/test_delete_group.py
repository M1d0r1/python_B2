from model.group import Group
import random


def test_delete_group(app, db):
    # for index in range(1,101):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group for deletion"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups

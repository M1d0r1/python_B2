from model.group import Group
import random
from utils.randomdata import RandomData
import allure

def test_modify_group(app, db, check_ui):
    with allure.step("If there are no group create one"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Group for modification"))
    with allure.step("Given a list of groups and the data for modification"):
        old_groups = db.get_group_list()
        old_group = random.choice(old_groups)
        group = Group()
        # Prepare data
        group.name = "%s %s" % (old_group.name, RandomData.get_random_string())
        group.header = "%s %s" % (old_group.header, RandomData.get_random_string())
        group.footer = "%s %s" % (old_group.footer, RandomData.get_random_string())
        group.id = old_group.id
    with allure.step("When modifying the group"):
        app.group.modify_by_id(group.id, group)
    with allure.step("Then the new list of groups is equal to the old list with a modified group"):
        new_groups = db.get_group_list()
        old_groups.remove(old_group)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            for i in range(0, len(new_groups)):
                new_groups[i] = new_groups[i].clear()
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name(app, db, check_ui):
    with allure.step("If there are no groups create one"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Group for modification"))
    with allure.step("Given a list of groups"):
        old_groups = db.get_group_list()
        old_group = random.choice(old_groups)
        group = Group(name="Only name " + str(old_group.id))
        group.id = old_group.id
    with allure.step("When modifying only the name of the group"):
        app.group.modify_by_id(old_group.id, group)
    with allure.step("Then the new list of groups is equal to the old list with a modified group"):
        new_groups = db.get_group_list()
        old_groups.remove(old_group)
        old_groups.append(group.clear())
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            for i in range(0, len(new_groups)):
                new_groups[i] = new_groups[i].clear()
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

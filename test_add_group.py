# -*- coding: utf-8 -*-
import pytest
from group import Group
import unittest
import time
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
     app.login(admin="admin", password="secret")
     # Set the index in order to distinguish the created groups
     tmstp = str(time.time())
     ind = tmstp[13:15]
     app.create_group(Group(name="Group"+ind, header="Header"+ind, footer="Footer"+ind))
     app.logout()

    # def test_add_empty_group(self):
    #     wd = self.wd
    #     self.open_start_page(wd)
    #     self.login(wd, "admin", "secret")
    #     self.create_group(wd, Group(name="", header="", footer=""))
    #     self.navigate_to_groups(wd)
    #     self.logout(wd)


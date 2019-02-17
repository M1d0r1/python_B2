# -*- coding: utf-8 -*-
import pytest
from model.group import Group
import time
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
     app.session.login(admin="admin", password="secret")
     # Set the index in order to distinguish the created groups
     tmstp = str(time.time())
     ind = tmstp[13:15]
     app.group.create(Group(name="Group"+ind, header="Header"+ind, footer="Footer"+ind))
     app.session.logout()


def test_add_empty_group(app):
    app.session.login(admin="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


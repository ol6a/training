# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.fiz_contact import Fiz_contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_regfiz_zakaz(app):
    app.go_to_home()
    app.registration_fiz(Fiz_contact("мтест167", "мтест167", "мтест167", "m167@moi-uni.ru", "89213456789", "12345", "12345"))
    app.go_to_catalog()
    app.go_to_number_category()
    app.select_course()
    app.registration_order()
    app.payment_address()
    app.payment_address()
    app.oplata_kvit()
    app.confirm_order()
    app.logout()




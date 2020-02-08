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
    app.session.registration_fiz(Fiz_contact("мтест169", "мтест169", "мтест169", "m169@moi-uni.ru", "89213456789", "12345", "12345"))
    app.go_to_catalog()
    app.go_to_number_category()
    app.select_course()
    app.fizzakaz.registration_order()
    app.fizzakaz.payment_address()
    app.fizzakaz.payment_address()
    app.fizzakaz.oplata_kvit()
    app.fizzakaz.confirm_order()
    app.session.logout()




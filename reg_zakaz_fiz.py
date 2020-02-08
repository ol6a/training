# -*- coding: utf-8 -*-
import unittest
from application import Application
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from fiz_contact import Fiz_contact

class reg_zakaz_fiz (unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_regfiz_zakaz(self):

        self.app.go_to_home()
        self.app.registration_fiz(Fiz_contact("мтест164", "мтест164", "мтест164", "m164@moi-uni.ru", "89213456789", "12345", "12345"))
        self.app.go_to_catalog()
        self.app.go_to_number_category()
        self.app.select_course()
        self.app.registration_order()
        wd.find_element_by_id("button-payment-address").click()
        self.app.payment_address()
        self.app.oplata_kvit()
        self.app.confirm_order()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
     unittest.main()
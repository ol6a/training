# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from fiz_contact import Fiz_contact

class reg_zakaz_fiz (unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_regfiz_zakaz(self):
        wd = self.wd
        wd.get("https://test01.moi-uni.ru/")
        self.registration_fiz(Fiz_contact("мтест163", "мтест163", "мтест163", "m163@moi-uni.ru", "89213456789", "12345", "12345"))
        self.go_to_catalog()
        self.go_to_number_category()
        self.select_course()
        self.registration_order()
        wd.find_element_by_id("button-payment-address").click()
        self.payment_address()
        self.oplata_kvit()
        self.confirm_order()
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("(//a[contains(text(),'Выход')])[3]").click()

    def confirm_order(self):
        wd = self.wd
        wd.find_element_by_id("button-confirm").click()

    def oplata_kvit(self):
        wd = self.wd
        wd.find_element_by_link_text("скачать квитанцию").click()
        wd.find_element_by_id("button-payment-method").click()

    def payment_address(self):
        wd = self.wd
        wd.find_element_by_id("button-payment-address").click()

    def registration_order(self):
        wd = self.wd
        wd.find_element_by_link_text("Оформить заказ").click()

    def select_course(self):
        wd = self.wd
        wd.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def go_to_number_category(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/div[5]/div/div/div/a[7]/p").click()

    def go_to_catalog(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@id='osnovnoe-menu']/li[2]/a/span").click()

    def registration_fiz(self, fiz_contact):
        wd = self.wd
        wd.find_element_by_link_text("Регистрация").click()
        wd.find_element_by_id("input-lastname").click()
        wd.find_element_by_xpath("//fieldset[@id='account']/div[2]").click()
        wd.find_element_by_id("input-lastname").clear()
        wd.find_element_by_id("input-lastname").send_keys(fiz_contact.lastname)
        wd.find_element_by_id("input-firstname").click()
        wd.find_element_by_id("input-firstname").clear()
        wd.find_element_by_id("input-firstname").send_keys(fiz_contact.firstname)
        wd.find_element_by_id("input-middlename").click()
        wd.find_element_by_id("input-middlename").clear()
        wd.find_element_by_id("input-middlename").send_keys(fiz_contact.middlename)
        wd.find_element_by_id("input-email").click()
        wd.find_element_by_id("input-email").clear()
        wd.find_element_by_id("input-email").send_keys(fiz_contact.email)
        wd.find_element_by_id("input-telephone").click()
        wd.find_element_by_id("input-telephone").clear()
        wd.find_element_by_id("input-telephone").send_keys(fiz_contact.telephone)
        wd.find_element_by_id("input-password").click()
        wd.find_element_by_id("input-password").clear()
        wd.find_element_by_id("input-password").send_keys(fiz_contact.password)
        wd.find_element_by_id("input-confirm").click()
        wd.find_element_by_id("input-confirm").clear()
        wd.find_element_by_id("input-confirm").send_keys(fiz_contact.confirmpassword)
        wd.find_element_by_name("handle_agree").click()
        wd.find_element_by_xpath(u"//input[@value='Продолжить']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()



if __name__ == "__main__":
    unittest.main()

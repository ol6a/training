class SessionHelper:
    def __init__(self, app):
        self.app=app
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//a[contains(text(),'Выход')])[3]").click()
    def registration_fiz(self, fiz_contact):
        wd = self.app.wd
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
        wd.find_element_by_xpath("//input[@value='Продолжить']").click()
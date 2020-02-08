from fixture.session import SessionHelper
from fixture.fizzakaz import FizZakazHelper
from selenium import webdriver

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.fizzakaz = FizZakazHelper(self)

    def go_to_home(self):
        wd = self.wd
        wd.get("https://test01.moi-uni.ru/")

    def select_course(self):
        wd = self.wd
        wd.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def go_to_number_category(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/div[5]/div/div/div/a[7]/p").click()

    def go_to_catalog(self):
        wd = self.wd
        wd.find_element_by_xpath("//ul[@id='osnovnoe-menu']/li[2]/a/span").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
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


    def destroy(self):
        self.wd.quit()




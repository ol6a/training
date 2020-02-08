class FizZakazHelper:
    def __init__(self, app):
        self.app=app

    def registration_order(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Оформить заказ").click()

    def payment_address(self):
        wd = self.app.wd
        wd.find_element_by_id("button-payment-address").click()

    def oplata_kvit(self):
        wd = self.app.wd
        wd.find_element_by_link_text("скачать квитанцию").click()
        wd.find_element_by_id("button-payment-method").click()

    def confirm_order(self):
        wd = self.app.wd
        wd.find_element_by_id("button-confirm").click()
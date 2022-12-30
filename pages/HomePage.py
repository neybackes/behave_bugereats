from base.BasePage import *


class HomePage(BasePage):

    #validador de pagina
    

    def __init__(self, driver):
        super().__init__(driver)  

    def get_title(self):
        return super().get_title()
   
    def get_element(self, locator):
        return super().get_element(locator)
    
    def validate_value(self):
        pass
    
    def wait_for_element(self, locator, expected_message, timeout=10):
        super().wait_for_element(locator, expected_message, timeout)

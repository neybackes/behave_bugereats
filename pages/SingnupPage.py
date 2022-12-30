from base.BasePage import *


class SignupPage(BasePage, Locator):
    
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

    
    def fill_up_registration_form(self, delivery, cpf=False):
        fake = Faker()
        cpf = '12345678911'        
        if cpf == True:
            cpf = '123456789AA'
        
        self.get_element(Locator.input_name).send_keys(fake.name())
        self.get_element(Locator.input_cpf).send_keys(cpf)
        self.get_element(Locator.input_email).send_keys(fake.email())
        self.get_element(Locator.input_whatsapp).send_keys(fake.phone_number())

        self.get_element(Locator.input_postal_code).send_keys('04534011')
        self.get_element(Locator.button_search).click()

        time.sleep(10)

        self.get_element(Locator.input_address_number).send_keys('123')
        self.get_element(Locator.input_details).send_keys('casa')

        address = self.get_element(Locator.input_address).get_attribute("value")
        district = self.get_element(Locator.input_district).get_attribute("value")
        city_uf = self.get_element(Locator.input_city).get_attribute("value")

        assert address == 'Rua Joaquim Floriano', f'Expected message: Rua Joaquim Floriano, actual message: {address}'
        assert district == 'Itaim Bibi', f'Expected message: Itaim Bibi, actual message: {district}'
        assert city_uf == 'São Paulo/SP', f'Expected message: São Paulo/SP, actual message: {city_uf}'
        
        self.get_element((Locator.input_delivery_method, delivery)).click()
        self.get_element(Locator.input_upload_file).send_keys(Locator.upload_file)

            
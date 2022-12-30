import abc
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
 





class Locator(object):

    
    home_title = "Buger Eats"
    home_text_validate = (By.CSS_SELECTOR,'#root main h1')

    signup_home_button = (By.CSS_SELECTOR,'a[href="/deliver"')
    signup_text_validate = (By.CSS_SELECTOR,'#page-deliver form h1')


    #inserindo os dados do deliver
    input_name = (By.CSS_SELECTOR, 'input[name="fullName"]')
    input_cpf = (By.CSS_SELECTOR, 'input[name="cpf"]')
    input_email = (By.CSS_SELECTOR, 'input[name="email"]')
    input_whatsapp = (By.CSS_SELECTOR, 'input[name="whatsapp"]')

    #inserindo o postalCode
    input_postal_code = (By.CSS_SELECTOR, 'input[name="postalcode"]')
    button_search = (By.CSS_SELECTOR, 'div[class="field"] input[type="button"]')

    #inserindo o number e complemento
    input_address_number = (By.CSS_SELECTOR, 'input[name="address-number"]')
    input_details = (By.CSS_SELECTOR, 'input[name="address-details"]')

    #validando a busca do postalCode
    input_address = (By.CSS_SELECTOR, 'input[name="address"]')
    input_district = (By.CSS_SELECTOR, 'input[name="district"]')
    input_city = (By.CSS_SELECTOR, 'input[name="city-uf"]')

    #metodo de entrega
    #how can in put a variable inside a locator?

    delivery_method = ['img[alt="Moto"]', 'img[alt="Van/Carro"]', 'img[alt="Bicicleta"]']
    input_delivery_method = By.CSS_SELECTOR

    #upload de arquivo
    upload_file = '/home/neybackes/Documentos/behave_bugereats/base/resources/cnh-digital.jpg'
    input_upload_file = (By.CSS_SELECTOR, 'input[type="file"]')

    #subimissão do formulario
    button_submit = (By.CSS_SELECTOR, 'button[type="submit"]')

    modal_message = (By.CSS_SELECTOR, '.swal2-container .swal2-html-container')

    alert_error = (By.CLASS_NAME, '.alert-error')


    

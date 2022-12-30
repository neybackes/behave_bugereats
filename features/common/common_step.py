from behave import *
from base.BasePage import *
from pages.SingnupPage import SignupPage
from pages.HomePage import HomePage


locator = Locator()

@given('"Home Page"')
def access_home_page(context):
    # code to access the home page
    context.driver.get('https://buger-eats-qa.vercel.app/')
    
@then('\'Validar titulo home\'')
def valdiate_home_title(context):
    context.home_page = HomePage(context.driver) 
    title = context.home_page.get_title()
    assert title == "Buger Eats", f'Expected title: "Buger Eats", actual title: {title}'
    
@when(u'"Cadastra-se para fazer entregas"')
def acess_singnup_page(context):
    context.signup_page = SignupPage(context.driver)    
    context.signup_page.get_element(locator.signup_home_button).click()

@then(u'\'Validar pagina de cadastro\'')
def validate_register_page(context):       
    expected_message = "Cadastre-se para\nfazer entregas"
    actual_message = context.signup_page.get_element(locator.signup_text_validate).text
    assert actual_message == expected_message, f'Expected message: {expected_message}, actual message: {actual_message}'


    
from behave import *
from common.common_step import *
from pages.SingnupPage import SignupPage
from base.BasePage import Locator

locator = Locator()


@given(u'que eu estou na pagina "Home"')
def step_impl(context):
    access_home_page(context)
    valdiate_home_title(context)
    
@when(u'eu clico em "Cadastra-se para fazer entregas"')
def step_impl(context):
    context.signup_page = SignupPage(context.driver)
    acess_singnup_page(context)

@then(u'eu devo ver a pagina de cadastro')
def step_impl(context):       
    validate_register_page(context)

@given(u'eu estou na pagina ""Cadastra-se para fazer entregas"')
def step_impl(context):
    context.signup_page = SignupPage(context.driver)
    access_home_page(context)
    acess_singnup_page(context)
    validate_register_page(context)


@when(u'eu preencho o cadastro')
def step_impl(context):
   context.signup_page.fill_up_registration_form(locator.delivery_method[0])
   

@then(u'eu clico em  "Cadastra-se para fazer entregas"')
def step_impl(context):
    context.signup_page.get_element(locator.button_submit).click()

    
@then(u'eu devo ver uma mensagem de sucesso')
def step_impl(context):
    expected_message = "Recebemos os seus dados. Fique de olho na sua caixa de email, pois e em breve retornamos o contato."
    context.signup_page.wait_for_element(locator.modal_message, expected_message)
from behave import *
from common.common_step import *
from pages.HomePage import HomePage
from base.BasePage import Locator


locator = Locator()

@given(u'eu acessei a pagina "home page"')
def step_impl(context):
    access_home_page(context)         
    
@when(u'eu vejo a mensagem "Seja um parceiro entregador pela Buger Eats"')
def step_impl(context):
    context.home_page = HomePage(context.driver)  
    expected_message = "Seja um parceiro entregador pela Buger Eats"
    actual_message = context.home_page.get_element(locator.home_text_validate).text
    assert actual_message == expected_message, f'Expected message: {expected_message}, actual message: {actual_message}'

@then('o titulo da pagina deve ser "Buger Eats"')
def step_impl(context):
    valdiate_home_title(context)
from behave import *
from selenium.webdriver.common.by import By




@given(u'eu acessei a documentacao do Behave')
def step_impl(context):
    context.driver.get("https://behave.readthedocs.io/en/latest/")


@then(u'o titulo da pagina deve ser "{text}"')
def step_impl(context, text):
    actual_title = context.driver.title
    expected_title = text
    assert actual_title == expected_title, f"Expected title to be {expected_title} but got {actual_title}"   


@then(u'eu devo ver a mensagem "{text}"')
def step_impl(context, text):
    actual_message = context.driver.find_element(By.CSS_SELECTOR, '#welcome-to-behave h1').text
    expected_message = text
    assert actual_message == expected_message, f"Expected message to be {expected_message} but got {actual_message}"
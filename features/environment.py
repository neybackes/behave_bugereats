from selenium import webdriver
import os

def before_all(context):
    # code to run before all scenarios
    # create a webdriver instance
    context.driver = webdriver.Chrome()
    context.driver.set_page_load_timeout(30)
    context.driver.maximize_window()
    context.driver.set_script_timeout(30)

def before_scenario(context, scenario):
    
    context.driver.delete_all_cookies()

def after_scenario(context, scenario):
    
    if scenario.status == "passed":        
        if not os.path.exists('reports'):
            os.makedirs('reports')        
        context.driver.save_screenshot(f'reports/{scenario.name}.png')
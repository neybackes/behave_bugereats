from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.set_page_load_timeout(30)
    context.driver.maximize_window()
    context.driver.set_script_timeout(30)

def after_all(context):    
    pass

def before_scenario(context, scenario):   
    pass

def after_scenario(context, scenario):
    # code to run after each scenario
    context.driver.quit()

def before_feature(context, feature):
    # code to run before each feature
    pass
def after_feature(context, feature):
    # code to run after each feature
    pass

def before_step(context, feature):
    # code to run before each feature
    pass
def after_step(context, feature):
    # code to run after each feature
    pass



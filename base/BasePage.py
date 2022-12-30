from base.utilities import *


class BasePage(abc.ABC):
    def __init__(self, driver):
        self.driver = driver    

    
    @abc.abstractmethod
    def get_title(self):
        return self.driver.title
    
    @abc.abstractmethod   
    def get_element(self, locator):
        return self.driver.find_element(*locator)
    @abc.abstractmethod
    def validate_value(self, locator, expected_value):
        pass

    @abc.abstractmethod
    def wait_for_element(self,locator, expected_message, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            )
            # Get the text of the element
        element_text = self.driver.find_element(*locator).text
        # Compare the element text to the expected text        
        assert element_text ==  expected_message, f'Expected message: {expected_message}, actual message: {element_text}'
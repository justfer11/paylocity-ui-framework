from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_visible(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_clickable(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_text_present(driver, locator, text, timeout):
    return WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

def wait_invisible(driver, locator, timeout):
    return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located(locator))

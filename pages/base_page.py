from selenium.webdriver.common.by import By
from utils.waits import wait_visible, wait_clickable
from config.settings import EXPLICIT_WAIT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_time = EXPLICIT_WAIT

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return wait_visible(self.driver, (by, value), self.wait_time)
    
    def click(self, by, value):
        el = wait_clickable(self.driver, (by, value), self.wait_time)
        el.click()
        return el
    
    def type(self, by, value, text, clear=True):
        el = self.find(by, value)
        if clear:
            el.clear()
        el.send_keys(text)
        return el
    
    def get_text(self, by, value):
        return self.find(by, value).text
    
    def exists(self, by, value):
        try:
            self.find(by, value)
            return True
        except Exception:
            return False
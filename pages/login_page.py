from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "Username")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit'].btn.btn-primary")

    def login(self, username, password):
        self.type(*self.USERNAME_INPUT, username)
        self.type(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)
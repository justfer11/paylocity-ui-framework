from behave import given, when
from pages.login_page import LoginPage
from config.settings import get_credentials

@given('I am logged in as "{alias}"')
def step_login_with_alias(context, alias):
    username, password = get_credentials(alias)
    context.driver.get(context.base_url)
    context.login_page = LoginPage(context.driver)
    context.login_page.login(username, password)

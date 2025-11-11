from utils.browser import create_driver
from config.settings import BASE_URL, EXPLICIT_WAIT
from pages.benefits_dashboard_page import BenefitsDashboardPage
from pages.login_page import LoginPage

def before_scenario(context, scenario):
    context.driver = create_driver()
    context.driver.implicitly_wait(EXPLICIT_WAIT)
    context.base_url = BASE_URL
    context.login_page = LoginPage(context.driver)
    context.page = BenefitsDashboardPage(context.driver)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()

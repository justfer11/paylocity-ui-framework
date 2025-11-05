from behave import given, then
from utils.assertions import assert_true

@given("I am on the Benefits Dashboard page")
def step_open_dashboard(context):

    assert_true(context.page.exists(*context.page.TABLE), "Dashboard table not visible")

@then("I should see the Benefits Dashboard page")
def step_verify_dashboard(context):
    assert_true(context.page.exists(*context.page.TABLE), "Dashboard table not visible")

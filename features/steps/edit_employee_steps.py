from behave import given, when, then
from utils.assertions import assert_true
import uuid

@then('the employee "{first}" "{last}" exists in the table')
def step_employee_exists(context, first, last):
    context.page.wait_for_employee_in_table(first, last)
    data = context.page.find_employee_in_table(first, last)
    assert_true(data is not None, f"Employee not found: {first} {last}")
    context.current_employee_data = data

@when('I select the Action Edit for "{first}" "{last}"')
def step_select_edit(context, first, last):
    context.page.click_edit_employee(first, last)

@when('I update the employee details:')
def step_update_employee(context):
    row = context.table.rows[0]
    context.firstName = row['firstName'].strip()
    context.lastName = row['lastName'].strip()
    context.dependents = int(row["dependents"].strip())
    context.page.fill_employee_form(context.firstName, context.lastName, context.dependents)

@when("I update the employee") 
def step_update_employee(context):
    context.page.update_employee()

@then('I select the Action Delete for "{first}" "{last}"')
def step_select_delete(context, first, last):
    context.page.click_delete_employee(first, last)

@then('the employee "{first}" "{last}" should not exist in the table')
def step_employee_not_exists(context, first, last):
    data = context.page.find_employee_in_table(first, last)
    assert_true(data is None, f"Employee still found in table: {first} {last}")

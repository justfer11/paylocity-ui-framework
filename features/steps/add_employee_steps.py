from behave import when, then
from utils.assertions import assert_true, assert_number_close
from utils.data import parse_currency

@when("I select Add Employee")
def step_click_add_employee(context):
    context.page.click_add_employee()

@when("I enter employee details:")
def step_enter_employee_details(context):
    row = context.table.rows[0]
    context.firstName = row['firstName'] 
    context.lastName = row['lastName']
    context.dependents = int(row["dependents"])
    context.page.fill_employee_form(context.firstName, context.lastName, context.dependents)

@when("I save the employee")
def step_save_employee(context):
    context.page.save_employee()

@then('I should see the employee "{first}" "{last}" in the table')
def step_verify_employee_in_table(context, first, last):
    context.page.wait_for_employee_in_table(first, last)
    data = context.page.find_employee_in_table(first, last)
    assert_true(data is not None, f"Employee not found: {first} {last}")
    context.current_employee_data = data

@then('the benefits cost calculations for "{first}" "{last}" should be correct')
def step_verify_benefit_calc(context, first, last):
    context.page.wait_for_employee_in_table(first, last)
    data = context.page.find_employee_in_table(first, last)
    assert_true(data is not None, f"Employee row not found for calc verification: {first} {last}")

    salary_text = data["salary"]
    gross_text = data["gross"]
    benefits_text = data["benefits"]
    net_text = data["net"]

    annual_salary = parse_currency(salary_text)
    gross_pay = parse_currency(gross_text)
    benefits_cost = parse_currency(benefits_text)
    net_pay = parse_currency(net_text)

    periods = round(annual_salary / gross_pay) if gross_pay else 26
    base = 1000.00
    per_dep = 500.00
    annual_benefits = base + per_dep * context.dependents
    period_benefits = annual_benefits / periods
    expected_net = gross_pay - period_benefits

    assert_number_close(
        benefits_cost, round(period_benefits, 2), tolerance=0.5,
        msg=f"Benefits cost mismatch. Expected ~{round(period_benefits,2)}, got {benefits_cost}"
    )
    assert_number_close(
        net_pay, round(expected_net, 2), tolerance=0.5,
        msg=f"Net pay mismatch. Expected ~{round(expected_net,2)}, got {net_pay}"
    )


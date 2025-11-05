from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page import BasePage
from utils.waits import *

class BenefitsDashboardPage(BasePage):
    ADD_EMPLOYEE_BTN = (By.ID, "add")

    # Form fields
    FORM_WINDOW = (By.ID, "employeeModal")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    DEPENDENTS_INPUT = (By.ID, "dependants")
    ADD_BTN = (By.ID, "addEmployee")
    UPDATE_BTN = (By.ID, "updateEmployee")

    # Employee table
    TABLE = (By.ID, "employeesTable")
    ROWS = (By.CSS_SELECTOR, "#employeesTable tbody tr")
    HEADER = (By.CSS_SELECTOR, "#employeesTable thead tr th")

    COL_ID         = 0
    COL_FIRSTNAME  = 1
    COL_LASTNAME   = 2
    COL_DEPENDENTS = 3
    COL_SALARY     = 4
    COL_GROSS      = 5
    COL_BENEFITS   = 6
    COL_NET        = 7
    COL_ACTIONS    = 8

    ACTION_EDIT_ICON = (By.CSS_SELECTOR, ".fa-edit")
    ACTION_DELETE_ICON = (By.CSS_SELECTOR, ".fas.fa-times")

    DELETE_MODAL = (By.ID, "deleteModal")
    DELETE_BTN = (By.ID, "deleteEmployee")


    def click_add_employee(self):
        el = wait_clickable(self.driver, self.ADD_EMPLOYEE_BTN, self.wait_time)
        el.click()
        return el
    
    def fill_employee_form(self, first, last, dependents):
        wait_visible(self.driver, self.FORM_WINDOW, self.wait_time)
        wait_visible(self.driver, self.FIRST_NAME_INPUT, self.wait_time)
        self.type(*self.FIRST_NAME_INPUT, first)
        self.type(*self.LAST_NAME_INPUT, last)
        self.type(*self.DEPENDENTS_INPUT, str(dependents))

    def save_employee(self):
        self.click(*self.ADD_BTN)
        wait_invisible(self.driver, self.FORM_WINDOW, self.wait_time)
    
    def update_employee(self):
        self.click(*self.UPDATE_BTN)
        wait_invisible(self.driver, self.FORM_WINDOW, self.wait_time)

    def get_rows(self):
        wait_visible(self.driver, self.TABLE, self.wait_time)
        table = self.find(*self.TABLE)
        return table.find_elements(*self.ROWS)
    
    def parse_row(self, row_el):
        cells = row_el.find_elements(By.TAG_NAME, "td")
        if len(cells) < 9:
            return {}
        return {
            "id": cells[self.COL_ID].text.strip(),
            "firstName": cells[self.COL_FIRSTNAME].text.strip(),
            "lastName": cells[self.COL_LASTNAME].text.strip(),
            "dependents": int(cells[self.COL_DEPENDENTS].text.strip()),
            "salary": cells[self.COL_SALARY].text.strip(),
            "gross": cells[self.COL_GROSS].text.strip(),
            "benefits": cells[self.COL_BENEFITS].text.strip(),
            "net": cells[self.COL_NET].text.strip(),
        } 
      
    
    def find_employee_in_table(self, first, last):
        for attempt in range(3):  # retry a few times in case of staleness
            try:
                for row in self.get_rows():
                    data = self.parse_row(row)
                    if data.get("firstName") == first and data.get("lastName") == last:
                        return data
                return None
            except StaleElementReferenceException:
                continue
        return None


    
    def click_edit_employee(self, first, last):
        for row in self.get_rows():
            try:
                data = self.parse_row(row)
                if data.get("firstName") == first and data.get("lastName") == last:
                    row.find_element(*self.ACTION_EDIT_ICON).click()
                    return
            except StaleElementReferenceException:
                continue
        raise AssertionError(f"Employee {first} {last} not found for edit")

    
    def wait_for_employee_in_table(self, first, last):
        WebDriverWait(self.driver, self.wait_time).until(
            lambda d: self.find_employee_in_table(first, last) is not None,
            message=f"Employee not found in table: {first} {last}"
        )
    
    
    def click_delete_employee(self, first, last):
        for row in self.get_rows():
            try:
                data = self.parse_row(row)
                if data.get("firstName") == first and data.get("lastName") == last:
                    row.find_element(*self.ACTION_DELETE_ICON).click()
                    wait_visible(self.driver, self.DELETE_MODAL, self.wait_time)
                    el = wait_clickable(self.driver, self.DELETE_BTN, self.wait_time)
                    el.click()
                    WebDriverWait(self.driver, self.wait_time).until(
                        lambda d: self.find_employee_in_table(first, last) is None,
                        message=f"Employee {first} {last} still present after delete"
                    )
                    return
            except StaleElementReferenceException:
                continue
        raise AssertionError(f"Employee {first} {last} not found for delete")
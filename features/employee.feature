Feature: Employee management on Benefits Dashboard
As an Employer
I want to input my employee data
So that I can get a preview of benefits costs

Background:
    Given I am logged in as "testuser"
    Then I should see the Benefits Dashboard page

Scenario: Add Employee
    When I select Add Employee
    And I enter employee details:
        | firstName | lastName | dependents |
        | Alice    | Harper   | 2         |
    And I save the employee
    Then I should see the employee "Alice" "Harper" in the table
    And the benefits cost calculations for "Alice" "Harper" should be correct

Scenario: Edit Employee
    #When I select Add Employee
    #And I enter employee details:
    #    | firstName | lastName | dependents |
    #    | Peter    | Pan   | 2         |
    #And I save the employee
    Then the employee "Alice" "Harper" exists in the table
    When I select the Action Edit for "Alice" "Harper"
    And I update the employee details:
        | firstName | lastName | dependents |
        | Robin    | Hood   | 4         |
    And I update the employee
    Then I should see the employee "Robin" "Hood" in the table
    And the benefits cost calculations for "Robin" "Hood" should be correct

Scenario Outline: Delete Employee
    Then the employee "<first>" "<last>" exists in the table
    And I select the Action Delete for "<first>" "<last>"
    Then the employee "<first>" "<last>" should not exist in the table

    Examples:
      | first   | last   | 
      | Robin   | Hood   | 
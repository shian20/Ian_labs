Feature: dividing two numbers
  
  Scenario: when dividing two integers
    Given two valid non zero integers
    When dividing the integers
    Then it should result to another integer
    
  Scenario: when dividing two integers
    Given zero to integers
    When dividing zero to the integers
    Then it should result to zero
    
  Scenario: when dividing two integers
    Given zero to zero
    When dividing the zero to zero
    Then it should result to undefined
    

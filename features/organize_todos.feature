Feature: Organize/Manage/View todos effectively

  As a user,
  I want to manage my todos effectively
  So that I can organize my tasks easily

  Scenario: Add a new todo
    Given I am on the Todos page
    When I type "Read and write work emails" in the input field and press Enter
    Then the todo "Read and write work emails" should appear in the list

  Scenario: Edit an existing todo
    Given I am on the Todos page
    And I have a todo "draft new sales document"
    When I double-click on "draft new sales document" and change the text to "pay monthly bills"
    And I press "Enter"
    Then the todo should be updated to "pay monthly bills"

  Scenario: Cancel editing a todo
    Given I am on the Todos page
    And I have a todo "daily standup meet"
    When I double-click on "daily standup meet" and leave the input field empty
    And I press "Tab"
    Then the todo "daily standup meet" should remain unchanged

  Scenario: Mark a todo as completed
    Given I am on the Todos page
    And I have a todo "attend bug triage"
    When I click the checkbox next to todo lists
         | todo_text     |
         | attend bug triage |
    Then the todo "attend bug triage" should be marked as completed


  Scenario: Mark a completed todo as incomplete
    Given I am on the Todos page
    And I have a todo "file Iras submission"
    When I have a completed todo and select all as "Yes"
    And I click the checkbox next to todo lists
         | todo_text     |
         | file Iras submission |
    Then the todo "file Iras submission" should be marked as not completed

  Scenario: Delete a todo
    Given I am on the Todos page
    Given I have a todo "Read and write work emails"
    When I click the delete button next to "Read and write work emails"
    Then the todo "Read and write work emails" should be removed from the list

    Scenario: View all todos
    Given I am on the Todos page
    And I have a todo below todo list
      | todo_text     |
      | Read and write work emails |
      | clear the bins      |
      | workout       |
    When I click on the "Completed" filter
    And I click on the "All" filter
    Then I should see all todos including
      | todo_text     |
      | Read and write work emails |
      | clear the bins      |
      | workout       |
    And I should see count of todo as below
     | text_count     |
     | 3 items left! |

  Scenario: View active and completed todos
    Given I am on the Todos page
    And I have a todo below todo list
      | todo_text     |
      | call Johnny karky       |
      | draft a new homepage      |
      | daily standup meet       |
    When I click on the "Completed" filter
    Then I should see count of todo as below
     | text_count     |
     | 3 items left! |
    When I click on the "Active" filter
    Then I should see count of todo as below
     | text_count     |
     | 3 items left! |

  Scenario: View mixed of all, active and completed todos
    Given I am on the Todos page
    And I have a todo below todo list
      | todo_text     |
      | file Iras submission       |
      | pay monthly bills      |
      | attend bug triage       |
    When I click the checkbox next to todo lists
      | todo_text     |
      | file Iras submission       |
      | attend bug triage       |
    And I click on the "Active" filter
    Then I should see count of todo as below
     | text_count     |
     | 1 item left! |
    When I click on the "All" filter
    And I click the checkbox next to todo lists
         | todo_text     |
         | file Iras submission |
    And I click on the "Completed" filter
    Then I should see count of todo as below
     | text_count     |
     | 2 items left! |
    When I click the checkbox next to todo lists
         | todo_text     |
         | attend bug triage |
    And I click on the "All" filter
    Then I should see count of todo as below
     | text_count     |
     | 3 items left! |

  Scenario: View all todo list of make it 2 completed and revert all back active
    Given I am on the Todos page
    And I have a todo below todo list
      | todo_text     |
      | call Johnny Memon       |
      | Cycling      |
      | Jogging       |
      | Bike ride       |
    When I click the checkbox next to todo lists
     | todo_text     |
     | Cycling |
     | Bike ride |
    And I click on the "Active" filter
    Then I should see count of todo as below
     | text_count     |
     | 2 items left! |
    When I click on the "All" filter
    When I click the checkbox next to todo lists
     | todo_text     |
     | Cycling |
     | Bike ride |
    Then I should see count of todo as below
     | text_count     |
     | 4 items left! |

 Scenario: Completing some of the todos and try clearing completed todos
    Given I am on the Todos page
    And I have a todo below todo list
      | todo_text     |
      | Running       |
      | Cycling      |
      | Jogging       |
      | Bike ride       |
      | Long Drive       |
    When I click the checkbox next to todo lists
     | todo_text     |
     | Cycling |
     | Bike ride |
     | Running |
    And I click on Clear completed
    Then I should see count of todo as below
     | text_count     |
     | 2 items left! |
    Given I have a todo below todo list
     | todo_text     |
      | Speed Walking       |
    When I click on the "Completed" filter
    And I click on the "All" filter
    Then I should see count of todo as below
     | text_count     |
     | 3 items left! |

  Scenario: Mixed of todos active and Completed filer them based on action
    Given I am on the Todos page
    And I have a todo below todo list
      | todo_text     |
      | Read and write work emails      |
      | file Iras submission       |
      | pay monthly bills       |
      | clear the bins       |
      | workout       |
    When I click the checkbox next to todo lists
     | todo_text     |
     | clear the bins       |
      | file Iras submission        |
    Then I should see count of "Completed" as "2"
    And I should see count of "Active" as "3"

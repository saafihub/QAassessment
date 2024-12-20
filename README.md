## <u>About</u>
Technical Assessment : Playwright+Python

This Playwright-based automation framework is structured using the Page Object Model (POM) and Playwright features. It is designed to accommodate multiple types of tests—API, UI functionality, with BDD Style within a single framework. The framework is built with scalability and extensibility in mind to add more test types with enhanced maintainability, reusability and also by separating concerns (e.g., test logic, page objects, and test data), the framework makes it easier to manage and scale as the application grows.

In this Automation framework, Covered user story derived with 12 Scenarios through comprehensive End-to-End (E2E) testing. This approach integrated UI layers, ensuring a robust assessment of  application’s functionality. 

This Framework is Scalable to combine various testing methodologies not only to ensure complete coverage of user requirements also improved the clarity and communication of test cases among stakeholders. This holistic approach significantly contributes to delivering a high-quality product that aligns with user expectations.

## <u>Automated Testing Framework Design</u>
1.	<u>Page Object Model (POM)</u>: 
        Each UI component and page flow are encapsulated in a separate class, reducing duplication and ensuring reusable and maintainable code. This structure enhances readability and scalability of test cases.
2.	<u>BDD Implementation</u>: 
         Select scenarios are implemented with BDD syntax, enhancing communication with non-technical stakeholders.
3.	<u>Test Data Management</u>: 
         Dynamic and static test data configurations are included to support test scenarios, can able to use external files and environment-specific configurations.
4.	<u>Reporting</u>: 
         Detailed test execution reports with screenshots and logs for failed steps are generated, aiding in faster debugging and resolution.

## <u>Test Architecture and Tools</u>
1.	<u>Tool & Language</u>: Playwright(UI) with Python [Can also acheive with Selenium, Cypress etc]
2.	<u>Design Pattern</u>: Page Object Model (POM)
3.	<u>Testing Framework(Hybrid)</u>: BDD Structured using Playwright’s Cucumber-style syntax.
4.	<u>Continuous Integration</u>: Jenkins/GitHub Actions (Can Integrate)

## <u>Why Playwright?</u>
Playwright over selenium for faster, more reliable test execution with built-in features like automatic waiting, cross-browser consistency, and modern web and api support. Playwright simplifies test writing and offers better handling of complex web applications, while Selenium can be slower and requires more manual setup and synchronization.


## Framework Structure
      ├── features      # feature files
      ├── pages         # Page Object Model (POM) classes
      ├── steps         # step definition files
      ├── logs          # generate test logs 
      ├── reports       # generated reports etc
      ├── utils         # Utility classes (e.g., logger etc)
      config.json       # configuration files
      behave.ini        # init files
      environment.py    # application hooks
      README.md         # Instruction file.
      requirement.txt   # install dependencies
      
   

## Prerequisites
   ```
   Install Python 3.10 or higher(3.11(recommended)).
   Ensure python installed correctly
   python --version
   ```
1. Clone the repository to your local machine:  `QAassessment`.

   ```
   git clone https://github.com/saafihub/QAassessment.git
   cd QAassessment
   ```
2. Build the Project(Steps).
   ```
   Once done with python installation follow the below steps
       1. pip install virtualenv
       2. To isolate virtual environment, Goto ‘QAassessment’> Type Command: ‘py -3.11 -m venv qa_assess_tests’
       3. To get isolated environment, Go to folder ‘qa_assess_tests>Scripts’ and Type: ‘activate’
       4. Go back to root folder ‘QAassessment’
       5. To install all necessary packages, need to run this requirement file, Type: ‘pip install -r requirements.txt’
   ```
   
5. Run tests.

   ```
   1. # Run ui tests and generate allure reports[regenerated on "./allure-results"].
   To run tests --> behave --format allure_behave.formatter:AllureFormatter --outfile ./allure-results
   
   2. # Run ui tests and generate junit reports [junit report regenerated on "./reports"].
   To run tests --> behave --junit
 
 
   ```
6. View reports and logs.
   ```
    1. Check Allure report : allure serve ./allure-results
   
    2. Check Junit report : junit2html ./reports/TESTS-features.organize_todos.xml ./reports/testReport.html

    ```

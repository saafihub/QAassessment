## About
Technical Challenge : Playwright(UI)+Python

This Playwright-based automation framework is structured using the Page Object Model (POM) and Playwright features. It is designed to accommodate multiple types of tests—API, UI functionality, with BDD Style within a single framework. The framework is built with scalability and extensibility in mind to add more test types with enhanced maintainability, reusability and also by separating concerns (e.g., test logic, page objects, and test data), the framework makes it easier to manage and scale as the application grows.

In this Automation framework, Covered 12 Scenarios through comprehensive End-to-End (E2E) testing. This approach integrated functionality of UI layers, ensuring a robust assessment of  application’s functionality and performance. 

By combining various testing methodologies not only ensured complete coverage of user requirements also improved the clarity and communication of test cases among stakeholders. This holistic approach significantly contributes to delivering a high-quality product that aligns with user expectations.

For More Info : Automation Test Strategy document.docx

```
Why Playwright?
Playwright over selenium for faster, more reliable test execution with built-in features like automatic waiting, cross-browser consistency, and modern web and api support. Playwright simplifies test writing and offers better handling of complex web applications, while Selenium can be slower and requires more manual setup and synchronization.
```

## Framework Structure
      ├── features      # feature files
      ├── pages         # Page Object Model (POM) classes
      ├── steps         # step definition files
      ├── reports       # generated class files, reports etc
      ├── utils         # Utility classes (e.g., logger etc)
      config.json       # configuration files
      behave.ini        # init files
      environment.py    # application hooks
      README.md         # Instruction file.
      requirement.txt   # install dependencies
      
   

## Prerequisites
   ```
   Install Python 3.10 or higher(3.11).
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
   Once done with above steps then continue in terminal
       1. pip install virtualenv
       2. To isolate virtual environment, Goto ‘QAassessment’> Type Command: ‘py -3.11 -m venv qa_assess_tests’
       3. To get isolated environment, Go to folder ‘qa_assess_tests>Scripts’ and Type: ‘activate’
       4. Go back to root folder ‘QAassessment’
       6. To install all necessary packages, need to run the sample tests, Type: ‘pip install -r requirements.txt’
       7. playwright install
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

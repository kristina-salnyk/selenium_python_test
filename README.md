## Selenium Python Test

Designed to test sending emails from the Gmail mail client.

### Setup

Before using it you need to install some modules.

 1. Cloning the repository:

    ```shell
    git clone https://github.com/kristina-salnyk/selenium_python_test.git
    ```

2. Installing all the dependencies:

    ```shell
    pip install -r requirements.txt
    ```
    
3. Add a chromedriver.exe file to the project directory.

### Architecture

    /selenium_python_test:

        test.py                         #The file that references the test suite. It's the file to run the test.

        test_case.py                    #Сontains all the steps to complete the test.

        string_methods.py               #Includes the necessary methods for working with strings

        webdriver_actions.py            #Сontains webdriver methods for interacting with web-page elements.

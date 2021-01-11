*** Settings ***
Library           SeleniumLibrary
Suite Setup         Go to google
Suite Teardown     Close All Browsers
Library             C:/Users/Anna_Poimenova/PycharmProjects/RobotProject/test/FirstModule.py

*** Test Cases ***
Test
    [Tags]           basic
    Check test data first  2    22
    Search and check    pytest  python

*** Keywords ***
Go to google
    Create Webdriver    Chrome   executable_path=C:/Users/Anna_Poimenova/PycharmProjects/RobotProject/test/chromedriver_win32/chromedriver.exe
    Go to    https://habr.com/ru

Check test data first
    [Arguments]     ${query}    ${expected_result}
    Test Data First     ${query}
    Result Check    ${expected_result}

Search and check
    [Arguments]     ${query}    ${expected_result}
    Click Button    id=search-form-btn
    Input Text      id=search-form-field  ${query}
    Press Keys	    id=search-form-field	    ENTER
    Wait Until Page Contains    ${expected_result}






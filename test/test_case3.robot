*** Settings ***
Library           SeleniumLibrary
Suite Setup         Go to google
Suite Teardown     Close All Browsers

*** Test Cases ***
Test
    [Tags]           basic
    Search and check    pytest  python


*** Keywords ***
Go to google
    Create Webdriver    Chrome   executable_path=C:/Users/Anna_Poimenova/PycharmProjects/robot-framework/test/chromedriver_win32/chromedriver.exe
    Go to    https://habr.com/ru

Search and check
    [Arguments]     ${query}    ${expected_result}
    Click Button    id=search-form-btn
    Input Text      id=search-form-field  ${query}
    Press Keys	    id=search-form-field	    ENTER
    Wait Until Page Contains    ${expected_result}





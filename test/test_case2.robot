*** Settings ***
Library             C:/Users/Anna_Poimenova/PycharmProjects/RobotProject/test/ComPayments.py

*** Test Cases ***
Test
    [Tags]           basic
    Search and check    2


*** Keywords ***
Search and check
    [Arguments]     ${query}
    Open App
    Click Menu Payments
    Quit App





*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  String
Library  Collections

*** Variables ***
${URL1}     http://montrealgazette.com/
${URL2}     https://www.usatoday.com/
${URL3}     http://www.foxnews.com/
${URL4}     http://www.cnn.com/
${URL5}     https://ca.reuters.com/

*** Test Cases ***
Validate Availability
    [Template]    Open URL
    ${URL1}
    ${URL2}
    ${URL3}
    ${URL4}
    ${URL5}

*** Keywords ***
Open URL
    [Arguments]  ${URL}
    Create Webdriver    Chrome   executable_path=C:/Users/Anna_Poimenova/PycharmProjects/RobotProject/test/chromedriver_win32/chromedriver.exe
    Go to    ${URL}
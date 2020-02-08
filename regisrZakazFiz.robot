*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}   firefox
${SELSPEED}  0.0s

*** Test Cases ***
Регистрация + Новый заказ физ лица
    [Setup]  Run Keywords  Open Browser  https://test01.moi-uni.ru/  ${BROWSER}
    ...              AND   Set Selenium Speed  ${SELSPEED}
    # open    https://test01.moi-uni.ru/
    click    link=Регистрация
    click    id=input-lastname
    click    xpath=//fieldset[@id='account']/div[2]
    type    id=input-lastname    Мтест152
    click    id=input-firstname
    type    id=input-firstname    Мтест152
    click    id=input-middlename
    type    id=input-middlename    Мтест152
    click    id=input-email
    type    id=input-email    m152@moi-uni.ru
    click    id=input-telephone
    type    id=input-telephone    89213456789
    click    id=input-password
    type    id=input-password    12345
    click    id=input-confirm
    type    id=input-confirm    12345
    click    name=handle_agree
    click    xpath=//input[@value='Продолжить']
    waitForElementPresent    xpath=//ul[@id='osnovnoe-menu']/li[2]/a/span
    click    xpath=//ul[@id='osnovnoe-menu']/li[2]/a/span
    waitForElementPresent    xpath=//div[@id='content']/div[5]/div/div/div/a[7]/p
    click    xpath=//div[@id='content']/div[5]/div/div/div/a[7]/p
    click    xpath=(//button[@type='button'])[2]
    click    link=Оформить заказ
    click    id=button-payment-address
    click    link=скачать квитанцию
    click    id=button-payment-method
    click    id=button-confirm
    click    xpath=(//a[contains(text(),'Выход')])[3]
    [Teardown]  Close Browser

*** Keywords ***
open
    [Arguments]    ${element}
    Go To          ${element}

clickAndWait
    [Arguments]    ${element}
    Click Element  ${element}

click
    [Arguments]    ${element}
    Click Element  ${element}

sendKeys
    [Arguments]    ${element}    ${value}
    Press Keys     ${element}    ${value}

submit
    [Arguments]    ${element}
    Submit Form    ${element}

type
    [Arguments]    ${element}    ${value}
    Input Text     ${element}    ${value}

selectAndWait
    [Arguments]        ${element}  ${value}
    Select From List   ${element}  ${value}

select
    [Arguments]        ${element}  ${value}
    Select From List   ${element}  ${value}

verifyValue
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

verifyText
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

verifyElementPresent
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

verifyVisible
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

verifyTitle
    [Arguments]                  ${title}
    Title Should Be              ${title}

verifyTable
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

assertConfirmation
    [Arguments]                  ${value}
    Alert Should Be Present      ${value}

assertText
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

assertValue
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

assertElementPresent
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

assertVisible
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

assertTitle
    [Arguments]                  ${title}
    Title Should Be              ${title}

assertTable
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

waitForText
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

waitForValue
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

waitForElementPresent
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

waitForVisible
    [Arguments]                  ${element}
    Page Should Contain Element  ${element}

waitForTitle
    [Arguments]                  ${title}
    Title Should Be              ${title}

waitForTable
    [Arguments]                  ${element}  ${value}
    Element Should Contain       ${element}  ${value}

doubleClick
    [Arguments]           ${element}
    Double Click Element  ${element}

doubleClickAndWait
    [Arguments]           ${element}
    Double Click Element  ${element}

goBack
    Go Back

goBackAndWait
    Go Back

runScript
    [Arguments]         ${code}
    Execute Javascript  ${code}

runScriptAndWait
    [Arguments]         ${code}
    Execute Javascript  ${code}

setSpeed
    [Arguments]           ${value}
    Set Selenium Timeout  ${value}

setSpeedAndWait
    [Arguments]           ${value}
    Set Selenium Timeout  ${value}

verifyAlert
    [Arguments]              ${value}
    Alert Should Be Present  ${value}

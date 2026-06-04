*** Settings ***
Library    SeleniumLibrary
Resource   ../variables/common_variables.robot

*** Keywords ***
Abrir Navegador Y Maximizar
    [Arguments]    ${url}
    ${chrome_options} =     Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --headless
    Call Method    ${chrome_options}    add_argument    --window-size\=1920,1080
    Call Method    ${chrome_options}    add_argument    --disable-gpu
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Create Webdriver    Chrome    options=${chrome_options}
    Go To    ${url}

Tomar Captura De Pantalla
    [Arguments]    ${nombre_archivo}
    Set Screenshot Directory    ${EXECDIR}/screenshots
    Capture Page Screenshot    ${nombre_archivo}

Cerrar Navegador
    Close Browser

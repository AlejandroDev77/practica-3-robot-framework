*** Settings ***
Documentation    Pruebas automatizadas de Practica 3 con Robot Framework
Library          SeleniumLibrary
Resource         ../keywords/common_keywords.robot
Resource         ../variables/common_variables.robot
Test Teardown    Cerrar Navegador

*** Test Cases ***
Ejercicio 2 - Login Incorrecto
    [Documentation]    Validar login con credenciales invalidas.
    Abrir Navegador Y Maximizar    ${URL}/login
    # Assert 1
    Wait Until Element Is Visible    css:.login-form h2    timeout=10s
    Element Text Should Be    css:.login-form h2    Login to your account
    
    Input Text    name:email    ${INVALID_EMAIL}
    Input Text    name:password    ${INVALID_PASSWORD}
    Click Button    xpath://button[@data-qa='login-button']
    
    # Assert 2
    Wait Until Element Is Visible    xpath://form[@action='/login']/p    timeout=10s
    Element Text Should Be    xpath://form[@action='/login']/p    Your email or password is incorrect!
    
    Tomar Captura De Pantalla    ej2_error_login.png

Ejercicio 3 - Busqueda de Productos
    [Documentation]    Validar que la busqueda retorne resultados correctamente.
    Abrir Navegador Y Maximizar    ${URL}/products
    
    # Assert 1
    Wait Until Element Is Visible    css:.title.text-center    timeout=10s
    Element Should Contain    css:.title.text-center    ALL PRODUCTS
    
    Input Text    id:search_product    ${SEARCH_TERM}
    Click Button    id:submit_search
    
    # Assert 2
    Wait Until Element Contains    css:.title.text-center    SEARCHED PRODUCTS    timeout=10s
    Element Should Contain    css:.title.text-center    SEARCHED PRODUCTS
    
    Tomar Captura De Pantalla    ej3_searched_products.png

Ejercicio 6 - Suscripcion
    [Documentation]    Validar la funcionalidad de suscripcion por correo.
    Abrir Navegador Y Maximizar    ${URL}
    
    Wait Until Element Is Visible    css:.single-widget h2    timeout=10s
    Scroll Element Into View         css:.single-widget h2
    
    # Assert 1
    Element Should Contain    css:.single-widget h2    SUBSCRIPTION
    
    # Manejar el error tipografico en la pagina (susbscribe)
    Input Text    id:susbscribe_email    test_robot@example.com
    Click Button    id:subscribe
    
    # Assert 2
    Wait Until Element Is Visible    id:success-subscribe    timeout=10s
    Element Should Contain    id:success-subscribe    You have been successfully subscribed!
    
    Tomar Captura De Pantalla    ej6_subscription_success.png

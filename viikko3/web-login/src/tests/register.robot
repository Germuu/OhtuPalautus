*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  marko
    Set Password  marko1234
    Set Password Confirmation  marko1234
    Submit Credentials
    Register Should Succeed   

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message   Username must be at least 3 characters and (a-z)

Register With Valid Username And Too Short Password
    Set Username  bilboswaggins
    Set Password  1122
    Set Password Confirmation  1122
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long


Register With Valid Username And Invalid Password
    Set Username  bilboswaggins
    Set Password  bilboswaggins
    Set Password Confirmation  bilboswaggins
    Submit Credentials
    Register Should Fail With Message  Password must include non alphabetical symbols


Register With Nonmatching Password And Password Confirmation
    Set Username  bilboswaggings
    Set Password  bilbo123
    Set Password Confirmation  bilbo321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match
    

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  12ei1d879ds
    Set Password Confirmation  12ei1d879ds
    Submit Credentials
    Register Should Fail With Message  Username taken

Login After Successful Registration
    Set Username  marko
    Set Password  marko1234
    Set Password Confirmation  marko1234
    Submit Credentials
    Register Should Succeed  
    Go To Login Page
    Set Username  marko
    Set Password  marko1234
    Click Button  Login
    Main Page Should Be Open


Login After Failed Registration
    Set Username  bilboswaggins
    Set Password  bilboswaggins
    Set Password Confirmation  bilboswaggins
    Submit Credentials
    Register Should Fail With Message  Password must include non alphabetical symbols
    Go To Login Page
    Set Username  bilboswaggins
    Set Password  bilboswaggins
    Click Button  Login
    Login Page Should Be Open

    
    




*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}



*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
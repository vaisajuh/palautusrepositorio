*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Index page

*** Test Cases ***
Click Login Link
    Click Link Login
    Login Page Should Be Open

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

*** Keywords ***
Click Link Login
    Click Link Login

Go To Index Page
    Index Page Should Be Open
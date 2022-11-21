*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input new Command
    Input Credentials  ddff  jees123123
    Output Should Contain  User with username ddff already exists

Register With Too Short Username And Valid Password
    Input new Command
    Input Credentials  dd  jees123123
    Output Should Contain  Username or password is too short

Register With Valid Username And Too Short Password
    Input new Command
    Input Credentials  ddd  jed3
    Output Should Contain  Username or password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input new Command
    Input Credentials  ddd  jed3

*** Keywords ***
Input New Command And Create User
    Input new Command
    Input Credentials  ddff  jees123123
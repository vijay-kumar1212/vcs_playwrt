"""

official website https://playwright.dev/

Applications supports: web browser apps, mobile web apps and API

Languages supported: JavaScript, Type Script, Java, Python and .net(c#)

Browsers supported: Chromium, webkit(safari), and Firefox (head/head less)

OS Supported: Windows, macOS, Linux, Supports CI Runs

Features of playwright:

Free & Open source

MULTI-BROWSER  AND MULTIPLE LANGUAGES AND MULTIPLE OS

Easy setup and configuration

Functional, API & accessibility testing(by using 3rd party plugins).

Built in reports, custom reports

Supports CI, CD, Docker

Parallel testing

Auto wait: to solve synchronize problems we are using diff waits in selenium.
whereas in playwright it will wait for element to be available.

built in Assertions

multi tab and multi window support

supports different kinds frames and we identify shadow dom elements

Test parameter

emulate mobile devices.

Faster than other tools

to install pytest plugin pip install pytest-playwright

to install required browsers playwright install

create a new project folder


how to create and run playwright tests

to run tests from terminal

use command as pytest -s  this command will run all the modules available in the current package or directory.

-s will print logs and any print statements

if we want to run specific function from specific module use below command
pytest module_name::function name
pytest test_rahul.py::test_ui_validation_dynamic_card_selection -s -v
pytest test_rahul::test_ui_validation_dynamic_card_selection -s -v

-v stands for verbose

this will provide full names of tests and more details

-m smoke if we have any tests marked with smoke only will run

"""

# Constructor

"""
constructor is just like a method which will be called automatically when we create a object for that class.

If we haven't defined any constructor the default constructor will be called.

class variable and instance variable

The variables which created inside a constructor is known as instance variable.


"""
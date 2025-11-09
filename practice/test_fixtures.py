import pytest


@pytest.fixture(scope='module')
# if we set scope as module that function will run once.
# If we set scope as function this function will run before every function which are mapped.
# if we set scope as class, it will run at class level
def pre_work():
    print("This will initiate browser instance")
    # to run this func before running anu test function we have to use pytest.fixture

def test_initial_check(pre_work):
    #To call pre_work function before running this function we have to pass that pre_work function name
    # as an argument in this function.
    print("First test function")

def test_second_check(pre_work):
    print("Check in at level 2")
import json

import pytest
from playwright.sync_api import Playwright, expect

from practice.pob.login import LoginPage
from practice.pob.dashboard import DashBoard
from practice.utils.api_base import APIUtils

with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]

# in the above user_credentials_list we have a list of users.
# If we want to run the below script with all the available users,
# we have to use parameterize concept as below
# In the below line user_credentials is the parameter
# To work with parametrization we need to set a fixture which returns user_credentials  param
# So, providing the fixture name as user_credentials in method level to return user_credentials param
# For this defining fixture user_credentials in conf test file



@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    user_name = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
    # create order
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright,user_credentials)
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    login_page.login(user_name, password)
    dashboard = DashBoard(browserInstance)
    dashboard.selectOrdersNavLink()

    #orderhistory page
    browserInstance.locator("tr").filter(has_text=order_id).get_by_role("button", name='View').click()
    expect(browserInstance.locator(".tagline")).to_contain_text("Thank you for Shopping with Us")
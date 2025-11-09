from playwright.sync_api import Playwright, expect
from practice.utils.api_base import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # create order
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").click()
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    psge.get_by_role("button", name="Orders").click()

    #orderhistory page
    page.locator("tr").filter(has_text=order_id).get_by_role("button", name='View').click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping with Us")

import time

from playwright.async_api import expect
from playwright.sync_api import Page, Playwright

from practice.utils.api_base import APIUtils


def intercept_response(route):
    # we have to use the abort method to stop the network call
    route.fulfill(json={"data":[],"message":"No Orders"})

def test_network(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    # first we have to listen to the network calls
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").click()
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    # when there are no data need to verify the error message
    order_text = page.locator(".mt-4").text_content()
    print(order_text)

def interceptRequest(route):
    # we have to use the abort method to stop the network call
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    # first we have to listen to the network calls
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?", interceptRequest)
    page.get_by_placeholder("email@example.com").click()
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    page.get_by_role('button', name="View").first.click()
    time.sleep(5)
    print(page.locator(".blink_me").text_content())

def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    token = api_utils.generate_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Script to inject token in session local storage
    page.add_init_script(f"window.localStorage.setItem('token', '{token}');")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="Orders").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_text('Your Orders')).to_be_visible()
    context.close()


import string
import time

from playwright.sync_api import Page, expect, Playwright


def test_rahul_academy_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()


def test_firefox_browser(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("Incorrect username/password")).to_be_visible()

# dynamic selection of card items from the list:

def test_ui_validation_dynamic_card_selection(playwright:Playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.locator("#signInBtn").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    black_berry = page.locator("app-card").filter(has_text="Blackberry")
    black_berry.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

    # window handles and tab handles
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        child_page = newPageInfo.value
        text=child_page.locator(".red").text_content()
        mail = text.split("at ")[1].split(" with")[0]
        print(text)
        assert mail == "mentor@rahulshettyacademy.com"
    time.sleep(5)


# Identify elements by place holders

def test_ui_checks(playwright:Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

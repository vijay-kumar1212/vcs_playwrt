import string
import time

from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import new_context


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
    # https://playwright.dev/docs/test-assertions

    # window handles and tab handles
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        child_page = newPageInfo.value
        text=child_page.locator(".red").text_content()
        mail = text.split("at ")[1].split(" with")[0]
        print(text)
        assert mail == "mentor@rahulshettyacademy.com"
    page.bring_to_front()  # ensures focus on original window
    child_page.close() # to close the child window
time.sleep(5)


# Identify elements by place holders

def test_ui_checks(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_placeholder('Hide/Show Example').fill("Rahul")
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    # handling alerts
    # we have to create an event listener to handle this
    # dialog.accept is a anonymous function to handle that we are using lambda
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    #     mouse hover actions
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
    # handling frames
    pageFrame = page.frame_locator('#courses-iframe')
    pageFrame.get_by_role('link', name="All Access plan").click()
    expect(pageFrame.locator('body')).to_contain_text("Happy Subscibers!")
    # In Playwright, you don’t need to explicitly “switch back” like Selenium
    # (driver.switch_to.default_content()).
    # Playwright automatically brings the context back to the main page when you start using
    # the page object again.
    # dealing with web tables
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            coloumnValue = index
            print(f"Price coloumn value is {coloumnValue}")
            break
    expect(page.locator('tr').filter(has_text="Rice").locator('td').nth(coloumnValue)).to_contain_text('37')
    #  to use recored and playback feature using codegen use below command in terminal
    # playwright codegen https://www.ladbrokes.com/en/sports

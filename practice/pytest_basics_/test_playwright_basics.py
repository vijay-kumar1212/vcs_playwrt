from playwright.sync_api import Page
def test_playwright_basics(playwright):  #here playwright is a fixture provided by pytest-playwright package
    # this is a global fixture
    browser = playwright.chromium.launch(headless=False, args=["--start-fullscreen"])
    context = browser.new_context() # opening browser in incognito mode.
    page = context.new_page() # it will open a new page
    page.goto("https://sports.ladbrokes.com")


# Another way to invoke browser
# we have one more fixture "page" in this browser invoke in chromium in single context head less mode
def test_invoke_browser(page:Page):
    # this implementation will run the test in head less mode
    # to run it on headed mode click on run button on the gutter area
    # modify run configuration and provided additional arguments as --headed
    page.goto("https://sports.ladbrokes.com")


def test_core_locators(page:Page):
    page.goto("https://www.coral.co.uk/en/sports")
    page.locator("//span[contains(text(),'LOG IN')]").click()
    # we can identify the element by using the label of the element
    # to use get by label element should be wrapped in label tag or element id should be referred in for parameter
    # <label for='username' class='text-white' username><label>
    # <br>
    # <input> name='username', id='username'
    # page.get_by_label(" Email or Username ").fill("varna")
    page.locator("#userId").type("varna")
    page.locator("//input[@type='password']").fill("Lbr12345")
    page.wait_for_selector("#rememberMe").click()
    page.get_by_role("button", name=" Log in ").click()

from playwright.sync_api import sync_playwright
"""
here sync_api will run threads one by one i.e after successfully completion of execution on one thread the next one will be executed.
where as in async_api multiple threads will run in parallel.
"""
from screeninfo import get_monitors

"""
First we have to install playwright by using pip install playwright

there by we have to run playwright install to download latest browsers.
"""
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # browser = p.webkit.launch(headless=False)
    page = browser.new_page()
    # page.set_viewport_size({'width':1920, 'height':1080})
    # Get screen resolution of the primary monitor
    # we need to install from screeninfo import get_monitors
    # monitor = get_monitors()[0]
    # screen_width, screen_height = monitor.width, monitor.height
    # page.set_viewport_size({"width": screen_width, "height": screen_height})
    page.goto("https://beta-sports.coral.co.uk/")
    print(page.title())
    page.wait_for_timeout(3000)  # This will take time in milliseconds
    page.locator("//span[contains(text(),'LOG IN')]").click()
    page.locator("#userId").type("varna")
    page.locator("//input[@type='password']").fill("Lbr12345")
    page.wait_for_selector("#rememberMe").click()
    page.locator("//button[contains(text(), 'Log in')]").click()
    page.wait_for_timeout(9000)
    browser.close()


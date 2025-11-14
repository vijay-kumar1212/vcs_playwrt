
class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login(self, user_email, password):
        self.page.get_by_placeholder("email@example.com").click()
        self.page.get_by_placeholder("email@example.com").fill(user_email)
        self.page.get_by_role("textbox", name="enter your passsword").fill(password)
        self.page.get_by_role("button", name="Login").click()

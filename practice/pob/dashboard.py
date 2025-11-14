
class DashBoard:
    def __init__(self, page):
       self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="Orders").click()
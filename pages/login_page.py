from conftest import email, page, password, base_url
from playwright.async_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):

        self.page.goto(base_url)
        self.page.get_by_role("button", name="Sign up/Login").click()
        self.page.get_by_role("button", name="Close cookie consent").click()
        self.page.get_by_role("button", name="Sign in").click()
        self.page.get_by_role("button", name="Close cookie consent").click()

        self.page.get_by_role("button", name="Continue with email").click()
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("button", name="Continue", exact=True).click()


        self.page.get_by_role("checkbox", name="Remember me").click()
        self.page.get_by_role("textbox", name="Password").click()
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Continue", exact=True).click()
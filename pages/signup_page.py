from conftest import base_url
from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_fullname_input = page.get_by_role("textbox", name="Name")
        self.user_signup_email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.signup_button = page.get_by_role("button", name="Sign up")

    def enter_fullname(self, full_name: str):
        self.user_fullname_input.fill(full_name)

    def enter_user_signup_email(self, signup_email: str):
        self.user_signup_email_input.fill(signup_email)

    def enter_password(self, password: str):
        self.password_input.fill(password)
        
    def click_signup(self):
        self.signup_button.click()

    def signup(self, full_name: str, signup_email: str, password: str):
        self.page.goto(f"https://realpha.com/register")

        # self.page.goto(f"{base_url}/register")

        # self.page.get_by_role("button", name="Continue with email").click()
        # self.enter_fullname(full_name)
        # self.enter_user_signup_email(signup_email)
        # self.enter_password(password)
        self.page.wait_for_timeout(200000)
        # self.page.get_by_role("button", name="Continue", exact=True).click()

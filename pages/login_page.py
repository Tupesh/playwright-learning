from conftest import email, page, password, base_url
from playwright.async_api import Page, expect

login_url = f"{base_url}/login"

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
             


    def enter_user_email(self, email: str):
        self.user_email_input.fill(email)

    def enter_password(self, password: str):
        self.password_input.fill(password)
        
    def click_login(self):
        self.login_button.click()
        
    def login(self, email: str, password: str):
        self.page.goto(login_url)

        self.page.get_by_role("button", name="Accept all").click()

        self.page.get_by_role("button", name="Continue with email").click()
        
        self.enter_user_email(email)

        self.page.get_by_role("button", name="Continue", exact=True).click()
        
        self.enter_password(password)

        self.page.get_by_role("button", name="Continue", exact=True).click()

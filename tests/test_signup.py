from pages.signup_page import SignupPage
from conftest import *
from playwright.sync_api import Page, expect

register_url = f"{base_url}/register"


def test_signin(page):

    sign_in = SignupPage(page)
    sign_in.signup(full_name, signup_email, password)
    

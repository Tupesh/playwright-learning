from pages.login_page import LoginPage
from conftest import *
from playwright.sync_api import Page, expect

def test_save_search(page):

    login_page = LoginPage(page)
    login_page.login(email, password)

    page.get_by_role("button", name="Close", exact=True).click()
    page.get_by_role("link", name="Saved", exact=True).click()
    expect(page.get_by_role("button", name="Daily").first).to_be_visible()
    page.wait_for_timeout(2000)

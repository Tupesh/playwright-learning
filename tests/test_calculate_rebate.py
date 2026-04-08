import re, random
from pages.login_page import LoginPage
from conftest import *
from playwright.sync_api import Page, expect


def generate_random_number() -> int:
    return random.randint(500000, 10000000)



homeprice = generate_random_number()

def rebate_amount() :
    return (homeprice*0.015)

def test_save_search(page):

    login_page = LoginPage(page)
    login_page.login(email, password)


    expect(page.get_by_label("Notifications alt+T").get_by_role("listitem")).to_contain_text("Login successful")

    # page.wait_for_timeout(5000)

    expect(page.get_by_role("dialog", name="Your homebuying hub")).to_be_visible()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()

    expect(page.get_by_role("main")).to_contain_text("Good afternoon, Automation")
 
    expect(page.get_by_role("main")).to_contain_text("Your reAlpha Savings")


    expect(page.get_by_text("Buying with reAlpha")).to_be_visible()

    page.get_by_role("button", name="Edit").click()
    page.get_by_role("textbox", name="What is your target home").fill(str(homeprice))
    page.get_by_role("button", name="Save").click()

    expect(page.get_by_role("main")).to_contain_text(f"Buying with reAlpha increasesyour buying power by${rebate_amount():,.2f}")


    expect(page.get_by_label("Notifications alt+T").get_by_role("listitem")).to_contain_text("Rebate amount updated successfully")

    page.wait_for_timeout(5000)
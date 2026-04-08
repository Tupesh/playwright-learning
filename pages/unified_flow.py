from conftest import base_url, page
from playwright.sync_api import Page, expect
import re

class RealphaMortgageFlow:
    def __init__(self, page: Page):
        self.page = page

    def property_search(self):
        self.page.goto(base_url)

        # Accept cookies only if present
        accept_all = self.page.get_by_role("button", name="Accept all")
        if accept_all.is_visible():
            accept_all.click()

        self.page.get_by_role("link", name="Get started").click()

        expect(
            self.page.get_by_text("Where are you planning to buy")
        ).to_be_visible()

        search_box = self.page.get_by_role("textbox", name="City or Zip code")
        expect(search_box).to_be_visible()
        expect(search_box).to_be_editable()

        # Start with fill. If your dropdown does not react, swap to press_sequentially("mia")
        search_box.fill("mia")
        expect(search_box).to_have_value("mia")
    


        # Strongest accessible version:
        # assumes the dropdown uses ARIA roles like listbox/option
        suggestions_box = self.page.get_by_role("listbox")
        expect(
            suggestions_box,
            "Suggestion dropdown should appear after entering city text"
        ).to_be_visible()

        miami_option = self.page.get_by_role("option", name=re.compile(r"miami", re.I))
        expect(
            miami_option,
            "At least one Miami suggestion should be shown"
        ).to_be_visible()

        miami_option.first.click()

        # After selection, the field should reflect the chosen suggestion
        expect(search_box).to_have_value(re.compile(r"miami", re.I))









""" 


class TestRealphaMortgageFlow:

    def __init__(self, page: Page):
        self.page = page   


    def property_search(self):
        self.page.goto(base_url)
        self.page.get_by_role("button", name="Accept all").click()
        self.page.get_by_role("link", name="Get started").click()
        expect(self.page.locator("div").filter(has_text="Where are you planning to buy").first).to_be_visible()

        self.page.get_by_role("textbox", name="City or Zip code").fill("mia")
        # self.page.get_by_role("textbox", name="City or Zip code").click()
        # self.page.get_by_role("textbox", name="City or Zip code").click()
        # self.page.get_by_text("FL, USA").first.click()
        self.page.wait_for_timeout(2000)
        




    # def test_mortgage_flow(self):
        
    #     self.page.get_by_role("button", name="Continue").click()
    #     expect(self.page.get_by_text("Good news!Homebuyers in")).to_be_visible()
    #     self.page.get_by_role("button", name="Continue").click()
    #     self.page.get_by_role("textbox", name="Enter home price").click()
    #     self.page.get_by_role("textbox", name="Enter home price").fill("67,0000")
    #     page.get_by_role("button", name="Continue").click()
    #     page.get_by_text("$6,700", exact=True).click()
    #     page.get_by_role("button", name="Continue").click()
    #     page.get_by_text("+$3,350 cash backNo, I'd like").click()
    #     expect(page.get_by_text("+$3,350 cash back")).to_be_visible()
    #     page.get_by_text("$10,050").click()
    #     page.get_by_role("button", name="Continue").click()
    #     page.get_by_role("button", name="Single-family home").click()
    #     page.get_by_role("button", name="Continue").click()
    #     page.get_by_role("button", name="+").first.click()
    #     page.get_by_role("button", name="+").nth(5).click()
    #     expect(page.get_by_text("$10,050")).to_be_visible()
    #     page.get_by_role("button", name="Continue").click()
    #     expect(page.get_by_text("$10,050")).to_be_visible()
    #     page.get_by_role("textbox", name="Name").click()
    #     page.get_by_role("textbox", name="Name").fill("Automation unified flow")
    #     page.get_by_role("textbox", name="Name").press("Tab")
    #     page.get_by_role("textbox", name="Email").fill("tupesh+automationunifiedflow1@realpha.com")
 """
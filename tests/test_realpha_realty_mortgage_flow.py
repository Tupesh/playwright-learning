from pages.unified_flow import RealphaMortgageFlow
from conftest import *
from playwright.sync_api import Page, expect

def test_mortgage_flow(page):
    
    mortgage_flow = RealphaMortgageFlow(page)
    mortgage_flow.property_search()
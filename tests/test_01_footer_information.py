import os

from dotenv import load_dotenv
from workflows import workflows
from pytest_bdd import scenario, given, then


load_dotenv()
BASE_URL = os.environ.get("BASE_URL")
STANDARD_USR = os.environ.get("STANDARD_USR")
PASSWORD = os.environ.get("PASSWORD")


@scenario('features/01_footer_information.feature', 'Navigating to Twitter from footer')
def test_navigating_to_twitter():
    print('Starting features/01_footer_information.feature - Navigating to Twitter from footer')
    
    
@given("I am on a inventory page of SauceDemo")
def open_inventory_page(page):
    workflows.login(page, BASE_URL, STANDARD_USR, PASSWORD)
    workflows.validate_inventory_page(page)


@then("The Twitter icon in the footer is visible")
def click_twitter_icon(page):
    workflows.contains_twitter_icon(page)


@scenario('features/01_footer_information.feature', 'Navigating to Facebook from footer')
def test_navigating_to_facebook():
    print('Starting features/01_footer_information.feature - Navigating to Facebook from footer')
    
    
@then("The Facebook icon in the footer is visible")
def click_facebook_icon(page):
    workflows.contains_facebook_icon(page)


@scenario('features/01_footer_information.feature', 'Navigating to Linkedin from footer')
def test_navigating_to_linkedin():
    print('Starting features/01_footer_information.feature - Navigating to Linkedin from footer')


@then("The Linkedin icon in the footer is visible")
def click_linkedin_icon(page):
    workflows.contains_linkedin_icon(page)

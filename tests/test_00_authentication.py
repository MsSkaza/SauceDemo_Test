import os

from dotenv import load_dotenv
from workflows import workflows
from pytest_bdd import scenario, given, when, then

load_dotenv()
BASE_URL = os.environ.get("BASE_URL")
STANDARD_USR = os.environ.get("STANDARD_USR")
LOCKED_USR = os.environ.get("LOCKED_USR")
INVALID_USR = os.environ.get("INVALID_USR")
PASSWORD = os.environ.get("PASSWORD")


@scenario('features/00_authentication.feature', 'Successful login with valid credentials')
def test_successful_login_with_valid_credentials():
    print('Starting features/00_authentication.feature - Successful login with valid credentials')


@given("I am on the SauceDemo login page")
def go_to_login_page(page):
    workflows.open_login_page(page, BASE_URL)


@when("I login with valid credentials")
def login_with_valid_credentials(page):
    workflows.login(page, BASE_URL, STANDARD_USR, PASSWORD)


@then("I should see the inventory page")
def open_inventory_page(page):
    workflows.validate_inventory_page(page)


@scenario('features/00_authentication.feature', 'Failed login with locked credentials')
def test_failed_login_with_locked_credential():
    print('Starting features/00_authentication.feature - Failed login with locked credentials')


@when("I login with locked credentials")
def login_with_locked_credentials(page):
    workflows.login(page, BASE_URL, LOCKED_USR, PASSWORD)


@then("I should see an error message about locked user")
def error_message_locked_user(page):
    workflows.validate_error_message(page, "Epic sadface: Sorry, this user has been locked out.")


@scenario('features/00_authentication.feature', 'Failed login with invalid credentials')
def test_failed_login_with_invalid_credential():
    print('Starting features/00_authentication.feature - Failed login with invalid credentials')


@when("I login with invalid credentials")
def login_with_invalid_credentials(page):
    workflows.login(page, BASE_URL, INVALID_USR, PASSWORD)


@then("I should see an error message about invalid user")
def error_message_invalid_user(page):
    workflows.validate_error_message(page, "Epic sadface: Username and password do not match any user in this service")


@scenario('features/00_authentication.feature', 'Logout from SauceDemo')
def test_logout_from_saucedemo():
    print('Starting features/00_authentication.feature - Logout from SauceDemo')


@given("I am logged in to SauceDemo")
def logged_in(page):
    workflows.login(page, BASE_URL, STANDARD_USR, PASSWORD)
    workflows.validate_inventory_page(page)


@when("I click the logout button")
def click_the_logout_button(page):
    workflows.logout(page)


@then("I should be redirected to the login page")
def redirected_to_the_login_page(page):
    workflows.validate_login_page(page)

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def open_login_page(page, url):
    login_page = LoginPage(page)
    page.goto(url)
    login_page.verify_header_text()


def validate_login_page(page):
    login_page = LoginPage(page)
    login_page.verify_header_text()


def login(page, url, username, password):
    login_page = LoginPage(page)
    page.goto(url)
    login_page.login(username, password)


def validate_error_message(page, message):
    login_page = LoginPage(page)
    login_page.has_error_message(message)


def validate_inventory_page(page):
    inventory_page = InventoryPage(page)
    inventory_page.verify_header_text()


def logout(page):
    inventory_page = InventoryPage(page)
    inventory_page.logout()


def contains_twitter_icon(page):
    inventory_page = InventoryPage(page)
    inventory_page.contains_twitter_icon()


def contains_facebook_icon(page):
    inventory_page = InventoryPage(page)
    inventory_page.contains_facebook_icon()


def contains_linkedin_icon(page):
    inventory_page = InventoryPage(page)
    inventory_page.contains_linkedin_icon()

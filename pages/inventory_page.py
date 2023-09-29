from playwright.sync_api import Page


class InventoryPage:
    HEADER: str = '//div[@class="app_logo"]'
    TITLE: str = '//span[@class="title"]'
    MENU_BUTTON: str = '#react-burger-menu-btn'
    LOGOUT_BUTTON: str = '#logout_sidebar_link'
    TWITTER_ICON: str = '//li[@class="social_twitter"]'
    FACEBOOK_ICON: str = '//li[@class="social_facebook"]'
    LINKEDIN_ICON: str = '//li[@class="social_linkedin"]'

    def __init__(self, page: Page):
        self.page = page

    def verify_header_text(self):
        assert self.page.inner_text(self.HEADER) == 'Swag Labs'
        assert self.page.inner_text(self.TITLE) == 'Products'

    def open_burger_menu(self):
        self.page.click(self.MENU_BUTTON)

    def logout(self):
        self.open_burger_menu()
        self.page.click(self.LOGOUT_BUTTON)

    def contains_twitter_icon(self):
        self.page.is_visible(self.TWITTER_ICON)

    def contains_facebook_icon(self):
        self.page.is_visible(self.FACEBOOK_ICON)

    def contains_linkedin_icon(self):
        self.page.is_visible(self.LINKEDIN_ICON)

from playwright.sync_api import Page


class LoginPage:
    HEADER: str = '//div[@class="login_logo"]'
    LOGIN_BUTTON: str = "#login-button"
    ERROR: str = '//h3[@data-test="error"]'
    USR_FIELD: str = "#user-name"
    PWD_FIELD: str = "#password"

    def __init__(self, page: Page):
        self.page = page

    def login(self, username, password):
        self.page.fill(self.USR_FIELD, username)
        self.page.fill(self.PWD_FIELD, password)

    def verify_header_text(self):
        assert self.page.is_visible(self.HEADER)
        assert self.page.inner_text(self.HEADER) == 'Swag Labs'

    def has_error_message(self, message):
        assert self.page.is_visible(self.ERROR)
        assert self.page.inner_text(self.ERROR) == message

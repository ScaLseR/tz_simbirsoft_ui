from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:
    """base class for all pages"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """open page"""
        self.browser.get(self.url)

    def go_to_login_page(self):
        """go to authorization page"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_disk_page(self):
        """go to yandex disk page"""
        link = self.browser.find_element(*BasePageLocators.DISK_LINK)
        link.click()

    def go_to_new_window(self):
        """go to new window in browser"""
        new_window = self.browser.window_handles[1]
        old_window = self.browser.window_handles[0]
        self.browser.switch_to.window(new_window)

    def is_element_present(self, how, what):
        """find element on page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

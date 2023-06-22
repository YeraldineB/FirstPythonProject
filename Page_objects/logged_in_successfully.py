from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url: str = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.XPATH, "//div[@id='loop-container']//article//h1[@class='post-title']")
    __log_out_button_locator = (By.XPATH, "//div[@id='loop-container']/div/article//a["
                                          "@href='https://practicetestautomation.com/practice"
                                          "-test-login"
                                          "/']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return self._url

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button_locator)

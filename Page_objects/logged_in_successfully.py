from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfullyPage:
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.XPATH, "//div[@id='loop-container']//article//h1[@class='post-title']")
    __log_out_button_locator = (By.XPATH, "//div[@id='loop-container']/div/article//a["
                                          "@href='https://practicetestautomation.com/practice"
                                          "-test-login"
                                          "/']")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    def is_logout_button_displayed(self) -> bool:
        return self._driver.find_element(self.__log_out_button_locator).is_displayed()

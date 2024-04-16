
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def wait_visibility(self, locator):
        return WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(locator)
        )
    def wait_presence(self, locator):
        return WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(locator)
        )
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_click(self, *locator):
        return WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(*locator)
        )
    def send_keys(self, locator, value):
        self.wait_visibility(locator).clear()
        self.wait_visibility(locator).send_keys(value)
    def url_is(self, url):
        return WebDriverWait(self.driver, 25).until(
            EC.url_to_be(url)
        )
    def title_is(self, title):
        return WebDriverWait(self.driver, 25).until(
            EC.title_is(title)
        )

    def get_text(self, locator):
        return self.wait_presence(locator).text

    def get_value(self, locator):
        return self.wait_presence(locator).get_attribute("value")

    def action_scroll_to_element(self, locator):
        action = ActionChains(self.driver)
        action.scroll_to_element(locator).perform()

    def hover(self, locator):
        action = ActionChains(self.driver)
        action.move_to_element(locator).perform()

    def action_click(self, locator):
        action = ActionChains(self.driver)
        action.click(locator).perform()
    def file_upload(self, locator, path):
        self.wait_presence(locator).send_keys(path)

    def switch_to_alert_and_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def refresh_page(self):
        self.driver.refresh()
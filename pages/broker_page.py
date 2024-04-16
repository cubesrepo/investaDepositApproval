import time

import TestData
from pages.base_page import BasePage


class BrokerPage(BasePage):
    def valid_broker(self):
        time.sleep(1)

        self.url_is("https://devenv.investa.trade/Welcome/Onboarding/BrokerSelection"), "wrong broker url"
        self.title_is("Select Broker")

        self.wait_clickable(TestData.broker.ISI).click()
        time.sleep(0.5)
        self.send_keys(TestData.broker.BROKER_PIN, TestData.PASSWORD)
        time.sleep(0.5)
        self.wait_clickable(TestData.broker.GO).click()
        time.sleep(1)


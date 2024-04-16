import pytest

from pages.broker_page import BrokerPage
from tests.base_test import BaseTest

@pytest.mark.order(2)
class TestBroker(BaseTest):

    def test_valid_broker(self, driver):
        brokerpage = BrokerPage(driver)
        brokerpage.valid_broker()
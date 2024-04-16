import pytest

from pages.controlpanel_page import ControlpanelPage
from tests.base_test import BaseTest

@pytest.mark.order(3)
class Testcontrolpanel(BaseTest):
    def test_goto_controlpanel(self, driver):
        controlpanelpage = ControlpanelPage(driver)
        controlpanelpage.goto_controlpanel()
import time

import TestData
from pages.base_page import BasePage


class ControlpanelPage(BasePage):

    def goto_controlpanel(self):
        time.sleep(1)

        assert self.url_is("https://devenv.investa.trade/Portfolio"), "wronmg home page url"
        assert self.title_is("Portfolio | InvestaTrade"), "wrong title"

        self.wait_clickable(TestData.controlpanel.PROFILE).click()
        time.sleep(0.5)
        self.wait_clickable(TestData.controlpanel.CONTROL_PANEL).click()
        time.sleep(1)

        self.url_is("https://devenv.investa.trade/Account/Admin/AdminDashboard")
        self.title_is("Dashboard | Control Panel | InvestaTrade")

        time.sleep(0.5)

        self.wait_clickable(TestData.cashinapproval.WALLET).click()
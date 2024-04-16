import pytest

from pages.cashinapproval_page import CashinapprovalPage
from tests.base_test import BaseTest

@pytest.mark.order(4)
class Testcashinapproval(BaseTest):

    def test_valid_cashin_approval(self,driver):
        cashinapprovalpage = CashinapprovalPage(driver)
        cashinapprovalpage.valid_cashin_approval_loop()

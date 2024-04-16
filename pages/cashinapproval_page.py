import logging
import time

import TestData
from pages.base_page import BasePage


class CashinapprovalPage(BasePage):

    def go_to_view_wallet(self, user_id):
        view_wallet_btn = self.wait_clickable(TestData.cashinapproval.VIEW_WALLET_TRANSAC)
        self.action_click(view_wallet_btn)
        time.sleep(0.5)

        self.send_keys(TestData.cashinapproval.USER_OR_EMAIL, user_id)
        time.sleep(0.5)

        search_btn = self.wait_clickable(TestData.cashinapproval.SEARCH)
        self.action_click(search_btn)

    def valid_approve_deposit(self):
        time.sleep(1)

        cash_in_approval_btn = self.wait_clickable(TestData.cashinapproval.CASHIN_APPROVAL_BTN)
        self.action_click(cash_in_approval_btn)

        time.sleep(1)
        # get the user_id to search and deposit_no
        user_id = self.get_text(TestData.cashinapproval.VIEW_USERID)
        deposit_no = self.get_text(TestData.cashinapproval.VIEW_DEPOSITNO)


        time.sleep(1)

        self.go_to_view_wallet(user_id)

        time.sleep(1)
        # retreive avail cash before deposit
        avail_cash_of_user_id_before_deposit = self.get_text(TestData.cashinapproval.AVL_CASH).replace(',', '').replace(
            ' PHP', '')
        total_deposit_of_user_id_before_deposit = self.get_text(TestData.cashinapproval.TOTAL_DEPO).replace(',', '').replace(
            ' PHP', '')

        time.sleep(1)
        cash_in_approval_btn = self.wait_clickable(TestData.cashinapproval.CASHIN_APPROVAL_BTN)
        self.action_click(cash_in_approval_btn)

        time.sleep(1)

        view_btn = self.wait_clickable(TestData.cashinapproval.VIEW_BTN)
        self.action_click(view_btn)

        time.sleep(0.5)
        # retrieve amount paid and fees
        amount_paid = self.get_value(TestData.cashinapproval.AMOUNT_PAID).replace(',', '').replace(' PHP', '')
        fees = (self.get_value(TestData.cashinapproval.FEES).replace(',', '').replace(' PHP', '') or 0.0)

        time.sleep(0.5)

        self.send_keys(TestData.cashinapproval.ACCOUNT_TRADING_PIN, TestData.PASSWORD)

        time.sleep(0.5)

        approve_btn = self.wait_clickable(TestData.cashinapproval.APPROVE_BTN)
        self.action_click(approve_btn)

        time.sleep(1)
        self.switch_to_alert_and_accept()
        time.sleep(1)
        self.go_to_view_wallet(user_id)

        time.sleep(1)

        total_subtract_amountpaid_fees = float(amount_paid) - float(fees)

        total_expected_total_deposit = float(total_deposit_of_user_id_before_deposit) + total_subtract_amountpaid_fees
        total_actual_deposit = float(self.get_text(TestData.cashinapproval.TOTAL_DEPO).replace(',', '').replace(' PHP', ''))


        total_expected_avail_cash = float(
            avail_cash_of_user_id_before_deposit) + total_subtract_amountpaid_fees

        total_actual_avail_cash = float(
            self.get_text(TestData.cashinapproval.AVL_CASH).replace(',', '').replace(' PHP', ''))

        print(f"Expected avail cash: {total_expected_avail_cash:.6f}")
        print(f"Actual avail cash: {total_actual_avail_cash:.6f}")

        print(f"Expected Depo: {total_expected_total_deposit:.2f}")
        print(f"Actual Depo: {total_actual_deposit:.2f}")

        assert f"{total_expected_avail_cash:.6f}" == f"{total_actual_avail_cash:.6f}"
        assert f"{total_expected_total_deposit:.2f}" == f"{total_actual_deposit:.2f}"

        time.sleep(0.5)

        descript = self.wait_presence(TestData.cashinapproval.DEPOSIT_NO_DESCRIPT)
        self.action_scroll_to_element(descript)

        time.sleep(0.5)

        descriptclick = self.wait_clickable(TestData.cashinapproval.DEPOSIT_NO_DESCRIPT)
        self.action_click(descriptclick)
        time.sleep(1)

        descriptTitle = self.get_text(TestData.cashinapproval.DEPOSIT_TITLE_OUTPUT)
        descripTitleCut = descriptTitle[len("Deposit No: "):]

        status = self.get_text(TestData.cashinapproval.STATUS)
        print(descripTitleCut)
        print(deposit_no)

        assert descripTitleCut == deposit_no
        assert status == "COMPLETED"

        close = self.wait_clickable(TestData.cashinapproval.CLOSE)
        self.action_click(close)
    def valid_cashin_approval_loop(self):
        while True:
            try:
                self.valid_approve_deposit()
            except Exception as e:
                print(e)
                break


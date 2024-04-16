from selenium.webdriver.common.by import By

BASE_URL = "https://devenv.investa.trade/login"
EMAIL = "qa-team@investagrams.com"
PASSWORD = "123456"


class login:
    EMAIL = By.XPATH, "//input[@name='Username']"
    PASSWORD = By.XPATH, "//input[@name='Password']"
    LOGIN = By.XPATH, "//button[@type='submit']"
    TOAST_SUCCESSFUL = By.XPATH, "//span[@id='AlertNotificationTextMessage']"

class broker:
    ISI = By.XPATH, "//button[1]"
    BROKER_PIN = By.XPATH, "//input[@placeholder='Enter your trading pin']"
    GO = By.XPATH, "//div[@class='btn ml-1 investa-btn-blue']"
    TOAST_BROKER_SUCCESSFUL = By.XPATH, "//span[@id='AlertNotificationTextMessage']"

class controlpanel:
    PROFILE = By.XPATH, "//img[@class='rounded-circle profile-picture-sidebar mb-0']"
    CONTROL_PANEL = By.XPATH, "//a[@href='/Account/Admin/AdminDashboard']"

class cashinapproval:
    WALLET = By.XPATH, "//a[@href='#wallet-nav']"
    CASHIN_APPROVAL_BTN = By.XPATH, "//a[@href='/Account/Admin/Wallet/DepositApprovalAdmin']"

    VIEW_USERID = By.XPATH, "//tbody/tr[1]/td[2]"
    VIEW_BTN = By.XPATH, "//tbody/tr[1]/td[6]//input[@value='View']"
    VIEW_DEPOSITNO = By.XPATH, "//tbody/tr[1]/td[1]"

    AMOUNT_PAID = By.XPATH, "//input[@data-ng-value=\"(CashIn.Data.Detailed.Total | numberPriceFormat) + ' ' + CashIn.Data.Detailed.Currency\"]"
    FEES = By.XPATH, "//input[@data-ng-value=\"(CashIn.Data.Detailed.CashInMethodFees | numberPriceFormat) + ' ' + CashIn.Data.Detailed.Currency\"]"
    ACCOUNT_TRADING_PIN  = By.ID, "accountTradingPinInput"
    APPROVE_BTN = By.XPATH, "//input[@value='Approve']"
    VIEW_WALLET_TRANSAC = By.XPATH, "//a[@href='/Account/Admin/Wallet/ManageWalletAdmin']"

    USER_OR_EMAIL = By.XPATH, "//input[@placeholder='Username or Email']"
    SEARCH = By.XPATH, "//button[@data-ng-click='Wallet.searchUser()']"

    AVL_CASH = By.XPATH, "//span[text()='Available Cash:']/following-sibling::strong[@class='ng-binding']"
    TOTAL_DEPO = By.XPATH, "//span[text()='Total Deposit:']/following-sibling::strong[@class='ng-binding']"

    DEPOSIT_NO_DESCRIPT = By.XPATH, "//tr[@data-ng-repeat=\"entity in Wallet.Data.WalletLogList.List track by entity.Id\"]/td[2]"
    DEPOSIT_TITLE_OUTPUT = By.XPATH, "//h4[@class='modal-title ng-binding']"
    STATUS = By.XPATH, "//td[@data-ng-class=\"(Wallet.Data.CashInDetails.CashIn.Status == 1) ? 'text-success' : 'text-danger'\"]"
    CLOSE = By.XPATH, "//button[@class='close']"
from unittest import mock, TestCase
from parameterized import *
from app.Account_company import AccountCompany
from app.Account_personal import AccountPersonal


class TestPersonalExpressTransfers(TestCase):
    personal_data = {
        "name": "Antoni",
        "last_name": "Krawczyk",
        "pesel": "12345678901",
        # "promo_code": "PROM_401",
    }

    def setUp(self):
        self.acc_personal = AccountPersonal(**self.personal_data)
        self.acc_personal.history = []

    def compare_balance_and_history(
        self, acc: AccountCompany | AccountPersonal, expected_balance, expected_history
    ):
        self.assertEqual(
            acc.history,
            expected_history,
            f"History equals: {acc.history} instead of {expected_history}!",
        )
        self.assertEqual(
            acc.balance,
            expected_balance,
            f"Balance is equal: {acc.balance} instead of {expected_balance}!",
        )

    @parameterized.expand(
        [
            (0, 0, 0, []),
            (100, 100, -1, [-100, -1]),
            (0, 100, 0, []),
            (1000, 1000, -1, [-1000, -1]),
            (500, 400, 99, [-400, -1]),
            (100, 200, 100, []),
            (200, 100, 99, [-100, -1]),
        ]
    )
    def test_express_private_transfers(
        self, balance, transfer_val, expected_balance, expected_history
    ):
        self.acc_personal.balance = balance
        self.acc_personal.express_outgoing_transfer(transfer_val)
        self.compare_balance_and_history(
            self.acc_personal, expected_balance, expected_history
        )


class TestCompanyExpressTransfers(TestCase):
    company_data = {"name": "Mateusz", "nip": "8461627563"}

    @mock.patch("app.Account_company.AccountCompany.validate_nip")
    def setUp(self, mock_object) -> None:
        mock_object.return_value = True
        self.acc_company = AccountCompany(**self.company_data)
        self.acc_company.history = []

    def compare_balance_and_history(
        self, acc: AccountCompany | AccountPersonal, expected_balance, expected_history
    ):
        self.assertEqual(
            acc.history,
            expected_history,
            f"History equals: {acc.history} instead of {expected_history}!",
        )
        self.assertEqual(
            acc.balance,
            expected_balance,
            f"Balance is equal: {acc.balance} instead of {expected_balance}!",
        )

    @parameterized.expand(
        [
            (0, 0, 0, []),
            (100, 100, -5, [-100, -5]),
            (100, -100, 100, []),
            (0, 100, 0, []),
            (1000, 1000, -5, [-1000, -5]),
            (500, 400, 95, [-400, -5]),
            (100, 200, 100, []),
        ]
    )
    def test_express_company_transfers(
        self, balance, transfer_val, expected_balance, expected_history
    ):
        self.acc_company.balance = balance
        self.acc_company.express_outgoing_transfer(transfer_val)

        self.compare_balance_and_history(
            self.acc_company, expected_balance, expected_history
        )

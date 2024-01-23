from unittest import mock, TestCase
from parameterized import *
from app.Account_company import AccountCompany
from app.Account_personal import AccountPersonal


class TestBasicTransfers(TestCase):
    personal_data = {
        "name": "Antoni",
        "last_name": "Krawczyk",
        "pesel": "12345678901",
        # "promo_code": "PROM_401",
    }
    company_data = {"name": "Mateusz", "nip": "1234567890"}

    def test_receive_value_error(self):
        acc = AccountPersonal(**self.personal_data)
        self.assertRaises(ValueError, acc.receive_transfer, "0")

    def test_outgoing_value_error(self):
        acc = AccountPersonal(**self.personal_data)
        self.assertRaises(ValueError, acc.outgoing_transfer, "0")

    @mock.patch("app.Account_company.AccountCompany.validate_nip")
    def setUp(self, mock_object):
        mock_object.return_value = True
        self.acc_personal = AccountPersonal(**self.personal_data)
        self.acc_personal.history = []
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

    def account_receive_or_execute_transfer(
        self,
        acc: AccountCompany | AccountPersonal,
        transfer_value,
        expected_balance,
        expected_history,
    ):
        if transfer_value > 0:
            acc.receive_transfer(transfer_value)
            acc.receive_transfer(-transfer_value)
        elif transfer_value < 0:
            acc.outgoing_transfer(transfer_value)
            acc.outgoing_transfer(-transfer_value)
        else:
            acc.receive_transfer(-transfer_value)
            acc.receive_transfer(transfer_value)
            acc.outgoing_transfer(transfer_value)
            acc.outgoing_transfer(-transfer_value)
        self.compare_balance_and_history(acc, expected_balance, expected_history)

    # negative transfer = outgoing, positive = received just for the test cases
    @parameterized.expand(
        [
            (0, 0, 0, []),
            (0, 100, 100, [100]),
            (100, -100, 0, [-100]),
            (0, -100, 0, []),
            (1000, -1000, 0, [-1000]),
            (1000, 1000, 2000, [1000]),
            (500, -400, 100, [-400]),
            (100, -200, 100, []),
            (100, 200, 300, [200]),
        ]
    )
    def test_basic_transfers(
        self, balance, transfer_val, expected_balance, expected_history
    ):
        self.acc_personal.balance = balance
        self.acc_company.balance = balance
        self.account_receive_or_execute_transfer(
            self.acc_personal, transfer_val, expected_balance, expected_history
        )
        self.account_receive_or_execute_transfer(
            self.acc_company, transfer_val, expected_balance, expected_history
        )

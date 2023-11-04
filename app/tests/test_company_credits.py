import unittest
from ..Account_company import AccountCompany
from parameterized import *


class TestCompanyCredits(unittest.TestCase):
    name = "Company"
    nip = "1234567890"

    def setUp(self):
        self.acc_company = AccountCompany(self.name, self.nip)

    def check_balance(self, acc: AccountCompany, balance):
        self.assertEqual(
            acc.balance,
            balance,
            f"Balance is equal: {acc.balance} instead of {balance}!",
        )

    def check_decision(self, decision, expected_decision):
        self.assertEqual(
            decision,
            expected_decision,
            f"Decision is {decision} instead of {expected_decision}",
        )

    @parameterized.expand(
        [
            ([], 0, 100, False, 0),
            ([], 200, 100, False, 200),
            ([100, 200, 300], 200, 100, False, 200),
            ([-100, 100], 200, 100, False, 200),
            ([1775], 0, 100, False, 0),
            ([1775], 200, 100, False, 200),
            ([-1775, 1], 200, 100, True, 300),
            ([-1775, -1], 200, 100, True, 300),
            ([-1775, 1775], 200, 100, True, 300),
            ([-1775, 1775], 0, 100, False, 0),
            ([-1775, 1775], 200, 100, True, 300),
        ]
    )
    def test_taking_credits(
        self, history, balance, credit_val, expected_decision, expected_balance
    ):
        self.acc_company.balance = balance
        self.acc_company.history = history
        decision = self.acc_company.take_credit(credit_val)
        self.check_decision(decision, expected_decision)
        self.check_balance(self.acc_company, expected_balance)

import unittest
from ..Account_company import AccountCompany
from ..Account_personal import AccountPersonal
from parameterized import *


class TestCredits(unittest.TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    example_credit = 1000

    def setUp(self):
        self.acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)

    def check_balance(self, acc: AccountPersonal, balance):
        self.assertEqual(
            acc.saldo, balance, f"Balance is equal: {acc.saldo} instead of {balance}!"
        )

    def check_decision(self, decision, expected_decision):
        self.assertEqual(
            decision,
            expected_decision,
            f"Decision is {decision} instead of {expected_decision}",
        )

    @parameterized.expand(
        [
            ([], 1, False, 0),
            ([100], 1, False, 0),
            ([100, 100], 500, False, 0),
            ([100, 100, 100], 100_000, True, 100_000),
            ([100, 100, -100, 100], 100_000, False, 0),
            ([-100, 100, 100, 100], 500, True, 500),
            ([-100, 100, 100, 100], 0, False, 0),
            ([-100, 100, 100, 100], -1, False, 0),
            ([-100, 100, -100, 100], 1000, False, 0),
            ([-500, -500, 1000, 1000, 1], 1000, True, 1000),
            ([-500, -500, -500, -500, -500], 1000, False, 0),
        ]
    )
    def test_taking_credits(
        self, history, credit_val, expected_decision, expected_balance
    ):
        self.acc_personal.history = history
        decision = self.acc_personal.take_credit(credit_val)
        self.check_decision(decision, expected_decision)
        self.check_balance(self.acc_personal, expected_balance)

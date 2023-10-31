import unittest
from ..Account_company import AccountCompany
from ..Account_personal import AccountPersonal


class TestCredits(unittest.TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    example_credit = 1000

    def setUp(self):
        self.acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)

    def test_2_transfers(self):
        self.acc_personal.history = [-100, 100]
        decision = self.acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            self.acc_personal.saldo,
            0,
            "Kredyt  został udzielony, a nie powinien!",
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_3_incoming_transfers(self):
        self.acc_personal.history = [-100, 100, 100, 100]
        decision = self.acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            self.acc_personal.saldo,
            self.example_credit,
            "Kredyt nie został udzielony, a powinien!",
        )
        self.assertTrue(decision, "Decyzja powinna być pozytywna!")

    def test_3_incoming_transfers(self):
        self.acc_personal.history = [-100, 100, 100, 100]
        decision = self.acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            self.acc_personal.saldo,
            self.example_credit,
            "Kredyt nie został udzielony, a powinien!",
        )
        self.assertTrue(decision, "Decyzja powinna być pozytywna!")

    def test_mixed_transfers(self):
        self.acc_personal.history = [-100, 100, -100, 100]
        decision = self.acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            self.acc_personal.saldo, 0, "Kredyt  został udzielony, a powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_five_last_positive_transactions(self):
        self.acc_personal.history = [
            -500,
            -500,
            1000,
            self.example_credit,
            1,
        ]  # sum = 1001

        decision = self.acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            self.acc_personal.saldo,
            self.example_credit,
            "Kredyt nie został udzielony, a powinien!",
        )
        self.assertTrue(decision, "Decyzja powinna być pozytywna!")

    def test_five_last_negative_transactions(self):
        self.acc_personal.history = [-500, -500, -500, -500, -500]  # sum = 1

        decision = self.acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            self.acc_personal.saldo,
            0,
            "Kredyt  został udzielony, a nie powinien!",
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_no_history_credit(self):
        decision = self.acc_personal.take_credit(self.example_credit)
        self.acc_personal.history = []
        self.assertEqual(
            self.acc_personal.saldo, 0, "Kredyt  został udzielony, a nie powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_negative_credit_amount(self):
        decision = self.acc_personal.take_credit(-1)
        self.acc_personal.history = []
        self.assertEqual(
            self.acc_personal.saldo, 0, "Kredyt  został udzielony, a nie powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_zero_credit_amount(self):
        decision = self.acc_personal.take_credit(0)
        self.acc_personal.history = []
        self.assertEqual(
            self.acc_personal.saldo, 0, "Kredyt  został udzielony, a nie powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

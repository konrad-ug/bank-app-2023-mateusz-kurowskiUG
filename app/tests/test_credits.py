import unittest
from ..Account_company import AccountCompany
from ..Account_personal import AccountPersonal


class TestCredits(unittest.TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    example_credit = 1000

    def test_3_incoming_transfers(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        acc_personal.history = [-100, 100, 100, 100]
        decision = acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            acc_personal.saldo,
            self.example_credit,
            "Kredyt nie został udzielony, a powinien!",
        )
        self.assertTrue(decision, "Decyzja powinna być pozytywna!")

    def test_mixed_transfers(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        acc_personal.history = [-100, 100, -100, 100]
        decision = acc_personal.take_credit(self.example_credit)
        self.assertEqual(acc_personal.saldo, 0, "Kredyt  został udzielony, a powinien!")
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_five_last_positive_transactions(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        acc_personal.history = [-500, -500, 1000, self.example_credit, 1]  # sum = 1001

        decision = acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            acc_personal.saldo,
            self.example_credit,
            "Kredyt nie został udzielony, a powinien!",
        )
        self.assertTrue(decision, "Decyzja powinna być pozytywna!")

    def test_five_last_negative_transactions(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        acc_personal.history = [-500, -500, -500, -500, -500]  # sum = 1

        decision = acc_personal.take_credit(self.example_credit)
        self.assertEqual(
            acc_personal.saldo,
            0,
            "Kredyt  został udzielony, a nie powinien!",
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_no_history_credit(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        decision = acc_personal.take_credit(self.example_credit)
        acc_personal.history = []
        self.assertEqual(
            acc_personal.saldo, 0, "Kredyt  został udzielony, a nie powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_negative_credit_amount(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        decision = acc_personal.take_credit(-1)
        acc_personal.history = []
        self.assertEqual(
            acc_personal.saldo, 0, "Kredyt  został udzielony, a nie powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

    def test_zero_credit_amount(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        decision = acc_personal.take_credit(0)
        acc_personal.history = []
        self.assertEqual(
            acc_personal.saldo, 0, "Kredyt  został udzielony, a nie powinien!"
        )
        self.assertFalse(decision, "Decyzja powinna być negatywna!")

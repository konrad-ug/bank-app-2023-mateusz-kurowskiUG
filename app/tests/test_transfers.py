import unittest

from ..Account_company import AccountCompany
from ..Account_personal import AccountPersonal


class TestTransfers(unittest.TestCase):
    name = "Antoni"
    last_name = "Krawczyk"
    pesel = "12345678901"
    prom_code = "PROM_401"

    company_name = "Company"
    company_nip = "1234567890"

    test_balance = 100
    test_expense = 50
    test_correct_balance = test_balance - test_expense

    def test_transfer_no_balance(self):
        acc_personal = AccountPersonal(
            self.name, self.last_name, self.pesel, self.prom_code
        )
        acc_personal.outing_transfer(self.test_expense)
        self.assertEqual(
            acc_personal.saldo, 0, f"Saldo nie jest równe {self.test_correct_balance}"
        )

        acc_company = AccountCompany(self.company_name, self.company_nip)
        acc_company.outing_transfer(self.test_expense)
        self.assertEqual(
            acc_company.saldo, 0, f"Saldo nie jest równe {self.test_correct_balance}"
        )

    def test_transfer_incorrect_amount(self):
        acc_personal = AccountPersonal(
            self.name, self.last_name, self.pesel, self.prom_code
        )
        acc_personal.saldo = self.test_balance
        acc_personal.outing_transfer(-self.test_expense)
        self.assertEqual(
            acc_personal.saldo,
            self.test_balance,
            f"Saldo nie jest równe {self.test_balance}",
        )

        acc_company = AccountCompany(self.company_name, self.company_nip)
        acc_company.saldo = self.test_balance
        acc_company.outing_transfer(-self.test_expense)
        self.assertEqual(
            acc_company.saldo,
            self.test_balance,
            f"Saldo nie jest równe {self.test_balance}",
        )

    def test_outgoing_transfer(self):
        acc_personal = AccountPersonal(
            self.name, self.last_name, self.pesel, self.prom_code
        )
        acc_personal.saldo = self.test_balance
        acc_personal.history = []
        acc_personal.outing_transfer(self.test_expense)
        self.assertEqual(
            acc_personal.saldo,
            self.test_correct_balance,
            "Przelew nie został wykonany!",
        )
        self.assertEqual(
            acc_personal.history, [-self.test_expense], "Historia się nie zgadza!"
        ),

        acc_company = AccountCompany(self.company_name, self.company_nip)
        acc_company.saldo = self.test_balance
        acc_company.history = []
        acc_company.outing_transfer(self.test_expense)
        self.assertEqual(
            acc_company.saldo,
            self.test_correct_balance,
            f"Saldo nie jest równe {self.test_correct_balance}",
        )
        self.assertEqual(
            acc_company.history, [-self.test_expense], "Historia się nie zgadza!"
        )

    def test_receive_transfer(self):
        acc_personal = AccountPersonal(
            self.name,
            self.last_name,
            self.pesel,
        )
        acc_personal.saldo = 0
        acc_personal.history = []
        acc_personal.receive_transfer(self.test_correct_balance)
        self.assertEqual(
            acc_personal.saldo,
            self.test_correct_balance,
            f"Przelew w wysokości {self.test_correct_balance} nie dotarł!",
        )
        self.assertEqual(
            acc_personal.history,
            [self.test_correct_balance],
            "Historia się nie zgadza!",
        ),

        acc_company = AccountCompany(self.company_name, self.company_nip)
        acc_company.history = []
        acc_company.saldo = 0
        acc_company.receive_transfer(self.test_correct_balance)
        self.assertEqual(
            acc_company.saldo,
            self.test_correct_balance,
            f"Przelew w wysokości {self.test_correct_balance} nie dotarł!",
        )
        self.assertEqual(
            acc_company.history, [self.test_correct_balance], "Historia się nie zgadza!"
        ),

    def test_express_valid_transfer(self):
        acc_personal = AccountPersonal(
            self.name, self.last_name, self.pesel, self.prom_code
        )
        acc_personal.saldo = self.test_balance
        acc_personal.history = []
        acc_personal.express_outgoing_transfer(self.test_expense)
        self.assertEqual(
            acc_personal.saldo,
            self.test_balance - self.test_expense - acc_personal.express_transfer_fee,
            "Saldo się nie zgadza!",
        )
        self.assertEqual(
            acc_personal.history,
            [-self.test_expense, -acc_personal.express_transfer_fee],
            "Historia konta się nie zgadza!",
        )
        acc_company = AccountCompany(self.company_name, self.company_nip)
        acc_company.saldo = self.test_balance
        acc_company.history = []
        acc_company.express_outgoing_transfer(self.test_expense)
        self.assertEqual(
            acc_company.saldo,
            self.test_correct_balance - acc_company.express_transfer_fee,
            f"Saldo się nie zgadza!",
        )
        self.assertEqual(
            acc_company.history,
            [-self.test_expense, -acc_company.express_transfer_fee],
            "Historia konta się nie zgadza!",
        )

    def test_express_invalid_transfer(self):
        acc_personal = AccountPersonal(self.name, self.last_name, self.pesel)
        acc_personal.saldo = self.test_expense
        acc_personal.express_outgoing_transfer(self.test_expense)
        self.assertEqual(
            acc_personal.saldo,
            self.test_expense,
            "Saldo się nie zgadza!",
        )
        self.assertEqual(acc_personal.history, [], "Historia się nie zgadza!"),

        acc_company = AccountCompany(self.company_name, self.company_nip)
        acc_company.saldo = self.test_expense
        acc_company.express_outgoing_transfer(self.test_expense)
        self.assertEqual(
            acc_company.saldo,
            self.test_expense,
            f"Saldo się nie zgadza!",
        )
        self.assertEqual(acc_company.history, [], "Historia się nie zgadza!"),

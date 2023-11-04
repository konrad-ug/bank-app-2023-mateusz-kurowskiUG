import unittest
from parameterized import *
from ..Account_personal import AccountPersonal
from ..Account_company import AccountCompany


class TestCreateBankAccountPersonal(unittest.TestCase):
    def check_names(self, acc: AccountPersonal, name, last_name):
        self.assertEqual(acc.name, name, f"Name is equal {acc.name} instead of {name}!")
        self.assertEqual(
            acc.last_name,
            last_name,
            f"Last name is equal {acc.last_name} instead of {last_name}!",
        )

    def check_balance(self, acc: AccountPersonal, balance):
        self.assertEqual(
            acc.saldo, balance, f"Balance is equal {acc.saldo} instead of {balance}!"
        )

    def check_pesel(self, acc: AccountPersonal, pesel, is_pesel_valid):
        if is_pesel_valid:
            self.assertEqual(
                acc.pesel,
                pesel,
                "Pesel nie istnieje!",
            )
        else:
            self.assertEqual(
                acc.pesel,
                "PESEL not valid!",
                "Pesel nie istnieje!",
            )

    @parameterized.expand(
        [
            ("Dariusz", "Jan", "12345678901", True, 0),
            # INVALID PESEL
            ("", "", "", False, 0),
            ("Dariusz", "Jan", "12345678901234567", False, 0),
            ("Dariusz", "Jan", "500", False, 0, "PROM_997"),  # pesel INVALID
            ("Darius", "Jan", "11990112345", False, 0, "PROM_997"),  # 1901
            ("Darius", "Jan", "99240343666", False, 0, "PROM_997"),  # 1901
            # VALID CODES
            ("Dariusz", "Jan", "12345678901", True, 50, "PROM_XYZ"),  # 2012
            ("Dariusz", "Jan", "00220791395", True, 50, "PROM_401"),  # 2000r.
            ("Dariusz", "Jan", "60020723813", True, 50, "PROM_997"),  # 1960r.
            ("Dariusz", "Jan", "50020763618", True, 0, "PROM_997"),  # 1950r.
            ("Dariusz", "Jan", "11110112345", True, 0, "PROM_111"),  # 1901r.
            # INVALID CODES
            ("Dariusz", "Jan", "12345678901", True, 0, "PRSADASSAD"),  # 2012
            ("Dariusz", "Jan", "12345678901", True, 0, "XPROM_401X"),  # 2012
            ("Dariusz", "Jan", "12345678901", True, 0, "PR0M_XYZ"),  # 2012
            ("Dariusz", "Jan", "70020796359", True, 0, "PR12M_1"),  # 1970r.
        ]
    )
    def test_creating_basic_account(
        self,
        first_name,
        last_name,
        pesel,
        is_pesel_valid,
        valid_balance=0,
        promo_code=None,
    ):
        acc_personal = AccountPersonal(first_name, last_name, pesel, promo_code)
        self.check_names(acc_personal, first_name, last_name)
        self.check_pesel(acc_personal, pesel, is_pesel_valid)
        self.check_balance(acc_personal, valid_balance)

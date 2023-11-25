import unittest
from parameterized import *
from ..Account_company import AccountCompany


class TestBasicCompanyMethods(unittest.TestCase):
    name = "Januszex"
    nip = "1234567890"
    balance = 0
    acc = AccountCompany(name, nip)

    def test_get(self):
        self.assertEqual(self.acc["name"],self.name,"Get name not working!")
    
    def test_dict(self):
        dicted = {"name": self.name, "nip": self.nip, "balance": self.balance}
        self.assertEqual(self.acc.__dict__(), dicted, "__dict__ did't work!")

    def test_str(self):
        self.assertEqual(
            self.acc.__str__(), f"{self.acc.name} {self.nip} {self.balance}"
        )

    def test_equal(self):
        second_acc = AccountCompany(self.name, self.nip)
        self.assertEqual(self.acc, second_acc, "__eq__ does not work!")


class CreateCompanyAccount(unittest.TestCase):
    @parameterized.expand(
        [
            ("Mkurowski", "1234567890", True),
            ("", "", False),
            ("Mkurowski", "123", False),
        ]
    )
    def test_create_company_account(self, name, nip, is_nip_valid):
        self.acc_company = AccountCompany(name, nip)
        if is_nip_valid:
            self.assertEqual(
                self.acc_company.nip, nip, f"NIP: {nip} nie został zapisany!"
            )
        else:
            self.assertEqual(
                self.acc_company.nip,
                "Niepoprawny NIP!",
                f"NIP: {nip} nie jest prawidłowy!",
            )
        self.assertEqual(
            self.acc_company.name, name, f"Nazwa: `{name}` nie została zapisana"
        )

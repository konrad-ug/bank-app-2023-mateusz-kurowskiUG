import unittest
from parameterized import *
from ..Account_company import AccountCompany


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

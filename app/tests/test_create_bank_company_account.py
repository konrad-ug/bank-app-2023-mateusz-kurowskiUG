from unittest import TestCase, mock
from parameterized import *
from app.Account_company import AccountCompany


class TestBasicCompanyMethods(TestCase):
    name = "Januszex"
    nip = "8461627563"
    balance = 0

    @mock.patch("app.Account_company.AccountCompany.validate_nip")
    def setUp(self, mock_object):
        mock_object.return_value = True
        self.acc = AccountCompany(self.name, self.nip)

    def test_get(self):
        self.assertEqual(self.acc["name"], self.name, "Get name not working!")

    def test_dict(self):
        dicted = {"name": self.name, "nip": self.nip, "balance": self.balance}
        self.assertEqual(self.acc.__dict__(), dicted, "__dict__ did't work!")

    def test_str(self):
        self.assertEqual(
            self.acc.__str__(), f"{self.acc.name} {self.nip} {self.balance}"
        )

    @mock.patch("app.Account_company.AccountCompany.validate_nip")
    def test_equal(self, mock_object):
        mock_object.return_value = True
        second_acc = AccountCompany(self.name, self.nip)
        self.assertEqual(self.acc, second_acc, "__eq__ does not work!")


class TestCreateCompanyAccount(TestCase):

    @parameterized.expand([
        ("Mkurowski", "8461627563", True, False),
        ("Mkurowski", "8461627562", False, True),
        ("", "", False, False),
        ("Mkurowski", "123", False, False),
        ("Mkurowski", "5841932578", True, False),
    ])
    @mock.patch("app.Account_company.AccountCompany.validate_nip")
    def test_create_company_account(
            self,  name, nip, is_nip_valid, raises_error, mock_validate_nip
    ):
        mock_validate_nip.return_value = is_nip_valid

        if raises_error:
            with self.assertRaises(ValueError):
                AccountCompany(name, nip)
        else:
            acc_company = AccountCompany(name, nip)

            if is_nip_valid:
                self.assertEqual(acc_company.nip, nip,
                                 f"NIP: {nip} not saved!")

            else:
                self.assertEqual(
                    acc_company.nip, "Niepoprawny NIP!", f"NIP: {
                        nip} is not valid!"
                )
                self.assertEqual(
                    acc_company.name, name, f"Name: '{name}' not saved!"
                )

# dla wyższej oceny 100% coverage (lab09)


class Test_For_Coverage(TestCase):
    name = "Januszex"
    nip = "8461627563"

    @mock.patch("app.Account_company.requests.get")
    def test_for_coverage(self, mocked):
        mocked.return_value.text = "test"
        mocked.return_value.status_code = 200
        acc = AccountCompany(self.name, self.nip)
        self.assertEqual(acc.name, self.name, "Name has not been saved")

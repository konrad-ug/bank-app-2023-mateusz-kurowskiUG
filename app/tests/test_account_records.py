import unittest
from parameterized import *
from ..AccountsRecord import AccountsRecord
from ..Account_personal import AccountPersonal
import copy


class TestAccountRecords(unittest.TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "65112238477"
    second_pesel = "71081619681"
    dicted = {"name": name, "last_name": last_name, "pesel": pesel, "balance": 0}

    @classmethod
    def setUpClass(cls):
        cls.acc = AccountPersonal(cls.name, cls.last_name, cls.pesel)
        AccountsRecord.accounts = [cls.acc]

    def setUp(self):
        self.acc = AccountPersonal(self.name, self.last_name, self.pesel)
        AccountsRecord.accounts = [self.acc]

    def test_adding_accounts(self):
        AccountsRecord.add_acc_to_record(self.acc)
        self.assertEqual(
            AccountsRecord.accounts,
            [self.acc, self.acc],
            f"Account: {self.acc} hasn't been added!",
        )
        self.assertEqual(
            AccountsRecord.number_of_acc(),
            len(AccountsRecord.accounts),
            f"The length of accouts does not match value {AccountsRecord.number_of_acc()}",
        )

    def test_searching_valid_account(self):
        found = AccountsRecord.search_for_acc(self.pesel)

        self.assertIsNotNone(found, "Account should exist!")
        if found is not None:
            self.assertEqual(
                found.name,
                self.acc.name,
                f"Found acc name: {found.name} does not match with {self.acc.name}",
            )
            self.assertEqual(
                found.last_name,
                self.acc.last_name,
                f"Found acc last name: {found.last_name} does not match with {self.acc.last_name}",
            )
            self.assertEqual(
                found.pesel,
                self.acc.pesel,
                f"Found acc pesel: {found.pesel} does not match with {self.acc.pesel}",
            )

    def test_searching_invalid_account(self):
        found = AccountsRecord.search_for_acc("11")
        self.assertIsNone(found, "Acc shouldn't exist!")

    def test_deleting_valid_account(self):
        AccountsRecord.delete_acc(self.acc.pesel)
        self.assertEqual(AccountsRecord.accounts, [], f"record should be empty!")

    def test_deleting_invalid_account(self):
        prev_record = AccountsRecord.accounts
        AccountsRecord.delete_acc("")
        self.assertEqual(
            AccountsRecord.accounts, prev_record, f"Invalid acc has been deleted!"
        )

    def test_counting_accounts(self):
        lenght_of_AR = len(AccountsRecord.accounts)
        self.assertEqual(lenght_of_AR, AccountsRecord.number_of_acc())

    def test_modyfying_valid_account(self):
        test_props = {"name": "Ja", "last_name": "Kowalsk", "pesel": "65112238478"}
        result = AccountPersonal(**test_props)
        updated = AccountsRecord.modify_acc(self.pesel, test_props)
        self.assertEqual(updated, result, "Account hasn't been updated!")

    def test_modyfying_invalid_account(self):
        updated = AccountsRecord.modify_acc("pesel", {"name": "brak"})
        self.assertEqual(
            updated, None, "Modyfying acc does not work! Found some fake acc!"
        )

    @classmethod
    def tearDownClass(cls):
        AccountsRecord.accounts.clear()

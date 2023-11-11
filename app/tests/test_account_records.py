import unittest
from parameterized import *
from ..AccountsRecord import AccountsRecord
from ..Account_personal import AccountPersonal


class TestAccountRecords(unittest.TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    acc = AccountPersonal(name, last_name, pesel)

    @classmethod
    def SetUpClass(cls):
        cls.account = AccountPersonal(cls.name, cls.last_name, cls.pesel)

    def test_adding_accounts(cls, self):
        AccountsRecord.add_acc_to_record(cls)
        self.assertEqual(AccountsRecord.accounts, [self.acc, self.acc])

    def test_searching_accounts(self):
        self.assertEqual(AccountsRecord.search_for_acc(self.pesel), self.acc)

    def test_deleting_accounts(self):
        AccountsRecord.delete_acc(self.pesel)
        self.assertEqual(AccountsRecord.accounts, [])

    def test_counting_accounts(self):
        self.assertEqual(AccountsRecord.number_of_acc(), 1)

    @classmethod
    def tearDownClass(cls):
        AccountsRecord.accounts = []

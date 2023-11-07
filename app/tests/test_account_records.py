import unittest
from parameterized import *
from ..AccountsRecord import AccountsRecord
from ..Account_personal import AccountPersonal


@classmethod
class TestAccountRecords(unittest.TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    acc = AccountPersonal(name, last_name, pesel)


    @classmethod
    def SetUpClass(cls):
        account = AccountPersonal(cls.name, cls.last_name, cls.pesel)

    def test_adding_accounts(self):
        ...

    def test_searching_accounts(self, accounts_to_add, expected_register):
        ...

    def test_deleting_accounts(self, accounts_to_add, expected_register):
        ...

    def test_counting_accounts(self, accounts_to_add, expected_register):
        ...

    @classmethod
    def tearDownClass(cls):
        AccountsRecord.accounts = []

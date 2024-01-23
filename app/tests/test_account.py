from unittest import TestCase
from app.Account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account()

    def test_eq__(self):
        self.assertEqual(
            self.account, self.account, "__eq__ method of Account class failed"
        )

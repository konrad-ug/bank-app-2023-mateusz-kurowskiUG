import unittest

from ..Account import Account
from ..Account_company import Account_Company
from ..Account_personal import Account_Personal


class TestTransfers(unittest.TestCase):
    name = "Antoni"
    last_name = "Krawczyk"
    pesel = "12345678901"
    prom_code = "PROM_401"

    name2 = "Jan"
    last_name2 = "Kowalski"
    pesel2 = "12345678902"
    prom_code2 = "PROM_401"

    def transfer_no_balance(self):
        acc1 = Account_Personal(self.name, self.last_name, self.pesel, self.prom_code)
        acc1.saldo = 0
        acc1.transfer(50)
        self.assertEqual(acc1.saldo, 0, "Saldo nie jest równe 0")

    def transfer_incorrect_amount(self):
        acc1 = Account_Personal(self.name, self.last_name, self.pesel, self.prom_code)
        acc1.transfer(-50)
        self.assertEqual(acc1.saldo, 0, "Saldo nie jes")
        self.assertEqual(acc1.saldo, 0, "Saldo nie jest równe 0")

    def outgoing_transfer(self):
        acc1 = Account_Personal(self.name, self.last_name, self.pesel, self.prom_code)
        acc1.saldo = 100
        acc1.transfer(50)
        self.assertEqual(acc1.saldo, 50, "Przelew nie został wykonany!")

    def receive_transfer(self):
        acc1 = Account_Personal(self.name, self.last_name, self.pesel, self.prom_code)
        acc1.receive_transfer(50)
        self.assertEqual(acc1.saldo, 50, "Przelew nie dotarł!")

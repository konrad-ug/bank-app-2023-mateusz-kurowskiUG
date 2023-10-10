import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    last_name = "Januszewski"
    pesel = "12345678901"
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.name, self.last_name,self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.name, "Imie nie zostało zapisane!")
        self.assertEqual(
            pierwsze_konto.nazwisko, self.last_name, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
    # tutaj proszę dodawać nowe testy

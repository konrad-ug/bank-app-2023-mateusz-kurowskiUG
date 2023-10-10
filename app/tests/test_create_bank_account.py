import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    last_name = "Januszewski"
    pesel = "12345678901"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.name, self.last_name, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.name, "Imie nie zostało zapisane!")
        self.assertEqual(
            pierwsze_konto.nazwisko, self.last_name, "Nazwisko nie zostało zapisane!"
        )
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Pesel nie został zapisany!")
        self.assertEqual(len(pierwsze_konto.pesel), 11, "Pesel nie ma 11 znaków!")

    def test_tworzenie_konta_z_krotkim_pesel(self):
        konto = Konto(self.name, self.last_name, "1234")
        self.assertEqual(
            konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!"
        )

    def test_tworzenie_konta_z_dlugim_pesel(self):
        konto = Konto(self.name, self.last_name, "123456789123456789123456789")
        self.assertEqual(
            konto.pesel, "Niepoprawny pesel!", "Pesel nie został zapisany!"
        )

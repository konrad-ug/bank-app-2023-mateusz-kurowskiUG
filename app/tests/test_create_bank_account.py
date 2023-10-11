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

    def test_poprawny_kod_rabatowy(self):
        konto = Konto(self.name, self.last_name, self.pesel, "PROM_401")
        self.assertEqual(konto.saldo, 50, "Saldo nie jest równe 50!")

    def test_niepoprawny_kod_rabatowy(self):
        kod_rabatowy = "EASDASSAD_123"
        konto = Konto(self.name, self.last_name, self.pesel, kod_rabatowy)
        self.assertEqual(konto.saldo, 0, "Saldo nie jest równe 0!")

    def test_osoba_urodzona_w_2000_r(self):
        konto = Konto(self.name, self.last_name, "00220791395", "PROM_997")
        self.assertEqual(
            konto.znajdz_rok_urodzenia(), 2000, "Rok urodzenia nie jest równy 2000!"
        )

    def test_osoba_urodzona_w_1960_r(self):
        konto = Konto(self.name, self.last_name, "60020723813", "PROM_997")
        self.assertEqual(
            konto.znajdz_rok_urodzenia(), 1960, "Rok urodzenia nie jest równy 1960!"
        )
        self.assertEqual(konto.saldo, 50, "Saldo nie jest równe 0!")

    def test_osoba_urodzona_w_1950_r(self):
        konto = Konto(self.name, self.last_name, "50020763618", "PROM_997")
        self.assertEqual(
            konto.znajdz_rok_urodzenia(), 1950, "Rok urodzenia nie jest równy 1950!"
        )
        self.assertEqual(konto.saldo, 0, "Saldo nie jest równe 0!")

    def test_osoba_niepoprawny_pesel(self):
        konto = Konto(self.name, self.last_name, "1237890", "PROM_997")
        self.assertEqual(
            konto.znajdz_rok_urodzenia(),
            0,
            "Pesel powinien być niepoprawny!",
        )
        self.assertEqual(konto.saldo, 0, "Saldo nie jest równe 0!")

    def test_osoba_urodzona_w_1970_r_zly_kod(self):
        konto = Konto(self.name, self.last_name, "70020796359", "PR12M_1")
        self.assertEqual(
            konto.znajdz_rok_urodzenia(),
            1970,
            "Pesel się nie zgadza!",
        )
        self.assertEqual(konto.saldo, 0, "Saldo nie jest równe 0!")

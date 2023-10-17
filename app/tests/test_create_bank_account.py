import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    name = "Dariusz"
    last_name = "Januszewski"
    pesel = "12345678901"

    def porownaj_dane(self, konto: Konto, imie, nazwisko):
        self.assertEqual(konto.imie, imie, "Imie nie zostało zapisane!")
        self.assertEqual(konto.nazwisko, nazwisko, "Nazwisko nie zostało zapisane!")

    def porownaj_balans(self, konto: Konto, balans):
        self.assertEqual(konto.saldo, balans, f"Saldo nie jest równe {balans}")

    def porownaj_pesel(self, konto: Konto, pesel):
        self.assertEqual(
            konto.pesel,
            pesel,
            "Pesel nie istnieje!",
        )

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.name, self.last_name, self.pesel)
        self.porownaj_dane(pierwsze_konto, pierwsze_konto.imie, pierwsze_konto.nazwisko)
        self.porownaj_balans(pierwsze_konto, 0)
        self.porownaj_pesel(pierwsze_konto, self.pesel)

    def test_tworzenie_konta_z_krotkim_pesel(self):
        konto = Konto(self.name, self.last_name, "1234")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "Niepoprawny pesel!")
        self.porownaj_balans(konto, 0)

    def test_tworzenie_konta_z_dlugim_pesel(self):
        konto = Konto(self.name, self.last_name, "123456789123456789123456789")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "Niepoprawny pesel!")
        self.porownaj_balans(konto, 0)

    def test_poprawny_kod_rabatowy(self):
        konto = Konto(self.name, self.last_name, self.pesel, "PROM_401")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_balans(konto, 50)
        self.porownaj_pesel(konto, self.pesel)

    def test_niepoprawny_kod_rabatowy(self):
        kod_rabatowy = "EASDASSAD_123"
        konto = Konto(self.name, self.last_name, self.pesel, kod_rabatowy)
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_balans(konto, 0)
        self.porownaj_dane(konto, self.name, self.last_name)

    def test_osoba_urodzona_w_2000_r(self):
        konto = Konto(self.name, self.last_name, "00220791395", "PROM_997")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "00220791395")
        self.porownaj_balans(konto, 50)

    def test_osoba_urodzona_w_1960_r(self):
        konto = Konto(self.name, self.last_name, "60020723813", "PROM_997")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "60020723813")
        self.porownaj_balans(konto, 50)

    def test_osoba_urodzona_w_1950_r(self):
        konto = Konto(self.name, self.last_name, "50020763618", "PROM_997")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "50020763618")
        self.porownaj_balans(konto, 0)

    def test_osoba_niepoprawny_pesel(self):
        konto = Konto(self.name, self.last_name, "1237890", "PROM_997")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "Niepoprawny pesel!")
        self.porownaj_balans(konto, 0)

    def test_osoba_urodzona_w_1970_r_zly_kod(self):
        konto = Konto(self.name, self.last_name, "70020796359", "PR12M_1")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "70020796359")
        self.porownaj_balans(konto, 0)

    # zakładam, że bank nie zezwala na zakładanie kont osobom nie urodzonym.
    def test_osoba_urodzona_w_2099_r(self):
        konto = Konto(self.name, self.last_name, "99240343666", "PR12M_1")
        self.porownaj_dane(konto, self.name, self.last_name)
        self.porownaj_pesel(konto, "Niepoprawny pesel!")
        self.porownaj_balans(konto, 0)

import unittest

from ..Account import Account
from ..Account_personal import Account_Personal
from ..Account_company import Account_Company


class TestCreateBankAccount_Personal(unittest.TestCase):
    name = "Dariusz"
    last_name = "Januszewski"
    pesel = "12345678901"

    def porownaj_dane(self, acc: Account_Personal, name, last_name):
        self.assertEqual(acc.name, name, "name nie zostało zapisane!")
        self.assertEqual(acc.last_name, last_name, "last_name nie zostało zapisane!")

    def porownaj_balans(self, acc: Account_Personal, balans):
        self.assertEqual(acc.saldo, balans, f"Saldo nie jest równe {balans}")

    def porownaj_pesel(self, acc: Account_Personal, pesel):
        self.assertEqual(
            acc.pesel,
            pesel,
            "Pesel nie istnieje!",
        )

    def test_tworzenie_konta(self):
        acc = Account_Personal(self.name, self.last_name, self.pesel)
        self.porownaj_dane(
            acc,
            self.name,
            self.last_name,
        )
        self.porownaj_balans(acc, 0)
        self.porownaj_pesel(acc, self.pesel)

    def test_tworzenie_konta_z_krotkim_pesel(self):
        acc = Account_Personal(self.name, self.last_name, "1234")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "Niepoprawny pesel!")
        self.porownaj_balans(acc, 0)

    def test_tworzenie_konta_z_dlugim_pesel(self):
        acc = Account_Personal(self.name, self.last_name, "123456789123456789123456789")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "Niepoprawny pesel!")
        self.porownaj_balans(acc, 0)

    def test_poprawny_kod_rabatowy(self):
        acc = Account_Personal(self.name, self.last_name, self.pesel, "PROM_401")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_balans(acc, 50)
        self.porownaj_pesel(acc, self.pesel)

    def test_niepoprawny_kod_rabatowy(self):
        kod_rabatowy = "EASDASSAD_123"
        acc = Account_Personal(self.name, self.last_name, self.pesel, kod_rabatowy)
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_balans(acc, 0)
        self.porownaj_dane(acc, self.name, self.last_name)

    def test_osoba_urodzona_w_2000_r(self):
        acc = Account_Personal(self.name, self.last_name, "00220791395", "PROM_997")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "00220791395")
        self.porownaj_balans(acc, 50)

    def test_osoba_urodzona_w_1960_r(self):
        acc = Account_Personal(self.name, self.last_name, "60020723813", "PROM_997")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "60020723813")
        self.porownaj_balans(acc, 50)

    def test_osoba_urodzona_w_1950_r(self):
        acc = Account_Personal(self.name, self.last_name, "50020763618", "PROM_997")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "50020763618")
        self.porownaj_balans(acc, 0)

    def test_osoba_niepoprawny_pesel(self):
        acc = Account_Personal(self.name, self.last_name, "1237890", "PROM_997")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "Niepoprawny pesel!")
        self.porownaj_balans(acc, 0)

    def test_osoba_urodzona_w_1970_r_zly_kod(self):
        acc = Account_Personal(self.name, self.last_name, "70020796359", "PR12M_1")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "70020796359")
        self.porownaj_balans(acc, 0)

    # zakładam, że bank nie zezwala na zakładanie kont osobom nie urodzonym.
    def test_osoba_urodzona_w_2099_r(self):
        acc = Account_Personal(self.name, self.last_name, "99240343666", "PR12M_1")
        self.porownaj_dane(acc, self.name, self.last_name)
        self.porownaj_pesel(acc, "Niepoprawny pesel!")
        self.porownaj_balans(acc, 0)


class CreateCompanyAccount_Personal(unittest.TestCase):
    name = "Mkurowski"
    nip = "1234567890"
    invalid_nip = nip[1:5]

    def create_valid_Account_Personal(self):
        acc = Account_Personal(self.name, self.nip)
        self.assertEqual(self.name, acc.name, "Nazwa nie została zapisana!")
        self.assertEqual(self.nip, acc.nip, "Nip nie został zapisany!")

    def create_invalid_Account_Personal(self):
        acc = Account_Personal(self.name, self.invalid_nip)
        self.assertEqual(self.name, acc.name, "Nazwa nie została zapisana!")
        self.assertEqual(acc.nip, "Nieporawny NIP!", "NIP powinien być niepoprawny!")

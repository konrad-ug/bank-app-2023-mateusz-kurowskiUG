import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if len(pesel) != 11:
            self.pesel = "Niepoprawny pesel!"
        else:
            self.pesel = pesel

        if (
            kod_rabatowy
            and self.czy_poprawny_kod_rabatowy(kod_rabatowy)
            and self.znajdz_rok_urodzenia() >= 1960
        ):
            self.saldo = 50

    def czy_poprawny_kod_rabatowy(self, kod_rabatowy):
        return kod_rabatowy and re.match("^PROM_...$", kod_rabatowy) is not None

    def znajdz_rok_urodzenia(self):
        if self.pesel == "Niepoprawny pesel!":
            return 0
        else:
            match self.pesel[2]:
                case "2":
                    return int(f"20{self.pesel[0:2]}")
                case "3":
                    return int(f"20{self.pesel[0:2]}")
                case "0":
                    return int(f"19{self.pesel[0:2]}")
                case "1":
                    return int(f"19{self.pesel[0:2]}")

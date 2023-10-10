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

        if kod_rabatowy and self.czy_poprawny_kod_rabatowy(kod_rabatowy):
            self.saldo = 50

    def czy_poprawny_kod_rabatowy(self, kod_rabatowy):
        return kod_rabatowy and re.match("^PROM_...$", kod_rabatowy) is not None

    def find_rok_urodzenia(self):
        if pesel == "Niepoprawny pesel!":
            return "Niepoprawny pesel!"
        else:
            return self.pesel[0:2]

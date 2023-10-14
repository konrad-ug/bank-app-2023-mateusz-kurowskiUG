import re, datetime


class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        if self.validate_pesel(pesel):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.promoBank(kod_rabatowy):
            self.saldo = 50

    def czy_poprawny_kod_rabatowy(self, kod_rabatowy):
        return kod_rabatowy and re.match("^PROM_...$", kod_rabatowy) is not None

    def validate_pesel(self, pesel):
        if len(pesel) != 11:
            return False
        else:
            found_year = self.znajdz_rok_urodzenia(pesel)
            if found_year > datetime.date.today().year:
                return False
            elif found_year is None:
                return False
            else:
                return True

    def znajdz_rok_urodzenia(self, pesel):
        match pesel[2]:
            case "2":
                return int(f"20{pesel[0:2]}")
            case "3":
                return int(f"20{pesel[0:2]}")
            case "0":
                return int(f"19{pesel[0:2]}")
            case "1":
                return int(f"19{pesel[0:2]}")
            case default:
                return None

    def promoBank(self, kod_rabatowy=None):
        if self.pesel != "Niepoprawny pesel!" and kod_rabatowy is not None:
            return (
                self.czy_poprawny_kod_rabatowy(kod_rabatowy)
                and self.znajdz_rok_urodzenia(self.pesel) >= 1960
            )
        else:
            return False

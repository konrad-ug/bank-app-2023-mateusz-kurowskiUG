import re, datetime
from .Account import Account


class Account_Personal(Account):
    def __init__(self, name, last_name, pesel, promo_code=None):
        express_transfer_fee = 1
        self.name = name
        self.last_name = last_name
        self.saldo = 0
        if self.validate_pesel(pesel):
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

        if self.promoBank(promo_code):
            self.saldo = 50

    def czy_poprawny_promo_code(self, promo_code):
        return promo_code and re.match("^PROM_...$", promo_code) is not None

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

    def promoBank(self, promo_code=None):
        if self.pesel != "Niepoprawny pesel!" and promo_code is not None:
            return (
                self.czy_poprawny_promo_code(promo_code)
                and self.znajdz_rok_urodzenia(self.pesel) >= 1960
            )
        else:
            return False

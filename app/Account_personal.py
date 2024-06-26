import re
import datetime
from typing import Any
from app.Account import Account

try:  # pragma: no cover
    from typing import Self  # pragma: no cover
except ImportError:  # pragma: no cover
    from typing_extensions import Self  # pragma: no cover


class AccountPersonal(Account):
    def __init__(self, name, last_name, pesel, promo_code=None):
        self.express_transfer_fee = 1
        self.name = name
        self.last_name = last_name
        self.balance = 0
        self.email_msg = "Twoja historia konta to:"
        if self.validate_pesel(pesel):
            self.pesel = pesel
        else:
            self.pesel = "PESEL not valid!"

        if self.promoBank(promo_code):
            self.balance = 50

    def __dict__(self):
        return {
            # "type": "Personal",
            "name": self.name,
            "last_name": self.last_name,
            "pesel": self.pesel,
            "balance": self.balance,
            "history": self.history,
        }

    def __str__(self) -> str:
        return f"{self.name} {self.last_name} {self.balance}"

    def __eq__(self, __value: Self) -> bool:
        return (
            self.history == __value.history
            and self.name == __value.name
            and self.balance == __value.balance
            and self.express_transfer_fee == __value.express_transfer_fee
            and self.pesel == __value.pesel
            and self.last_name == __value.last_name
        )

    def czy_poprawny_promo_code(self, promo_code):
        return promo_code and re.match("^PROM_...$", promo_code) is not None

    def validate_pesel(self, pesel):
        if len(pesel) != 11:
            return False
        found_year = self.znajdz_rok_urodzenia(pesel)
        if found_year is None or found_year > datetime.date.today().year:
            return False
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
        if self.pesel != "PESEL not valid!" and promo_code is not None:
            return (
                self.czy_poprawny_promo_code(promo_code)
                and self.znajdz_rok_urodzenia(self.pesel) >= 1960
            )
        else:
            return False

    def check_three_last_transactions(self):
        last_three = self.history[-3:]
        if all(element > 0 for element in last_three) and len(last_three) == 3:
            return True
        return False

    def check_five_last_transactions(self, val):
        last_five = self.history[-5:]
        if sum(last_five) > val and len(last_five) == 5:
            return True
        return False

    def take_loan(self, amount):
        if amount <= 0:
            return False
        if self.check_three_last_transactions() or self.check_five_last_transactions(
            amount
        ):
            self.balance += amount
            return True
        return False

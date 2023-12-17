from typing import Self
from app.Account import Account
import datetime
import requests

MF_PROD = "https://wl-api.mf.gov.pl/"
MF_TEST = "https://wl-test.mf.gov.pl/"


class AccountCompany(Account):
    def __init__(self, name, nip):
        super().__init__()
        self.express_transfer_fee = 5
        self.name = name
        self.email_msg = "Historia konta Twojej firmy to:"

        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            if self.validate_nip(nip):
                self.nip = nip
            else:
                raise ValueError

    def __str__(self):
        return f"{self.name} {self.nip} {self.balance}"

    def __dict__(self):
        return {
            "name": self.name,
            "nip": self.nip,
            "balance": self.balance,
        }

    def __eq__(self, __value: Self) -> bool:
        return (
            self.balance == __value.balance
            and self.name == __value.name
            and self.express_transfer_fee == __value.express_transfer_fee
            and self.history == __value.history
            and self.nip == __value.nip
        )

    def validate_nip(self, nip, BANK_APP_MF_URL=MF_TEST):
        date = datetime.datetime.today().strftime("%Y-%m-%d")
        response = requests.get(
            f"{BANK_APP_MF_URL}/api/search/nip/{nip}", params={"date": date}
        )
        print(response.text)
        return response.status_code == 200

    def take_credit(self, amount):
        if amount <= 0:
            return False
        if self.validate_company_credit(amount):
            self.balance += amount
            return True
        return False

    # check if the balance is at least twice as big as the requested value of credit
    def validate_requested_amount(self, amount):
        return True if self.balance >= 2 * amount else False

    # check if there is at least one transfer to ZUS in the history of account
    def check_transfer_to_ZUS(self):
        return True if self.history.count(-1775) > 0 else False

    # two above validation functions combined
    def validate_company_credit(self, amount):
        return self.validate_requested_amount(amount) and self.check_transfer_to_ZUS()

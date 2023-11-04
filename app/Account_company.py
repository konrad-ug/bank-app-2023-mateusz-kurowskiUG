from .Account import Account


class AccountCompany(Account):
    def __init__(self, name, nip):
        super().__init__()
        self.express_transfer_fee = 5
        self.name = name
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip

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

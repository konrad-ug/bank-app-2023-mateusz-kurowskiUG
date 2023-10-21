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

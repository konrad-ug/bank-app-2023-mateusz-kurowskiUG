from .Account import Account


class Account_Company(Account):
    def __init__(self, name, nip):
        super().__init__()
        self.name = name
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip

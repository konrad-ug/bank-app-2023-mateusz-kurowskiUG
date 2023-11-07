from .Account_personal import AccountPersonal


class AccountsRecord:
    accounts = []

    @classmethod
    def add_acc_to_record(cls, acc):
        if type(acc) == AccountPersonal:
            cls.accounts.append(acc)

    @classmethod
    def search_for_acc(cls, pesel):
        return filter(acc for acc in cls.accounts if acc.pesel == pesel)

    @classmethod
    def number_of_acc(
        cls,
    ):
        return len(cls.accounts)

    @classmethod
    def delete_acc(cls, pesel):
        cls.accounts = list(filter(acc for acc in cls.accounts if acc.pesel != pesel))

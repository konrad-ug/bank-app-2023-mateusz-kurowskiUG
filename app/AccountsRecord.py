from .Account_personal import AccountPersonal
import json


class AccountsRecord:
    accounts = []

    def __dict__(self):
        return [vars(i) for i in self.accounts]

    def toJSON():
        return json.dumps(cls, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @classmethod
    def add_acc_to_record(cls, acc):
        if isinstance(acc, AccountPersonal):
            cls.accounts.append(acc)

    @classmethod
    def search_for_acc(cls, pesel):
        found = next((acc for acc in cls.accounts if acc.pesel == pesel), None)

        return found

    @classmethod
    def number_of_acc(
        cls,
    ):
        return len(cls.accounts)

    @classmethod
    def delete_acc(cls, pesel):
        filtered = list(filter(lambda x: x.pesel != pesel, cls.accounts))
        cls.accounts = filtered

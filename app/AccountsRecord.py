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
    def modify_acc(cls, pesel, key, new_value):
        found = cls.search_for_acc(pesel)
        if found is not None:
            found[key] = new_value
            return found
        return None

    @classmethod
    def number_of_acc(
        cls,
    ):
        return len(cls.accounts)

    @classmethod
    def delete_acc(cls, pesel):
        num_prev = cls.number_of_acc()
        filtered = list(filter(lambda x: x.pesel != pesel, cls.accounts))
        cls.accounts = filtered
        num_curr = cls.number_of_acc()
        if num_curr == num_prev:
            return False
        return True

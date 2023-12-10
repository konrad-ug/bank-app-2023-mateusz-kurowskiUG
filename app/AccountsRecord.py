from app.Account_personal import AccountPersonal
import json


class AccountsRecord:
    accounts = []

    def __dict__(self):  # pragma: no cover
        return [vars(i) for i in self.accounts]

    @classmethod
    def add_acc_to_record(cls, acc):
        if isinstance(acc, AccountPersonal):
            cls.accounts.append(acc)

    @classmethod
    def search_for_acc(cls, pesel):
        for acc in cls.accounts:
            if acc.pesel == pesel:
                return acc
        return None

    @classmethod
    def modify_acc(cls, pesel, obj_props):
        found = cls.search_for_acc(pesel)
        if found is None:
            return None
        for key, item in obj_props.items():
            found[f"{key}"] = item
        return found

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

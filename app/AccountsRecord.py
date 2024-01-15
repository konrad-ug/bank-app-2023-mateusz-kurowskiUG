from app.Account_personal import AccountPersonal
from pymongo import MongoClient
import os


class AccountsRecord:
    accounts = []
    client = MongoClient("localhost", 27017)
    db = client["mydb"]
    collection = db["accounts"]

    @classmethod
    def add_acc_to_record(cls, acc):
        if isinstance(acc, AccountPersonal):
            cls.accounts.append(acc)
            return True
        return False

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

    @classmethod
    def load(cls):
        cls.accounts = []
        for account in cls.collection.find():
            try:
                name = account["name"]
                last_name = account["last_name"]
                pesel = account["pesel"]
                balance = account["balance"]
                history = account["history"]
                acc = AccountPersonal(name, last_name, pesel)
                acc.balance = balance
                acc.history = history
                cls.add_acc_to_record(acc)
            except KeyError:
                pass
        return cls.accounts

    @classmethod
    def save(cls):
        cls.collection.delete_many({})
        to_save = [acc.__dict__() for acc in cls.accounts]
        if len(to_save):
            cls.collection.insert_many(to_save)
        results = cls.collection.find({})
        parsed = [
            {
                "name": acc["name"],
                "last_name": acc["last_name"],
                "history": acc["history"],
                "balance": acc["balance"],
                "pesel": acc["pesel"],
            }
            for acc in results
        ]
        return list(parsed)

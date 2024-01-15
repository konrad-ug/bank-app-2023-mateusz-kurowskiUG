import unittest
import requests
from app.Account_personal import AccountPersonal


class TestApiZTransfers(unittest.TestCase):
    name = "Ja"
    last_name = "Kowalsk"
    pesel = "08303157990"
    url = "http://localhost:5000/api/accounts"
    acc = AccountPersonal(name, last_name, pesel)
    acc_json = acc.__dict__()
    start_balance = 100

    def getAcc(self):
        return requests.get(self.url + f"/{self.pesel}")

    @classmethod
    def setUpClass(cls):
        requests.post(cls.url + "/drop")

    @classmethod
    def tearDownClass(cls):
        requests.post(cls.url + "/drop")

    def setUp(self):
        requests.post(self.url, json=self.acc_json)
        requests.patch(
            self.url + f"/{self.pesel}", json={"balance": self.start_balance}
        )

    def tearDown(self) -> None:
        requests.delete(self.url + f"/{self.pesel}")

    def test_valid_incoming_transfer(self):
        body = {"amount": 60, "type": "incoming"}
        transfer = requests.post(self.url + f"/{self.pesel}/transfer", json=body)
        get = self.getAcc()
        self.assertEqual(transfer.status_code, 200, "transfer not executed!")
        self.assertEqual(
            get.json()["balance"],
            self.start_balance + body["amount"],
            "transfer not received!",
        )

    def test_invalid_incoming_transfer(self):
        body = {"amount": 40, "type": "incoming"}
        transfer = requests.post(self.url + f"/{111}/transfer", json=body)
        found = requests.get(self.url + f"/{111}")
        self.assertEqual(transfer.status_code, 404, "transfer shouldn't be executed!")
        self.assertEqual(found.status_code, 404, "Acc shouldn't be found!")

    def test_invalid_outgoing_transfer(self):
        body = {"amount": 5000, "type": "outgoing"}
        transfer = requests.post(self.url + f"/{self.pesel}/transfer", json=body)
        get = self.getAcc()
        self.assertEqual(transfer.status_code, 200, "transfer not executed!")
        self.assertEqual(
            get.json()["balance"], self.start_balance, "balance should different!"
        )

    def test_valid_outgoing_transfer(self):
        body = {"amount": 30, "type": "outgoing"}
        transfer = requests.post(self.url + f"/{self.pesel}/transfer", json=body)
        found = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(transfer.status_code, 200, "transfer not executed!")
        self.assertEqual(
            found.json()["balance"],
            self.start_balance - body["amount"],
            "outgoing transfer not executed!",
        )

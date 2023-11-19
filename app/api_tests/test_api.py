from unittest import TestCase
from ..api import *
import requests

# http cat


class TestApi(TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    url = "http://localhost:5000/api/accounts"
    acc = AccountPersonal(name, last_name, pesel)
    acc_json = acc.__dict__()

    def setUp(self) -> None:
        AccountsRecord.accounts = [self.acc]

    def tearDown(self) -> None:
        AccountsRecord.accounts = []

    def test_create_acc(self):
        response = requests.post(self.url, json=self.acc_json)
        self.assertEqual(response.status_code, 201)

    def test_get_acc(self):
        response - requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.acc_json)

    def test_valid_patch(self):
        test_obj = {
            "name": "Adam",
            "last_name": "Banan",
            "pesel": "10987654321",
            "balance": 10,
        }
        response = requests.patch(self.url + "/" + self.pesel, json=test_obj)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.acc_json)

    def test_invalid_patch(self):
        response = requests.patch(
            self.url + "/",
            json={
                "name": "Adam",
                "last_name": "Banan",
                "pesel": "10987654321",
                "balance": 10,
            },
        )
        self.assertEqual(response.status_code, 404)

    def test_deleting(self):
        ...

    def test_counting(self):
        response = requests.get(self.url + "/count")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"count": 1})

    def test_finding_valid_acc(self):
        response = requests.get(self.url + "/" + self.pesel)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.acc_json)

    def test_finding_invalid_acc(self):
        response = requests.get(self.url + "/" + "1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "Nie znaleziono konta"})

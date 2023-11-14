from unittest import TestCase
from ..api import *
import requests

# http cat


class TestApi(TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "12345678901"
    url = "http://localhost:5000/api/accounts"
    acc_json = {name, last_name, pesel}
    acc = AccountPersonal(name, last_name, pesel)

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

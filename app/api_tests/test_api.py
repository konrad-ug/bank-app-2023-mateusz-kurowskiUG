from unittest import TestCase
from ..api import *
import requests

# http cat


class TestApi(TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "07303157776"
    url = "http://localhost:5000/api/accounts"
    acc = AccountPersonal(name, last_name, pesel)
    acc_json = acc.__dict__()

    def setUp(self):
        AccountsRecord.accounts = [self.acc]

    def tearDown(self):
        AccountsRecord.accounts = []

    def test_create_acc(self):
        response = requests.post(self.url, json=self.acc_json)
        self.assertEqual(response.status_code, 201)

    def test_get_acc(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_valid_patch(self):
        response2 = requests.post(self.url, json=self.acc_json)
        test_obj = {
            "name": "Adam",
            "last_name": "Banan",
            "pesel": "71081619681",
            "balance": 10,
        }
        response = requests.patch(self.url + f"/{self.pesel}", json=test_obj)
        print(f"DANE: {response.json()}")
        self.assertEqual(response.status_code, 200)
        response3 = requests.delete(f"{self.url}/71081619681")

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

    def test_valid_deleting(self):
        response = requests.delete(self.url + f"/{self.pesel}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_deleting(self):
        response = requests.delete(self.url + "/1")
        self.assertEqual(response.status_code, 404)

    def test_counting(self):
        response = requests.get(self.url + "/count")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"count": 0})

    def test_finding_valid_acc(self):
        response = requests.get(self.url + "/" + self.pesel)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.acc_json)

    def test_finding_invalid_acc(self):
        response = requests.get(self.url + "/" + "1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"message": "Nie znaleziono konta"})

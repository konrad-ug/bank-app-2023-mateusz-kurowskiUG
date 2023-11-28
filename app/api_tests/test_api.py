from unittest import TestCase
from ..api import *
import requests
import copy

# http cat

# TOTALLY NOT ATOMIC, BUT SETUP NOT WORKING FOR SOME REASON!


class TestApi(TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "07303157776"
    second_pesel = "71081619681"
    url = "http://localhost:5000/api/accounts"
    acc = AccountPersonal(name, last_name, pesel)
    acc_json = acc.__dict__()

    @classmethod
    def setUpClass(cls):
        AccountsRecord.accounts = [cls.acc]

    def setUp(self):
        AccountsRecord.accounts = [self.acc]

    def tearDown(self) -> None:
        AccountsRecord.accounts = []

    @classmethod
    def tearDownClass(cls):
        AccountsRecord.accounts = []

    def test_create_acc(self):
        response = requests.post(self.url, json=self.acc_json)
        self.assertEqual(response.status_code, 201, f"{response.text}")

        new_acc = {
            "name": "Jan",
            "last_name": "Kowalski",
            "pesel": self.second_pesel,
        }
        response = requests.post(self.url, json=self.acc_json)
        self.assertEqual(response.status_code, 409, "Acc should be created!")
        response = requests.delete(self.url + "/" + self.second_pesel)
        response = requests.delete(self.url + "/" + self.pesel)

    def test_get_acc(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "GET NOT WORKING!")

    def test_valid_patch(self):
        response = requests.post(self.url, json=self.acc_json)
        test_obj = {
            "name": "Adam",
            "last_name": "Banan",
            "pesel": self.second_pesel,
            "balance": 10,
        }
        response = requests.patch(self.url + "/" + self.acc.pesel, json=test_obj)
        self.assertEqual(response.status_code, 200, "Patch should be executed!")
        response = requests.delete(self.url + "/" + self.second_pesel)

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
        response = requests.post(self.url, json=self.acc_json)

        response = requests.delete(self.url + f"/{self.pesel}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_deleting(self):
        response = requests.delete(self.url + "/1")
        self.assertEqual(response.status_code, 404)

    def test_counting(self):
        response = requests.get(self.url + "/count")
        print(AccountsRecord.accounts)
        self.assertEqual(response.status_code, 200)

    def test_finding_valid_acc(self):
        response = requests.post(self.url, json=self.acc_json)

        response = requests.get(self.url + "/" + self.pesel)
        self.assertEqual(response.status_code, 200)
        response = requests.delete(self.url + "/" + self.pesel)

    def test_finding_invalid_acc(self):
        response = requests.get(self.url + "/" + "1")
        self.assertEqual(response.status_code, 404)

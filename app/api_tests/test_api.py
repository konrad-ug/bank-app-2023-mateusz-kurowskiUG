from unittest import TestCase
from ..api import *
import requests
import copy


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
        requests.post(cls.url + "/drop")

    @classmethod
    def tearDownClass(cls):
        requests.post(cls.url + "/drop")

    def setUp(self) -> None:
        requests.post(self.url, json=self.acc_json)

    def tearDown(self):
        requests.delete(self.url + "/" + self.pesel)

    def test_create_not_unique_acc(self):
        new_acc = {
            "name": "Jan",
            "last_name": "Kowalski",
            "pesel": self.pesel,
        }
        response = requests.post(self.url, json=new_acc)
        self.assertEqual(response.status_code, 409, "Acc should not be created!")

    def test_create_unique_acc(self):
        new_acc = {
            "name": "Jan",
            "last_name": "Kowalski",
            "pesel": self.second_pesel,
        }
        response = requests.post(self.url, json=new_acc)
        self.assertEqual(response.status_code, 201, "Acc should  be created!")
        requests.delete(self.url + "/" + self.second_pesel)

    def test_get_acc(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "GET NOT WORKING!")

    def test_valid_patch(self):
        test_obj = {
            "name": "Adam",
            "last_name": "Banan",
            "pesel": self.second_pesel,
            "balance": 10,
        }
        response = requests.patch(self.url + "/" + self.acc.pesel, json=test_obj)
        self.assertEqual(response.status_code, 200, "Patch should be executed!")
        response = requests.patch(
            self.url + "/" + self.second_pesel, json=self.acc_json
        )
        self.assertEqual(response.status_code, 200, "Patch should be executed!")

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
        self.assertEqual(response.json(), {"count": 1})
        self.assertEqual(response.status_code, 200)

    def test_finding_valid_acc(self):
        response = requests.get(self.url + "/" + self.pesel)
        self.assertEqual(response.status_code, 200)

    def test_finding_invalid_acc(self):
        response = requests.get(self.url + "/" + "1")
        self.assertEqual(response.status_code, 404)

    def test_01_saving(self):
        response = requests.patch(self.url + "/save")
        self.assertEqual(response.status_code, 200, "Save should be successful")
        self.assertEqual(
            response.json(), [self.acc.__dict__()], "Save result should be different"
        )

    def test_02_loading(self):
        requests.post(self.url, json=self.acc_json)
        response = requests.patch(self.url + "/load")
        self.assertEqual(response.status_code, 200, "Load should be successful")
        self.assertEqual(
            response.json(), [self.acc.__dict__()], "Load result should be different"
        )

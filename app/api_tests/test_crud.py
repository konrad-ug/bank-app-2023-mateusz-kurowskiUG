from unittest import TestCase
from app.Account_personal import AccountPersonal
import requests
import copy


class TestApi(TestCase):
    name = "Jan"
    last_name = "Kowalski"
    pesel = "07303157776"
    second_pesel = "71081619682"
    url = "http://localhost:5000/api/accounts"
    acc_json = AccountPersonal(name, last_name, pesel).__dict__()

    @classmethod
    def setUpClass(cls):
        requests.post(cls.url + "/drop")

    @classmethod
    def tearDownClass(cls):
        requests.post(cls.url + "/drop")

    def test_01_create_acc(self):
        response = requests.post(self.url, json=self.acc_json)
        self.assertEqual(response.status_code, 201, f"{response.text}")
        self.assertEqual(
            response.json(),
            self.acc_json,
            "POST returned something different than original object!",
        )

    def test_02_create_acc_already_exists(self):
        response = requests.post(self.url, json=self.acc_json)
        self.assertEqual(response.status_code, 409, "Acc should not be created!")

    def test_03_get_all_acc(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "GET NOT WORKING!")
        self.assertEqual(
            response.json(),
            [self.acc_json],
            "GET response is different than posted object in array.",
        )

    def test_04_get_acc_by_pesel(self):
        response = requests.get(self.url + "/" + self.pesel)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), self.acc_json, "GET returned different object!"
        )

    def test_05_valid_patch(self):
        test_obj = {
            "name": "Adam",
            "last_name": "Banan",
            "pesel": self.second_pesel,
            "balance": 10,
        }
        response = requests.patch(self.url + "/" + self.pesel, json=test_obj)
        self.assertEqual(response.status_code, 200, "Patch should be executed!")
        self.assertEqual(
            response.json(), {**test_obj, "history": []}, "Object didn't get changed!"
        )

    def test_06_invalid_patch(self):
        response = requests.patch(
            self.url + "/111111111111111111111111",
            json={
                "name": "Adam",
                "last_name": "Banan",
                "pesel": "10987654321",
                "balance": 10,
            },
        )
        self.assertEqual(response.status_code, 404)

    def test_07_valid_deleting(self):
        response = requests.delete(self.url + f"/{self.second_pesel}")
        self.assertEqual(response.status_code, 200)

    def test_08_invalid_deleting(self):
        response = requests.delete(self.url + "/1")
        self.assertEqual(response.status_code, 404)

    def test_09_counting(self):
        response = requests.get(self.url + "/count")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"count": 0}, "Counter does not work!")

    def test_10_finding_invalid_acc(self):
        response = requests.get(self.url + "/" + "1")
        self.assertEqual(response.status_code, 404)

from behave import fixture
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()

URL = "http://localhost:5000/api/accounts"
user_json = {
    "name": "Adam",
    "last_name": "Adamowicz",
    "pesel": "62082062325",
    "balance": 0,
}


def before_scenario(context, scenario):
    if "bdd_transfers" in scenario.effective_tags:
        create = requests.post(URL, json=user_json)
        assert_equal(create.status_code, 201)


def after_scenario(context, scenario):
    if "bdd_transfers" in scenario.effective_tags:
        delete_user = requests.delete(f"{URL}/{user_json['pesel']}")
        assert_equal(delete_user.status_code, 200)

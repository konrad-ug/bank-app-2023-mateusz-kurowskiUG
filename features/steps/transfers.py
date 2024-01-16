from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual
import ast

assert_equal = AssertEqual()
user_json = {
    "name": "Adam",
    "last_name": "Adamowicz",
    "pesel": "62082062325",
    "balance": 0,
}
URL = f"http://localhost:5000/api/accounts"


@when("User sends a transfer: {amount}")
def send_transfer(context, amount):
    amount_stripped = int(amount.strip('"'))
    json_body = {"amount": amount_stripped, "type": "outgoing"}
    create_resp = requests.post(f"{URL}/{user_json['pesel']}/transfer", json=json_body)
    assert_equal(create_resp.status_code, 200)


@when("User receives a transfer: {amount}")
def receive_transfer(context, amount):
    amount_stripped = int(amount.strip('"'))
    json_body = {"amount": amount_stripped, "type": "incoming"}
    create_resp = requests.post(f"{URL}/{user_json['pesel']}/transfer", json=json_body)
    assert_equal(create_resp.status_code, 200)


@step("User's history equals: {history}")
def check_history(context, history):
    history_stripped = history.strip('"')
    history_list = ast.literal_eval(history_stripped)
    resp = requests.get(f"{URL}/{user_json['pesel']}")
    assert_equal(resp.status_code, 200)
    assert_equal(resp.json()["history"], history_list)


@then("User's balance equals: {amount}")
def check_history(context, amount):
    history_stripped = int(amount.strip('"'))
    resp = requests.get(f"{URL}/{user_json['pesel']}")
    assert_equal(resp.status_code, 200)
    assert_equal(resp.json()["balance"], history_stripped)


@given("User's balance equals: {amount}")
def add_balance(context, amount):
    amount_stripped = int(amount.strip('"'))
    create_resp = requests.patch(
        f"{URL}/{user_json['pesel']}", json={"balance": amount_stripped}
    )
    assert_equal(create_resp.status_code, 200)

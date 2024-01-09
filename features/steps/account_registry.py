from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual


assert_equal = AssertEqual()
URL = "http://localhost:5000"


@when("I create an account using name: {name}, last name: {last_name}, pesel: {pesel}")
def create_acc(context, name, last_name, pesel):
    name_stripped = name.strip('"')
    last_name_stripped = last_name.strip('"')
    pesel_stripped = pesel.strip('"')
    json_body = {
        "name": name_stripped,
        "last_name": last_name_stripped,
        "pesel": pesel_stripped,
    }
    create_resp = requests.post(URL + "/api/accounts", json=json_body)
    assert_equal(create_resp.status_code, 201)


@step('Number of accounts in registry equals: "{count}"')
def count_accs(context, count):
    counted_accs = requests.get(URL + f"/api/accounts/count").json()["count"]
    assert_equal(counted_accs, int(count))


@step('Account with pesel "{pesel}" exists in registry')
def account_with_pesel_exists(context, pesel):
    assert_equal(requests.get(URL + f"/api/accounts/{pesel}").status_code, 200)


@when('I delete account with pesel: "{pesel}"')
def delete_acc(context, pesel):
    resp = requests.delete(URL + f"/api/accounts/{pesel}")
    assert_equal(resp.status_code, 200)


@step('Account with pesel "{pesel}" does not exist in registry')
def check_if_acc_with_pesel_does_not_exist(context, pesel):
    new_pesel = pesel.strip('"')
    resp = requests.get(URL + f"/api/accounts/{new_pesel}")
    assert_equal(resp.status_code, 404)


@when("I save the account registry")
def save_accounts(context):
    resp = requests.patch(URL + f"/api/accounts/save")
    assert_equal(resp.status_code, 200)


@when("I load the account registry")
def load_registry(context):
    resp = requests.patch(URL + f"/api/accounts/load")
    assert_equal(resp.status_code, 200)


@when("I update last name to {last_name} for account with pesel: {pesel}")
def update_last_name(context, pesel, last_name):
    last_name_stripped = last_name.strip('"')
    pesel_stripped = pesel.strip('"')
    json_body = {"last_name": last_name_stripped}
    resp = requests.patch(URL + f"/api/accounts/{pesel_stripped}", json=json_body)
    assert_equal(resp.status_code, 200)


@then('Last name in account with pesel "{pesel}" is "{last_name}"')
def check_last_name(context, pesel, last_name):
    pesel_stripped = pesel.strip('"')
    res = requests.get(URL + f"/api/accounts/{pesel_stripped}")
    assert_equal(res.json()["last_name"], last_name)

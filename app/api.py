from flask import Flask, request, jsonify
from json import dumps, loads
from app.Account_personal import AccountPersonal
from app.AccountsRecord import AccountsRecord
from bson import json_util

app = Flask(__name__)


@app.route("/api/accounts", methods=["POST"])
def add_acc():
    data = request.get_json()
    name = data["name"]
    last_name = data["last_name"]
    pesel = data["pesel"]

    if not name or not last_name or not pesel:
        return "Seems like you didn't provide name, last_name or pesel", 403

    found = AccountsRecord.search_for_acc(pesel)
    if found is None:
        acc = AccountPersonal(name, last_name, pesel)
        acc.history = []
        AccountsRecord.add_acc_to_record(acc)
        return jsonify(acc.__dict__()), 201
    else:
        return jsonify({"message": "Pesel should be UNIQUE!"}), 409


@app.route("/api/accounts/count", methods=["GET"])
def how_many_accs():
    return jsonify({"count": AccountsRecord.number_of_acc()}), 200


6


@app.route("/api/accounts", methods=["GET"])
def get_accounts():
    return [i.__dict__() for i in AccountsRecord.accounts], 200


@app.route("/api/accounts/<pesel>", methods=["GET"])
def search_for_acc(pesel):
    response = AccountsRecord.search_for_acc(pesel)
    if response is None:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    return jsonify(response.__dict__()), 200


@app.route("/api/accounts/<pesel>", methods=["PATCH"])
def update_acc(pesel):
    if pesel is None:
        return jsonify({"message": "Niewłaściwy pesel!"}), 404

    data = request.get_json()
    obj = {}

    if "name" in data and data["name"]:
        obj["name"] = data["name"]

    if "last_name" in data and data["last_name"]:
        obj["last_name"] = data["last_name"]

    if "pesel" in data and data["pesel"]:
        obj["pesel"] = data["pesel"]

    if "balance" in data and data["balance"]:
        obj["balance"] = data["balance"]

    result = AccountsRecord.modify_acc(pesel, obj)
    if result is None:
        return jsonify({"message": "Account not found!"}), 404
    return result.__dict__(), 200


@app.route("/api/accounts/<pesel>", methods=["DELETE"])
def delete_acc(pesel):
    if pesel is None:
        return jsonify({"message": "Niewłaściwy pesel!"}), 404
    result = AccountsRecord.delete_acc(pesel)
    if result:
        return jsonify({"message": "Konto usunięte"}), 200
    return jsonify({"message": "Nie znaleziono konta"}), 404


@app.route("/api/accounts/<pesel>/transfer", methods=["POST"])
def transfer(pesel):
    data = request.get_json()

    if pesel is None:
        return jsonify({"message": "No pesel provided!"}), 404

    amount = data["amount"]
    transfer_type = data["type"]
    if not amount or not transfer_type:
        return jsonify({"message": "No amount or type provided!"}), 404

    found_acc = AccountsRecord.search_for_acc(pesel)
    if found_acc is None:
        return jsonify({"message": "Couldn't find acc with such a pesel!"}), 404
    match transfer_type:
        case "incoming":
            found_acc.receive_transfer(amount)
        case "outgoing":
            found_acc.outgoing_transfer(amount)

        case _:
            return jsonify({"message": "wrong type of transfer"}), 403
    return jsonify({"message": "Zlecenie przyjęte do realizacji!"}), 200


@app.route("/api/accounts/save", methods=["PATCH"])
def save():
    return loads(json_util.dumps(AccountsRecord.save())), 200


@app.route("/api/accounts/load", methods=["PATCH"])
def load():
    accs = AccountsRecord.load()
    return jsonify([i.__dict__() for i in accs]), 200


@app.route("/api/accounts/drop", methods=["POST"])
def drop():
    AccountsRecord.accounts = []
    AccountsRecord.save()
    return loads(json_util.dumps(AccountsRecord.save())), 200

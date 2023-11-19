from flask import Flask, request, jsonify
from json import dumps as json_dumps
from .Account_personal import AccountPersonal
from .AccountsRecord import AccountsRecord

app = Flask(__name__)


@app.route("/api/accounts", methods=["POST"])
def add_acc():
    data = request.get_json()
    print(f"Request o stworzenie konta z danymi: {data}")
    acc = AccountPersonal(data["name"], data["last_name"], data["pesel"])
    AccountsRecord.add_acc_to_record(acc)
    return jsonify({"message": "Konto stworzone"}), 201


@app.route("/api/accounts/count", methods=["GET"])
def how_many_accs():
    return jsonify({"count": AccountsRecord.number_of_acc()}), 200


@app.route("/api/accounts", methods=["GET"])
def get_accounts():
    return [i.__dict__() for i in AccountsRecord.accounts], 200


@app.route("/api/accounts/<pesel>", methods=["GET"])
def search_for_acc(pesel):
    response = AccountsRecord.search_for_acc(pesel)
    if response is not None:
        return jsonify(response.__dict__()), 200
    return jsonify({"message": "Nie znaleziono konta"}), 404


@app.route("/api/accounts/<pesel>", methods=["PATCH"])
def update_acc(pesel):
    found = AccountsRecord.search_for_acc(pesel)
    if found is None:
        return jsonify("Nie znaleziono konta do modyfikacji!")
    data = request.get_json()
    if "name" in data:
        found.name = data["name"]
    if "last_name" in data:
        found.last_name = data["last_name"]
    if "pesel" in data:
        found.pesel = data["pesel"]
    if "balance" in data:
        found.balance = data["balance"]

    return jsonify(found.__dict__()), 200


@app.route("/api/accounts/<pesel>", methods=["DELETE"])
def delete_acc(pesel):
    if pesel is None:
        return jsonify({"message": "Niewłaściwy pesel!"}), 404
    result = AccountsRecord.delete_acc(pesel)
    if result:
        return jsonify({"message": "Konto usunięte"}), 200
    return jsonify({"message": "Nie znaleziono konta"}), 404

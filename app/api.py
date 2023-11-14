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
    return json_dumps(AccountsRecord.accounts), 200


@app.route("/api/accounts/<pesel>", methods=["GET"])
def search_for_acc(pesel):
    response = AccountsRecord.search_for_acc(pesel)
    app.logger.debug(response)
    app.logger.debug(pesel)

    if response is not None:
        return jsonify(response.__dict__), 200
    return jsonify({"message": "Nie znaleziono konta"}), 404

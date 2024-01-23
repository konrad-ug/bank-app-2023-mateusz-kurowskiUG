[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12305625&assignment_repo_type=AssignmentRepo)

# Bank app

Myślę, że udało mi się spełnić wymagania na: 5
Jedyne zakomentowane linijki do coverage to importy bibliotek w Account_personal oraz metody prywatne **setitem** oraz **getitem**
Imię i nazwisko: Mateusz Kurowski

Grupa: III

Project uses Poetry and requires _Python 3.12_
`Poetry install` to install dependencies
`Poetry shell` to activate venv
`python3 -m coverage run -m unittest` coverage
`python3 -m coverage report --omit="*/test*" -d tests/coverage` coverage
`python3 -m coverage html`
`poetry export -f requirements.txt --output requirements.txt` to create requirements.txt
`flask --app app/api.py run`
`python -m unittest discover app.tests` to SKIP api_tests
`docker compose -f compose.yml up` to run mongo

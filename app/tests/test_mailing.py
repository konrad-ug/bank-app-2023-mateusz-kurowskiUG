from unittest import mock, TestCase
from app.SMTPServer import SMTPConnection
from app.Account_company import AccountCompany
from app.Account_personal import AccountPersonal
from datetime import datetime


class TestMailing(TestCase):
    date = datetime.now().strftime("%Y-%m-%d")
    receiver = "email@email.com"

    @mock.patch("app.Account_company.AccountCompany.validate_nip")
    def setUp(self, mocked_object):
        mocked_object.return_value = True
        self.acc_personal = AccountPersonal("Osoba", "Jeden", "58052553113")
        self.acc_company = AccountCompany("Company", "5841932579")
        self.mock_server = mock.MagicMock(SMTPConnection())
        self.mock_server.send_email.return_value = False

    def tearDown(self):
        self.mock_server = None
        self.acc_personal = None
        self.acc_company = None


    def test_personal_email_not_valid(self):
        personal_email = self.acc_personal.send_history_on_email("", self.mock_server)
        self.mock_server.send_email.assert_called_once_with(
            f"Wyciąg z dnia {self.date}",
            f"{self.acc_personal.email_msg} {self.acc_personal.history}",
            "",
        )
        self.assertEqual(personal_email, False, "Mailing result should be different")
        self.assertEqual(
            self.mock_server.send_email.return_value,
            False,
            "Mailing result should be different",
        )

    def test_personal_email_with_history(self):
        self.acc_personal.history = [100, 200, -100]
        personal_email = self.acc_personal.send_history_on_email("", self.mock_server)
        self.mock_server.send_email.assert_called_once_with(
            f"Wyciąg z dnia {self.date}",
            f"{self.acc_personal.email_msg} {self.acc_personal.history}",
            "",
        )
        self.assertEqual(personal_email, False, "Mailing result should be different")
        self.assertEqual(
            self.mock_server.send_email.return_value,
            False,
            "Mailing result should be different",
        )

    def test_personal_email_valid(self):
        self.mock_server.send_email.return_value = True
        personal_email = self.acc_personal.send_history_on_email(
            self.receiver, self.mock_server
        )
        self.mock_server.send_email.assert_called_once_with(
            f"Wyciąg z dnia {self.date}",
            f"{self.acc_personal.email_msg} {self.acc_personal.history}",
            self.receiver,
        )
        self.assertEqual(personal_email, True, "Mailing result should be different")

    def test_company_email_not_valid(self):
        company_email = self.acc_company.send_history_on_email("", self.mock_server)
        self.mock_server.send_email.assert_called_once_with(
            f"Wyciąg z dnia {self.date}",
            f"{self.acc_company.email_msg} {self.acc_company.history}",
            "",
        )
        self.assertEqual(
            company_email, False, "Company Email result should be different"
        )

    def test_company_email_with_history(self):
        self.acc_company.history = [100, 200, -100]
        personal_email = self.acc_personal.send_history_on_email("", self.mock_server)
        self.mock_server.send_email.assert_called_once_with(
            f"Wyciąg z dnia {self.date}",
            f"{self.acc_personal.email_msg} {self.acc_personal.history}",
            "",
        )
        self.assertEqual(personal_email, False, "Mailing result should be different")
        self.assertEqual(
            self.mock_server.send_email.return_value,
            False,
            "Mailing result should be different",
        )

    def test_company_email_valid(self):
        self.mock_server.send_email.return_value = True
        company_email = self.acc_company.send_history_on_email(
            self.receiver, self.mock_server
        )
        self.mock_server.send_email.assert_called_once_with(
            f"Wyciąg z dnia {self.date}",
            f"{self.acc_company.email_msg} {self.acc_company.history}",
            self.receiver,
        )
        self.assertEqual(
            company_email, True, "Company Email result should be different"
        )

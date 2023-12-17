from unittest import mock, TestCase
from app.SMTPServer import SMTPConnection
from app.Account_company import AccountCompany
from app.Account_personal import AccountPersonal


class TestMailing(TestCase):
    @mock.patch("app.Account_company.")
    def setUp(self,mocked_object):
        self.acc_personal = AccountPersonal("Osoba", "Jeden", "58052553113")
        self.acc_personal = AccountPersonal("Osoba", "Dwa", "05303144226")
        self.acc_company = AccountCompany("Company", "5841932579")
        self.acc_company = AccountCompany("Company", "5841932578")
        self.mock_obj = mock.MagicMock(SMTPConnection())

    def tearDown(self):
        self.mock_obj = None
        self.acc_personal = None
        self.acc_personal2 = None
        self.acc_company = None
        self.acc_company2 = None

    def test_server(self, receiver):
        emailed = self.acc_personal.send_history_on_email(receiver)
        self.assertEqual(emailed, False, "Emailing reslt should be different")

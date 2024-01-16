from unittest import TestCase
from requests import post, delete, Timeout


class TestPerformance(TestCase):
    name = "Adam"
    last_name = "Adamowicz"
    pesel = "90011141896"
    acc_json = {"name": name, "last_name": last_name, "pesel": pesel}
    perf_time_test = 2

    def create_acc(self):
        try:
            create = post(
                "http://localhost:5000/api/accounts",
                json=self.acc_json,
                timeout=self.perf_time_test,
            )
            self.assertGreater(
                self.perf_time_test,
                create.elapsed.total_seconds(),
                f"Response later than {self.perf_time_test} seconds after request!",
            )
            self.assertEqual(create.status_code, 201, "Acc should  be created!")
        except Timeout:
            self.fail(
                f"Response later than {self.perf_time_test} seconds after request!"
            )

    def delete_acc(self):
        try:
            delete_response = delete(
                f"http://localhost:5000/api/accounts/{self.pesel}",
                timeout=self.perf_time_test,
            )
            self.assertGreater(
                self.perf_time_test,
                delete_response.elapsed.total_seconds(),
                f"Response later than {self.perf_time_test} seconds after request!",
            )
            self.assertEqual(
                delete_response.status_code, 200, "Delete should be performed!"
            )
        except Timeout:
            self.fail(
                f"Response later than {self.perf_time_test} seconds after request!"
            )

    def test_hundred_accs(self):
        for i in range(100):
            self.create_acc()
            self.delete_acc()

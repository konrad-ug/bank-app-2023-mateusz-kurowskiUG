from typing import Any
from datetime import datetime
from app.SMTPServer import SMTPConnection
try:  # pragma: no cover
    from typing import Self  # pragma: no cover
except ImportError:  # pragma: no cover
    from typing_extensions import Self  # pragma: no cover


class Account:
    balance = 0
    express_transfer_fee = 0
    history = []
    email_msg = ""

    def __setitem__(self, __name: str, __value: Any):  # pragma: no cover
        setattr(self, __name, __value)

    def __getitem__(self, __name: str) -> Any:  # pragma: no cover
        return getattr(self, __name)

    def __eq__(self, __value: Self) -> bool:  # pragma: no cover
        return (
            self.balance == __value.balance
            and self.express_transfer_fee == __value.express_transfer_fee
            and self.history == __value.history
        )

    def outgoing_transfer(self, amount: float):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            self.history.append(-amount)
            return True
        return False

    def receive_transfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)
            return True
        return False

    def express_outgoing_transfer(self, amount):
        if (
            self.balance - (amount + self.express_transfer_fee)
            >= -self.express_transfer_fee
            and amount > 0
        ):
            self.balance -= amount + self.express_transfer_fee
            self.history.append(-amount)
            self.history.append(-self.express_transfer_fee)

    def send_history_on_email(self, receiver, SMTP_class: SMTPConnection):
        date = datetime.now().strftime("%Y-%m-%d")
        topic = f"Wyciąg z dnia {date}"
        content = f"{self.email_msg} {self.history}"
        return SMTP_class.send_email(topic, content, receiver)

try:  # pragma: no cover
    from typing import Self  # pragma: no cover
except ImportError:  # pragma: no cover
    from typing_extensions import Self  # pragma: no cover


class Account:
    balance = 0
    express_transfer_fee = 0
    history = []

    def __eq__(self, __value: Self) -> bool:  # pragma: no cover
        return (
            self.balance == __value.balance
            and self.express_transfer_fee == __value.express_transfer_fee
            and self.history == __value.history
        )

    def outing_transfer(self, amount: float):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            self.history.append(-amount)

    def receive_transfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)

    def express_outgoing_transfer(self, amount):
        if (
            self.balance - (amount + self.express_transfer_fee)
            >= -self.express_transfer_fee
            and amount > 0
        ):
            self.balance -= amount + self.express_transfer_fee
            self.history.append(-amount)
            self.history.append(-self.express_transfer_fee)

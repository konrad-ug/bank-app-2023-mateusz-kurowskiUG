import re, datetime


class Account:
    saldo = 0
    express_transfer_fee = 0

    def outing_transfer(self, amount: float):
        if self.saldo >= amount:
            self.saldo -= amount

    def receive_transfer(self, amount):
        if amount > 0:
            self.saldo += amount

    def express_outgoing_transfer(self, amount):
        if self.saldo - (amount + self.express_outgoing_transfer) >= 0:
            self.saldo -= amount + self.express_transfer_fee

import re, datetime


class Account:

    def transfer(self, amount: float):
        if self.saldo >= amount:
            self.saldo -= amount

    def receive_transfer(self, amount):
        if amount > 0:
            self.saldo += amount

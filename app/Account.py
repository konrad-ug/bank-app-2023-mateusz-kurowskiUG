class Account:
    balance = 0
    express_transfer_fee = 0
    history = []

    def outing_transfer(self, amount: float):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            self.history.append(-amount)

    def receive_transfer(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(amount)

    def express_outgoing_transfer(self, amount):
        if self.balance - (amount + self.express_transfer_fee) >= 0:
            self.balance -= amount + self.express_transfer_fee
            self.history.append(-amount)
            self.history.append(-self.express_transfer_fee)

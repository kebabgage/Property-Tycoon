class Bank:
    def __init__(self, balance=15000):
        self.balance = balance

    def decrease_balance(self, amount):
        self.balance -= amount

    def increase_balance(self, amount):
        self.balance += amount

    def getBankBalance(self):
        return self.balance


class BankAccount():
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds")

b, w = map(int, input().split())
account = BankAccount()
account.deposit(b)
account.withdraw(w)  
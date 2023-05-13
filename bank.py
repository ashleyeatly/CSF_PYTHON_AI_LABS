class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def balance(self):
        return self.account_balance

    def withdraw(self, amount):
        self.account_balance -= amount
        return self.account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

# abc = BankAccount(1000)
# print(abc.balance())
# print(abc.withdraw(10))
# print(abc.deposit(20))

class CheckingAccount(BankAccount):

    def __init__(self,account_balance, fee):
        super().__init__(account_balance)
        self.fee = fee

    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount - self.fee
        return self.account_balance

x1 = CheckingAccount(1000, 10)
print(x1.balance())
print(x1.withdraw(10))
print(x1.deposit(20))



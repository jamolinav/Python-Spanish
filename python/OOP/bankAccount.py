class BankAccount:
    def __init__ (self, in_rate, balance=0):
        self.in_rate = in_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print (f'Saldo: {self.balance}')
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.in_rate
        return self

if __name__ == '__main__':
    cuenta1 = BankAccount(0.01, 100)
    cuenta2 = BankAccount(0.05)

    cuenta1.deposit(100).deposit(100).deposit(100).yield_interest().display_account_info()
    cuenta2.deposit(100).deposit(100).withdraw(120).yield_interest().display_account_info()

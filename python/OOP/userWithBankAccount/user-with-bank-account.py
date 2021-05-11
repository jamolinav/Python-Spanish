from bankAccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, bankAccount):
        self.accounts.append(bankAccount)
    
    def getTotalAccount(self):
        print(f'Tiene {len(self.accounts)} cuenta(s)')

    def make_deposit(self, id_account, amount):
        for account in self.accounts:
            if account.getId() == id_account:
                account.deposit(amount)

    def make_withdrawal(self, id_account, amount):
        for account in self.accounts:
            if account.getId() == id_account:
                account.withdraw(amount)
    
    def display_user_balance(self):
        for account in self.accounts:
            print('idAccount: {} {}'.format(account.getId(), account.display_account_info()))

if __name__ == '__main__':
    user = User('Juan', 'jamolinav@gmail.com')
    cuenta1 = BankAccount(1, 0.02, 0)
    cuenta2 = BankAccount(2, 0.04, 100)
    user.add_account(cuenta1)
    user.add_account(cuenta2)
    user.getTotalAccount()
    user.display_user_balance()
    user.make_deposit(1,50)
    user.make_withdrawal(2,10)
    user.display_user_balance()

class Usuario:
    def __init__ (self, name, amount=0):
        self.amount = amount
        self.name = name

    def make_withdrawal(self, amount):
        if self.amount >= amount:
            self.amount -= amount
        else:
            print (f'No tiene saldo suficiente para este monto: {amount}')
        return self
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def display_user_balance(self):
        print(f'Usuario: {self.name}, Saldo: $ {self.amount}')
        return self
    def transfer_money (self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.make_deposit(amount)
        return self

user1 = Usuario('Pedro')
user2 = Usuario('Juan')
user3 = Usuario('Diego')

user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(150).display_user_balance()
print('*' * 10)
user2.make_deposit(200).make_deposit(300).make_withdrawal(100).make_withdrawal(150).display_user_balance()
print('*' * 10)
user3.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(80).display_user_balance()
print('*' * 10)
user1.transfer_money(user3, 80).display_user_balance()
user3.display_user_balance()
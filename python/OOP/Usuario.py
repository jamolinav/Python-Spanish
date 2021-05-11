
class Usuario:
    def __init__ (self, name, amount=0):
        self.amount = amount
        self.name = name

    def make_withdrawal(self, amount):
        if self.amount >= amount:
            self.amount -= amount
        else:
            print (f'No tiene saldo suficiente para este monto: {amount}')
            return False
        return True
    def make_deposit(self, amount):
        self.amount += amount
    
    def display_user_balance(self):
        print(f'Usuario: {self.name}, Saldo: $ {self.amount}')

    def transfer_money (self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.make_deposit(amount)

user1 = Usuario('Pedro')
user2 = Usuario('Juan')
user3 = Usuario('Diego')

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(150)
user1.display_user_balance()
print('*' * 10)
user2.make_deposit(200)
user2.make_deposit(300)
user2.make_withdrawal(100)
user2.make_withdrawal(150)
user2.display_user_balance()
print('*' * 10)
user3.make_deposit(100)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.make_withdrawal(80)
user3.display_user_balance()
print('*' * 10)
user1.transfer_money(user3, 80)
user1.display_user_balance()
user3.display_user_balance()
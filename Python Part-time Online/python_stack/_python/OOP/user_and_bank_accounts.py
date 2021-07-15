#Summary:
# This program is a bank account managment tool that allows Users to create an account by enter their creates a class (User) that allows a 


#Objectives:
# 



import bank_account

class User:
    def __init__(self, username, email, interest, balance = 0):
        self.name = username
        self.email = email
        self.accounts = bank_account.BankAccount(interest, balance)

    def make_deposit(self, amount):
        self.account_balance.deposit(amount)

    def make_withdrawal(self, amount):
        self.account_balance.withdrawal(amount)

    def display_user_balance(self):
        self.account_balance.display_account_info()

    def transfer_money(self, other_user, amount):
        if self == other_user:
            pass
            # Catches if User is transfering money to self.
        else:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            
            


Sam = User("Sam", "sam@test.com", 0.02)
Veronica = User("Veronica", "veronica@test.com", 0.02)
Trevor = User("Trevor", "trevor@test.com", 0.02)
Trevor.account_balance2 = bank_account.BankAccount(0.04, 5000)
print (Trevor.account_balance2.account_balance)

Sam.make_deposit(200)
Sam.make_deposit(700)
Sam.make_withdrawal(500)
Sam.display_user_balance()

Veronica.make_deposit(600)
Veronica.make_withdrawal(400)
Veronica.make_withdrawal(100)
Veronica.display_user_balance()

Trevor.make_deposit(800)
Trevor.make_withdrawal(100)
Trevor.make_withdrawal(200)
Trevor.make_withdrawal(300)
Trevor.display_user_balance()

Trevor.transfer_money(Veronica,100)
Trevor.transfer_money(Trevor,100)
print()
Veronica.display_user_balance()
Trevor.display_user_balance()



# Checklist:
# Update the User class __init__ method
# Update the User class make_deposit method
# Update the User class make_withdrawal method
# Update the User class display_user_balance method
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
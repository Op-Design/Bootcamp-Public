#Summary:
# This program is a bank account managment tool that allows Users to create an account by enter their creates a class (User) that allows a 


#Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the
# amount and add that amount to other other_user's balance



class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        if self == other_user:
            pass
            # Catches if User is transfering money to self.
        else:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
            
            


Sam = User("Sam", "sam@test.com")
Veronica = User("Veronica", "veronica@test.com")
Trevor = User("Trevor", "trevor@test.com")

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
# Create a file with the User class, including the __init__ and make_deposit methods
# Add a make_withdrawal method to the User class
# Add a display_user_balance method to the User class
# Create 3 instances of the User class
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
# Have the second user make 2 deposits and 2 withdrawals and then display their balance
# Have the third user make 1 deposits and 3 withdrawals and then display their balance
# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
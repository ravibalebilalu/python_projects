from account import Account
from bank import Bank
from user_interface import UserInterface



bank = Bank()
user_interface  = UserInterface()
 

signal = 0

while signal != 6:
    signal = user_interface.display_menu()
    if signal == 1:
        bank.create_account()
    elif signal == 2:
        bank.deposite()
    elif signal == 3:
        bank.withdraw()
    elif signal == 4:
        bank.check_balance()
    elif signal == 5:
        bank.display()

 


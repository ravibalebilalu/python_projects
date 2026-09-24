from account import Account
import csv
import os
import random

class Bank:
    def __init__(self,filename="bank.csv") -> None:
        self.filename = filename
        self.fiednames = ["account_number","account_holder_name","account_type","balance",]
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename,"w",newline="")as f:
                writer = csv.DictWriter(f,fieldnames=self.fiednames)
                writer.writeheader()

    def create_account(self):
        print("cccccccccccc")
        account_holder_name = input("Enter name:\t")
        account_type = input("Enter account type:\t")
        account_number = random.randint(1111111111,99999999999)
        account = {
            "account_number":account_number,
            "account_holder_name":account_holder_name,
            "account_type":account_type,
            "balance":0
        }

        try:
            with open(self.filename,"a",newline="")as f:
                writer = csv.DictWriter(f,fieldnames=self.fiednames)
                writer.writerow(account)
        except FileNotFoundError as e:
            print(e)
        return True
    
    def get_all_accounts(self):
        try:
            with open(self.filename,"r",newline="")as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            print("Database not found!")
            return []

    def _rewrite_accounts(self,accounts):
        with open(self.filename,"w",newline="")as f:
            writer = csv.DictWriter(f,fieldnames=self.fiednames)
            writer.writeheader()
            writer.writerows(accounts)
    def get_account_number(self):
        while True:
            try:
                account_number = int(input("Enter account number:\t"))
                break
            except Exception:
                print("Enter valied account number...")
                continue
        return account_number
    
    def deposite(self):
        # ask user to enter valied account number
        account_number = self.get_account_number()

        # verify account number exist
        all_accounts = self.get_all_accounts()
         
        account = [account for account in all_accounts if account["account_number"] == str(account_number) ][0]
        while True:
            try:
                amount = int(input("Enter amount to deposite:\t"))
                if amount >0:
                    break

            except Exception:
                print("Enter valid amount!")
                continue
        # update balance
        updated_fields = {
            "account_number":account_number,
            "account_holder_name":account["account_holder_name"],
            "account_type":account["account_type"],
            "balance": int(account["balance"]) + amount
        }
        found = False
        for ac in all_accounts:
            if int(ac["account_number"]) == account_number:
                ac.update(updated_fields)
                found = True
        # rewrite datafile
        if found:
            self._rewrite_accounts(all_accounts)
            print(f"Account {account_number} is deposited with amount {amount}")
        else:
            print(f"Account {account_number} not found")

        return found


    def withdraw(self):
        account_number = self.get_account_number()

        all_accounts = self.get_all_accounts()
         
        account = [account for account in all_accounts if account["account_number"] == str(account_number) ][0]
        while True:
            try:
                amount = int(input("Enter amount to withdraw:\t"))
                if amount <= int(account["balance"]) and amount >0:
                    break
                else:
                    print("You have no sifficient balance!")

            except Exception:
                print("Enter valid amount!")
                continue
        # update balance
        updated_fields = {
            "account_number":account_number,
            "account_holder_name":account["account_holder_name"],
            "account_type":account["account_type"],
            "balance": int(account["balance"]) - amount
        }
        print(updated_fields)
        found = False
        for ac in all_accounts:
            if int(ac["account_number"]) == account_number:
                ac.update(updated_fields)
                found = True
        # rewrite datafile
        if found:
            self._rewrite_accounts(all_accounts)
            print(f"Account {account_number} is withdrawed with amount {amount}")
        else:
            print(f"Account {account_number} not found")

        return found

    def check_balance(self):
        account_number = self.get_account_number()
        all_accounts = self.get_all_accounts()
        try:
            account = [account for account in all_accounts if account["account_number"] == str(account_number) ][0]
            print(f"Balance: {account['balance']}")
        except Exception:
            print("Account not fond!")

    def display(self):
        all_accounts = self.get_all_accounts()
        for account in all_accounts:
            print(account)


        





        
    
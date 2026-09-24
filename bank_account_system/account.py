class Account:
    def __init__(self,acc_number,acc_holder_name ) -> None:
        self.account_number = acc_number
        self.account_holder_name = acc_holder_name
        self.account_type = None
        self.balance = 0

    def display(self):
        print(f"""

            account_number          : {self.account_number}
            account_holder_name     : {self.account_holder_name}
            account_type            : {self.account_type}
            balance                 : {self.balance}
                """)
        

    
class UserInterface:
    def display_menu(self):
        print("""
            1.Add Account
            2.Deposite
            3.Withdraw
            4.Check Balance
            5.Display accounts
            6.Exit
                """)
        action = self.user_acion()
        return action


    def user_acion(self):
        while True:
            user_choice = input("Choose action:\t")
            try:
                user_choice_value = int(user_choice)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if user_choice_value in {1,2,3,4,5,6}:
                return user_choice_value
            else:
                print("Please enter a number between 1 and 6.")

            

class UserInterface:
    def user_option(self):
        valied_options = {1,2,3,4,5,6}
        while True:
            user_signal = input("Enter a number between 1 and 6:\t")
            try:
                value = int(user_signal)
            except ValueError:
                 print("Invalid input. Please enter a number.")
                 continue
            if value in valied_options:
                return value
            else:
                print("Please enter a number between 1 and 5.")
                 

    def employee_options(self):
        print("""
             ------- OPTIONS ---------
            | 1.Add Employee          |   
            | 2.Remove Employee       |
            | 3.Update Employee       |
            | 4.Search Employee       |
            | 5.Display Employee      |  
            | 6.Exit                  |
             -------------------------

            """)
        feedback = self.user_option()
        return feedback

    def get_employeeid(self):
        while True:
            try:
                id = int(input("Enter employee id:\t"))
                return  id
            except ValueError as e:
                print(e)
                continue
            
    
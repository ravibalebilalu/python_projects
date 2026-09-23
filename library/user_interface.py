class UserInterface:
     

    def user_option(self):
        while True:
            
            try:
                user_signal = input("Enter specific value\t")
                if user_signal in "123456":
                    return int(user_signal)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                 

    def library_options(self):
        print("""
             ------- OPTIONS ---------
            | 1.Add Book              |   
            | 2.Remove Book           |
            | 3.Search Book           |
            | 4.Display Books         |  
            | 5.Display Authors       |
            | 6.Exit                  |
             -------------------------

            """)
        feedback = self.user_option()
        return feedback
    


    
             
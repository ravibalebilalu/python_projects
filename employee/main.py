from employee import Employee
from database import Database
from user_interface import UserInterface

database = Database()

user_interface = UserInterface()
 
signal = 0

while signal != 6:
    signal = user_interface.employee_options()

    if signal == 1:
        database.add_employee()
    elif signal == 2:
        employee_id = user_interface.get_employeeid()
        database.remove_employee(employee_id)
    elif signal == 3:
         
        database.update_employee()
    elif signal == 4:
        database.find_employee()
    elif signal == 5:
        employees = database.get_all_employees()
        for employee in employees:
            print(employee)
 



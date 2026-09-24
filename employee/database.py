import csv
import os
from employee import Employee

class Database:

    def __init__(self,filename="employees.csv") -> None:
        self.filename = filename
        self.fieldnames = ["id","name","position","department","salary","joining_date",]
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename,"w",newline="")as f:
                writer = csv.DictWriter(f,fieldnames=self.fieldnames)
                writer.writeheader()


    def add_employee(self):
        while True:
            try:
                id = int(input("Enter id:\t"))
                name  = input("Enter name:\t")
                position  = input("Enter position:\t")
                department  = input("Enter department:\t")
                salary  = int(input("Enter salary:\t"))
                joining_date  = input("Enter joining date (YYYY-MM-DD):\t")
                emplyoyee = {
                    "id":id,
                    "name":name,
                    "position":position,
                    "department":department,
                    "salary":salary,
                    "joining_date":joining_date,
                    
                }
                print(emplyoyee)
                break
            except Exception:
                print("Enter valied key!")

        try:
            with open(self.filename,"a",newline="")as f:
                writer = csv.DictWriter(f,fieldnames=self.fieldnames)
                writer.writerow(emplyoyee)
        except Exception as e:
            print(f"Error adding employee: {e}")

    def get_all_employees(self):
        try:
            with open(self.filename,"r",newline="")as f:
                reader = csv.DictReader(f)
                return list(reader)

        except FileNotFoundError:
            print("Database file not found.")
            return []

    def find_employee(self):
        id = int(input("Enter id: \t"))
        employees = self.get_all_employees()
        for employee in employees:
            if employee["id"] == str(id):
                print(employee)
                return employee
        print("Not found")
        return None
    
    def _rewrite_file(self,employees):
        with open(self.filename,"w",newline="")as f:
            writer = csv.DictWriter(f,fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(employees)

    def update_employee(self):
        updated_fields = {}

        employee = self.find_employee()
        if employee:
            while True:
                try:

                    print("which fields would you like to update?")
                    print("Options:")


                    name_new  = input(f"\tname: {employee['name']}->\t")
                    position_new  = input(f"\tposition: {employee['position'].strip()}->\t")
                    department_new  = input(f"\t department: {employee['department']}->\t")
                    salary_new  = input(f"\tsalary: {employee['salary']}->\t")
                    joining_date_new  = input(f"\tjoining_date:  {employee['joining_date']}->\t")
                    break
                except Exception:
                    print("Enter valied key")

            updated_fields = {
                "id":employee["id"],
                "name": name_new if name_new else employee["name"],
                "position": position_new if position_new else employee["position"],
                "department": department_new if department_new else employee["department"],
                "salary": salary_new if salary_new else employee["salary"],
                "joining_date" : joining_date_new if joining_date_new else employee["joining_date"],

            }
           

            employees = self.get_all_employees()
            found = False
            for emp in employees:
                if employee["id"] == emp["id"]:
                    emp.update(updated_fields)
                    found = True
            if found:
                self._rewrite_file(employees)
                print(f"Employee {id} updated")
            else:
                print(f"Employee {id} not found!")
            return found
        else:
            print("no employee found!")

    def remove_employee(self,id):
            employees = self.get_all_employees()
            remaining = [employee for employee in employees if employee["id"] != str(id)]
            if len(employees) == len(remaining):
                print(f"Employee {id} not found!")
                return False
            self._rewrite_file(remaining)
            print(f"Employee {id} deleted")
            return True



    


    




class Employee:
    def __init__(self,id,name,position,department,salary,joining_date) -> None:
        self.id    = id
        self.name    = name
        self.position    = position
        self.department    = department
        self.salary    = salary
        self.joining_date    = joining_date

    def __str__(self) -> str:
        return self.name


    def display(self):
        print(f"""
                        id:\t{self.id}
                        name:\t{self.name}
                        position:\t{self.position}
                        department:\t{self.department}
                        salary:\t\t{self.salary}
                        joining_date:\t{self.joining_date}

            """)



        
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = str(salary)


employees = [
    Employee('Egor', 100),
    Employee('Petya', 101),
    Employee('Vasya', 102)
]

for employee in employees:
    print(employee.name, employee.salary)
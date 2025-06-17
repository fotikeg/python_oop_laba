class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name}:{self.salary}"
class EmployeeCollection:
    def __init__(self):
        self.employees = []
    def add_employee(self,name, salary):
        new_employee = Employee(name, salary)
        self.employees.append(new_employee)
    def all_employee(self):
        if not self.employees:
            print('Список пуст')
        else:
            for employee in self.employees:
                print(employee)
    def total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary
    def avg_salary(self):
        if not self.employees:
            return 0
        total_salary = self.total_salary()
        average_salary = total_salary/len(self.employees)
        return average_salary

collection = EmployeeCollection()

collection.add_employee('Фатьянов', 225000)
collection.add_employee('Фатьянов2',100)
collection.add_employee('Фатьянов3',69)
print(collection.all_employee())
total_salary = collection.total_salary()
print(total_salary)
average_salary = collection.avg_salary()
print(average_salary)
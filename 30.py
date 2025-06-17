class User:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name


class Employee(User):
    def __init__(self, first_name="", last_name="", salary=0):
        super().__init__(first_name, last_name)
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


employee = Employee()
employee.set_first_name("Егор")
employee.set_last_name("Фатьянов")
employee.set_salary(356952)
first_name = employee.get_first_name()
last_name = employee.get_last_name()
salary = employee.get_salary()

print(f"Имя: {first_name} \nФамилия: {last_name} \nЗарплата: {salary}")
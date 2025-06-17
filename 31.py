class User:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Employee(User):
    def __init__(self, name="", age=18):
        super().__init__()
        self.set_name(name)
        self.set_age(age)
    def set_age(self, age):
        if 18 <= age <= 65:
            self.age = age
        else:
            raise ValueError("18-65 лет")
    def get_age(self):
        return self.age

employee = Employee()
employee.set_name("Егор Фатьянов")
try:
    employee.set_age(50)
    print(f"Имя: {employee.get_name()} \nВозраст: {employee.get_age()}")
    employee.set_age(17)
except ValueError as e:
    print(e)
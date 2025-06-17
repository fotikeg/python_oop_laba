class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name.title(), self.salary)

user1 = Employee('egor','500 dollars')
user1.show()
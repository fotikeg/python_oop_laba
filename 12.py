class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def name(self):
        return self.name
    def salary(self):
        return self.salary
    def show(self):
        self.salary += (self.salary * 10 / 100)


user = Employee('egor', 500)
print(user.name)
print(user.salary)
print(user.show)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.__addSign(self.salary)

    def __addSign(self, num):
        return str(num) + '$'
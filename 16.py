class User:
    __name = None
    __surname = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age


user = User('egor', 500, 18)
print(user.getName())
print(user.getSalary())
print(user.getAge())
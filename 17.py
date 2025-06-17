class User:
    __name = None
    __surname = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def getSalary(self):
        return self.__salary

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age


user = User('', 500, '')
user.setName('Егор')
user.setAge(18)
print(user.getName())
print(user.getAge())
print(user.getSalary())
class User:
    __name = None
    __surname = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setSurn(self, surname):
        self.__surname = surname
    def getSurn(self):
        return self.__surname

class Employee(User):
    def getFull(self):
        return self.__name + ' ' + self.__surname

employee = Employee()
employee.setName("Егор")
employee.setSurn("Фатьянов")
print(f"Имя: {employee.getName()} \nФамилия: {employee.getSurn()}")
try:
    print(employee.getFull())
except AttributeError as e:
    print(f"Ошибка: {e}")
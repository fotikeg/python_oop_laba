class User:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self._capeFirst(self.name)
    def _capeFirst(self, stri):
        return stri.capitalize()

class Employee(User):
    def setSurn(self, surname):
        self.surname = surname
    def getSurn(self):
        return self._capeFirst(self.surname)

employee = Employee()
employee.setName("Егор")
employee.setSurn("Фатьянов")
print(employee.getName())
print(employee.getSurn())
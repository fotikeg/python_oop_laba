class User:
    def set_information(self, name):
        self.name = name

    def get_information(self):
        return self.name


class Employee(User):
    pass


employee = Employee()
employee.set_information('egor')
name = employee.get_information()
print(name)
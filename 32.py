class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('need age more 0')

class Employee(User):
    def setAge(self, age):
        super().setAge(age)
        if age > 120:
            raise Exception('need age less 120')


employee = Employee()
try:
    employee.setAge(35)
    print(f"Age: {employee.age}")
except Exception as e:
    print(e)
try:
    employee.setAge(135)
except Exception as e:
    print(e)
try:
    employee.setAge(-22)
except Exception as e:
    print(e)
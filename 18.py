class Employee:
    def __init__(self, name, salary, age):
        self._name = name
        self._salary = salary
        self._age = age

    def name(self):
        return self._name

    def salary(self):
        return f"{self._salary}$"

    def age(self):
        return self._age

    def age(self, correct_age):
        if 0 <= correct_age <= 120:
            self._age = correct_age
        else:
            raise ValueError('Incorrect age')


user = Employee('Egor', 300, 18)
print(user.name())
print(user.salary())
print(user.age())
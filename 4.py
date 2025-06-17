class Employee:
    name = None
    salary = None
    pass

user1 = Employee()
user2 = Employee()

user1.name = "Романенко"
user1.salary = 52
user2.name = "Белавин"
user2.salary = 35

print(user1.name)
print(user2.name)
salary = user1.salary + user2.salary
print(salary)
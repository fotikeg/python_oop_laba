class Student:
    def show(self):
        return self.cape(self.name)

    def cape(self, stri):
        return stri.title()


user = Student()

user.name = 'egor'
user.surname = 'fatianov'
user.show()
print(user.cape(user.name))
print(user.cape(user.surname))
print(user.cape(user.name[0]) + '.' + user.cape(user.surname[0]) + '.')
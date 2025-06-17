class Emoloyee:
    def show(self, name, salary):
        return name + ' - ' + salary


user = Emoloyee()
user.show('Fatianov', '500 Dollars ')
print(user.show('Fatianov', '500 Dollars '))
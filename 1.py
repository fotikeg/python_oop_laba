class Car:
    color = None
    fuel = None
    tires = None
    durability = None

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def drift(self):
        pass

    def endurance(self):
        pass


MyCar = Car()
MyCar.color = 'black'
print('Цвет машины: ' + MyCar.color)
MyCar.fuel = 95
print('Количество топлива: ' + str(MyCar.fuel))
MyCar.tires = 'new'
print('Состояние покрышек: ' + MyCar.tires)
MyCar.durability = 100
print('Прочность машины = ' + str(MyCar.durability) + '%.')

MyCar.go()
MyCar.turn()
MyCar.drift()
MyCar.stop()
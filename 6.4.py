class Car():
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print(f'Машина повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print(f'Текущая скорость автомобиля: {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)


a = TownCar(70, 'Белый', 'Mazda', False, 'налево')
print(a.speed)
print(a.color)
print(a.name)
print(a.is_police)
print(a.direction)
a.go()
a.stop()
a.turn()
a.show_speed()

b = SportCar(120, 'Синий', 'Jaguar', False, 'направо')
print(b.speed)
print(b.color)
print(b.name)
print(b.is_police)
print(b.direction)
b.go()
b.stop()
b.turn()
b.show_speed()

c = WorkCar(40, 'Черный', 'Hyundai', False, 'направо')
print(c.speed)
print(c.color)
print(c.name)
print(c.is_police)
print(c.direction)
c.go()
c.stop()
c.turn()
c.show_speed()

d = PoliceCar(90, 'Голубой', 'Nissan', True, 'налево')
print(d.speed)
print(d.color)
print(d.name)
print(d.is_police)
print(d.direction)
d.go()
d.stop()
d.turn()
d.show_speed()

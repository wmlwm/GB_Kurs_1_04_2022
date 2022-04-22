class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"{self.name} остановился")

    def turn(self):
        print(f"{self.name} повернул")

    def show_speed(self):
        print(f"{self.name} едет со скоростью {self.speed} км.ч")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль превысил скорость 60 км.ч на {self.speed - 60} км.ч")
        else:
            print(f"Автомобиль едет со скоростью {self.speed} км.ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Автомобиль превысил скорость 40 км.ч на {self.speed - 40} км.ч")
        else:
            print(f"Автомобиль едет со скоростью {self.speed} км.ч")


class PoliceCar(Car):
    pass


t = TownCar(55, 'Black', 'Lincoln')
s = SportCar(90, 'Red', 'Ford Mustang', False)
w = WorkCar(41, 'Yelow', 'GMC', False)
p = PoliceCar(120, 'Black\White', 'Ford', True)

t.go()
t.show_speed()
t.turn()
t.stop()
w.go()
w.show_speed()
w.turn()
w.stop()
print(w.color)
p.go()
print(f'is_police - {p.is_police}')

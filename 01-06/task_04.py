from time import sleep


def tik():
    sleep(0.5)


class Car:

    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if self.speed == 0:
            self.speed = speed
            print(f"{self.full_name()} поехала со скоростью {self.speed} км/ч")
        else:
            print(f"{self.full_name()} уже едет!")
        tik()

    def stop(self):
        if self.speed > 0:
            self.speed = 0
            print(f"{self.full_name()} остановилась")
        else:
            print(f"{self.full_name()} уже стоит!")
        tik()

    def turn(self, direction):
        if self.speed > 0:
            print(f"{self.full_name()} повернула {direction}")
        else:
            print(f"{self.full_name()} не может повернуть стоя на месте!")
        tik()

    def show_speed(self):
        print(
            f"{self.full_name()} {'едет со скоростью' if self.speed > 0 else 'стоит на месте. Скорость'} {self.speed} км/ч")
        tik()

    def speed_change(self, speed=None, delta=None):
        new_speed = speed if speed is not None else delta + self.speed if delta is not None else delta
        if new_speed:
            if new_speed > self.speed:
                print(f"{self.full_name()} разогналась до {new_speed} км/ч")
            elif new_speed < self.speed:
                print(f"{self.full_name()} снизила скорость до {new_speed} км/ч")
            else:
                print(f"{self.full_name()} продолжает ехать со скоростью {new_speed} км/ч")
            self.speed = new_speed
        elif new_speed == 0:
            print(f"{self.full_name()} остановка")
            self.speed = new_speed
        tik()

    def full_name(self):
        return f"{'Полицейска' if self.is_police else self.color.title()} {self.name}"


class TownCar(Car):
    max_speed = 60

    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        super().show_speed()
        if self.speed > self.max_speed:
            print(f"Превышение скорости на {self.speed - self.max_speed} км/ч!!!")


class SportCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name)


class WorkCar(TownCar):
    max_speed = 40

    def __init__(self, color, name):
        super().__init__(color, name)


class PoliceCar(Car):

    def __init__(self, name):
        super().__init__("черная", name, True)


print(" = " * 30)
tc_1 = TownCar("красная", "Вольво")
print(f"Издеваемся над {tc_1.full_name()}")
tc_1.show_speed()
tc_1.go(50)
tc_1.show_speed()
tc_1.go(40)
tc_1.turn("влево")
tc_1.stop()
tc_1.turn("вправо")
tc_1.go(40)
tc_1.speed_change()
tc_1.speed_change(speed=50)
tc_1.show_speed()
tc_1.speed_change(delta=50)
tc_1.show_speed()
tc_1.stop()

print(" = " * 30)
tc_2 = SportCar("зеленая", "Феррари")
print(f"Восхищаемся, глядя на {tc_2.full_name()}")
tc_2.go(5)
tc_2.show_speed()
while tc_2.speed < 360:
    tc_2.speed_change(delta=45)
while tc_2.speed > 50:
    tc_2.speed_change(delta=-60)
tc_2.turn("назад")
tc_2.stop()

print(" = " * 30)
tc_4 = PoliceCar("1155")
print(f"Это {tc_4.full_name()}")
tc_4.go(40)
tc_4.show_speed()

print(" = " * 30)
tc_3 = WorkCar("желтый", "Школьный автобус")
print(f"А это {tc_3.full_name()}")
tc_3.stop()
tc_3.speed_change(speed=60)
tc_3.show_speed()
tc_4.speed_change(speed=80)
tc_4.speed_change(delta=-20)
while tc_3.speed > 0:
    tc_3.speed_change(delta=-10)
    tc_4.speed_change(delta=-10)

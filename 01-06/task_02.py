class Road:
    # Длина и ширина в метрах
    _length = 0
    _width = 0

    # Удельный вес в кг/м3
    __specific_weight = 2500
    # Толщина покрытия в см
    _height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return self._length * self._width * self.__specific_weight * self._height / 100000

    def set_params(self, length=None, width=None, height=None):
        if length:
            self._length = length
        if width:
            self._width = width
        if height:
            self._height = height

    def calc_toString(self):
        return f"Для дороги длиной {self._length} м., шириной {self._width} м. и толщиной покрытия {self._height} см. потребуется {self.calc()} т. асфальта"


road = Road(5000, 20)
print(road.calc_toString())

road.set_params(length=12000, width=30)
print(road.calc_toString())

road.set_params(length=1, width=1, height=100)
print(road.calc_toString())

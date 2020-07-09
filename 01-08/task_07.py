class myComplex:
    x, y = 0, 0
    def __init__(self, *xy):
        try:
            if len(xy) > 2:
                raise ValueError
            elif len(xy) == 2:
                x, y = xy
            elif len(xy) == 1:
                x, y = 0, xy[0]
            else:
                x, y = 0, 0
            if type(x) not in [int, float] or type(y) not in [int, float]:
                raise ValueError
            self.x = x
            self.y = y
        except ValueError:
            print("Не верные значения")

    def __add__(self, other):
        return myComplex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return myComplex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return myComplex(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __truediv__(self, other):
        try:
            x = (self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2)
            y = (self.y * other.x - self.x * other.y) / (other.x ** 2 + other.y ** 2)
            return myComplex(x, y)
        except ZeroDivisionError:
            print("Деление на ноль!")

    def __str__(self):
        return f"({self.x if self.x != 0 else ''}{'+' if self.x != 0 and self.y >= 0 else ''}{self.y}j)"

    @staticmethod
    def examples(c_1, c_2):
        """
        Статичный метод для вывода примеров операций над комплексными числами
        """
        print(f"Сложение: {c_1} + {c_2} = {c_1 + c_2}")
        print(f"Вычитание 1: {c_1} - {c_2} = {c_1 - c_2}")
        print(f"Вычитание 2: {c_2} - {c_1} = {c_2 - c_1}")
        print(f"Умножение: {c_1} * {c_2} = {c_1 * c_2}")
        try:
            print(f"Деление 1: {c_1} / {c_2} = {c_1 / c_2}")
        except:
            print("---")
        try:
            print(f"Деление 2: {c_2} / {c_1} = {c_2 / c_1}")
        except:
            print("---")
        print("*" * 30)


dc_1 = complex(1, 2)
print(dc_1)
dc_2 = complex(3, 4)
print(dc_2)
myComplex.examples(dc_1, dc_2)
dc_3 = complex()
print(dc_2)
myComplex.examples(dc_1, dc_3)

mc_1 = myComplex(1, 2)
print(mc_1)
mc_2 = myComplex(3, 4)
print(mc_2)
myComplex.examples(mc_1, mc_2)
mc_3 = myComplex()
print(mc_3)
myComplex.examples(mc_1, mc_3)

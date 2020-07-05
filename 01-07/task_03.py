class Cell:
    cells_count = 0

    def __init__(self, count):
        self.__count = abs(count)
        self.current_cell = self.cells_count
        Cell.cells_count += 1

    @property
    def count(self):
        return self.__count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count >= other.count:
            return Cell(self.count - other.count)
        else:
            print("Вычитать можно только из большего меньшее!")

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        try:
            return Cell(self.count // other.count)
        except ZeroDivisionError:
            print("Деление на нулевую клетку!")

    def make_order(self, count_in_row):
        cell_count = self.__count
        while cell_count > 0:
            print("*" * (count_in_row if cell_count > count_in_row else cell_count))
            cell_count -= count_in_row

    def __str__(self):
        return f"Клетка {self.current_cell} с количеством ячеек {self.count}"


cell_1 = Cell(11)
print(cell_1)
cell_1.make_order(3)

cell_2 = Cell(45)
print(cell_2)
cell_2.make_order(10)

print("\nСуммирование (cell_1 + cell_2):")
print(cell_1 + cell_2)

print("\nРазность 1 (cell_1 - cell_2):")
print(cell_1 - cell_2)

print("\nРазность 2 (cell_2 - cell_1):")
print(cell_2 - cell_1)

print("\nУмножение (cell_1 * cell_2):")
print(cell_1 * cell_2)

print("\nДеление 1 (cell_1 / cell_2):")
print(cell_1 / cell_2)

print("\nДеление 2 (cell_2 / cell_1):")
print(cell_2 / cell_1)

cell_3 = Cell(0)
print(f"\n{cell_3}")
print("Деление 3 (деление на 0) (cell_1 / cell_3):")
print(cell_1 / cell_3)

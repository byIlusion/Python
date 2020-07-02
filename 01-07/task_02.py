from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def clothes_type(self):
        pass

    @property
    @abstractmethod
    def size(self):
        pass

    @size.setter
    @abstractmethod
    def size(self, size):
        pass

    @abstractmethod
    def calculate(self):
        pass


class Coat(ClothesAbstract):
    __clothes_type = "Пальто"
    __min_size = 35
    __max_size = 60

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > self.__max_size:
            self.__size = self.__max_size
            print(f"Внимание! Размер {size} ({self.__clothes_type}) уменьшен до максимального: {self.__size}")
        elif size < self.__min_size:
            self.__size = self.__min_size
            print(f"Внимание! Размер {size} ({self.__clothes_type}) увеличен до минимального: {self.__size}")
        else:
            self.__size = size

    @property
    def clothes_type(self):
        return self.__clothes_type

    def calculate(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f"Тип: {self.clothes_type}, размер: {self.size}, расход ткани: {self.calculate():.02f} метров"


class Costume(ClothesAbstract):
    __clothes_type = "Костюм"
    __min_size = 100
    __max_size = 200

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > self.__max_size:
            self.__size = self.__max_size
            print(f"Внимание! Рост {size} ({self.__clothes_type}) уменьшен до максимального: {self.__size}")
        elif size < self.__min_size:
            self.__size = self.__min_size
            print(f"Внимание! Рост {size} ({self.__clothes_type}) увеличен до минимального: {self.__size}")
        else:
            self.__size = size

    @property
    def clothes_type(self):
        return self.__clothes_type

    def calculate(self):
        # Что-то кажется формула неверная, или я не понял как ее интерпретировать на моей задаче.
        return self.size * 2 + 0.3

    def __str__(self):
        return f"Тип: {self.clothes_type}, размер: {self.size}, расход ткани: {self.calculate():.02f} метров"


clothes_1 = Coat(40)
print(f"Пример 1:\n{clothes_1}", end="\n\n")
print(f"Размер у {clothes_1.clothes_type} на примере 1: {clothes_1.size}", end="\n\n")
clothes_1 = Coat(30)
print(f"Пример 2:\n{clothes_1}", end="\n\n")
clothes_1 = Coat(80)
print(f"Пример 3:\n{clothes_1}", end="\n\n")

clothes_2 = Costume(170)
print(f"Пример 4:\n{clothes_2}", end="\n\n")
clothes_2 = Costume(70)
print(f"Пример 5:\n{clothes_2}", end="\n\n")
clothes_2 = Costume(270)
print(f"Пример 6:\n{clothes_2}", end="\n\n")

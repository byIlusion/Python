class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def get_position(self):
        return self.position


workers = []
workers.append(Position("Иван", "Иванов", "Плотник", {"wage": 10000, "bonus": 2000}))
workers.append(Position("Петр", "Петров", "Сборщик", {"wage": 8000, "bonus": 8000}))
workers.append(Position("Семен", "Семенов", "Конструктор", {"wage": 15000, "bonus": -2000}))
workers.append(Position("Сан", "Саныч", "Дирик", {"wage": 8800, "bonus": 120000}))

[print(f"{w.get_position()} {w.get_full_name()} получил {w.get_total_income()}") for w in workers]

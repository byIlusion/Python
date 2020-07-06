class Date:
    __month_list = {
        1: ("Январь", 31),
        2: ("Февраль", 28),
        3: ("Март", 31),
        4: ("Апрель", 30),
        5: ("Май", 31),
        6: ("Июнь", 30),
        7: ("Июль", 31),
        8: ("Август", 31),
        9: ("Сентябрь", 30),
        10: ("Октябрь", 31),
        11: ("Ноябрь", 30),
        12: ("Декабрь", 31),
    }
    date_parsed = []

    def __init__(self, date):
        self.date = date
        try:
            self.date_parsed = self.parse_date(date)
            self.day, self.month, self.year = self.date_parsed
        except:
            print("Не удалось распознать дату!")
        if not Date.validate_date(self.date_parsed):
            print("Сброс даты")
            self.day, self.month, self.year = 1, 1, 2020

    @classmethod
    def parse_date(cls, date):
        try:
            return list(map(int, date.split("-")))
        except:
            print("Не верный формат даты!")

    @staticmethod
    def validate_date(date):
        try:
            if len(date) != 3:
                raise Exception
            day, month, year = date
            if month < 1 or month > len(Date.__month_list):
                raise Exception
            day_max = Date.__month_list[month][1]
            if Date.__month_list[month][1] < 30 and year % 4 == 0:
                day_max += 1
            if day < 1 or day > day_max:
                raise Exception
        except:
            print("Ошибка даты!")
            return False
        else:
            return True

    def __str__(self):
        return f"{self.day:02d} {self.__month_list[self.month][0][:3].lower()}. {self.year} год."


d_1 = Date("06-07-2020")
print(d_1, end=f"\n{'*' * 30}\n\n")

d_2 = Date("06-июля")
print(d_2, end=f"\n{'*' * 30}\n\n")

d_3 = Date("32-07-2020")
print(d_3, end=f"\n{'*' * 30}\n\n")

date = "11-08-2020"
print(f"Парсинг даты {date}: {Date.parse_date(date)}")
print(f"Валидация даты из данных {Date.parse_date(date)}: {Date.validate_date(Date.parse_date(date))}")
print(Date(date), end=f"\n{'*' * 30}\n\n")

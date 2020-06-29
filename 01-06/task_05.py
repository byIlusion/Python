class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print(f"Это {self.title.lower()}. Начинаем отрисовку.")


stationery = Stationery()
stationery.draw()


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        print(f"В правой руке {self.title.lower()}, делаем рисунок в стиле грфики")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        print(f"{self.title.title()} нужен чтоб заштриховать рисунок")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        print(f"{self.title.title()} вообще не для рисования, а так...")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()

import os


class Warehouse:
    last_id = 0
    warehouses = []

    def __init__(self, name):
        self.name = name
        self.id = self.last_id
        self.equipments = {}
        Warehouse.last_id += 1
        Warehouse.warehouses.append(self)

    def __str__(self):
        return f"{self.name} [{self.id}] - ({len(self.equipments)})"

    @staticmethod
    def create_warehouse(name=""):
        while name == "":
            name = input("Введите название склада: ")
        temp = Warehouse(name)

    def add_equipment(self, equipment, count=1):
        if equipment.id not in self.equipments:
            self.equipments[equipment.id] = {
                "obj": equipment,
                "count": count
            }
        else:
            self.equipments[equipment.id]["count"] += count

    def remove_equipment(self, id, count=1):
        if id in self.equipments:
            if self.equipments[id]["count"] > count:
                self.equipments[id]["count"] -= count
                return {
                    "obj": self.equipments[id]["obj"],
                    "count": count
                }
            else:
                return self.equipments.pop(id)
        else:
            return None

    def gen_equipments(self):
        for i, eq in self.equipments.items():
            yield f"{eq['obj']} - {eq['count']} шт"

    def list_equipments(self):
        if len(self.equipments):
            [print(f"{eq}") for eq in self.gen_equipments()]
        else:
            print("На данном складе оргтехники нет!")

    def get_equipments(self, index=None):
        if index is None:
            return [(eq['obj'], eq['count']) for eq in self.equipments.values()]
        else:
            return list(self.equipments.values())[index]


class Equipment:
    last_id = 0
    types = ["", "Printer", "Scanner", "MFU"]
    eq_type = 0
    equipments = []

    def __init__(self, name, count=1):
        self.name = name
        self.id = self.last_id
        self.count = count
        self.warehouses = {}
        Equipment.last_id += 1
        Equipment.equipments.append(self)
        self.add_to_warehouse(count, 0)

    def __str__(self):
        return f"id {self.id}: {Equipment.types[self.eq_type]} - {self.name}"

    @classmethod
    def create_equipment(cls, name="", count=0):
        while name == "":
            name = input(f"Введите название оргтехники ({cls.types[cls.eq_type]}): ")
        while count <= 0:
            try:
                count = int(input(f"Введите количество ({cls.types[cls.eq_type]} {name}): "))
                if count <= 0:
                    raise ValueError
            except ValueError:
                print("Должно быть целое положительное число")
                count = 0
        temp = cls(name, count)

    def add_to_warehouse(self, count, warehouse_id):
        self.warehouses[warehouse_id] = count
        Warehouse.warehouses[warehouse_id].add_equipment(self, count)

    def remove_from_warehouse(self, count, warehouse_id):
        if warehouse_id in self.warehouses:
            if self.warehouses[warehouse_id] > count:
                self.warehouses[warehouse_id] -= count
            else:
                self.warehouses.pop(warehouse_id)
        Warehouse.warehouses[warehouse_id].remove_equipment(self.id, count)

    def list(self):
        [print(f"id {i}: {Warehouse.warehouses[i].name} - {eq} шт") for i, eq in self.warehouses.items()]

    def get_with_count(self):
        return f"{Equipment.types[self.eq_type]} - {self.name} [{self.id}] ({self.count} шт.)"

    def move_count(self, count, from_id, to_id):
        self.remove_from_warehouse(count, from_id)
        self.add_to_warehouse(count, to_id)


class EqPrinter(Equipment):
    eq_type = 1
    actions = ["Печатать"]

    def action(self, action):
        if action == 1:
            self.to_print(self.enter_text())

    def enter_text(self):
        text = []
        print("Введите текст для печати:")
        while True:
            line = input()
            if line == '':
                break
            text.append(line)
        return "\n".join(text)


    def to_print(self, text=''):
        print(f"{'* ' * 30}\n{Equipment.types[self.eq_type]} {self.name} (id={self.id}) печатает:\n{text}", end=f"\n{'* ' * 30}\n\n")


class EqScanner(Equipment):
    eq_type = 2
    actions = ["Сканировать"]

    def action(self, action):
        if action == 1:
            self.to_scan()

    def to_scan(self):
        print(f"{'* ' * 30}\n{Equipment.types[self.eq_type]} {self.name} (id={self.id}) сканирует...", end=f"\n{'* ' * 30}\n\n")


class EqMFU(Equipment):
    eq_type = 3
    actions = ["Печатать", "Сканировать", "Копировать"]

    def action(self, action):
        if action == 1:
            self.to_print(self.enter_text())
        if action == 2:
            self.to_scan()
        if action == 3:
            self.to_coping()

    def enter_text(self):
        text = []
        print("Введите текст для печати:")
        while True:
            line = input()
            if line == '':
                break
            text.append(line)
        return "\n".join(text)

    def to_print(self, text=''):
        print(f"{'* ' * 30}\n{Equipment.types[self.eq_type]} {self.name} (id={self.id}) печатает:\n{text}", end=f"\n{'* ' * 30}\n\n")

    def to_scan(self):
        print(f"{'* ' * 30}\n{Equipment.types[self.eq_type]} {self.name} (id={self.id}) сканирует...", end=f"\n{'* ' * 30}\n\n")

    def to_coping(self):
        print(f"{'* ' * 30}\n{Equipment.types[self.eq_type]} {self.name} (id={self.id}) делает копию документа...", end=f"\n{'* ' * 30}\n\n")


def get_menu(elements, question="Выберете действие"):
    while True:
        os.system("cls||clear")
        print(f"{'-' * 59}\n{' >> '.join(breadcrumbs)}\n{'- ' * 30}")
        menu = [f"{i} => {el}" for i, el in enumerate(elements, 1)]
        menu.append("0 => Выход")
        menu = "\n".join(menu)
        print(f"{menu}\n{'-' * 59}")
        action = input(f"{question} [0-{len(elements)}]: ")
        if action.isdigit() and int(action) >= 0 and int(action) <= len(elements):
            print("\n\n")
            return int(action)


def manage_main_menu():
    breadcrumbs.append("Главное меню")
    while True:
        action = get_menu(["Просмотр списка складов", "Просмотр полного списка товаров"], "Выберете действие")
        if action == 0:
            break
        if action == 1:
            manage_warehouses()
        if action == 2:
            manage_equipment(Equipment.equipments)
    breadcrumbs.pop()


def manage_warehouses():
    breadcrumbs.append("Склады")
    while True:
        menu = Warehouse.warehouses.copy()
        menu.append("Добавить склад")
        action_1 = get_menu(menu, "Выберете склад для действий")
        if action_1 == 0:
            break
        elif action_1 == len(menu):
            Warehouse.create_warehouse()
        else:
            breadcrumbs.append(str(Warehouse.warehouses[action_1 - 1].name))
            current_warehouse = Warehouse.warehouses[action_1 - 1]
            while True:
                action_2 = get_menu(["Список оргтехники данного склада", "Переместить оргтехнику..."])
                if action_2 == 0:
                    break
                if action_2 == 1:
                    current_warehouse.list_equipments()
                    input("")
                if action_2 == 2:
                    breadcrumbs.append("Перемещение оргтехники")

                    sel_equipments = None
                    count = 0
                    action_3 = get_menu([el for el in current_warehouse.gen_equipments()], "Выберете что перемещать")
                    if action_3 != 0:
                        sel_equipments, max_count = current_warehouse.get_equipments(action_3 - 1).values()

                        while count == 0:
                            try:
                                count = int(input("Введите количество для перемещения: "))
                                if count > max_count:
                                    count = 0
                                    raise ValueError
                            except ValueError:
                                print("Должно быть число и не больше допустимого!")

                    if sel_equipments is not None and count > 0:
                        menu = Warehouse.warehouses.copy()
                        menu.remove(current_warehouse)
                        while True:
                            action_3 = get_menu(menu, "Выберете склад куда переметсить")
                            if action_3 != 0:
                                sel_equipments.move_count(count, current_warehouse.id, menu[action_3 - 1].id)
                            break

                    breadcrumbs.pop()
            breadcrumbs.pop()
    breadcrumbs.pop()


def manage_equipment(equipments):
    breadcrumbs.append("Оргтехника")
    while True:
        menu = equipments.copy()
        menu.append("Добавить оргтехнику")
        action_1 = get_menu(menu, "Выберете оргтехнику для действий")
        if action_1 == 0:
            break
        if action_1 == len(menu):
            breadcrumbs.append("Добавление оргтехники")
            menu = Equipment.types[1:]
            action_2 = get_menu(menu, "Выберете тип оргтехники")
            if action_2 == 1:
                EqPrinter.create_equipment()
            if action_2 == 2:
                EqScanner.create_equipment()
            if action_2 == 3:
                EqMFU.create_equipment()
            breadcrumbs.pop()
        else:
            current_equipment = equipments[action_1 - 1]
            breadcrumbs.append(str(current_equipment))
            menu = current_equipment.actions.copy()
            menu.append("Наличие на складах")
            while True:
                action_2 = get_menu(menu)
                if action_2 == 0:
                    break
                elif action_2 == len(menu):
                    current_equipment.list()
                    input("")
                else:
                    current_equipment.action(action_2)
                    input()

            breadcrumbs.pop()
    breadcrumbs.pop()


breadcrumbs = []

# Добавляем склады
# warehouse_1 = Warehouse("Склад оптовый")
Warehouse.create_warehouse("Склад оптовый")
# print(warehouse_1)
# store_1 = Warehouse("Магазин основной")
Warehouse.create_warehouse("Магазин основной")
# print(store_1)


# Создаем объекты оргтехники
# printer_1 = EqPrinter("Cannon Printer", 10)
EqPrinter.create_equipment("Cannon Printer", 10)
# print(printer_1)
# printer_1.to_print("Text\ntext")
#
# scanner_1 = EqScanner("HP Scan", 2)
EqScanner.create_equipment("HP Scan", 2)
# print(scanner_1)
# scanner_1.to_scan()
#
# mfu_1 = EqMFU("Epson L366")
EqMFU.create_equipment("Epson L366", 1)
# print(mfu_1)
# mfu_1.to_print('text')
# mfu_1.to_scan()


manage_main_menu()

print(f"{'+' * 20}  Пока!  {'+' * 20}")

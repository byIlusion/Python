class Warehouse:
    count = 0
    warehouses = []
    equipments = {}

    def __init__(self, name):
        self.name = name
        self.id = self.count
        Warehouse.count += 1
        Warehouse.warehouses.append(self)

    def __str__(self):
        return f"{self.name} [{self.id}] - ({len(self.equipments)})"

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


class Equipment:
    last_id = 0
    types = ["", "Printer", "Scanner", "MFU"]
    type = 0
    equipments = []
    warehouses = {}

    def __init__(self, name, count=1):
        self.name = name
        self.id = self.last_id
        Equipment.last_id += 1
        self.count = count
        Equipment.equipments.append(self)

    def __str__(self):
        return f"{Equipment.types[self.type]} - {self.name} [{self.id}] ({self.count} шт.)"

    # def move_count(self, count):
    #     if count > self.count:
    #         print("Превышено количество!")



class EqPrinter(Equipment):
    type = 1
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
        print(f"{'* ' * 30}\n{Equipment.types[self.type]} {self.name} (id={self.id}) печатает:\n{text}", end=f"\n{'* ' * 30}\n\n")


class EqScanner(Equipment):
    type = 2
    actions = ["Сканировать"]

    def action(self, action):
        if action == 1:
            self.to_scan()

    def to_scan(self):
        print(f"{'* ' * 30}\n{Equipment.types[self.type]} {self.name} (id={self.id}) сканирует...", end=f"\n{'* ' * 30}\n\n")


class EqMFU(Equipment):
    type = 3
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
        print(f"{'* ' * 30}\n{Equipment.types[self.type]} {self.name} (id={self.id}) печатает:\n{text}", end=f"\n{'* ' * 30}\n\n")

    def to_scan(self):
        print(f"{'* ' * 30}\n{Equipment.types[self.type]} {self.name} (id={self.id}) сканирует...", end=f"\n{'* ' * 30}\n\n")

    def to_coping(self):
        print(f"{'* ' * 30}\n{Equipment.types[self.type]} {self.name} (id={self.id}) делает копию документа...", end=f"\n{'* ' * 30}\n\n")


# Добавляем склады
warehouse_1 = Warehouse("Склад оптовый")
# print(warehouse_1)
store_1 = Warehouse("Магазин основной")
# print(store_1)


# Создаем объекты оргтехники
printer_1 = EqPrinter("Cannon Printer", 10)
# print(printer_1)
# printer_1.to_print("Text\ntext")
#
scanner_1 = EqScanner("HP Scan", 2)
# print(scanner_1)
# scanner_1.to_scan()
#
mfu_1 = EqMFU("Epson L366")
# print(mfu_1)
# mfu_1.to_print('text')
# mfu_1.to_scan()


breadcrumbs = []


def get_menu(elements, question="Выберете действие"):
    while True:
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
        action_1 = get_menu(Warehouse.warehouses, "Выберете склад для действий")
        if action_1 > 0:
            breadcrumbs.append(str(Warehouse.warehouses[action_1 - 1]))
            # print(Warehouse.warehouses[action_1 - 1])
            current_warehouse = Warehouse.warehouses[action_1 - 1]
            # print(current_warehouse)
            action_2 = get_menu(["Список оргтехники данного склада"])
            if action_2 > 0:
                breadcrumbs.append("Список оргтехники")
                action_3 = get_menu(current_warehouse.equipments)
                breadcrumbs.pop()
            breadcrumbs.pop()
        else:
            break
    breadcrumbs.pop()


def manage_equipment(equipments):
    breadcrumbs.append("Оргтехника")
    while True:
        action_1 = get_menu(equipments, "Выберете оргтехнику для действий")
        if action_1 > 0:
            current_equipment = equipments[action_1 - 1]
            breadcrumbs.append(str(current_equipment))
            menu = current_equipment.actions.copy()
            menu.append("Переместить на другой склад")
            while True:
                action_2 = get_menu(menu)
                if action_2 == 0:
                    break
                if action_2 == len(menu):
                    print("Реализовать перемещение")
                else:
                    current_equipment.action(action_2)

            breadcrumbs.pop()
        else:
            break
    breadcrumbs.pop()


manage_main_menu()

print(f"{'+' * 20}  Пока!  {'+' * 20}")

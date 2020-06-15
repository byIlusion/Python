import os
default_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}), 
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

products = [] if 'default_list' not in locals() else default_list.copy()
while True:
    os.system('cls||clear')
    print("1 - Добавить товар к списку")
    print("2 - Смотреть список товаров")
    print("3 - Смотреть аналитику по таварам")
    print("0 - Выход", end="\n\n")
    command = input("Введите команду: ")
    print()
    if command.isdigit() and 0 <= int(command) <= 3:
        if command == '0':
            break

        elif command == '1':
            product = {}
            product['название'] = input("Введите название товара: ")
            while True:
                product['цена'] = input("Введите стоимость товара: ")
                if product['цена'].isnumeric():
                    product['цена'] = float(product['цена'])
                    break
                else:
                    print("Не верный ввод стоимости. Должно быть число!")
            while True:
                product['количество'] = input("Введите количество товара: ")
                if product['количество'].isdigit():
                    product['количество'] = int(product['количество'])
                    break
                else:
                    print("Не верный ввод количества. Должно быть целое число!")
            while True:
                product['eд'] = input("Выберете единицу измерения товара:\n1 - шт.\n2 - компл.\n")
                if product['eд'].isdigit() and 1 <= int(product['eд']) <= 2:
                    product['eд'] =  'шт.' if product['eд'] == '1' else 'компл.'
                    break
                else:
                    print("Не верный ввод. Попробуйте еще!")

            product_index = products[len(products) - 1][0] + 1 if len(products) else 0
            products.append((product_index, product))

        elif command == '2':
            print(f"Список товаров:\n{'#':^5}{'Название':^20}{'Цена':^10}{'Количество':^15}{'Ед. изм.':^7}")
            for product in products:
                print(f"{product[0]:^5}{product[1]['название']:<20}{product[1]['цена']:>10.2f}{product[1]['количество']:^15}{product[1]['eд']:^7}")

        else:
            print(f"Аналитика товаров:")
            analitica = {
                "название": [],
                "цена": [],
                "количество": [],
                "eд": []
            }
            for product in products:
                analitica["название"].append(product[1]["название"])
                analitica["цена"].append(product[1]["цена"])
                analitica["количество"].append(product[1]["количество"])
                analitica["eд"].append(product[1]["eд"])

            print(f"Всего товаров: {len(products)}")
            print(f"Уникальных товаров: {len(list(set(analitica['название'])))} - {list(set(analitica['название']))}")
            print(f"Стоимость всех товаров: {sum(analitica['цена']):.2f}")
            print(f"Уникальных цен: {len(list(set(analitica['цена'])))} - {list(set(analitica['цена']))}")
            print(f"Количество всех товаров: {sum(analitica['количество'])}")
            print(f"Уникальных количеств: {len(list(set(analitica['количество'])))} - {list(set(analitica['количество']))}")
            print(f"Количество штучных товаров: {analitica['eд'].count('шт.')}")
            print(f"Количество комплектов: {analitica['eд'].count('компл.')}")

        input("Нажмите Enter для возврата в меню")
    else:
        input("Не верная команда... Нажмите Enter")

print("Good bye!")

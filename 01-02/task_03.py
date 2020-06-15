month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
month_dict = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима'
}
month_num = input("Введите номер месяца (1-12): ")
month_num = int(month_num) if month_num.isdigit() and 1 <= int(month_num) <= 12 else None
if month_num:
    print(f"{month_num}-й месяц года - это {month_list[month_num - 1]}, и это {month_dict[month_num]}")
else:
    print("Не верный ввод")

from sys import argv

hours = 0.0
rate = 500
award = 50


def output_help(error=None):
    if error:
        print(error)
    print(f"Использование: python3 {argv[0]} [ЧАСЫ] [СТАВКА] [ПРЕМИЯ]")
    print("\t[ЧАСЫ]\t\t- Float. Выработка в часах.")
    print(f"\t[СТАВКА]\t- Int. Ставка за час в у.е. (По-умолчанию: {rate})")
    print(f"\t[ПРЕМИЯ]\t- Int. Премия в процентах. (По-умолчанию: {award})")
    print(f"Пример ввода: python3 {argv[0]} 2.5 100 15")


if 2 <= len(argv) <= 4:
    try:
        hours = float(argv[1])
        if len(argv) > 2:
            rate = int(argv[2])
        if len(argv) == 4:
            award = int(argv[3])
        print(f"Расчет ЗП сотрудника")
        print(f"ЗП: {hours} * {rate} = {hours * rate} у.е.")
        print(f"Премия: {hours * rate} * {award}% = {hours * rate * (award / 100)} у.е.")
        print(f"Итог: {hours * rate} + {hours * rate * (award / 100)} = {hours * rate + hours * rate * (award / 100)}")
    except ValueError:
        output_help("Не верный ввод!!!")
else:
    output_help()

def division(a, b):
    # Добавить try except
    if b == 0:
        print("Деление на ноль!")
        return
    else:
        return a / b

while True:
    digits = input("Введите пример деления (a/b): ").split("/")
    if len(digits) == 2 and digits[0].isnumeric() and digits[1].isnumeric():
        print(division(float(digits[0]), float(digits[1])))
        break
    else:
        print("Не верный ввод. Попробуйте еще!")
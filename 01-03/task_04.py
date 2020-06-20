def my_pow(x, y):
    """Кастомная функция возведения в степень

    Позиционные параметры:
    x - число, которое необходимо возвести в степень
    y - степень числа

    """
    x_pow = 1
    try:
        for i in range(abs(y)):
            x_pow *= x
        if y < 0:
            x_pow = 1 / x_pow
        return x_pow
    except TypeError:
        return "Возведение в дробную степень не реализовано!"


while True:
    try:
        x = float(input("Введите действительное положительное число X (но можно и отрицательное): "))
        y = int(input("Введите целое отрицательное число Y (но можно и положительное): "))
        break
    except:
        print("Не верный ввод. Начните заново!")

print(f"Вариант 1: кастомня функция my_pow({x}, {y}) = {my_pow(x, y)}")
print(f"Вариант 2: базовыя функция pow({x}, {y}) = {pow(x, y)}")
print(f"Вариант 3: стандартный арифмитический оператор {x} ** {y} = {x ** y}")

def division(a, b):
    '''Функция деления. Возвращает частное от деления'''
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return "Ошибка! Деление на ноль!"
    except ValueError:
        return "Не число!"

while True:
    '''Ввод примера, пока не будет верного ввода'''
    digits = input("Введите пример деления (a/b) или нажмите Enter: ").replace(',', '.').split("/")
    if digits == ['']:
        break
    try:
        '''Обработка если числа не 2'''
        if len(digits) != 2:
            raise Exception("Должно быть 2 числа")
        print(division(digits[0], digits[1]))
    except ValueError:
        print("Не верный ввод. Попробуйте еще!")
    except Exception as e:
        print(e)

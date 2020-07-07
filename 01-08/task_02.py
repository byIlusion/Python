class MyZeroDevisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a, b = map(int, input("Введите пример деления (к примеру, 5/3): ").split('/'))
    if b == 0:
        raise MyZeroDevisionException("Ошибка! Деление на ноль!")
    c = a / b
except MyZeroDevisionException as err:
    print(err)
except:
    print("Ошибка ввода!")
else:
    print(f"{a} / {b} = {c:.02f}")

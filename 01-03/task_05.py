def filter_digits(bad_str):
    """Функция фильтрует входящую строку и возвращает массив из целых чисел,
    которые были в строке.

    """
    clear_str = ''
    for c in bad_str:
        if ord(c) == 32 or 48 <= ord(c) <= 57:
            clear_str += c
    return clear_str.strip().split()

doWork = True
summa = 0
summ_func = lambda s, el: s + int(el)
while doWork:
    elements = input("Вводите числа через пробел. \"Q\" в конце ввода - выход:\n")
    if elements[len(elements) - 1:len(elements)].lower() == 'q':
        doWork = False
    elements = filter_digits(elements)
    print(f"\t{summa}", end='')
    for el in elements:
        print(f" + {el}", end='')
        summa = summ_func(summa, el)
    print(f" = {summa}")
    print(f"summa = {summa}")

print('Exit')

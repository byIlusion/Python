from itertools import count, cycle, takewhile


# Вариант А
print("Вариант A:")
def my_iterator(start, stop, step=1):
    """Кастомный итератор с задаваемым диапазоном и шагом

    start - Стартовое число
    stop - Конечное число
    step - Шаг итератора

    """
    for el in count(start, step):
        if el > stop:
            break
        print(el)


my_iterator(3, 10)


# Вариант B
print("Вариант B:")
def my_cycle(itering, count_iterations):
    """Кастомный итератор по циклу

    itering - Итерируемый элемент
    count_iterations - количество итераций

    """
    for el in cycle(itering):
        if count_iterations <= 0:
            break
        print(el)
        count_iterations -= 1


custom_list = [True, False, None]
my_cycle(custom_list, 7)


# Вариант *A
print("Вариант A*:")
def my_iter(num, stop, step=1):
    """Кастомный итератор с задаваемым диапазоном и шагом
    без "break"

    num - Стартовое число
    stop - Конечное число
    step - Шаг итератора

    """
    iterator = count(num, step)
    while stop > num:
        num = next(iterator)
        print(num)


my_iter(13, 20, 3)


# Вариант A**
print("Вариант A**:")
def my_iter_2(start, stop):
    """Кастомный итератор с задаваемым диапазоном
    без "break"

    start - Стартовое число
    stop - Конечное число

    """
    iterator = iter(range(start, stop + 1))
    for el in iterator:
        print(el)


my_iter_2(21, 30)


# Вариант A***
print(f"Вариант A***:\n{list(takewhile(lambda x: x < 11, count(3)))}")

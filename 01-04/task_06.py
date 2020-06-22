from itertools import count, cycle, takewhile

# Вариант А
def my_iterator(start, stop, step = 1):
    """Кастомный итератор с задаваемым диапазоном

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


# Вариант *
# print(takewhile(lambda x: x < 10, [el for el in count(0)]))

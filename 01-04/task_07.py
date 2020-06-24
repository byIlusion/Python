def fact(n):
    """Функция расчитывает факториал

    :param n: Число, до которого расчитывается факториал
    :return: Указатель на итератор

    """
    f = 1
    for el in range(1, n + 1):
        f *= el
        yield f


num = 10
result_list = {f"!{i}": el for i, el in enumerate(fact(num), 1)}
print(f"Факториал чисел от !1 до !{num} (представление в словаре):\n{result_list}")

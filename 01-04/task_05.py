from functools import reduce


def my_comp(a, b):
    return a * b


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Исходный список: {my_list}\nКонечный результат: {reduce(my_comp, my_list)}")

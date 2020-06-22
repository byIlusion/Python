init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [el for el in init_list if init_list.count(el) == 1]
print(f"Исходный список: {init_list}\nКонечный список: {result_list}")

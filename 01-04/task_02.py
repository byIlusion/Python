init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for i, el in enumerate(init_list) if i > 0 and el > init_list[i - 1]]
print(f"Исходный список: {init_list}\nКонечный список: {result_list}")

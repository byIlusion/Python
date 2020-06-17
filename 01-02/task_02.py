list_init = []
# list_init = ['5', 'h', 'hello', 'True', '123', 'qwer', 'asdasdasd']   # Чтоб не париться с вводом
while True:
    el = input("Введите элемент списка и/или нажмите Enter: ")
    if el == '':
        break
    list_init.append(el)

list_result = list_init.copy()
i = 0
while i < len(list_result) - 1:
    list_result[i], list_result[i + 1] = list_result[i + 1], list_result[i]
    i += 2

print(f"Исходный список: \t{list_init}")
print(f"Измененный список: \t{list_result}")

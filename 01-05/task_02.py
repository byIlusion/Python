file_name = "files/text for task_01.txt"
try:
    with open(file_name) as f:
        text_from_file = f.readlines()
    print(f"Количество строк в тексте: {len(text_from_file)}")
    [print(f"Строка {i}, символов: {len(el)} \t-> {el!r}") for i, el in enumerate(text_from_file, 1)]
except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Ошибка открытия файла")

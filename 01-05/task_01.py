file_name = "files/text for task_01.txt"
f = open(file_name, "w")
print("Вводите текст (ввод пустой строки - выход):")
while True:
    line = input()
    if line == '':
        break
    f.write(line + "\n")

f.close()
print(f"Данные сохранены в файл {file_name}")

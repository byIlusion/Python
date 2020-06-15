text = input("Введите текст:\n")
text_list = text.split()
for i, word in enumerate(text_list, 1):
    print(f"{i}: {word[:10]}")

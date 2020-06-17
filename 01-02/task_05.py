rating = rating_current = []
while True:
    el = input("Добавьте значение рейтинга (1-9) и/или нажмите Enter: ")
    if el == '':
        break
    if el.isdigit() and 1 <= int(el) <= 9:
        rating_current = rating.copy()
        pos = 0
        for i, v in enumerate(rating):
            if int(el) > v:
                pos = i
                break
            else:
                pos = i + 1

        rating_current.insert(pos, el)  # Список для отображения куда добавлен новый элемент
        rating.insert(pos, int(el))     # Список рейтингов
        print(f"Текущее состояние рейтинга:\n{rating_current}")
    else:
        print("Не верный ввод, попробуйте еще!")
print(f"Рейтинг в итоге:\n{rating}")

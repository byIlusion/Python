rating = rating_current = []
while True:
    el = input("Добавьте значение рейтинга (1-9) и/или нажмите Enter: ")
    if el == '':
        break
    if el.isdigit() and 1 <= int(el) <= 9:
        rating_current = rating.copy()
        if int(el) in rating:
            print(rating.index(int(el), -1))
            # print(rating.index(int(el)))
        # print(int(el) in rating)
        # max_el = max(rating)
        # min_el = min(rating)

        # print(f"max: {max(rating)} min: {min(rating)}")
        rating_current.append(el)
        rating.append(int(el))
        print(f"Текущее состояние рейтинга:\n{rating_current}")
    else:
        print("Не верный ввод, попробуйте еще!")
print(f"Рейтинг в итоге:\n{rating}")

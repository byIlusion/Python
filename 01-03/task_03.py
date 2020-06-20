def sumTwoFromThree(s1, s2, s3):
    """Функция принимает 3 обязательных параеметра и возвращает сумму 2-х максимальных значений"""
    elements = [s1, s2, s3]
    return elements.pop(elements.index(max(elements))) + elements.pop(elements.index(max(elements)))


while True:
    digits = input(f"Введите 3 целых числа в строку через пробел: ").strip().split()
    try:
        for i, d in enumerate(digits):
            digits[i] = int(d)
        if len(digits) != 3:
            raise Exception
        break
    except:
        print("Не верный ввод! Попробуйте еще!")

summ = sumTwoFromThree(digits[0], digits[1], digits[2])
print(f"Сумма 2-х максимальных значений из списка {digits} равна: {summ}")

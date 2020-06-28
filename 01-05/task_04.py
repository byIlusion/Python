def roman(num):
    """Функция, которая принимает целое положительное число и преобразует в римский стиль
    Сам придумал, нигде не тырил.

    num - целое положительное число
    Возвращает число в римском стиле

    """
    roman_numerals = {
        0: "",
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        5000: "Ṽ",
        10000: "Ẍ",
        50000: "Ĺ",
        100000: "Ĉ",
        500000: "Ď",
        1000000: "Ḿ"
    }
    r_num = ""
    num = str(abs(int(num)))
    for i, n in enumerate(num):
        n = int(n)
        if 5 <= n < 9:
            r_num += roman_numerals[10 ** (len(num) - i - 1) * 5]
        if 0 < n % 5 < 4:
            r_num += (roman_numerals[10 ** (len(num) - i - 1)] * (n % 5))
        elif n == 4:
            r_num += roman_numerals[10 ** (len(num) - i - 1)] + roman_numerals[10 ** (len(num) - i - 1) * 5]
        elif n == 9:
            r_num += roman_numerals[10 ** (len(num) - i - 1)] + roman_numerals[10 ** (len(num) - i)]
    return r_num


numeral_translate_ru = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}

try:
    with open("files/text_4.txt") as f:
        for row in f:
            print(f"Входящая строка: {row.strip()}\nПреобразованная: {numeral_translate_ru[row.split(' - ')[0].lower()].title()} - {roman(row.split(' - ')[1])}", end="\n\n")
except IOError:
    print("Error!")

print("Задание со звездочкой (преобразование арабских чисел в римские):")
for num in range(1, 50, 3):
    print(f"{num}: {roman(num)}")

def my_title_cap(word):
    """Функция использует стандартную функцию преобразования слова с заглавной буквы"""
    return word.capitalize()

def my_title_ord(text):
    """Функция принимает текст, и уменьшает код первой буквы каждого слова до заглавной
    Работает только на латинских словах

    """
    return " ".join(list(map(
        lambda word: chr(ord(word[:1]) - 32) + word[1:] if ord(word[:1]) > 32 else word,
        text.split()
    )))

def my_title(text):
    """Функция принимает любой текст
    Возвращает текст, в котором каждое слово начинается с заглавной буквы
    Пример: "text Text tEXT" => "Text Text Text"

    """
    return " ".join(list(map(lambda word: word[:1].upper() + word[1:].lower(), text.split())))

def filter_upper_text(word):
    """Функция убирает из входящей строки все заглавные буквы"""
    clear_word = ''
    for ch in word:
        clear_word += ch if ch.islower() else ''
    return clear_word

text = "Lorem ipsum DOLOR sit amet consectetur AdipisCING elit"
# text = input("Введите предложение латинскими буквами:\n").strip()
words = text.split()

filtered_words = []
for word in words:
    filtered_words.append(filter_upper_text(word))
    if len(filtered_words[len(filtered_words) - 1]) == 0:
        filtered_words.pop()
filtered_text = " ".join(filtered_words)

print('* ' * 30)
print(f"Исходный текст:\n{text}")
print('- ' * 30)
print(f"Вар-1-1. Исходный текст и стандартная функция title():\n{text.title()}", end='\n\n')
print(f"Вар-1-2. Исходный текст в нижнем регистре и функция my_title_capitalize():\n{' '.join(list(map(lambda word: my_title_cap(word), text.lower().split())))}", end='\n\n')
print(f"Вар-1-3. Исходный текст в нижнем регистре и функция my_title_ord():\n{my_title_ord(text.lower())}", end='\n\n')
print(f"Вар-1-4. Исходный текст в нижнем регистре и функция my_title():\n{my_title(text.lower())}", end='\n\n')

print('* ' * 30)
print(f"Фильтрованный текст:\n{filtered_text}")
print('- ' * 30)
print(f"Вар-2-1. Фильтрованный текст и стандартная функция title():\n{filtered_text.title()}", end='\n\n')
print(f"Вар-2-2. Фильтрованный текст и функция my_title_capitalize():\n{' '.join(list(map(lambda word: my_title_cap(word), filtered_words)))}", end='\n\n')
print(f"Вар-2-3. Фильтрованный текст и функция my_title_ord():\n{my_title_ord(filtered_text)}", end='\n\n')
print(f"Вар-2-3. Фильтрованный текст и функция my_title():\n{my_title(filtered_text)}", end='\n\n')

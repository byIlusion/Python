sec = int(input('Введите время в секундах: '))

day = 60 * 60 * 24
if sec > day:
    sec = sec - (sec // day) * day

min = sec // 60
sec -= min * 60
hours = min // 60
min -= hours * 60

print(f"Время: {hours:02d}:{min:02d}:{sec:02d}")

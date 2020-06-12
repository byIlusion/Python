revenue = float(input("Введите сумму выручки: "))
costs = float(input("Введите сумму издержек: "))
gain = revenue - costs

if gain > 0:
    print(f"Прибыль: {gain:.2f}")
    rent = gain / revenue * 100
    print(f"Рентабельность: {rent:.1f}%")
    workerCount = int(input("Сколько сотрудников в вашей фирме? "))
    print(f"Прибыль в расчете на каждого сотрудника: {gain / workerCount:.2f}")
elif gain == 0:
    print("Нет прибыли, но и нет издержек")
else:
    print(f"Убыток: {gain * -1:.2f}")

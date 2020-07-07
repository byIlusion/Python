class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


nums = []
while True:
    try:
        num = input("Введите число (Enter - выход): ")
        if num == '':
            break
        if num.isdigit():
            nums.append(int(num))
        else:
            nums.append(float(num))
    except:
        print(MyException("Ошибка! Вводить можно только числа!"))

print(nums)

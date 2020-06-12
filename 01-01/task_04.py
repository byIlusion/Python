num = int(input("Enter any number: "))
maxDigit = 0

if num > 0:
    while num > 0:
        digit = num % 10
        if digit > maxDigit:
            maxDigit = digit
        if maxDigit == 9:
            break
        num //= 10

    print(f"Maximum digit is {maxDigit}")
else:
    print("Number must be >0")

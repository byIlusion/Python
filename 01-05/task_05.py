from random import randint


f_name = "files/nums for task_05.txt"
try:
    with open(f_name, "w+") as f:
        print(" ".join([str(randint(-99, 100)) for _ in range(30)]), file=f)
        print(f"Последовательность чисел записана в файл {f_name}", end="\n\n")
        f.seek(0)
        nums_str = f.read()
    print(f"Последовательность:\n{nums_str}\nСумма всех чисел в последовательности: {sum([int(el) for el in nums_str.split()])}")
except IOError:
    print("IO error!")

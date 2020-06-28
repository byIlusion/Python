def get_gastarbeiters():
    try:
        with open("files/text_3.txt") as f:
            gastarbeiters = f.readlines()
        return [{'name': ga.split()[0], 'salary': float(ga.split()[1])} for ga in gastarbeiters]
    except IOError:
        print("Error!")
        return None


gastarbeiters = get_gastarbeiters()
average_salary = 0
if gastarbeiters is not None:
    for ga in gastarbeiters:
        average_salary += ga['salary']
        if ga['salary'] < 20000:
            print(f"{ga['name']} ЗП меньше 20 тыс. ({ga['salary']:.02f})")
    average_salary /= len(gastarbeiters)
    print(f"Средняя ЗП среди работников: {average_salary:.02f}")
else:
    print("List of gastarbeiters is not found!")

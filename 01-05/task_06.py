def get_num(el):
    num = ""
    for ch in el:
        if ch.isdigit():
            num += ch
    return int(num) if num.isdigit() else 0


lessons = {}
try:
    with open("files/text_6.txt") as f:
        for row in f:
            row = row.split()
            lessons[row[0][:len(row[0]) - 1]] = sum([get_num(row[i]) for i in range(1, len(row))])
except IOError:
    print("IO error!")

print(lessons)

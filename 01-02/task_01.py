lst = [None, 1, 3.14, True, False, "text", [1, 2], ("a", "b"), {True, False}, {"a": 0, "b": 100}]
for i, v in enumerate(lst):
    print(f"{i}. Элемент: {v} - Тип: {type(v)}")

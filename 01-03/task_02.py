def printUserData(name, surname, year, city, email, phone=''):
  print(f"{surname} {name}, {year} г.р., проживающий(ая) в г. {city}. Эл. почта: {email}{' Номер телефона: ' + phone if phone else ''}")

schema = {'name': 1, 'surname': 1, 'year': 1, 'city': 1, 'email': 1, 'phone': 0}
translate = {'name': 'Имя', 'surname': 'Фамилия', 'year': 'Год рождения', 'city': 'Город проживания', 'email': 'Email', 'phone': 'Номер телефона'}
userData = {}
print("Введите данные")
for key, required in schema.items():
  while True:
    userData[key] = input(f"{translate[key]}{'(обязательное поле)' if schema[key] else ''}: ")
    if not schema[key] or userData[key] != '':
      break

'''Условие только для демонстрации что необязательные аргументы можно не передавать'''
if userData['phone']:
  printUserData(surname=userData['surname'], name=userData['name'], city=userData['city'], year=userData['year'], email=userData['email'], phone=userData['phone'])
else:
  printUserData(surname=userData['surname'], name=userData['name'], city=userData['city'], year=userData['year'], email=userData['email'])

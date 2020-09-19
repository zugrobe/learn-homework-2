# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
names_list = []
for i in students:
    names_list.append((i['first_name']))
freq = {} 
for item in names_list: 
    if item in freq: 
        freq[item] += 1
    else: 
        freq[item] = 1
for new_str in freq.items():
    print(new_str[0],": ", new_str[1])
print(" ")

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names_list = []
for i in students:
    names_list.append((i['first_name']))
freq = {} 
for item in names_list: 
    if item in freq: 
        freq[item] += 1
    else: 
        freq[item] = 1
for new_str in freq.items():
    u = max(freq, key=freq.get)
print("Самое частое имя среди учеников:", u)
# Пример вывода:
# Самое частое имя среди учеников: Маша
print(" ")

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for names in school_students:
    names_list = []
    for i in names:
        names_list.append((i['first_name']))
    freq = {}
    count = 0
    for item in names_list:
        if item in freq:
            freq[item] += 1
            count += 1 
        else: 
            freq[item] = 1
    u = max(freq, key=freq.get)
    print("Самое частое имя в классе", count, ":", u)
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print(" ")

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
group = []
for std_class in school:
  group = std_class['students']
  std_gender = []
  boys = 0
  girls = 0
  for name in group:
    std_gender = name['first_name']
    if is_male[std_gender] == True:
      boys += 1
    else:
      girls += 1
  print(f'В классе {std_class["class"]}: девочек {girls} и мальчиков {boys}')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
print(" ")

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
std_pool = []
boys = 0
girls = 0
m_group = None
f_group = None
for group in school:
  std_pool = group['students']
  students = []
  m = 0
  f = 0
  for name in std_pool:
    students = name['first_name']
    if is_male[students] == True:
      m += 1
    else:
      f += 1
  if m > boys:      
    boys = m
    m_group = group["class"]
  if f > girls:
    girls = f
    f_group = group["class"]
print(f'Больше всего мальчиков в классе {m_group}')
print(f'Больше всего девочек в классе {f_group}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
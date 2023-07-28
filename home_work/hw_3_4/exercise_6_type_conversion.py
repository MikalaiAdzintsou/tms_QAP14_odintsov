
# Перевести строку в массив
str_RS = "Robin Singh"
str_RS = str_RS.split()
arr_RS = list(str_RS)
print(arr_RS)  # Перевести строку в массив

str_love_arr = "I love arrays they are my favorite"
str_love_arr = str_love_arr.split()
str_love_arr = list(str_love_arr)
print(str_love_arr)  # Перевести строку в массив

# Добро пожаловать в Minsk Belarus

arr_name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
print('Привет,', ' '.join(arr_name), '! Добро пожаловать в', city, country)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку

print(' '.join(str_love_arr))

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6

arr_ten_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
arr_ten_elements[2] = -3
del arr_ten_elements[6]
print(arr_ten_elements)

# два словаря
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у одного словаря есть ключ "а",
# а у другого нету, то поставить значение None на соответствующую позицию
# (1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}

for key in a:
    for key2 in b:
        ab[key] = [a.get(key), b.get(key)]
for key3 in b:
    for key4 in a:
        ab[key3] = [a.get(key3), b.get(key3)]

print(ab)

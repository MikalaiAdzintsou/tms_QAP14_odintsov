# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов. Извлеките из строки первый символ,
# затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.

line = "Go0d morning!"
s_first = (line[0])
print(s_first)
s_last = (line[-1])
print(s_last)
s_third = (line[2])
print(s_third)
s_minus_third = (line[-3])
print(s_minus_third)
len_line = len(line)
print(len_line)

# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:

slice_8 = (line[:8])    # первые восемь символов
print(slice_8)

row_center = len_line // 2    # четыре символа из центра строки
row_center_end = row_center + 4
sl_four_center = (line[row_center:row_center_end])
print(sl_four_center)

slice_index_three = (line[3::3])    # символы с индексами кратными трем
print(slice_index_three)

revers_line = (line[::-1])     # переверните строку
print(revers_line)

# 3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

line = "my name is name"
my_name = "Mikalai"
spl_line = line.split()
spl_line[-1] = my_name
print(' '.join(spl_line))

#4 Есть строка: test_string = "Hello world!", необходимо

test_string = "Hello world!"    # напечатать на каком месте находится буква w
w_place = test_string.find("w")
print(w_place+1)

l_count = test_string.count('l')    # кол-во букв l
print(l_count)

print(test_string.startswith("Hello"))    # Проверить начинается ли строка с подстроки: “Hello”
print(test_string.endswith("qwe"))    # Проверить заканчивается ли строка подстрокой: “qwe”





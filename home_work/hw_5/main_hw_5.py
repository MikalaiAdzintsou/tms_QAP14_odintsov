from home_work.hw_5.hw_5_pac import el_line, len_line, slice_eight, slice_index_three, row_center, revers_line, \
    add_my_name, l_count, w_place, line_start, line_end

basic_string = 'Go0d morning!How are you?'
line = "my name is name"
my_name = "Mikalai"
test_string = "Hello world!"
# 1
print('первый символ', el_line(basic_string, 0), sep=' = ')
print('последний символ', el_line(basic_string, -1), sep=' = ')
print('третий символ с начала', el_line(basic_string, 2), sep=' = ')
print('третий символ с конца', el_line(basic_string, -3), sep=' = ')
print()
# 2 количество символов в строке
print('количество символов в строке', len_line(basic_string), sep=' = ')
print()
# 3 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:
print('первые восемь символов это', slice_eight(basic_string), sep=' - ')
print('четыре символа из центра строки это', row_center(basic_string), sep=' - ')
print('символы с индексами кратными трем', slice_index_three(basic_string), sep=' : ')
print()
# 4 переверните строку
print('перевернутая строка', revers_line(basic_string), sep=' : ')
print()
# 5 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
print(add_my_name(line, my_name), '(тут добавили имя в строку)', sep=' ')
print()
# 6 Есть строка: test_string = "Hello world!",
# необходимо напечатать на каком месте находится буква w и кол-во l в строке
print('буква "W" находится на позиции №:', w_place(test_string))
print('количество букв "l" в строке =', l_count(test_string))
print()
# 7  Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”
print(line_start(test_string))
print(line_end(test_string))

# reworked the exercise_2_lines into functions and added a package
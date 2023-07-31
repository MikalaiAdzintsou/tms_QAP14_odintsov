# Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его.
# Вывести полученное число

number_int = 5
if number_int > 0:
    number_int += 1
    print(number_int)
else:
    number_int = number_int
    print(number_int)

# Даны три целых числа. Найти количество положительных чисел в исходном наборе.

a, b, c = 1, 4, 5
if a > 0:
    a = 1
else:
    a = 0
if b > 0:
    b = 1
else:
    b = 0
if c > 0:
    c = 1
else:
    c = 0
positive_numbers = a + b + c
print(positive_numbers)

# Дан номер года (положительное целое число).
# Определить количество дней в этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366 дней.
# Високосным считается год, делящийся на 4, за исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000 являются).

year = 2024
if year // 100 == year / 100 and year / 400 != year // 400:
    print(365)
elif year // 4 == year / 4:
    print(366)
else:
    print(365)

# Дано целое число в диапазоне 1–7. Вывести строку — название дня недели, соответствующее данному числу
# (1 — «понедельник», 2 — «втор- ник» и т. д.).

numb_of_weak = 5
if numb_of_weak == 1:
    print('Monday')
elif numb_of_weak == 2:
    print('Tuesday')
elif numb_of_weak == 3:
    print('Wednesday')
elif numb_of_weak == 4:
    print('Thursday')
elif numb_of_weak == 5:
    print('Friday')
elif numb_of_weak == 6:
    print('Saturday')
elif numb_of_weak == 7:
    print('Sunday')
else:
    print('Enter a number from 1 to 7')

# Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
# Дан номер единицы массы (целое число в диапазоне 1–5) и масса тела в этих единицах
# (вещественное число). Найти массу тела в килограммах.

weight_index = 3
body_weight = 45900
if weight_index == 1 and body_weight > 0:
    print(body_weight)
elif weight_index == 2 and body_weight > 0:
    print(body_weight / 10000)
elif weight_index == 3 and body_weight > 0:
    print(body_weight / 1000)
elif weight_index == 4 and body_weight > 0:
    print(body_weight * 1000)
elif weight_index == 5 and body_weight > 0:
    print(body_weight * 100)
else:
    print('Enter a number from 1 to 5')



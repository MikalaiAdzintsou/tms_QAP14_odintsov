from random import randint

# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно

a = randint(-100, 100)
b = randint(-100, 100)
sum_i = 0

if a > b:
    a, b = b, a
print('Дано число А', a)
print('Дано число B', b)

for i in range(a, b + 1):
    # print(i)
    sum_i = sum_i + i
print('Сумма всех целых чисел:', sum_i)

# Найти сумму всех натуральных чисел  от A до B

sum_i_natural = 0
for i_natural in range(a, b + 1):
    # print(i_natural)
    if i_natural > 0:
        sum_i_natural = sum_i_natural + i_natural
print('Сумма всех натуральных чисел:', sum_i_natural)

# Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
pol = 1
otr = 0
num_otr = 0
for iter_c in range(0, 10):
    if iter_c < 10:
        c = randint(-100, 100)
        # print(c) - можно вывести что бы увидеть значения для операций
        if c > 0:
            pol = c * pol
        if c < 0:
            otr = c + otr
            num_otr = num_otr + 1
print('произведение положительных :', pol)
print('сумма отрицательных :', otr)
print('количество отрицательных :', num_otr)

# Дан словарь пловцов с их результатами. Напечатать лучший результат заплыва среди 6 участников
swimmers = {'Бекиш Александр': 21.07,
            'Будник Алексей': 20.34,
            'Гребень Анастасия': 22.12,
            'Давидович Татьяна': 30,
            'Дешук Дмитрий': 24.01,
            'Казак Анна': 28.17
            }
swm = []
for res in swimmers.values():
    swm.append(res)
print("The best result:", min(swm))

# Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного:
# [1, 5, 2, 9, 2, 9, 1] => 5.
# Напишите программу, которая будет выводить уникальное число
have_arr = [1, 5, 2, 9, 2, 9, 1]
for number_in_arr in have_arr:
    if number_in_arr in have_arr:
        count_arr = have_arr.count(number_in_arr)
        if count_arr == 1:
            print('number', number_in_arr, 'is uniq')



















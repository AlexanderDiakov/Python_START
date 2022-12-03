"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""

import random

num = int(input('Введите число '))

new_list = [random.randint(1, num) for i in range(num)]
sum_odds = 0
for i in range(1, num, 2):
    sum_odds += new_list[i]
print(new_list)
print(sum_odds)

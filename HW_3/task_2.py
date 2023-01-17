"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]

[2, 3, 5, 6]
[12, 15]
"""

import random

num = int(input('Введите число '))

new_list = [random.randint(0, num) for i in range(num)]
print(new_list)
print([new_list[i] * new_list[-1 - i] for i in range((len(new_list) + 1) // 2)])
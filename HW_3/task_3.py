"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""

first_list = list(map(float, input("Введите числа через пробел: ").split()))

new_list = [round(i % 1, 2) for i in first_list if i % 1 != 0]
print(max(new_list) - min(new_list))

"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""


new_list = [1, 2, 3, 5, 1, 5, 3, 10]

unique = [i for i in new_list if new_list.count(i) == 1]

repeatable_list = [i for i in new_list if (new_list.count(i)) > 1]
temp = []
for i in repeatable_list:
    if i not in temp:
        temp.append(i)
    repeatable_list = temp

without_rep = list(set(new_list))

print(new_list)
print(unique)
print(temp)
print(without_rep)

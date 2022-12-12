"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.

Ввод: значение типа <int>
Вывод: значение типа <int>

Примеры:
45
101101

3
11

2
10
"""

num = int(input("Введите число "))

bin_num = ''
while num > 0:
    bin_num += str(num % 2)
    num //= 2
print(bin_num)
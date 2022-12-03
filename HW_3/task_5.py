"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

num = int(input("Введите число N: "))

fib_list = [0] * (2 * num + 1)
fib_list[num + 1], fib_list[num - 1] = 1, 1
coef = -1
for i in range(num + 2, 2 * num + 1):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    fib_list[-i - 1] = fib_list[i] * coef
    coef *= -1
print(fib_list)

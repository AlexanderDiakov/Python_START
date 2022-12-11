"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""


def del_worlds(text, worlds):
    return ' '.join(filter(lambda x: not set(x) >= set(worlds), text.split()))


print(del_worlds('автобус, генерал швабра итог арбуз вагон', 'абв'))

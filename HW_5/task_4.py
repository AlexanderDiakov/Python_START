"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""

data = input("Введите строки символов: ")


def rle_coding(data):
    code = ""
    symbol = ""
    for s in data:
        if symbol:
            if s in symbol and len(symbol) < 9:
                symbol += s
            else:
                code += str(len(symbol)) + symbol[0]
                symbol = s
        else:
            symbol = s
    code += str(len(symbol)) + symbol[0]
    return code


def decoding(data):
    code = ""
    for i in range(0, len(data), 2):
        code += int(data[i]) * data[i + 1]
    return code


print(rle_coding(data))
print(decoding(rle_coding(data)))

"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

from random import randrange


def player_vs_player():
    n = randrange(100, 500)
    k = randrange(10, 30)
    name_0 = "Игрок 1"
    name_1 = "Игрок 2"
    order = bool(randrange(2))
    game = True

    while game:
        candy_max = k if k < n else n
        print(f"Ход делает {name_1 if order else name_0}")
        print(f"На столе {n} конфет")
        print(f"Можно взять от 1 до {candy_max}")

        while True:
            m = int(input("Введите количество конфет: "))
            if 1 <= m <= candy_max:
                break
            else:
                print("Не верное количество")
                print(f"Можно взять от 1 до {candy_max}")

        n -= m
        if n:
            order = not order
        else:
            game = False
        print()
    print(f"Выиграл {name_1 if order else name_0}")


def player_bot():
    n = randrange(100, 500)
    k = randrange(10, 30)
    name_0 = "Игрок"
    name_1 = "БОТ"
    order = bool(randrange(2))
    game = True

    while game:
        candy_max = k if k < n else n
        print(f"Ход делает {name_1 if order else name_0}")
        print(f"На столе {n} конфет")
        print(f"Можно взять от 1 до {candy_max}")

        if order:
            m = randrange(1, candy_max + 1)
            print(f"Бот взял {m} конфет")
        else:
            while True:
                m = int(input("Введите количество конфет "))
                if 1 <= m <= candy_max:
                    break
                else:
                    print("Не верное количество")
                    print(f"Можно взять от 1 до {candy_max}")

        n -= m
        if n:
            order = not order
        else:
            game = False
        print()
    print(f"Выиграл {name_1 if order else name_0}")


if __name__ == '__main__':
    player_vs_player()
    # player_bot()

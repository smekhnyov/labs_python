import random


def task1():
    try:
        x = int(input("Левая граница: "))
        y = int(input("Правая граница: "))
        if x > y:
            x, y = y, x
        print(f"Угадай число от {x} до {y}")
        number = random.randint(x, y)
        take = 1
        guess = int(input())
        while guess != number:
            if number > guess:
                print("Не угадал, загаданное число больше")
            elif number < guess:
                print("Не угадал, загаданное число меньше")
            take += 1
            guess = int(input())
        print("Хорош, ты угадал, загаданное число было", number, "\nЧисло попыток:", take)
    except ValueError:
        print("Invalid value")
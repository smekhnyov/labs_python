import random
import time
import threading

result6 = 1


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



def task2(left, right):
    if right == left:
        return right
    else:
        return right * task2(left, right - 1)


def task3(mas):
    summ = 0
    number = 0
    for i in mas:
        summ += i
        number += 1
    print("Среднее массива:", summ / number)


def task4(a: float) -> float:
    def to(b: float) -> float:
        return a + b
    return to


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        #print(f"Время выполнения -> {end_time - start_time}")
        return result, end_time - start_time
    return wrapper


@execution_time_decorator
def check_time(n):
    time.sleep(1)
    return n * n


@execution_time_decorator
def task2_5(left, right):
    if right == left:
        return right
    else:
        #time.sleep(1)
        return right * task2(left, right - 1)


def task6_start(left, right):
    global result6
    result6 *= task2(left, right)


def task6():
    try:
        num = int(input("Вычислить факториал от числа: "))
        thread_count = int(input("Количество потоков: "))
        if thread_count < 0:
            raise ValueError
        if thread_count > num:
            raise ValueError
        sizeOfParts = num//thread_count
        threads = []
        for i in range(0, thread_count):
            t1 = threading.Thread(target=task6_start, args=[i*sizeOfParts+1, (i+1)*sizeOfParts])
            t1.start()
            threads.append(t1)
        if num % thread_count != 0:
            t1 = threading.Thread(target=task6_start, args=[(i+1) * sizeOfParts + 1, num])
            t1.start()
            threads.append(t1)
        for i in threads:
            i.join()
        print(result6)

    except ValueError:
        print("Invalid value")


restart = True
while restart:
    try:

        menu = int(input("Выберите режим работы: "))
        if menu == 1:
            task1()
        elif menu == 2:
            try:
                num = int(input("Вычислить факториал от числа: "))
                if num < 0:
                    raise ValueError
                else:
                    print(task2(1, num))
            except ValueError:
                print("Invalid value")

        elif menu == 3:
            try:
                mas = []
                count = int(input("Введите количество чисел в массиве: "))
                if count < 0:
                    raise ValueError
                else:
                    print("Введите массив целых чисел: ")
                    for i in range(count):
                        mas.append(int(input()))
                    task3(mas)
            except ValueError:
                print("Invalid value")
        elif menu == 4:
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                print(f'add({a})({b}) = {task4(a)(b)}')
            except ValueError:
                print("Ошибка! Введено неверное значение.")
        elif menu == 5:
            result = task2_5(1,500)
            print(f"Результат: {result}")
        elif menu == 6:
            task6()
        elif menu == 7:
            restart = False
        else:
            raise ValueError
    except ValueError:
        print("Invalid value")

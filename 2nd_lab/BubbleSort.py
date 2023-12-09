import random
from ProfileDecorator import ProfileDecorator
import sys

sys.setrecursionlimit(5000)

@ProfileDecorator
def bubble_sort(array):
    size = len(array)

    if size <= 1:
        return array

    for index in range(size - 1):
        if array[index] > array[index + 1]:
            array[index], array[index + 1] = array[index + 1], array[index]

    return bubble_sort(array[:-1]) + [array[-1]]


def bubble_sort_call() -> None:
    array = enter_array()
    print("Изначальный массив:")
    print(*array, sep=", ")

    sorted_array = bubble_sort(array)

    print("Отсортированный массив:")
    print(*sorted_array, sep=", ")
    print("\n")
    calls, total_time = bubble_sort.get_stats()

    print(f"Количество вызовов: {calls}\nВремя выполнения: {total_time}\n")
    bubble_sort.clear_stats()


def enter_array():
    while True:
        try:
            array = []
            count = int(input("Введите размер массива: "))
            for number in range(count):
                array.append(random.randint(0, 1000))
            return array
        except ValueError:
            print("Некорректное значение")

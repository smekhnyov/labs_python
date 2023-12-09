from ProfileDecorator import ProfileDecorator
import sys


sys.setrecursionlimit(5000)


@ProfileDecorator
def factorial(left, right) -> int:
    if right == 0:
        return 1
    elif right == left:
        return right
    else:
        return right * factorial(left, right - 1)


@ProfileDecorator
def factorial_call() -> None:
    number = correct_number_input()
    result = factorial(1, number)
    calls, total_time = factorial.get_stats()

    print(f"Результат: {result}\n" + f"Количество вызовов: {calls}\n" + f"Время выполнения: {total_time}\n")
    factorial.clear_stats()


def correct_number_input(prompt="Введите натуральное число: ") -> int:
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= 0:
                return user_input
            else:
                print("Число должно быть натуральным")
        except ValueError:
            print("Некорректное значение")

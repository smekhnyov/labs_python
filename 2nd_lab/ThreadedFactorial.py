import Factorial
import threading

from ProfileDecorator import ProfileDecorator


@ProfileDecorator
def calculate_factorial(number, thread_number):
    def threaded_factorial(left, right):
        result.append(Factorial.factorial(left, right))

    result = []
    parts_size = number//thread_number
    threads = []

    for i in range(0, thread_number - 1):
        thread_child = threading.Thread(target=threaded_factorial, args=[i * parts_size + 1, (i + 1) * parts_size])
        thread_child.start()
        threads.append(thread_child)
    thread_main = threading.Thread(target=threaded_factorial, args=[(i + 1) * parts_size + 1, number])
    thread_main.start()
    threads.append(thread_main)

    for i in threads:
        i.join()
    global_result = 1
    for part in result:
        global_result *= part

    calls, total_time = Factorial.factorial.get_stats()

    return global_result, calls, total_time


def threaded_factorial_call() -> None:
    number = Factorial.correct_number_input()
    thread_number = correct_thread_number_input(number)

    result, calls, total_time = calculate_factorial(number, thread_number)
    calls_calc, total_time_calc = calculate_factorial.get_stats()

    print(f"Количество вызовов: {calls_calc}\n" + f"Время выполнения: {total_time_calc}\n")
    print(f"Результат: {result}\n" + f"Количество вызовов: {calls}\n" + f"Время выполнения: {total_time}\n")
    Factorial.factorial.clear_stats()


def correct_thread_number_input(number, prompt="Введите число потоков: ") -> int:
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 1 and user_input <= number:
                return user_input
            elif user_input <= 1:
                print("Количество потоков должно быть больше 1")
            elif user_input > number:
                print("Количество потоков не может быть больше числа, от которого вычисляется факториал")
        except ValueError:
            print("Некорректное значение")
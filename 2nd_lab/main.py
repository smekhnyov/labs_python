import BubbleSort
import Factorial
import ThreadedFactorial


restart = True
while restart:
    try:
        menu = int(input("Выберите, что хотите запустить: \n"
                         "1) Сортировка пузырьком случайного массива \n"
                         "2) Вычислить факториал в многопотоке \n" 
                         "3) Вычислить факториал в однопотоке \n"
                         "4) Выход \n"))
        if menu == 1:
            BubbleSort.bubble_sort_call()
        elif menu == 2:
            ThreadedFactorial.threaded_factorial_call()

        elif menu == 3:
            Factorial.factorial_call()
            calls, total_time = Factorial.factorial_call.get_stats()

            print(f"Количество вызовов: {calls}\n" + f"Время выполнения: {total_time}\n")
        elif menu == 4:
            restart = False
        else:
            raise ValueError
    except ValueError:
        print("Некорректное значение")

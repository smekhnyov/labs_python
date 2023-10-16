from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task2_5
from task6 import task6


def main():
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


main()
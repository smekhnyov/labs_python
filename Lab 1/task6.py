import threading
from task2 import task2

result6 = 1


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
        for i in range(0, thread_count - 1):
            t1 = threading.Thread(target=task6_start, args=[i*sizeOfParts+1, (i+1)*sizeOfParts])
            t1.start()
            threads.append(t1)
        t1 = threading.Thread(target=task6_start, args=[(i + 1) * sizeOfParts + 1, num])
        t1.start()
        threads.append(t1)
        for i in threads:
            i.join()
        print(result6)

    except ValueError:
        print("Invalid value")
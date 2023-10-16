def task2(left, right):
    if right == left:
        return right
    else:
        return right * task2(left, right - 1)
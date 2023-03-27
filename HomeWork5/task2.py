# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2    4
import time

a = int(input("Input number A:"))
b = int(input("Input number B:"))


def sum(n: int, m: int) -> int:
    if n == 0:
        return m
    elif m == 0:
        return n
    else:
        return sum(n - 1, m + 1)


start = time.time()
print(sum(a, b))
finish = time.time()
print(start - finish)

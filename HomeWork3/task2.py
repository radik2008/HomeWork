# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите число элементов  списка:"))
x = int(input("Введите число которое нужно наити:"))

import random

list = [random.randint(1, 100) for _ in range(n)]
print(list)

min_def = abs(list[0] - x)
min_num = list[0]

for i in list:
    if abs(i - x) < min_def:
        min_num = i
        min_def = abs(i - x)



print(F"разница между элементами {min_def}")
print(f"самый близкий по величине элемент {min_num}")

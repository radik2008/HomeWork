# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите чисело:"))
index = 0
nSqr = 0
while True:
    nSqr = 2 ** index
    if nSqr >= n:
        break
    print(f"2 в степени {index} - {nSqr}")
    index += 1

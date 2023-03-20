# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

num = int(input("Введите число монет:"))
index = 1
from random import randint
sizeCoinEagle = 0
sizeCoinTails = 0

while index <= num:
    sizeCoin = randint(0, 1)
    print(f"{index} - {sizeCoin}")
    if sizeCoin == 0:
        sizeCoinEagle += 1
    if sizeCoin == 1:
        sizeCoinTails += 1
    index += 1

print(f"Минимальное количество монет котррые нужно перевернуть {sizeCoinTails}")\
    if sizeCoinEagle > sizeCoinTails \
    else print(f"Минимальное количество монет котррые нужно перевернуть {sizeCoinEagle}")



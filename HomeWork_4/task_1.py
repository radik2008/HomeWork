# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random

num_1 = int(input("Input num first:"))
num_2 = int(input("Input num second:"))

list_1 = [random.randint(1, 9) for _ in range(num_1)]
list_2 = [random.randint(1, 9) for _ in range(num_2)]

print(list_1)
print(list_2)

print(set(list_1))
print(set(list_2))


new_list = set(list_1).intersection(list_2)

print(new_list)
print()

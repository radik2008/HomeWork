# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)
import random
print("Введите через запятую, длину списка, минимальное значение, максимальное значение, диапазон мин, диапазон макс")
my_values = tuple(map(int, (input("Input values: ").split(','))))
print(my_values)
my_list_1 = [random.randint(my_values[1], my_values[2]) for _ in range(my_values[0])]
print(my_list_1)
my_list_2=[]
for i in range(my_values[0]):
    if my_values[3] < my_list_1[i] < my_values[4]:
        my_list_2.append(i)
print(my_list_2)

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


a = int(input("Input number A:"))
b = int(input("Input number B:"))

def power(n: int, m: int) -> int:
    if m == 0:
        return 1
    res = n * power(n, m - 1)
    return res

print(power(a, b))

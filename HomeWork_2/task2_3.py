"""
Задача №3:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
"""

n = int(input("--> "))
my_list = []
for i in range(n):
    res = 2 ** i
    if res < n:
        my_list.append(res)
print(my_list)
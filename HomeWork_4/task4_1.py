"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""

import os
os.system('cls' if os.name == 'nt' else 'clear') #функция очистки терминала

import random
first_count = int(input("Введите размер первого набора чисел: "))
first_collection = []
sec_count = int(input("Введите размер второго набора чисел: "))
sec_collection = []
#print("Заполним первый набор: ")
num = 0
while num < first_count:
    #first_collection.append(input("--> ")) # Заполнение вручную
    first_collection.append(random.randint(1, 10)) # Заполнение рандомно
    num += 1
#print("Заполним второй набор: ")
num = 0
while num < sec_count:
    #sec_collection.append(input("--> ")) # Заполнение вручную
    sec_collection.append(random.randint(1, 10)) # Заполнение рандомно
    num += 1
print(f'Первый набор: {first_collection}')
print(f'Второй набор: {sec_collection}')
first_set = set(first_collection)
sec_set = set(sec_collection)
same_numbers = list(first_set.intersection(sec_set))
same_numbers.sort()
print(f'Совпадающие числа в двух наборах: {same_numbers}')
"""Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона
в виде чисел min_number, max_number.
Пример:
На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10
На выходе:
1
2
3
6
7
9
10
11
13
14
16
19
💡 Поделиться мнением
"""

from random import randint

a = int((input("Set the length of the list: "))) # задаём длину списка
list_1 = [randint(-10, 10) for i in range(a)]
min_number = int(input("Input min value: "))
max_number = int(input("Input max value: "))
print(list_1)
values_interval = {i for i in range(min_number, max_number + 1)}
for i in range(len(list_1)):
    if list_1[i] in values_interval:
        print(i, end=" ")

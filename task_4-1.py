"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо"""

var2 = "1 3 5 7 9"
var3 = "2 3 4 5"

var2 = var2.split()
var3 = var3.split()
new_list = list(map(lambda x: int(x), (sorted(set(var2) & set(var3)))))
print(*new_list)

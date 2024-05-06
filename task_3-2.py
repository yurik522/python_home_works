"""Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

Пример:

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5"""

list_1 = [i for i in range(-2000, 2001, 4)]
print(list_1)
k = int(input("Please, input any number: \n"))
i = 0
j = 0
diff = abs(list_1[i] - k)
for i in range(0, len(list_1)):
    if abs(list_1[i] - k) < diff:
        diff = abs(list_1[i] - k)
        j = i

print(list_1[j])

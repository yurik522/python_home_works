"""Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

number = int(input("Input number:\n"))
x = 0
i = 0
while x < number:
    x = 2**i
    i += 1
    if x > number:
        quit()
    print(x)

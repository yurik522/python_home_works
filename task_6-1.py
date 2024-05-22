from random import randint

a = int((input("Set the length of the list: ")))
list_1 = [randint(-10, 10) for i in range(a)]
min_number = int(input("Input min value: "))
max_number = int(input("Input max value: "))
print(list_1)
values_interval = {i for i in range(min_number, max_number + 1)}
for i in range(len(list_1)):
    if list_1[i] in set_value:
        print(i, end =" ")

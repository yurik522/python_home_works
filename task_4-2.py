from random import randint

arr = [randint(4, 20) for i in range(1000)]

max = 0
for i in range(0, len(arr) - 2):
    temp = arr[i] + arr[i + 1] + arr[i + 2]
    if temp > max:
        max = temp
print(arr, max, sep="\n")

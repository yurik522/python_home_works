from random import randint

arr = [randint(1, 50) for i in range(10)]

# max = 0
# for i in range(0, len(arr) - 2):
#     temp = arr[i] + arr[i + 1] + arr[i + 2]
#     if temp > max:
#         max = temp
# print(arr, max, sep="\n")

if len(arr) <= 3:
    print(arr, sum(arr))
    exit()
temp = arr[0] + arr[1] + arr[2]
max = arr[0] + arr[1] + arr[2]

for i in range(2, len(arr) - 1):
    temp = (
        temp - arr[i - 2] + arr[i + 1]
    )  # изначально позиционируемся на среднем элементе
    # от изначальной суммы трех элементов
    # отнимаем первый и добавляем следующий.
    if temp > max:
        max = temp

print(arr, max, sep="\n")

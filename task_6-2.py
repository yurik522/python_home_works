a1 = int(input("a = "))
d = int(input("d = "))
n = int(input("n = "))
for i in range(a1, a1 + (n - 1) * d + 1, d): # работает только с положительным шагом
    print(i)  
# progress_list = [a1 + (n - 1) * d for n in range(1, n + 1)]
print(*[a1 + (n - 1) * d for n in range(1, n + 1)], sep="\n")

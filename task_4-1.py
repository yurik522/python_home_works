var2 = "1 3 5 7 9"
var3 = "2 3 4 5"

var2 = var2.split()
var3 = var3.split()
new_list = list(map(lambda x: int(x), (sorted(set(var2) & set(var3)))))
print(*new_list)

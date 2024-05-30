def print_operation_table(operation, num_rows = 9, num_colummns = 9):
    if num_rows <= 1:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    
    for i in range(1, num_rows + 1):
        for j in range(1, num_colummns + 1):
            if j == num_colummns:
                print(operation(i, j))
                continue
            print(operation(i, j), end=" ")
        
print_operation_table(lambda x, y: x * y)

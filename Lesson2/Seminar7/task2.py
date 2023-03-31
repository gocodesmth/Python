# Напишите функцию def print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows = 6, num_columns = 6):
    if num_rows < 2 or num_columns < 2:
        print("Количество столбцов и ячеек таблицы должно быть больше 1")
    else:
        print(' '.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            print(i, end = ' ')
            for j in range(2, num_columns + 1):
                print(operation(i, j), end = ' ')
            print()
print_operation_table(lambda x, y: x +  y)
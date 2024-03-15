from decimal import Decimal, getcontext
import copy
from decimal import Decimal
# Установка точности для десятичных вычислений
getcontext().prec = 3

def normalize_matrix_row(matrix, row_index=0):
    # Цикл продолжается до тех пор, пока не будет достигнута последняя строка
    if row_index + 1 < len(matrix):
        print(matrix)

        # Нормализация строки путем деления на ведущий элемент
        pivot = matrix[row_index][row_index]
        for i in range(len(matrix[row_index])):
            matrix[row_index][i] = float(Decimal(matrix[row_index][i]) / Decimal(pivot))

        # Изменение строк матрицы с учетом нормализованной строки
        for i in range(row_index + 1, len(matrix)):
            # Вычисление коэффициента для комбинации строк
            factor = matrix[i][row_index]
            for j in range(len(matrix[i])):
                matrix[i][j] = float(Decimal(matrix[i][j]) - Decimal(matrix[row_index][j]) * Decimal(factor))
        return normalize_matrix_row(matrix, row_index + 1)

    # Обработка последней строки матрицы
    print(matrix)
    pivot = matrix[row_index][row_index]
    for i in range(len(matrix[row_index])):
        matrix[row_index][i] = float(Decimal(matrix[row_index][i]) / Decimal(pivot))
    print(matrix)

    # Определение решений системы уравнений
    solutions = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        sum = matrix[i][-1]
        for j in range(i + 1, len(matrix)):
            sum -= matrix[i][j] * solutions[j]
        solutions[i] = sum / matrix[i][i]

    print('Roots of the system:')
    for i, solution in enumerate(solutions, start=1):
        print(f'x_{i} = {solution}')

# Определение исходных матриц
matrix1 = [
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
]

matrix2 = [
    [2, 1, 4, 16],
    [3, 2, 1, 10],
    [1, 3, 3, 16]
]

matrix3 = [
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, 6]
]

# Выполнение преобразования и решение для каждой матрицы
solution1 = normalize_matrix_row(matrix1)
print('-------------------------------------------------------------------------------------------------------------------------------')
solution2 = normalize_matrix_row(matrix2)
print('-----------------------------------------------------------------------------------------------------------------------------------')
solution3 = normalize_matrix_row(matrix3)



import copy

# Реализация метода Гаусса для решения систем линейных уравнений
def gauss_elimination(matrix, current_row=0, step=0):
    # Цикл продолжается до обработки всех строк
    while step + 1 < len(matrix):
        print(matrix)
        # Создание копии текущей матрицы для сохранения предыдущих значений
        prev_matrix = copy.deepcopy(matrix)

        # Нормализация текущей строки делением на ведущий элемент
        pivot = matrix[current_row][current_row]
        for i in range(len(matrix[0])):
            matrix[current_row][i] = float(Decimal(matrix[current_row][i]) / Decimal(pivot))

        # Обнуление элементов в столбце ниже ведущего и пересчет остальных элементов строки
        for i in range(current_row + 1, len(matrix)):
            matrix[i][current_row] = 0  # Обнуляем элементы ниже ведущего
            for j in range(1, len(matrix[0])):
                # Пересчет элементов с использованием предыдущих значений
                matrix[i][j] = float(Decimal(prev_matrix[i][j]) - (Decimal(prev_matrix[i][step]) * Decimal(prev_matrix[step][j])) / Decimal(prev_matrix[step][step]))
        return gauss_elimination(matrix, current_row + 1, step + 1)

    # Последняя строка нормализуется отдельно
    print(matrix)
    pivot = matrix[current_row][current_row]
    for i in range(len(matrix[0])):
        matrix[current_row][i] = float(Decimal(matrix[current_row][i]) / Decimal(pivot))
    print(matrix)

    # Решение системы уравнений (обратный ход)
    solutions = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        sum = matrix[i][-1]  # Начинаем с последнего свободного члена
        for j in range(i + 1, len(matrix)):
            sum -= matrix[i][j] * solutions[j]  # Вычитаем известные решения
        solutions[i] = sum / matrix[i][i]  # Вычисляем текущее решение

    # Вывод решений
    print('Roots of the system:')
    for i, solution in enumerate(solutions, start=1):
        print(f'x_{i} = {solution}')

# Исходные матрицы для решения
matrix4 = [
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
]

matrix5 = [
    [2, 1, 4, 16],
    [3, 2, 1, 10],
    [1, 3, 3, 16]
]

matrix6 = [
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, 6]
]

# Выполнение метода Гаусса для каждой матрицы
solution4 = gauss_elimination(matrix4)
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
solution5 = gauss_elimination(matrix5)
print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
solution6 = gauss_elimination(matrix6)




def find_max_pivot(matrix, start_row):
    max_index = start_row
    max_value = matrix[start_row][start_row]
    for i in range(start_row + 1, len(matrix)):
        if abs(matrix[i][start_row]) > abs(max_value):
            max_index = i
            max_value = matrix[i][start_row]
    return max_index


def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]


def gauss_method_with_column_pivot(matrix):
    for i in range(len(matrix)):
        max_index = find_max_pivot(matrix, i)
        if max_index != i:
            swap_rows(matrix, i, max_index)

        pivot = Decimal(matrix[i][i])
        for j in range(i, len(matrix[i])):
            matrix[i][j] = float(Decimal(matrix[i][j]) / pivot)

        for k in range(i + 1, len(matrix)):
            factor = Decimal(matrix[k][i])
            for j in range(i, len(matrix[k])):
                matrix[k][j] = float(Decimal(matrix[k][j]) - factor * Decimal(matrix[i][j]))

    roots = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        sum = matrix[i][-1]
        for j in range(i + 1, len(matrix)):
            sum -= matrix[i][j] * roots[j]
        roots[i] = sum / matrix[i][i]

    print('Корни системы:')
    for i, root in enumerate(roots, start=1):
        print(f'x_{i} = {root}')


# Примеры матриц для решения
matrix7 = [
    [5, 0, 1, 11],
    [2, 6, -2, 8],
    [-3, 2, 10, 6]
]

matrix8 = [
    [2, 1, 4, 16],
    [3, 2, 1, 10],
    [1, 3, 3, 16]
]

matrix9 = [
    [-3, 2.099, 6, 3.901],
    [10, -7, 0, 7],
    [5, -1, 5, 6]
]

# Решение систем для каждой матрицы
solution7 = gauss_method_with_column_pivot(matrix7)
print(
    '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
solution8 = gauss_method_with_column_pivot(matrix8)
print(
    '----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
solution9 = gauss_method_with_column_pivot(matrix9)



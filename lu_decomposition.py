import numpy as np


def lu_decomposition(matrix):
    n = len(matrix)
    lower_matrix = np.zeros((n, n))
    upper_matrix = np.zeros((n, n))

    for k in range(n):
        for i in range(k, n):
            lower_matrix[i][k] = matrix[i][k] - np.dot(lower_matrix[i][:k], upper_matrix[:k, k])
        for j in range(k, n):
            upper_matrix[k][j] = (matrix[k][j] - np.dot(lower_matrix[k][:k], upper_matrix[:k, j])) / lower_matrix[k][k]

    return lower_matrix, upper_matrix


A = np.array([[2, 1, 4], [3, 2, 1], [1, 3, 3]])
b = np.array([16, 10, 16])

l, u = lu_decomposition(A)

print('Матрицы L и U')
print(l)
print(u)


y = np.linalg.solve(l, b)
x = np.linalg.solve(u, y)
print("\nРешения:")
print("y =", y)
print("x =", x)
import numpy as np

def jacobi_rotation(A, tol=1e-10, max_iterations=100):
    """
    :param A: Симметричная матрица (numpy array)
    :param tol: Допуск для проверки сходимости
    :param max_iterations: Максимальное количество итераций
    :return: Собственные значения и собственные векторы матрицы A
    """
    n = A.shape[0]
    V = np.eye(n)
    for i in range(max_iterations):
        # Находим наибольший внедиагональный элемент
        max_val = 0
        k = 0
        l = 0
        for j in range(n):
            for k_ in range(j + 1, n):
                if abs(A[j, k_]) > max_val:
                    max_val = abs(A[j, k_])
                    k = j
                    l = k_

        # Проверяем сходимость
        if max_val < tol:
            break

        # Считаем углы
        if A[k, k] == A[l, l]:
            theta = np.pi / 4
        else:
            theta = 0.5 * np.arctan(2 * A[k, l] / (A[k, k] - A[l, l]))

        # Считаем косинус и синус
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)

        # Обновляем матрицу A
        J = np.eye(n)
        J[k, k] = cos_theta
        J[l, l] = cos_theta
        J[k, l] = -sin_theta
        J[l, k] = sin_theta

        A = J.T @ A @ J
        V = V @ J

    eigenvalues = np.diag(A)
    eigenvectors = V
    return eigenvalues, eigenvectors

# Пример использования
A = np.array([[4, 1, 1],
              [1, 3, 1],
              [1, 1, 2]])

eigenvalues, eigenvectors = jacobi_rotation(A)
print("Собственные значения:")
print(eigenvalues)
print("Собственные векторы:")
print(eigenvectors)

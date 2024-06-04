import numpy as np
import matplotlib.pyplot as plt


def poisson_solver(n, f, tol=1e-5, max_iterations=10000):
    """
    :param n: Размер сетки
    :param f: Функция f(x, y)
    :param tol: Допуск для проверки сходимости
    :param max_iterations: Максимальное количество итераций
    :return: Решение u на сетке nxn
    """
    h = 1.0 / (n - 1)
    u = np.zeros((n, n))

    for iteration in range(max_iterations):
        u_new = np.copy(u)
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                u_new[i, j] = 0.25 * (u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1] - h ** 2 * f(i * h, j * h))

        if np.linalg.norm(u_new - u) < tol:
            break

        u = u_new

    return u


def f(x, y):
    """
    Заданная функция f(x, y).
    """
    return np.sin(np.pi * x) * np.sin(np.pi * y)


# Параметры сетки
n = 50

# Решение уравнения Пуассона
u = poisson_solver(n, f)

# Визуализация решения
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(8, 6))
cp = plt.contourf(X, Y, u, 20, cmap='viridis')
plt.colorbar(cp)
plt.title('Solution to Poisson Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

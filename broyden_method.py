import numpy as np

def broyden_method(f, x0, tol=1e-6, max_iter=100):
    """
    Реализация метода Бройдена для нахождения корня уравнения f(x)=0.

    :param f: Функция, корень которой мы ищем. Функция должна принимать вектор x в качестве аргумента и возвращать вектор того же размера.
    :param x0: Начальное приближение.
    :param tol: Допустимая погрешность.
    :param max_iter: Максимальное число итераций.
    :return: Приближенное значение корня уравнения.
    """
    n = len(x0)
    x = x0
    B = np.eye(n)  # Начальное приближение обратной матрицы Якоби

    for _ in range(max_iter):
        fx = f(x)
        if np.linalg.norm(fx) < tol:
            return x

        # Вычисление приращения x с использованием метода Ньютона
        s = np.linalg.solve(B, -fx)
        x_next = x + s

        # Вычисление приращения f(x) для обновления матрицы B
        delta_fx = f(x_next) - fx
        delta_x = x_next - x

        # Обновление матрицы B с использованием формулы Бройдена
        B += np.outer(delta_fx - np.dot(B, delta_x), delta_x) / np.dot(delta_x, delta_x)

        x = x_next

    return x

# Пример использования:
def f(x):
    return np.array([x[0]**2 - 4, x[1]**2 - 9])  # пример системы уравнений

# Начальное приближение
x0 = np.array([1.0, 2.0])

# Вызов метода Бройдена
root = broyden_method(f, x0)
print("Приближенный корень:", root)

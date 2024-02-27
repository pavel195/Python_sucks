def simplified_newton_method(f, x0, tol=1e-6, max_iter=1000):
    """
    Упрощенный метод Ньютона (метод касательной) для нахождения корня уравнения f(x) = 0.

    Параметры:
        f (function): Функция, уравнение f(x) = 0.
        x0 (float): Начальное предположение.
        tol (float): Допустимая погрешность (критерий останова), по умолчанию 1e-6.
        max_iter (int): Максимальное количество итераций, по умолчанию 1000.

    Возвращает:
        float: Приближенное значение корня.
        int: Количество выполненных итераций.
    """
    for i in range(max_iter):
        f_prime = (f(x0 + tol) - f(x0)) / tol
        x1 = x0 - f(x0) / f_prime
        if abs(x1 - x0) < tol:
            return x1, i + 1
        x0 = x1
    raise ValueError(f"Метод не сошёлся за {max_iter} итераций.")


# Пример использования:
import math


# Определение функции f(x)
def f(x):
    return x ** 2 - 2


# Начальное предположение
x0 = 1.0

# Применение упрощенного метода Ньютона
square, iterations = simplified_newton_method(f, x0)

print("Приближенный корень:", square)
print("Итераций выполнено:", iterations)

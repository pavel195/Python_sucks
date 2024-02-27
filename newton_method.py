def newton_method(f, df, x0, tol=1e-6, max_iter=1000):
    """
    Метод Ньютона для нахождения корня уравнения f(x) = 0.

    Параметры:
        f (function): Функция, уравнение f(x) = 0.
        df (function): Производная функции f(x).
        x0 (float): Начальное предположение.
        tol (float): Допустимая погрешность (критерий останова), по умолчанию 1e-6.
        max_iter (int): Максимальное к
        оличество итераций, по умолчанию 1000.

    Возвращает:
        float: Приближенное значение корня.
        int: Количество выполненных итераций.
    """
    x_prev = x0
    for i in range(max_iter):
        f_prev = f(x_prev)
        df_prev = df(x_prev)
        if df_prev == 0:
            raise ValueError("Производная равна нулю. Метод Ньютона не может быть применен.")
        x_next = x_prev - f_prev / df_prev
        if abs(x_next - x_prev) < tol:
            return x_next, i + 1
        x_prev = x_next
    raise ValueError(f"Метод не сошёлся за {max_iter} итераций.")


# Пример использования:
import math


# Определение функции f(x) и её производной df(x)
def f(x):
    return x ** 2 - 2


def df(x):
    return 2 * x


# Начальное предположение
x0 = 1.0

# Применение метода Ньютона
square, iterations = newton_method(f, df, x0)

print("Приближенный корень:", square)
print("Итераций выполнено:", iterations)

def bisection_method(f, a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs")

    iter_count = 0
    while iter_count < max_iter:
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    raise ValueError("Maximum number of iterations reached")

# Задаем функцию
def f(x):
    return x ** 3 - 2 * x - 5

# Начальные точки интервала
a = 1
b = 3

# Вызываем метод единственного деления
root = bisection_method(f, a, b)

print("Root:", root)

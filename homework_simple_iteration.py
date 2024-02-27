def simple_iteration_method(g, x0, tol=1e-6, max_iter=1000):
    """
    Метод простых итераций для нахождения корня уравнения x = g(x).

    Параметры:
        g (function): Итерационная функция.
        x0 (float): Начальное предположение.
        tol (float): Допустимая погрешность (критерий останова), по умолчанию 1e-6.
        max_iter (int): Максимальное количество итераций, по умолчанию 1000.

    Возвращает:
        float: Приближенное значение корня.
        int: Количество выполненных итераций.
    """
    x_prev = x0
    for i in range(max_iter):
        x_next = g(x_prev)
        if abs(x_next - x_prev) < tol:
            return x_next, i + 1  # i + 1, потому что range() начинается с 0
        x_prev = x_next
    raise ValueError(f"Метод не сошёлся за {max_iter} итераций.")


# Пример использования:
# Определение итерационной функции g(x)
def g(x):
    return (2 * x + 3) ** (1 / 3)


# Начальное предположение
x0 = 1.0

# Применение метода
root, iterarions = simple_iteration_method(g, x0)

print("Приближенный корень:", root)
print("Итераций выполнено:", iterarions)

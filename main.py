# метод дихотомии
def bisection_method(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        return None

    while (b - a) >= epsilon:
        c = (a + b) / 2

        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
# В этом коде f - это функция, для которой мы ищем корень,
# a и b - начальные значения интервала, в котором мы ищем корень,
# а epsilon - это требуемая точность результата.

# Определим функцию, для которой мы будем искать корень
def equation(x):
    return  (x-1)*(x-2)*(x-3)
result = bisection_method(equation, 0, 5, 0.0001)
print("Корень уравнения: ", result)
def f(x):
    return x**2  # Задаем функцию, для которой хотим вычислить интеграл

def rectangle_method(a, b, n):
    h = (b - a) / n  # Вычисляем ширину каждого прямоугольника
    integral = 0
    for i in range(n):
        integral += f(a + i * h) * h  # Суммируем площади прямоугольников
    return integral

a = 0  # Нижний предел интегрирования
b = 1  # Верхний предел интегрирования
n = 100  # Количество прямоугольников

result = rectangle_method(a, b, n)
print(result)  # Выводим результат

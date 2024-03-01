from sympy import symbols, Poly

def func(x):
    return x**5 + 2*x**4 - 5*x**3 + 8*x**2 - 7*x - 3

x = symbols('x')
polynomial = Poly(func(x), x)
coeff = polynomial.all_coeffs()

A = max(map(abs, coeff[:-1]))
B = max(map(abs, coeff[1:]))

print(f"A = {A}")
print(f"B = {B}")

r = 1 / (1 + (B / abs(coeff[-1])))
R = 1 + A / abs(coeff[0])

print(f"r = {r}")
print(f"R = {R}")

print(f"Интервалы корней уравнения: [{-R}, {-r}), ({r}, {R}]")

def lagrange(coeff):
    n = len(coeff) - 1
    for i, a in enumerate(coeff):
        if a < 0:
            break
    c = max(abs(j) for j in coeff if j < 0)
    return 1 + (c / coeff[0]) ** (1 / (n - i))

upper_bound = lagrange(coeff)

print(f"Верхняя граница положительных корней: {upper_bound}")

def count_sign_changes(coeff):
    return sum((1 for i in range(len(coeff) - 1) if coeff[i] * coeff[i+1] < 0))

def descartes_rule_of_signs(p):
    positive_root_bounds = count_sign_changes(p)
    p_neg = [a*(-1)**i for i, a in enumerate(p)]
    negative_root_bounds = count_sign_changes(p_neg)
    return positive_root_bounds, negative_root_bounds

positive_bounds, negative_bounds = descartes_rule_of_signs(coeff)

print(f"Максимальное количество положительных корней: {positive_bounds}")
print(f"Максимальное количество отрицательных корней: {negative_bounds}")

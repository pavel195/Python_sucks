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
# Теорема 5

from sympy import symbols, Poly, simplify

# Введите функцию
def func(x):
    return x**5 + 2*x**4 - 5*x**3 + 8*x**2 -7*x - 3

x = symbols('x')

polynomial = Poly(func(x), x)

# Извлечение коэффициентов многочлена
coeff = polynomial.all_coeffs()

# R - верхняя граница положительных корней уравнения P_n(x) = 0
def lagrange(coeff):
    a_n = coeff[0]
    n = len(coeff) - 1

    # Количество отрицательных коэффициентов
    i = sum(1 for a in coeff if a < 0)

    # Наибольший по модулю отрицательный коэффициент
    c = max(abs(j) for j in coeff if j < 0)

    return 1 + (c / a_n) ** (1 / (n - i))

upper_bound = lagrange(coeff)

print(f"R: {upper_bound}")

# R_1 — верхняя граница положительных корней уравнения P_1(x) = x^n*P_n(1/x) = 0
def p_1_for_R_1(coeff):
  n = len(coeff) - 1
  new_coeff = []

  for i in range(n + 1):
      term = coeff[i]
      new_coeff.append(term)

  new_coeff = new_coeff[::-1]

  if new_coeff[0] < 0:
      # Умножаем все элементы на -1
      new_coeff = [-x for x in new_coeff]

  return new_coeff

upper_bound_1 = lagrange(p_1_for_R_1(coeff))
print(f"R_1: {upper_bound_1}")

# R_2 — верхняя граница положительных корней уравнения P_2(x) = P_n(–x) = 0
def p_2_for_R_2(coeff):
    n = len(coeff) - 1
    new_coeff = coeff[::-1]  # Инвертируем порядок коэффициентов

    p_2 = Poly(sum(new_coeff[i] * ((-symbols('x'))**(n-i)) for i in range(n + 1)), x)

    return p_2.all_coeffs()[::-1]

upper_bound_2 = lagrange(p_2_for_R_2(coeff))
print(f"R2: {upper_bound_2}")

# R_3— верхняя граница положительных корней уравнения P_3(x) = x^n*P_n(-1/x)
def p_3_for_R_3(coeff):
  n = len(coeff) - 1
  new_coeff = []

  for i in range(n + 1):
      term = coeff[i]
      new_coeff.append(term)

  p_3 = sum(new_coeff[i] / ((-symbols('x'))**(n-i)) for i in range(n + 1))

  # Упрощаем выражение
  p_3_simplified = simplify(p_3)

  # Вытаскиваем коэффициенты при x
  new_coeff = [p_3_simplified.coeff(x, i) for i in range(-n, 1)]
  new_coeff = new_coeff[::-1]

  if new_coeff[0] < 0:
      # Умножаем все элементы на -1
      new_coeff = [-x for x in new_coeff]

  return new_coeff

upper_bound_3 = lagrange(p_3_for_R_3(coeff))
print(f"R_3: {upper_bound_3}")

print(f"Границы положительных корней: {1/upper_bound_1} <= +X*i <= {upper_bound}")
print(f"Границы отрицательных корней: {-upper_bound_2} <= -X*i <= {-1/upper_bound_3}")


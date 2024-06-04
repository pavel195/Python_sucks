import numpy as np
x = np.array([2,3,4,5], float)
func = np.array([7,5,8,7], float)

def divided_differences_coefs(points: list, function_values: list):
    x = points
    f_values = function_values

    n = len(x)
    results = np.zeros([n, n+1])

    for i in range(n):
        results[i, 0] = x[i]
        results[i, 1] = f_values[i]

    for i in range(2, n+1):
        for j in range(n+1-i):
            results[j, i] = (results[j+1, i-1] - results[j, i-1]) / (results[j+i-1, 0] - results[j, 0])

    return results[0][1:]

print(divided_differences_coefs(x, func))

def newton_polynom(points: list, function_values: list, eval_point: float):
    coefs = divided_differences_coefs(points, function_values)

    n = len(points) - 1

    result = coefs[n]

    for i in range(1, n + 1):
        result = coefs[n-i] + (eval_point - points[n-i]) * result

    return result

print(newton_polynom(x, func, 2.0))
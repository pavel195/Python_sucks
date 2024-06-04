import numpy as np

def power_iteration_method(matrix, tol=1e-6, max_iterations=1000, normalize_frequency=5):
    n = matrix.shape[0]
    v = np.random.rand(n)
    v /= np.linalg.norm(v)

    iteration = 0
    while iteration < max_iterations:

        w = np.dot(matrix, v)

        eigenvalue = np.dot(v, w)

        if iteration % normalize_frequency == 0:
            v /= np.linalg.norm(v)

        v_new = w / np.linalg.norm(w)

        if np.linalg.norm(v - v_new) < tol:
            break
        v = v_new
        iteration += 1

    return eigenvalue, v


A = np.array([[2, 1], [1, 3]])

dominant_eigenvalue, dominant_eigenvector = power_iteration_method(A)
print("Dominant eigenvalue:", dominant_eigenvalue)
print("Dominant eigenvector:", dominant_eigenvector)

def characteristic_polynomial(M):
    n = M.shape[0]
    coeffs = [1]
    for i in range(1, n + 1):

        minor_sum = np.sum(np.linalg.det(M[:i, :i]))
        coeffs.append((-1) ** i * minor_sum)
    return np.array(coeffs)


A = np.array([[2, 1], [1, 3]])

char_poly = characteristic_polynomial(A)
print("Characteristic polynomial:", char_poly)

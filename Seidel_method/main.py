import numpy as np


def input_matrix():
    n = int(input("Enter matrix size: "))
    print("Enter matrix:")
    a = np.array([input().strip().split() for _ in range(n)], float)
    return a

def input_vector():
    n = int(input("Enter vector size: "))
    print("Enter vector:")
    a = [0] * n
    for i in range(n):
        a[i] = float(input())
    return a


def func(matrix, B, E):
    n = matrix.shape[0]
    x = np.zeros(n, dtype=np.float64)
    count = 1
    while True:
        xx = x.copy()
        for i in range(n):
            x[i] = -(matrix[i, :] @ x - B[i] - matrix[i, i] * x[i]) / matrix[i, i]
        gap = abs(x - xx)
        print(f"Iteration {count}: {str(x)}")
        if max(gap) < E:
            break
        count += 1
    return x

if __name__ == '__main__':
    matrix = input_matrix()
    vector = input_vector()
    E = float(input("Enter E: "))
    print("\nResult:", func(matrix, vector, E))

# 1 0.47 -0.11 0.55
# 0.42 1 0.35 0.17
# -0.25 0.67 1 0.36
# 0.54 -0.32 -0.74 1

# 10 1 1
# 2 10 1
# 2 2 10
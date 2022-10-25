import numpy as np


def dd(X):
    D = np.diag(np.abs(X))
    S = np.sum(np.abs(X), axis=1) - D
    if np.all(D >= S):
        return True
    else:
        return False


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

def func(matrix, b, E,):
    n = matrix.shape[0]
    first = np.zeros(n, int).astype('float64')
    second = np.zeros(n, int).astype('float64')

    f1 = lambda x, y, z: (b[0] - y * matrix[0][1] - z * matrix[0][2]) / matrix[0][0]
    f2 = lambda x, y, z: (b[1] - matrix[1][0] * x - z * matrix[1][2]) / matrix[1][1]
    f3 = lambda x, y, z: (b[2] - matrix[2][0] * x - matrix[2][1] * y) / matrix[2][2]
    count = 0
    while True:
        second[0] = f1(first[0], first[1], first[2])
        second[1] = f2(first[0], first[1], first[2])
        second[2] = f3(first[0], first[1], first[2])
        print(f"Iteration {count}: {second}")
        count += 1

        maximum = np.max(abs(second-first)[np.nonzero(abs(second-first))])
        if maximum < E:
            break
        else:
            first, second = second, first

    return second

if __name__ == '__main__':
    matrix = input_matrix()
    vector = input_vector()
    E = float(input("Enter E: "))
    if dd(matrix):
        print("\nResult:", func(matrix, vector, E))
    else:
        print("matrix NOT diagonally dominant")

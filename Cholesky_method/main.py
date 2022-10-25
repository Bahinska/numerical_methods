import numpy as np
import math


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


def mat_print(A):
    col_maxes = [max([len(("{:g}").format(x)) for x in col]) for col in A.T]
    for x in A:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+"g}").format(y), end="  ")
        print("")
    print("")


def func(A, vector):
    n = A.shape[0]
    U = np.zeros((n, n), int).astype('float64')
    y, x = [0] * n, [0] * n
    for i in range(n):
        for j in range(n):
            try:
                if i == j:
                    U[i][i] = math.sqrt(A[i][i]-sum((U[k][i]**2) for k in range(i)))
                if j > i:
                    U[i][j] = (A[i][j] - sum((U[k][i]*U[k][j]) for k in range(i)))/U[i][i]
            except Exception as e:
                print(str(e))
                return
    Ut = U.transpose()
    print("U: ")
    mat_print(U)
    print("U transpose: ")
    mat_print(Ut)

    for i in range(n):
        y[i] = (vector[i] - sum((U[k][i] * y[k]) for k in range(i)))/U[i][i]
    print("Y: ", y, "\n")

    for i in range(n):
        x[n-i-1] = (y[n-i-1] - sum((U[n-i-1][k] * x[k]) for k in range(n-1, n-i-1, -1)))/U[i][i]
    print("X: ", x, "\n")


if __name__ == '__main__':
    vec = input_vector()
    matrix = input_matrix()
    func(matrix, vec)


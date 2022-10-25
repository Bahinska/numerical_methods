
def gauss(m):
    for row in range(len(m)):
        a = m[row][row]
        while a == 0:  # коли ведучий елемент 0 (дивимось чи є ненульові елементи в цій колонці)
            for i in range(row + 1, len(m)):
                if m[i][row] != 0:
                    # якщо такий елемент знайдено, міняємо рядки місцями
                    a = m[i][row]
                    m[[i, row]] = m[[row, i]]
                    break
                if i == len(m) - 1:
                    # якщо все 0
                    print("one solution doesn't exist")
                    return []

        # ділимо всі елементи рядка на перший
        for i in range(len(m[row])):
            m[row][i] = m[row][i] / a
        # множимо і додаємо рядок з іншими щоб отримати 0
        for r in range(row + 1, len(m)):
            a = m[r][row]
            if a != 0:
                for i in range(len(m[row])):
                    m[r][i] = m[row][i] * -1 * a + m[r][i]

    #  розв'язуємо лінійні рівняння
    results = [0] * len(m)
    for x in range(len(m) - 1, -1, -1):
        sum = 0
        for i in range(x + 1, len(m)):
            sum += m[x][i] * results[i]
        results[x] = m[x][-1] - sum

    return results


matrix = [
    [8, 7, 3, 18],
    [-7, -4, -4, -11],
    [-6, 5, -4, -15]
]
matrix2 = [
    [2, 2, -1, 1, 4],
    [4, 3, -1, 2, 6],
    [8, 5, -3, 4, 12],
    [3, 3, -2, 2, 6]
]

if __name__ == '__main__':
    print(gauss(matrix))
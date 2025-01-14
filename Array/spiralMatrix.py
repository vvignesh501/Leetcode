def spiralTraverse(array):
    # Write your code here.
    left = 0
    right = len(array[0])
    top = 0
    bottom = len(array)
    res = []

    while left < right and top < bottom:
        for i in range(left, right):
            res.append(array[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(array[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            res.append(array[bottom - 1][i])
        bottom -= 1

        for i in range(bottom - 1, top - 1, -1):
            res.append(array[i][left])
        left += 1
    return res


out = spiralTraverse([[1, 2, 3, 4],
                      [12, 13, 14, 5],
                      [11, 16, 15, 6],
                      [10, 9, 8, 7]])
print(out)

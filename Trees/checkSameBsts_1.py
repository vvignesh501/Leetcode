def sameBsts(arrayOne, arrayTwo):
    # Write your code here.

    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    if arrayOne[0] != arrayTwo[0]:
        return False

    getLeftBSTVal1 = getLeftBSTValues(arrayOne)
    getLeftBSTVal2 = getLeftBSTValues(arrayTwo)
    getRightBSTVal1 = getRightBSTValues(arrayOne)
    getRightBSTVal2 = getRightBSTValues(arrayTwo)

    return sameBsts(getLeftBSTVal1, getLeftBSTVal2) and sameBsts(getRightBSTVal1, getRightBSTVal2)


def getLeftBSTValues(arr):
    smaller = []
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            smaller.append(arr[i])
    return smaller


def getRightBSTValues(arr):
    bigger = []
    for i in range(1, len(arr)):
        if arr[i] >= arr[0]:
            bigger.append(arr[i])
    return bigger


out = sameBsts([10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81])
print(out)

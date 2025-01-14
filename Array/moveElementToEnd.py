def moveElementToEnd(array, toMove):
    # Write your code here.
    l = 0
    r = 1

    while l < r < len(array):
        if array[l] == array[r]:
            r += 1
        elif array[l] != array[r]:
            array[l], array[r] = array[r], array[l]
            l += 1
            r += 1
    return array


out = moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2)
print(out)

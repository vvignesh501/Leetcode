def sumOddLengthSubarrays(A):
    n = len(A)
    res = 0
    for l in range(1, n + 1, 2):
        print(l)
        for i in range(n - l + 1):
            print('Range', n - l + 1)
            print('Inner', i, l)
            res += sum(A[i:i + l])
    return res


print(sumOddLengthSubarrays([1,4,2,5,3]))
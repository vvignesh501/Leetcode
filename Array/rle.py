def rle(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

sol = Solution(n = 4)
print(sol)

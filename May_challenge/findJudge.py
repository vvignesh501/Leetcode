class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1:
            return N
        else:
            count = [0] * (N + 1)
            for pair in trust:
                count[pair[1]] += 1
                count[pair[0]] -= 1
            for i, val in enumerate(count):
                if val == N - 1:
                    return i
            return -1


g = Solution()
out = g.findJudge(2, [[1, 2]])
print(out)

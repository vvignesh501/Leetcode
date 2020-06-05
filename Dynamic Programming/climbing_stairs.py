import itertools

class Solution:
    def climbStairs(self, n: int):

        for i in range(0, n + 1):
            for subset in itertools.combinations(n, i):
                return subset



g = Solution()
out = g.climbStairs(2)
print(out)



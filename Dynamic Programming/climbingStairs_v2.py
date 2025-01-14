class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[-1], dp[-2] = 1, 1

        if n <= 1:
            return dp[-1]

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]


out = Solution().climbStairs(2)
print(out)
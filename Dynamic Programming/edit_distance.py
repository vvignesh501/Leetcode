class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        dp = [[float("inf")] * (len(str2) + 1) for c in range(len(str1) + 1)]

        for j in range(len(str2) + 1):
            dp[len(str1)][j] = len(str2) - j

        for k in range(len(str1) + 1):
            dp[k][len(str2)] = len(str1) - k

        for i in range(len(str1) - 1, -1, -1):
            for j in range(len(str2) - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


out = Solution().minDistance("horse", "ros")
print(out)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[0 for _ in range(len(word2) + 1)]for _ in range(len(word1) + 1)]

        r = len(word1)
        c = len(word2)

        for i in range(r + 1):
            dp[i][c] = r - i

        for j in range(c + 1):
            dp[r][j] = c - j

        for i in range(r -1, -1, -1):
            for j in range(c - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]

out = Solution().minDistance("horse", "ros")
print(out)

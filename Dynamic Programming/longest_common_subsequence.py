class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        text2=s[::-1]
        
        dp = [[0] * (n + 1) for _ in range(n + 1)] 

        for i in range(n):
            for j in range(n):

                if s[i]==text2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    
        return dp[n-1][n-1]


out = Solution().longestCommonSubsequence("abcde", "ace")
print(out)

class Solution:
    def wordBreak(self, s: str, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []

        # dp init
        n = len(s)
        dp = [[] for x in range(n + 1)]
        dp[0] = [0]

        # bottom up DP
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i].append(j)
        # print dp
        # backtrack
        res = []
        self.backtrack(dp, s, n, res, '')
        return res

    def backtrack(self, dp, s, idx, res, line):

        for i in dp[idx]:
            new_line = s[i:idx] + ' ' + line if line else s[i:idx]

            if i == 0:
                res.append(new_line)
            else:
                self.backtrack(dp, s, i, res, new_line)


out = Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print(out)

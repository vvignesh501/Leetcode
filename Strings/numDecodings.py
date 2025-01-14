class Solution:
    def numDecodings(self, s: str, memo={}) -> int:
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return 1

        if s[0] == '0':
            return 0

        if len(s) == 1:
            return 1

        if 1 <= int(s[:2]) <= 26:
            memo[s] = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            return memo[s]
        else:
            memo[s] = self.numDecodings(s[1:])
            return memo[s]


out = Solution().numDecodings("21")
print(out)
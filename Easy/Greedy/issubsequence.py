class Solution(object):
    def isSubsequence(self, s, t):
        j = 0

        cnt = len(s)
        if not s:
            return True
        for char in t:
            if char == s[j]:
                j += 1
            if j == cnt:
                return True
        return False


g = Solution()
out = g.isSubsequence("abc", "ahbgdc")
print(out)
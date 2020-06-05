class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        else:
            return -1


g = Solution()
out = g.firstUniqChar("loveleetcode")
print(out)

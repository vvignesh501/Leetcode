import collections
class Solution:
    def findAnagrams(self, s: str, p: str):
        vals = []
        n = len(p)
        h = collections.Counter(p)
        for i in range(len(s) - n + 1):
            if collections.Counter(s[i:i + n]) == h:
                vals.append(i)
        return vals


g = Solution().findAnagrams("cbaebabacd", "abc")
print(g)
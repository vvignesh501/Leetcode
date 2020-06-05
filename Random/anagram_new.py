class Solution():
    def anagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        if s == t:
           return s.index()
        else:
            return -1

s = "abab"
t = "ab"
out = Solution().anagram(s, t)
print(out)
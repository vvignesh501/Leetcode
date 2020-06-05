class Solution():
    def anagram(self, s, t):
        out = []
        if s!="" and t!="":
            for i in t:
                j = i
                for j in s:
                    if i == j:
                        out.append(i)
                        break
            return bool(out)
        elif s == "" and t == "":
            s = s.split(' ')
            t= t.split(' ')
            return bool(s)
        else:
            return bool(out)

s = "a"
t = "ab"
out = Solution().anagram(s, t)
print(out)
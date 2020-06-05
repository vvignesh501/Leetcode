class Solution:
    def removeDuplicate(self, S):
        out = []
        for i in range(0, len(S)):
            if not out:
                out.append(S[i])
            else:
                if out:
                    if out[-1] == S[i]:
                        out.pop(-1)
                    else:
                        out.append(S[i])
        return "".join(out)


g = Solution()
out = g.removeDuplicate("bbeddfeiiiek")
print(out)



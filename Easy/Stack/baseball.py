class Solution:
    def calPoints(self, ops):
        stack = []
        ans = 0
        for i in ops:
            if i == "C":
                m = stack.pop()
                ans -= m
            else:
                if i == "D":
                    m = stack[-1] * 2
                elif i == "+":
                    m = stack[-1] + stack[-2]
                else:
                    m = int(i)
                stack.append(m)
                ans += m
        return ans


g = Solution()
out = g.calPoints(["5", "2", "C", "D", "+"])
print(out)

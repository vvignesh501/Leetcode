class Solution:
    def reverse(self, x: int) -> int:
        xx = list(str(x))
        yy = []
        if xx[0] in ('+', '-'):
            yy[0] = xx[0]
        else:
            yy.append(xx.reverse())
        return yy


g = Solution()
out = g.reverse(123)
print(out)
import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        root = 0.0
        root = math.sqrt(num)

        if int(root + 0.5) ** 2 == num:
            return True
        else:
            return False
        return False


g = Solution()
out = g.isPerfectSquare(25)
print(out)
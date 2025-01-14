import math
import copy


class Solution:
    def reverse(self, x: int) -> int:

        MIN = -2147483648
        MAX = 2147483647
        out = 0
        new = copy.copy(abs(x))

        while new:

            reminder = new % 10
            new = int(new / 10)

            out = out * 10 + reminder

            if out >= MAX or out <= MIN:
                return 0

        return out if x > 0 else -out


out = Solution().reverse(-123)
print(out)

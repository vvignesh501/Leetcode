import math


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:

        l = 1
        r = max(piles)
        res = r
        while l <= r:
            total = 0
            k = (l + r) // 2
            for p in piles:
                if k <= 5:
                    print(k)
                total += math.ceil(p / k)

            if total <= h:
                res = min(res, k)
                r = k - 1
            elif total >= h:
                l = k + 1

        return res


out = Solution().minEatingSpeed([312884470], 968709470)
print(out)






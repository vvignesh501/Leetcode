import math


class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:

        low = 1
        high = max(nums)
        while low < high:
            mid = (low + (high-low) + 1)//2
            s = sum(map(lambda x: int(math.ceil(x / mid)), nums))
            if s <= threshold:
                high = mid
            else:
                low = mid + 1
        return low


out = Solution().smallestDivisor([1, 2, 5, 9], 6)
print(out)
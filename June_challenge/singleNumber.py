import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = collections.Counter(nums)
        for x, y in val.items():
            if y == 1:
                return x


g = Solution().singleNumber([2, 2, 3, 2])
print(g)

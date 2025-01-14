class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            else:
                d[num] = i


out = Solution().twoSum([5, 2, 4], 9)
print(out)

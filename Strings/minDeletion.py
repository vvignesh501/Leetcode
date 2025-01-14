class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        i = 0
        count = 0
        while i + 1 < len(nums):
            if (i - count) % 2 == 0 and nums[i] == nums[i + 1]:
                count += 1
            i += 1
        return count + (len(nums) - count) % 2


out = Solution().minDeletion([1, 1, 1, 2, 1, 1])
print(out)

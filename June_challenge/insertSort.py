class Solution:
    def searchInsert(self, nums, target: int) -> int:

        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)


g = Solution().searchInsert([1,3,5,6], 7)
print(g)
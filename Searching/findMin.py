class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            m = left + (right - left) // 2
            if nums[m] < nums[right]:
                right = m
            elif nums[m] > nums[right]:
                left = m
            else:
                right -= 1

        print(nums[left], nums[right])
        return min(nums[left], nums[right])  # two choices, return the smallest!


out = Solution().findMin([1, 3, 5])
print(out)

class Solution:
    def searchRange(self, nums, target):

        l = 0
        r = len(nums) - 1
        res = [-1, -1]

        # Traverse once from left to right, find the starting pos
        # Break when you find once

        while l <= r:

            if nums[l] == target:
                res[0] = l
                break

            l += 1

        # Traverse again from righ to left, find the ending pos
        # Break when you find twice

        while r >= 0:
            if nums[r] == target:
                res[1] = r
                break

            r -= 1

        return res


sol = Solution().searchRange(nums=[5,7,7,8,8,10], target=8)
print(sol)
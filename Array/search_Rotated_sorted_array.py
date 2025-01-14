class Solution:
    def search(self, nums, target: int) -> int:

        # perform binary search
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


out = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print(out)

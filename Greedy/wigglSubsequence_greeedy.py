class Solution:
    def wiggleMaxLength(self, nums) -> int:
        # we can maintain two status of the array while adding new numbers
        # up and down, meaning the last part of the wiggle array is going up or down
        # if nums[i] > nums[i - 1], the previous down wiggle becomes the up wiggle
        # if nums[i] < nums[i - 1], the previous up wiggle becomes the up wiggle
        # if nums[i] == nums[i - 1], skip it
        # O(n) time O(1) space

        up, down = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                down = up + 1
            elif nums[i] < nums[i - 1]:
                up = down + 1
        return max(up, down)


out = Solution().wiggleMaxLength([1, 4, 7, 2, 5])
print(out)

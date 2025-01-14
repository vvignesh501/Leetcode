class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # First sort the number
        nums.sort()
        output = []

        # For each number in nums, use another 2 pointer from nxt num till last num
        for i, num in enumerate(nums):

            # Check whether the current number and next number are same.
            # If yes, then ignore

            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sums = num + nums[l] + nums[r]
                if sums == 0:
                    output.append([num, nums[l], nums[r]])
                    l += 1

                    # No two results should be same under output
                    # If the previous number and current number are same.
                    # Then ignore the number and move on to the next number.

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                if sums > 0:
                    r -= 1
                if sums < 0:
                    l += 1

        return output


out = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(out)

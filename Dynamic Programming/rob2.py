class Solution:
    def rob(self, nums: List[int]) -> int:

        # f houses are in a circle, and you rob house 0, you can’t rob house n-1.
        # Similarly, if you rob house n-1, you can’t rob house 0.
        # So — you must make a choice:

        # Case 1: Rob from house 0 to n-2
        # You exclude the last house.
        # This behaves just like original House Robber problem.

        # Case 2: Rob from house 1 to n-1
        # You exclude the first house.

        if len(nums) == 1:
            return nums[0]

        def dp(nums):

            if len(nums) == 0:
                return 0

            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return dp[-1]
        
        # Case 1 and case 2
        return max(dp(nums[:-1]), dp(nums[1:]))

sol = Solution(nums = [2,3,2])
print(sol)

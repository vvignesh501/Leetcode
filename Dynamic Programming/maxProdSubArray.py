class Solution:
    def maxProduct(self, nums):
        curMax, curMin = 1, 1
        res = nums[0]

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
            res = max(res, curMax)
        return res


print(Solution().maxProduct([-3, -1, -1]))

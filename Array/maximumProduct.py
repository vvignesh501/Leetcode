"""
This program is a little complex one. If you miss one test case
scenario. You miss to get the maximum product value.
Especially when you have the subarray of all negatives.
Note (-) * (-) = + But (-) * (-) * (+) = -
Negative result means Product of min value not maxValue.
To get maxValue you need to consider both minVal and maxVal.
"""

class Solution:
    def maxProduct(self, nums) -> int:
        res = nums[0]
        maxVal, minVal = 1, 1
        for n in nums:
            # tmp used because maxVal value changes after maxVal calculated below
            tmp = n * maxVal
            # Compare the maximum of n, product of previous n*previous maxVal and n*previous minVal
            maxVal = max(n, n * maxVal, n * minVal)
            minVal = min(n, tmp, n * minVal)
            res = max(res, maxVal)
        return res


out = Solution().maxProduct([2, 3, -2, 4])
print(out)

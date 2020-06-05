class Solution:
    def maxSubArray(self, nums):
        sums = []
        i = 0
        if len(nums) >= 3:
            for i in range(0, (len(nums) - 1)):
                if not sums:
                    sums.append(max((nums[i] + nums[i + 1]), nums[i + 1]))
                else:
                    sums.append(max((sums[-1] + nums[i + 1]), nums[i + 1]))
            return max (i, max(sums))
        else:
            return max(sum(nums), max(nums))


g = Solution()
out = g.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(out)

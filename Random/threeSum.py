from collections import Counter


class Solution:
    def threeSum(self, nums):
        vals = []
        sum_ = 0
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    sum_ = nums[i] + nums[j] + nums[k]
                    if sum_ == 0:
                        if sorted(list((nums[i], nums[j], nums[k]))) not in vals:
                            vals.append(sorted(list((nums[i], nums[j], nums[k]))))

        return vals


g = Solution()
out = g.threeSum([3,0,-2,-1,1,2])
print(out)

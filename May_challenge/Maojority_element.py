class Solution:
    def majorityElement(self, nums):
        list=[]
        for i in nums:
            list.append(nums.count(i))
        return nums[list.index(max(list))]


g = Solution()
out = g.majorityElement([2,2,1,1,1,2,2])
print(out)
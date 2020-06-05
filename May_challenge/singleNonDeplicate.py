class Solution:
    def singleNonDuplicate(self, nums) -> int:
        num = []
        for i in nums:
            if nums.count(i) == 1:
                return i


g = Solution()
out = g.singleNonDuplicate([3,3,7,7,10,11,11])
print(out)
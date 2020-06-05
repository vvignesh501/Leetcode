class Solution:
    def arrayPairSum(self, nums) -> int:

        nums1 = sorted(nums)
        sum_ = 0
        for i in range(0, len(nums1)-1,2) :
            for j in range(i+1, len(nums1),2):
                sum_ += min(nums1[i], nums1[j])
                break
        return sum_


g = Solution()
out = g.arrayPairSum([1, 2, 5, 9, 10, 14])
print(out)
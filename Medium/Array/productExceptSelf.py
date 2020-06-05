class Solution:
    def productExceptSelf(self, nums):

        L = [0] * len(nums)
        R = [0] * len(nums)

        val = [0] * len(nums)
        L[0] = 1
        R[len(nums)-1] = 1

        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]

        for i in reversed(range(len(nums)-1)):
            R[i] = R[i+1] * nums[i+1]

        for j in range(len(nums)):
            val[j] = L[j] * R[j]

        return val


g = Solution()
out = g.productExceptSelf([1, 2, 3, 4])
print(out)